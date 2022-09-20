from pypylon import pylon
from datetime import datetime
import threading
import cv2
import argparse
import os
import numpy as np


SERIAL_NUMBER = '40076234'  # camera serial number

# variable initialization
auto_mode = True
preview = True
stereo = False
period = 5.0
directory_name = ''
image_to_watch = []
image_to_watch2 = []
active_thread = threading.Timer


def image_from_camera():
    # jezeli uzywamy dwoch kamer to przy czasie < 2s watki nie zdaza sie zamknac i zglaszaja bledy ale program dziala
    def perspective_camera(name):  # this function is used for stereo camera
        if stereo:
            cap = cv2.VideoCapture(2)
            ret, frame = cap.read()
            filename_stereo = directory_name + '/stereo_img_' + name + '.png'
            cv2.imwrite(filename_stereo, frame)
            cap.release()
            return frame

    if auto_mode:
        global active_thread
        active_thread = threading.Timer(period, image_from_camera)
        active_thread.start()

    tlf = pylon.TlFactory.GetInstance()
    devices = tlf.EnumerateDevices()  # list of plugged basler cameras
    cam = pylon.InstantCamera(tlf.CreateFirstDevice())

    for d in devices:
        if d.GetSerialNumber() == SERIAL_NUMBER:
            cam = pylon.InstantCamera(tlf.CreateFirstDevice(d))
        else:
            # this text is shown if serial number had been not found
            print(f'Serial Number not found. Current connected camera is {devices[0].GetSerialNumber}')

    cam.Open()
    cam.Gain = 9  # [dB]
    cam.ExposureTime = 30000  # [ms]
    cam.PixelFormat = "RGB8"

    with cam.GrabOne(1000) as result:
        img = result.Array  # this is RGB image in ndarray

        now = datetime.now()
        time_date = now.strftime("%m-%d-%Y_%H:%M:%S")
        filename = directory_name + '/img_' + time_date + '.png'
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(filename, img)

        perspective_img = perspective_camera(time_date)

        global image_to_watch, image_to_watch2
        image_to_watch = img
        image_to_watch2 = perspective_img

    cam.Close()

    now = datetime.now()
    print(f'zapisano {now}')


def show_image():  # this function is used to show recent image
    if preview:
        cv2.namedWindow('recent saved image')
        while True:
            img = cv2.resize(image_to_watch, (0, 0), fx=0.9, fy=0.9)
            cv2.imshow('recent saved image', img)
            if stereo:
                cv2.imshow('recent saved image', img)
                cv2.imshow('image from perspective camera', image_to_watch2)
                key = cv2.waitKey(30)
            else:
                cv2.imshow('recent saved image', img)
                key = cv2.waitKey(30)
            if key == ord('q') and not auto_mode:
                cv2.destroyAllWindows()
                break
            elif key == ord('q') and auto_mode:
                active_thread.cancel()  # it terminates thread responsible for timer
                cv2.destroyAllWindows()
                break
            elif key == ord('m') and not auto_mode:  # this condition is active when you use manual mode with preview
                image_from_camera()
                key = ord('a')


def main():
    parser = argparse.ArgumentParser(description=
                                     "This program gets images from Basler camera and transform omnidirectional images "
                                     "to panoramic. Example of usage: python3 main.py auto -t=5.5 -p In this case "
                                     "program is taking photo every 5.5 second and show user preview of taken photo")
    parser.add_argument("mode", choices=["manual", "auto"])
    parser.add_argument("-t", "--time",
                        help="In auto mode you must set period of time [s]. Default value is 5.0 seconds")
    parser.add_argument("-p", "--preview", action="store_true",
                        help="Preview of saved photos")
    parser.add_argument("-s", "--stereo", action="store_true",
                        help="Add this parameter if you are using omnidirectional camera and perspective camera")
    args = parser.parse_args()

    global auto_mode, period, preview, directory_name, stereo

    if args.mode == 'auto':
        auto_mode = True
        if type(args.time) == type('abc'):
            period = float(args.time)
    elif args.mode == 'manual':
        auto_mode = False

    preview = args.preview
    stereo = args.stereo

    print(f'auto mode: {auto_mode}, period: {period}, preview: {preview}')

    path = './stereo_kalibracja/'  # path to directory where new directory with images is created
    list_dir = os.listdir(path)
    directory_name = path + f'{len(list_dir)}'  # name of created directory
    os.mkdir(directory_name)

    image_from_camera()
    show_image()

    if not preview and not auto_mode:  # this condition is active if you use manual mode without preview
        key = ord('a')
        img = np.zeros((10, 10))
        cv2.namedWindow('a')
        cv2.imshow('a', img)
        while key != ord('q'):
            if key == ord('m'):
                image_from_camera()
            key = cv2.waitKey(30)


if __name__ == '__main__':
    main()

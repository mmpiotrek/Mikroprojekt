import cv2
import numpy as np
import polarTransform
import os


def vide():  # this function creates movie for FabMap application
    path = './eksperyment/3_pietro_test/'  # source directory for images to create video
    files = sorted(os.listdir(path))
    img = cv2.imread(path + files[0])  # initial value to initialize VideWriter
    out = cv2.VideoWriter('3_pietro_test.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 1, (np.shape(img)[1],
                                                                                               np.shape(img)[0]))
    for file in files:
        img = cv2.imread(path + file)
        out.write(img)
        print(f'frame added {file}')
    out.release()


def panorama(src_path, destination_path, name):
    image = cv2.imread(src_path)
    final, settings = polarTransform.convertToPolarImage(image, (768, 542), hasColor=True, initialRadius=80,
                                                         finalRadius=460, useMultiThreading=True)
    final = cv2.rotate(final, cv2.ROTATE_90_COUNTERCLOCKWISE)

    print(settings)

    cv2.imwrite(destination_path + 'panoramic_' + name, final)

    # uncomment lines below if you want to have preview
    # final = cv2.resize(final, (0, 0), fx=0.5, fy=0.5)
    # cv2.imshow('panorama', final)
    # cv2.imshow(f'{src_path}', image)
    # cv2.waitKey(10)
    # cv2.destroyAllWindows()


path = './eksperyment/QR_kody/'  # source directory path
directories = sorted(os.listdir(path))
for num, directory in enumerate(directories):
    if os.path.exists(path + f'panoramic_{num}'):
        continue
    os.mkdir(path + f'panoramic_{num}')  # creates new directory for panoramic images
    destination_directory = path + f'panoramic_{num}/'
    images = sorted(os.listdir(path + directory))
    for img in images:
        img_path = path + directory + '/' + img
        panorama(img_path, destination_directory, img)

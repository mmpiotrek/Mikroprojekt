#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "danekalibracja.h"

using namespace cv;
using namespace std;

Mat Omapx_calibration_central, Omapy_calibration_central, Opanorama_central, image1_kwadrat;
double width_pan = 2880;   //1620
double height_pan = 621;   //6440
int Rprocent = 100; // powierzchnia panoramy Opanorama_central w procentach
int Rmax = 460;
struct ocam_model o_cata;	// deklaracja obiektu kamery ocam_model
char * ocam_txt = "calib_results_1.txt";


int main(int argc, char** argv )
{
    Mat image;
    image = imread("/home/piotr/mikroprojekt/source/eksperyment/parter/22/img_08-17-2022_11:03:43.png");
    cout<<image.size()<<endl;
    image1_kwadrat = image;
    // Wprowadzenie modelu katadioptrycznego
    int check =  get_ocam_model(&o_cata, ocam_txt); // wczytuje strukture o_cata;
    if(check)
    {
         cout << "ERROR: Could not initialize catadioptric model parameters" << endl;
         return -1;
    }
    // Przeksztalcenie macierzowe sluzace do powstania panoramy metoda wykorzystujaca wiedze o parametrach uk�adu katadioptrycznego
	Opanorama_central.create(height_pan , width_pan , CV_8UC3);  // macierz uzywana do zapisywania obrazu
	Omapx_calibration_central.create(Opanorama_central.size(),CV_32FC1); // macierze Omapx, Omapy do przeksztalcenia bez znieksztalcen
    Omapy_calibration_central.create(Opanorama_central.size(),CV_32FC1); //
	Ocreate_panoramic_central( Omapx_calibration_central, Omapy_calibration_central, Rprocent, Rmax, &o_cata);
	remap(image1_kwadrat,Opanorama_central,Omapx_calibration_central,Omapy_calibration_central,INTER_LINEAR, (0,0,0)); 

    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    // int down_width = 1080;
    // int down_height = 720;
    // Mat resize_down;
	// resize(Opanorama_central, resize_down, Size(down_width, down_height), INTER_LINEAR);    
    imshow("Panorama Image",Opanorama_central);
    // cvtColor(Opanorama_central, result, COLOR_RGB2BGR);
    imwrite("panoramic_parter_calib3.png", Opanorama_central);
    waitKey(0);
    return 0;
}
#ifndef danekalibracja_h
#define danekalibracja_h
#include "opencv2/opencv.hpp"
#include <stdlib.h>
#include <stdio.h>
#include <float.h>
#include <math.h>

#define CMV_MAX_BUF 1024
#define MAX_POL_LENGTH 64
static const double PI = 3.14159265358979323846;
using namespace cv;

struct ocam_model
{
	double pol[MAX_POL_LENGTH];    // the polynomial coefficients: pol[0] + x"pol[1] + x^2*pol[2] + ... + x^(N-1)*pol[N-1]
	int length_pol;                // length of polynomial
	double invpol[MAX_POL_LENGTH]; // the coefficients of the inverse polynomial
	int length_invpol;             // length of inverse polynomial
	double xc;         // row coordinate of the center
	double yc;         // column coordinate of the center
	double c;          // affine parameter
	double d;          // affine parameter
	double e;          // affine parameter
	int width;         // image width
	int height;        // image height
};

/*------------------------------------------------------------------------------
 This function reads the parameters of the omnidirectional camera model from 
 a given TXT file
------------------------------------------------------------------------------*/
int get_ocam_model(struct ocam_model *myocam_model, char *filename);
void world2cam(double point2D[2], double point3D[3], struct ocam_model *myocam_model);
void cam2world(double point3D[3], double point2D[2], struct ocam_model *myocam_model);
void create_perspecive_undistortion_LUT( Mat mapx, Mat mapy, struct ocam_model *ocam_model, float sf);
void create_panoramic_undistortion_LUT ( Mat mapx, Mat mapy, float Rmin, float Rmax, float xc, float yc );

// Funkcja Ocam dodane
void Ovu2point2d(double point2d[2], double pointVU[2],struct ocam_model *myocam_model); // przeksztalcenie z VU do 2D
void Opoint2d2vu(double pointVU[2], double point2d[2],struct ocam_model *myocam_model); // przeksztalcenie z 2D do VU
void O3d2vu(double pointVU[2], double point3d[3],struct ocam_model *myocam_model); // przeksztalcenie z 3D do VU
void Ovu2d3(double point3d[3], double pointVU[2],struct ocam_model *myocam_model); // przeksztalcenie z VU do 3D
void Ocreate_panoramic_central( Mat mapx, Mat mapy, float Rprocent, float Rmax_new, ocam_model *myocam_model); // tworzy panorame z centraln¹ lini¹ poziom¹ na œrodku panoramy
void Ocreate_panoramic( Mat mapx, Mat mapy, float Rmin, float Rmax, struct ocam_model *myocam_model); // tworzy panorame z parametrami Rmin,Rmax
void Ocreate_projection( Mat mapx, Mat mapy, double f, double fi, double theta, struct ocam_model *myocam_model); // tworzy projection plane
// 3 uklady osi odniesienia (3D, VU, 2D)


//int dodajLiczby( int a, int b );

#endif

%module colotracker

%include <opencv.i>
%cv_instantiate_all_defaults

%{
   #include "colotracker.h"
%}

%include "colotracker.h"

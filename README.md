# Dart_Algorithm
This is a project that used a 720p webcam centered over a dart board to record dart throws for steel tipped darts.

The idea of this was to implement a system that could be utilized with a simple webcam or cheap camera rather than a multi-camera setup with a high cost.
The software uses adaptive thresholding and bounding rectangles to determine the location of the dart, continuing to associate a score with the position found.

A basic explanation is available within Sam_Presentation.py and then a further explanation of the math will also be uploaded.

Next Step: 
So the big step to improving this software is to find a way to determine the apex of the dart so that the accuracy can be increased for scoring.
As it currently stands the code works and will score efficiently but there is a lot of room for error if the dart is thrown at an odd angle or is close to another region.


References & Acknowledgements:
I would like to thank Chase Pavlick for helping with the math involved in mapping out the regions of the dartboard and also assisting with the adaptive thresholding.
I would also like to extend thanks to Kyle Greer and Jack Weiler for assiting with the hardware and assembly.

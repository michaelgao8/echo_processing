## Project Normal Echo 

### About:
The following contains scripts used to preprocess echocardiogram data for downstream modeling.

The echo studies are given in DICOM format, but also contain variation in the metadata elements that are available. These scripts explore the structure of the files and extract the metadata into structured form.

### Dependencies:

The version of python used to run the code contained in this repository was `2.7.14`.

The `mudicom` package has been modified for the purposes of this project. This is to extract a raw pixel stream due to issues with `mudicom`'s assumptions about the structure of the pixel data. The repository with the custom version is available here:
https://github.com/michaelgao8/mudicom

In addition, `mudicom` has depencies with installation instructions available here:

https://github.com/neurosnap/mudicom/blob/master/docs/install.rst

One potential issue is with the following line:

```$ ln -s /usr/lib/python2.7/dist-packages/_gdcmswig.so /virtualenv/path/python/site-packages/_gdcmswig.so```

The symbolic link fails in some instances because the name of `_gdcmswig.so` has a different name. It is called something along the lines of `_gdcmswig_x86_...so` 

Alternatively, Anaconda can install gdcm with `conda install -c conda-forge gdcm` (I think this also compiles gdcm to work with python3)

### TODO:

Build out containers with custom `mudicom` and other dependencies (`Tensorflow`, etc.)


""" 
The following file contains functions that facilitate the reading of ECHOs as 
well as processing the metadata associated with DICOM files
"""
import mudicom
import gdcm
import numpy as np

def get_grayscale_array(filename):
    # TODO: Include function to get the type of pixel representation (YCbCR vs RGB)
    """ 
    This function returns the image_array as a numpy array from a DICOM file.
    
    - Input:
        filename(chr): The filename of the study (.dcm format)
    - Returns:
        pixel_stream(ND numpy array): An array in the format of Frame x Height x Width
    """
    study = mudicom.load(filename)
    data = study.read()
    element_name_list = [x.name for x in data]
    element_value_list = [x.value for x in data]
    
    num_frames = element_value_list[element_name_list.index("Number of Frames")]
    rows = element_value_list[element_name_list.index("Rows")]
    columns = element_value_list[element_name_list.index("Columns")]
    channels = element_value_list[element_name_list.index("Samples per Pixel")]
    
    if channels == '1':
        pixel_stream = study.image.numpy
        pixel_stream.shape = int(num_frames), int(rows), int(columns)
    elif channels == '3':
        pixel_stream = study.image.numpy
        pixel_stream.shape = int(num_frames), int(rows), int(columns), int(channels)
        pixel_stream = pixel_stream[:,:,:,0]
    else:
        print("Number of channels not populated... exiting now")
        return None
    
    return pixel_stream


def get_view_name(filename):
    """
    This function returns the view that each echo is of. Examples include 'PSAX'
    and is located in the ViewName element in the DICOM format
    """
    study = mudicom.load(filename)
    data = study.read()
    element_name_list = [x.name for x in data]
    element_value_list = [x.value for x in data]
    
    view = element_value_list[element_name_list.index("View Name")]
    
    return view


def get_imagetype_data(filename):
    """
    This function will return information regarding the compression and storage
    types of the image as well as the color scheme that it is stored in
    """
    study = mudicom.load(filename)
    data = study.read()
    element_name_list = [x.name for x in data]
    element_value_list = [x.value for x in data]
    
    compression = element_value_list[element_name_list.index("Derivation Description")]
    color_scheme = element_value_list[element_name_list.index("Photometric Interpretation")]
    
    return compression, color_scheme


    
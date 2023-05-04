from django.http import HttpResponse

import pydicom

from django.conf import settings
from pydicom.data import get_testdata_file
import os
import numpy as np

# Create your views here.
def dicom(request):
    # Carga el archivo DICOM
    path = os.path.join(settings.MEDIA_ROOT, 'D0001.dcm')
    # filename=get_testdata_file(path)
    dcm = pydicom.dcmread(path)

    fg = dcm.group_dataset
    data = dcm.pixel_array
    # print('The image has {} x {} voxels'.format(data.shape[0],
    #                                         data.shape[1]))
    # structure=dcm.pixel_
    # max_structure=

    # Convierte la matriz de dosis a un array de numpy
    dose_array = np.array(data)

    # Encuentra la dosis máxima en el array de dosis
    max_dosis = np.amax(dose_array)  
    #mayor radiación punto mas oscurso

    print(fg)
    # Obtiene el nombre de las estructuras
    # estructuras=dcm.StructureSetROISequence

    return HttpResponse("hola mundo")
    # return HttpResponse(estructuras)

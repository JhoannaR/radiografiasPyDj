from django.shortcuts import render
from django.http import HttpResponse

import pydicom
from pylinac import load_log


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

    variable="Jhoanna"
    context={'variable': variable,
              'dosismax': max_dosis,
              'dose_array':dose_array}
    return render(request, 'dicom.html', context)
    # return HttpResponse(estructuras)


def dynalog(request):
    path = os.path.join(settings.MEDIA_ROOT, 'Tlog.bin')

    tlog = load_log(path)
    tlog.axis_data.gantry.plot_actual()  # plot the gantry position throughout treatment
    tlog.fluence.gamma.calc_map(doseTA=1, distTA=1, threshold=0.5, resolution=0.1)
    

    # actual=tlog.fluence.actual.calc_map()
    # # print(actual)

    # planned=tlog.fluence.expected.calc_map(resolution=1)


    # actual1=tlog.axis_data.mlc.leaf_axes[1].actual
    # difference1=tlog.axis_data.mlc.leaf_axes[1].difference
    # for n in actual1:
    #     print(n)

    # print(len(difference1))
    tlog.fluence.gamma.plot_map()  # show the gamma map as a matplotlib figure
    # tlog.publish_pdf()  # publish a PDF report
    # dlog = load_log("dynalog.dlg")
    return HttpResponse("dynalog")


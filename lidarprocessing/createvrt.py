import glob
from osgeo import gdal


def vrt(inputdir, output_vrt):
    pathtotiles = inputdir + '*.tif'
    listofalltiles = glob.glob(pathtotiles,recursive = True)
    listoftileswithoutborder = []
    for tile in listofalltiles:
        listoftileswithoutborder.append(tile)
    print(len(listoftileswithoutborder), 'tiles detected')
    # create vrt from none border tiles
    gdal.SetConfigOption('GDAL_NUM_THREADS', 'ALL_CPUS')
    vrt_options = gdal.BuildVRTOptions(resampleAlg='near', addAlpha=False)
    gdal.BuildVRT(output_vrt, listoftileswithoutborder, options=vrt_options)

indata = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/canopy_above_5m/'
output_vrt = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/canopy.vrt'
vrt(indata, output_vrt)
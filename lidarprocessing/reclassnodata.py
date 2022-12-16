import os
import whitebox
wbt = whitebox.WhiteboxTools()

indir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/binarycanopy/'
outdir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/binarycanopynodata/'

for tile in os.listdir(indir):
    if tile.endswith('.tif'):
        wbt.convert_nodata_to_zero(
            i = indir + tile, 
            output = outdir + tile
        )
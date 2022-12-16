import os
import whitebox
wbt = whitebox.WhiteboxTools()

indir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/canopy_above_5m/'
outdir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/binarycanopy/'

for tile in os.listdir(indir):
    if tile.endswith('.tif'):
        intile = indir + tile
        outtile = outdir + tile
        wbt.greater_than(
            input1 = intile , 
            input2 = 5, 
            output = outtile, 
            incl_equals=False
        )
import os
import whitebox
wbt = whitebox.WhiteboxTools()
lasdir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/las/'
heightdir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/height_above_ground/'
canopydir = 'Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/canopy_above_5m/'





for tile in os.listdir(lasdir):
    lasfile = lasdir + tile
    height = heightdir + tile.replace('.las', '.tif')
    # wbt.height_above_ground(
    #     i=lasfile, 
    #     output=height
    #     )



    wbt.lidar_tophat_transform(
        i = lasfile, 
        output = height, 
        radius=1.0
    )   

    ofile = canopydir + tile.replace('.las', '.tif')
    wbt.greater_than(
        input1 = height, 
        input2 = '5', 
        output = ofile, 
        incl_equals=False
    )
import whitebox
wbt = whitebox.WhiteboxTools()
wbt.set_working_dir('Y:/William/RIP_NATURE_2/Canada/download_las_tiles_canada/Download_las/')

wbt.lidar_tile_footprint(
    output=None, 
    i=None, 
    hull=False
)
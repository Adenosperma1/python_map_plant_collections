# To make this work you need:

#1
# csv files downloaded from Australian virtual herbarium. One species per file.
# name those species files with with the speciesName.csv. i.e. atricha.csv
# put them all in a single folder and set the var folder_csv below

#2
# you will ned shape files for the map
# put them all in a single folder and set vars below for the three shape files

#3. set up the species names, at the moment only takes one genus...

#4. Run the main.py file.

#####################################################

#1. folder paths
folder_base = '/Users/brendanwilde/Documents/code/python/Mapping/'
folder_csv = folder_base + 'species_csv_files/'
folder_shapes = folder_base + 'shape_files/'
# folder_shapes = folder_base + 'broken/'

#2.Shape file paths
shape_australia = folder_shapes + "shape_Australia/" + "AUS_2021_AUST_GDA2020.shp"
shape_states = folder_shapes + "shape_states/" + "STE_2021_AUST_GDA2020.shp"
shape_regions = folder_shapes + "shape_ibra7Regions/" + "IBRA7_regions.shp"

#3.Species details
genus = 'Ficus'

species_names = [
    'atricha',
    'cerasicarpa',
    'leucotricha',
    'platypoda',
    'sordidus'
]

species_colours = [
    'red',
    'blue',
    'green',
    'magenta',
    'orange'
]


#Map vars ################################################
figure_width, figure_height = 8, 8 # size of the window? The map seems to scale to this?
long_min, long_max = 110.5, 156.5 
lat_min, lat_max = -45, -8
bounding_box_line_thickness = 1

linewidth_australia, linewidth_states, linewidth_regions = 0.5, 0.7, 0.7 
edgecolor_australia, edgecolor_states, edgecolor_regions = 'black', 'grey','grey'
edgecolor_alpha_australia, edgecolor_alpha_states, edgecolor_alpha_regions = 1, 0.2, 0.2
color_australia, color_states, color_regions = 'none', 'none', 'none'

#Legend vars ##############################################
legend_position = 'lower left' #'upper right'
dot_size = 30
legend_font_size = 8
legend_frame = False

#tell vscode to trust the file and it should work
#set python version to 3.6.8 via the bottom of the screen
#check python version: python3 --version should = 3.6.8
#imports : python3 -m pip install geopanda
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import os

# Custom python file with most of the variables 
# so they can be shared by other scripts
from variables import *

# Custom python file with the Species object to hold all collections for each species
# public function get_locations() returns lats, longs : for all colections
# public function get_details_Nuytsia_formatted() returns string : for all collection details formatted for Nuytsia Journal
from class_species import Species

########################################################################
# shape files: Cheak if they exit and load them
# change details in variables.py

if os.path.isfile(shape_australia):
    border_australia = gpd.read_file(shape_australia)
else:
    print("main.py: Error: File not found: " + shape_australia)
    exit()
    
if os.path.isfile(shape_states):
    border_state = gpd.read_file(shape_states)
else:
    print("main.py: Error: File not found: " + shape_states)
    exit()
    
if os.path.isfile(shape_regions):
    border_region = gpd.read_file(shape_regions)
else:
    print("main.py: Error: File not found: " + shape_regions)
    exit()  


########################################################################
# species cvs files: Cheak if they exit
#loop through
for species in species_names:
    csv_path = folder_csv + species + '.csv'
    if os.path.isfile(csv_path) == False:
        print("main.py: Error: File not found:" + csv_path)
        exit()  


########################################################################
# make objects that hold a species details and a list of collection objects for each species listed in the speciesVar.py file
# change details in variables.py
all_species_collections = [Species(genus, species, color, folder_csv + species + '.csv') for species, color in zip(species_names, species_colours)]







########################################################################
# Plot everything 

# Plot the figure
# change details in variables.py
fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Adjust the bounding box position lat and longs
# change details in variables.py
ax.set_xlim(long_min, long_max)
ax.set_ylim(lat_min, lat_max)

# Turn off bounding box tick marks
ax.set_xticks([])
ax.set_yticks([])

# Adjust bounding box border thickness 
# change details in variables.py
for spine in ax.spines.values():
    spine.set_linewidth(bounding_box_line_thickness) 

# Plot the region borders
# change details in variables.py
border_region.plot(ax=ax, color=color_regions, edgecolor=edgecolor_regions, alpha=edgecolor_alpha_regions, linewidth=linewidth_regions)

# Plot state borders
# change details in variables.py
border_state.plot(ax=ax, color=color_states, edgecolor=edgecolor_states, alpha=edgecolor_alpha_states, linewidth=linewidth_states)

# Plot Australian border
# change details in variables.py
border_australia.plot(ax=ax, color=color_australia, edgecolor=edgecolor_australia, alpha=edgecolor_alpha_australia, linewidth=linewidth_australia)

# Map collection locations 
# Create formated text files of collection details for each species
for single_species_collections in all_species_collections:
    species_name = single_species_collections.species
    
    #Map locations of collections
    lats, longs = single_species_collections.get_locations()
    print("main.py: " + species_name + "... Mapping collections." )
    ax.scatter(longs, lats, color=single_species_collections.color, s=dot_size, zorder=5, label=single_species_collections.label)

    #Save text files with formated text for species collections
    species_details = single_species_collections.get_details_Nuytsia_formatted() 
    species_details_file_name = "_formated_" + species_name + ".txt"
    species_details_file_path = os.path.join(folder_csv, species_details_file_name)
    with open(species_details_file_path, "w") as file:
        print("main.py: " + species_name + "... Saving text formatted for Nutysia." )
        file.write(species_details)
    
# Plot the legend
legend = ax.legend(loc=legend_position, fontsize=legend_font_size, frameon=legend_frame)

print("main.py: Displaying Map.")
plt.show()


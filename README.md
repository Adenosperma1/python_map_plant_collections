Map plant collection records downloaded from Australian Virtual Herbarium (https://avh.chah.org.au)
and create a list of collections formated for Nuytsia Journal.

example map:

<img width="630" alt="Screen Shot 2024-06-12 at 11 12 41 pm" src="https://github.com/Adenosperma1/python_map_plant_collections/assets/44901073/a20b628b-b9db-4a02-9f5c-c6ff96961e96">

example text output: cerasicarpa.txt

Selected specimens examined. NORTHERN TERRITORY: GULF COASTAL: Robinson River Station, Bajana, G. M. Wightman 5459, 16 Sep. 1991, (DNA D0151285); GULF FALL AND UPLANDS: Near Clyde River; McArthur River area, L.A. Craven 3500, 29 Feb. 1976, (DNA D0151319); c.40km SSW of Nathan River homestead, L. Peter 10158, 28 Sep. 1985, (CANB 270705); QUEENSLAND: MITCHELL GRASS DOWNS: Jump up at Australian Age of Dinosaurs, Vindex Range, Winton, M.E. Gandini 1061, 7 Apr. 2009, (DNA D0146124); Jump up at Australian Age of Dinosaurs, Vindex Range, Winton, M.E. Gandini 1061, 7 Apr. 2009, (CANB 586872); Vindex Range SE of Winton, G. Sankowsky & N. Sankowsky 2742, 2 June 2007, (DNA D0151396); 'Rangelands', 15km N of Winton, B. Wilkinson AZI1582, 7 June 1999, (DNA D0062212); MOUNT ISA INLIER: Rockface below MIM weather station, off Oban Road Mt Isa, A. Fraser 360, 23 Oct. 2001, (CANB 586871); 20 km E of Cloncurry, D.J. Dixon & I.G. Champion 394, 8 Nov. 1997, (DNA D0151365); 20 km E of Cloncurry, D.J. Dixon & I.G. Champion 395, 8 Nov. 1997, (DNA D0151396); 20 km E of Cloncurry, D.J. Dixon & I.G. Champion 396, 8 Nov. 1997, (DNA D0151285); 20 km E of Cloncurry on north side of highway, D.J. Dixon & I.G. Champion 397, 8 Nov. 1997, (DNA D0151400); 1 km E of Cloncurry, D.J. Dixon & I.G. Champion 398, 8 Nov. 1997, (JCT-S13467); 1 km E of Cloncurry, D.J. Dixon & I.G. Champion 399, 8 Nov. 1997, (BRI AQ1013687); 1 km E of Cloncurry, D.J. Dixon & I.G. Champion 400, 8 Nov. 1997, (BRI AQ0666376); 1 km E of Cloncurry, D.J. Dixon & I.G. Champion 401, 8 Nov. 1997, (DNA D0151311); Warrigal Waterhole, East of Mount Isa, D.J. Dixon & I.G. Champion 403, 10 Nov. 1997, (DNA D0151283); Mount Isa Mines Weather Station, D.J. Dixon & I.G. Champion 405, 12 Nov. 1997, (DNA D0151400); Gregory Downs, Camooweal road, c. 10 km N of "Thorntonia", A. Rodd 3209, 24 June 1976, (DNA D0151286).

Usage:

variables.py:

Set up paths to Shape & Csv files.
Set up Genus and species names (currently only takes a single genus) and colour for each species.

main.py:

Creates map with collection locations. Shows a basic legend.
Creates a text file for each species with a list of all collections formatted for Nuytsia Journal.

example map out: see file map.png.






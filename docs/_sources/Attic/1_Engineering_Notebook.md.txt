# LiDAR

- https://en.wikipedia.org/wiki/Lidar


# What's New

## PotreeConverter

- https://github.com/potree/PotreeConverter

## Ajit examples

# PDAL

- conda install -c conda-forge pdal python-pdal gdal

#### March 2022 

- Exploring USGS LiDAR with STAC info
	- https://github.com/tonybutzer/ajit/blob/main/experiments/3dep/notebooks/notebooks/90_aws_lidar_3dep_basics_stac.ipynb
- Where on earth is ajits data from the bucket - plus .gitignore files
	- https://github.com/tonybutzer/ajit/blob/main/experiments/3dep/notebooks/notebooks/89_ajit_data_in_s3.ipynb

## Experiments

### Viewing Data With the Potree Viewer

- general notes
	- using prebuild containers for creating entwine trees		
	- using prebuilt container for potree viewer withpointer to localhost:8080
	- using an ssh tunnel for 8080 so that localhost:8080 is a valid tree
	- usgs-lidar is a REQUESTER PAYS BUCKET - its in us-west-2
	- https://github.com/hobu/usgs-lidar/  

### https://github.com/hobu/usgs-lidar/
- read this first

- specifics conversion

- specifics display
	-  see below

- need a potree users guide

- the big viewer - not as satisfying
	- https://usgs.entwine.io/data/view.html?r=%22https://s3-us-west-2.amazonaws.com/usgs-lidar-public/SD_Yankton_County_2012%22

#### Cool Notes from Readme

- https://github.com/connormanning/entwine

Getting started with Entwine is easy with Docker. First, we can index some publi
c data:

```
mkdir ~/entwine
docker run -it -v ~/entwine:/entwine connormanning/entwine build \
    -i https://data.entwine.io/red-rocks.laz \
    -o /entwine/red-rocks
```

Now we have our output at ~/entwine/red-rocks. We could have also passed a direc
tory like -i ~/county-data/ to index multiple files. Now we can statically serve
 ~/entwine with a simple HTTP server:

#### Http server - don't forget the tunnel
```
docker run -it -v ~/entwine:/var/www -p 8080:8080 connormanning/http-server
```

And view the data with Potree and Plasio.





### potree docker image

### 3DEP - conda based docker image - demo
- **base container**
- application container
- bucket scraper
- STAC json scraper
- simple panel app prototypes

### rclone testing from tallgrass:/caldera --> eccoe-lidar (s3 bucket)

### example

```
(lidarV2) [ec2-user@ip-10-12-69-95 ~]$ aws s3 ls s3://eccoe-lidar/ajit/
2022-03-06 17:54:05  137136235 HT404_1580305001_1264340300747572_1.las

 aws s3 sync data s3://eccoe-lidar/
upload: data/ajit/HT404_1580305001_1264340300747572_1.las to s3://eccoe-lidar/ajit/HT404_1580305001_1264340300747572_1.las

(lidarV2) [ec2-user@ip-10-12-69-95 ~]$ history | grep scp
  338  lscpu
  637  scp butzer@tallgrass.cr.usgs.gov:/caldera/projects/usgs/water/impd/butzer/* .
  654  history | grep scp

```

- working on command line ways to visualize LiDAR files and objects
	- lastools - compiling the gcc to create Linux binaries in a container
	- lastools - with Windows *.exe* files using wine in a docker container - cool maybe
	- lastools capabilities


## wine version
- https://github.com/hawkaa/docker-lastools/blob/master/Dockerfile

# Conversions Reprojecting Decimating

- https://www.cs.unc.edu/~isenburg/lastools/download/las2las_README.txt


		- 
### lastools
- [](http://lastools.org/)

- short list for now
	- **lasinfo**	prints out an overview of the contents of a LAS/LAZ file
 	- **laszip**	powerful, lossless LiDAR compressor that turns large LAS files into much smaller LAZ files that are only 7 - 20 percent of the original file size
	- __lasboundary__	computes a boundary polygon

- full list
 	- laszip	powerful, lossless LiDAR compressor that turns large LAS files into much smaller LAZ files that are only 7 - 20 percent of the original file size
	- lastile	creates a tiling of LAS/LAZ files
	- lassort	z-orders LAS/LAZ files
	- lasclip	clips away points falling into polygonal shapes (e.g. building footprints)
	- txt2las	converts LiDAR from standard ASCII to LAS/LAZ
	- las2txt	turns LAS/LAZ into human-readable and easy-to-parse text
	- lasinfo	prints out an overview of the contents of a LAS/LAZ file
	- las2shp	turns LAS/LAZ into ESRI's Shapefile format
	- shp2las	turns an ESRI's Shapefile into LAS/LAZ
	- lasmerge	can merge several LAS/LAZ files into one
	- e572las	extracts the points from the E57 format and stores them as LAS/LAZ files
	- las2las	filters, transforms, subsamples, clips, thins, ...
	- lasthin	implements a simple point thinning algorithm
	- las2tin	triangulates the points of a LAS/LAZ file into a TIN
	- las2dem	rasterizes them into a DEM
	- las2iso	extracts, optionally simplified, elevation contours
	- lasboundary	computes a boundary polygon
	- demzip	compresses and uncompresses raster data to RasterLAZ format
	- lasground	tool for bare-earth extraction
	- lasdatum	transforms from one horizontal datum to another
	- lasheight	computes the height of each LAS point above the ground
	- lasclassify	classifies buildings and high vegetation (i.e. trees)
	- lascanopy	computes popular forestry metrics and grids them onto a raster
	- lasoverlap	checks flight line overlap and/or vertical and horizontal alignment
	- lastrack	takes files together with a trajectory file by matching GPS time stamps
	- lascolor	colors LiDAR points based on imagery
	- lasoptimize	optimizes data for better compression and spatial coherency
	- lascontrol	computes the height at certain x and y control points and reports the difference
	- lasgrid	grids data onto a raster
	- lascopy	copies attributes using the GPS-time stamp and the return number
	- lasvoxel	computes a voxelization of points
	- lasdistance	classifies, flags, or removes points based on distance from polygonal segments
	- lasoverage	finds the "overage" of a airborne collect that get covered by multiple flightline
	- lasvalidate	determine if LAS files are conform to the ASPRS LAS specifications
	- lasindex	creates a *.lax file for a given *.las or *.laz file that contains spatial indexing information
	- lasnoise	flags or removes noise points in LAS/LAZ/BIN/ASCII files
	- lasduplicate	removes all duplicate points from a LAS/LAZ/ASCII file
	- lassplit	splits the input file(s) into several output files based on various parameters
	- lasreturn	reports geometric return statistics and repairs 'number of returns' field based on GPS times
	- lasprecision	reads LIDAR data in the LAS format and computes statistics about precision "advertised" in the header
	- laspublish	do 3D visualization of LiDAR data in a web browser using the WebGL Potree
	- lasview	visualizes the contents of a LAS/LAZ file and can also compute a TIN
	- blast2dem	process billion of LIDAR points from the LAS/LAZ format, triangulates them a seamless TIN, and rasters the TIN onto a DEM that can optionally be tiled
	- blast2iso	process billion of LIDAR points from the LAS/LAZ format, triangulates them a seamless (!) TIN, and extracts contours at the specified elevations from the TIN
	- and even more...	see the full product overview

# Photon Azure Viewer

- https://github.com/dcasota/photonos-scripts/wiki/Configure-Potree%2C-a-WebGL-based-viewer-for-large-point-clouds%2C-on-VMware-Photon-OS


## Areas od Study - Ideas

- https://code.visualstudio.com/docs/setup/linux

- https://www.usgs.gov/news/technical-announcement/usgs-3dep-lidar-point-cloud-now-available-amazon-public-dataset

- https://github.com/stac-extensions/pointcloud

- https://medium.com/codait/nodebooks-node-js-data-science-notebooks-aa140bea21ba

- https://www.amazon.com/Head-First-JavaScript-Programming-Freeman/dp/144934013X/ref=as_li_ss_tl?ie=UTF8&qid=1442769823&sr=8-15&keywords=javascript&linkCode=sl1&tag=nethta-20&linkId=840b2a3569091af4a8106c27c814a16b


- https://prd-tnm.s3.amazonaws.com/LidarExplorer/index.html#/

- https://github.com/n-riesco/ijavascript   # javascript jupyter kernel - more study needed

- https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/
# Links first blush

- https://pdal.io/workshop/exercises/georeferencing/index.html#exercise

- https://www.google.com/search?channel=tus5&client=firefox-b-1-d&q=node+gulp+watch

### formats for 3d pointclouds

- https://info.vercator.com/blog/what-are-the-most-common-3d-point-cloud-file-formats-and-how-to-solve-interoperability-issues

- https://www.google.com/search?channel=tus5&client=firefox-b-1-d&q=node+gulp+watch

### pointcloud to triangles

- https://stackoverflow.com/questions/63129494/generating-surface-mesh-from-point-cloud-using-plotly

- https://stackoverflow.com/questions/7879160/algorithm-for-generating-a-triangular-mesh-from-a-cloud-of-points

# open3d videos

- https://www.youtube.com/watch?v=Rsh4poEpahI
- https://www.youtube.com/watch?v=fY_BzTmU9io
- https://www.youtube.com/watch?v=zF3MreN1w6c


https://www.youtube.com/watch?v=VkRzNYxwyH0

### git
https://github.com/centreborelli/pypotree

### pypotree

- https://github.com/sitn/pytree

- https://colab.research.google.com/drive/1It3EbWy9W8Xf65ikP-_tpkVdJRmvwTQT#scrollTo=NfPO-aptsKlC

- https://github.com/potree/potree
- https://www.designsafe-ci.org/rw/user-guides/tools-applications/visualization/potree-viewer/
- https://twitter.com/m_schuetz/status/973145431894085632?lang=en

- https://github.com/centreborelli/pypotree/blob/master/pypotree.py


- https://github.com/sitn/pytree  
    - flask application

https://github.com/potree/PotreeDesktop/releases/tag/1.6

https://www.linode.com/community/questions/21270/how-to-serve-static-asset-files-with-flask-and-nginx
### medium article

- https://towardsdatascience.com/guide-to-real-time-visualisation-of-massive-3d-point-clouds-in-python-ea6f00241ee0

- https://blog.jupyter.org/ipygany-jupyter-into-the-third-dimension-29a97597fc33

https://github.com/widgetti/ipyvolume/blob/master/notebooks/demo-0.5.ipynb


### hoop 3d cad

- https://demo.techsoft3d.com/

- https://github.com/isl-org/Open3D/issues/537

- https://github.com/isl-org/Open3D/issues/376

- http://www.open3d.org/docs/0.9.0/tutorial/Basic/azure_kinect.html


### lidar books

https://www.goodreads.com/book/show/42996145-lidar-point-cloud-data-processing-and-applications

### jupyter viz

https://mapbox-mapboxgl-jupyter.readthedocs-hosted.com/en/latest/index.html

https://gist.githubusercontent.com/kapadia/6359528/raw/b97fe6b8e7d879d07d71603791fe818475ad7ba3/Ruse%2520IPython%2520Notebook

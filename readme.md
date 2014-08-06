# Tessellator

Django (1.6) web app for serving map tiles. 


## Configuration & Setup

Basic setup. 

```
$ git clone tessellator
$ python -m virtualenv tessellator-env
$ /path/to/tessellator-env/bin/activate
$ cd tessellator
$ pip install -r requirements.txt

```

Edit `settings.py`, change `MBTILES_ROOT` around line 91 to the local filesystem path that you are storing you *.mbtiles files. 

The folder structure should look like this: 

```
/path/to/tiles/
	file1.mbtiles
	file2.mbtiles
	group-a/
		file3.mbtiles
		file4.mbtiles
	group-b/
		file5.mbtiles
```

If there is a logical grouping of mbtiles databases, then they can be put in sub folders as above. 

## Using the Tiles

XYZ tiles are available at: 
	
	http://server/tiles/filename/%{z}/%{y}/%{x}.png

Grids (if present) are available at: 
	
	http://server/tiles/filename/%{z}/%{y}/%{x}.grid.json

A preview of the map is: 

	http://server/tiles/filename.png

Tile json:

	http://server/tiles/filename.json


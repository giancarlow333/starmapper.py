# starmapper.py

This Python script takes in a CSV file of 3D coordinates of stars and converts them to a 2D map.  This is designed in particular for science fiction writers and game masters.

## Usage

Download the script and invoke it on the command line.  Type `python3 starmapper.py -h` for help.

You may need to install dependencies:
	`pip install svgwrite`,
	`pip install pandas`

The input file must be a CSV file of the following format:

	`NAME,SPECTRAL TYPE,X,Y,Z`

The first row *must* include those column headers!  The names are hard-coded into the script.

A sample input file, `sample_file.csv`, is provided as an example.  If no input file is specified in the command line, this file is used by default.

The program will produce an image like this:

## Future development goals

Currently, when you click on the produced image, only the first quadrant is shown.  The other quadrants are *produced*, but are not visible.  You need to redraw the bounds using other software; I use [Inkscape](https://inkscape.org/).  I hope to fix this in the future.

## Technologies used

* [SVGWrite](https://pypi.org/project/svgwrite/) is used to create the SVG file
* [Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) is used to process the CSV file

---

(c) 2024 Giancarlo Whitaker

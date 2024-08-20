# starmapper.py

This Python script takes in a CSV file of 3D coordinates of stars and converts them to a 2D map.  This is designed in particular for science fiction writers and game masters.

## Usage

Download the script and invoke it on the command line.

TK.

You may need to install dependencies:
	`pip install svgwrite`
	`pip install pandas`

## Development goals

1. ~Script reads in a CSV file~~
2. ~~For each row in the file:~~
	1. ~~Place a circle at the X and Y coordinates~~
	2. ~~Color the circle based on its spectral type~~
	3. ~~Place text near the circle with the star's name and Z coordinate in parens~~
4. Resize the screen so everything is visible
5. Add a grid
6. Add a dark mode

## Technologies used

* [SVGWrite](https://pypi.org/project/svgwrite/) is used to create the SVG file
* [Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) is used to process the CSV file

---

(c) 2024 Giancarlo Whitaker

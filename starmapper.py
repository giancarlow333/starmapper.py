import argparse
import math
import pandas as pd
import svgwrite as svg

parser = argparse.ArgumentParser(description="This program reads an SVG file and uses it to create a 2D star map.", epilog="(c) 2024 Giancarlo Whitaker")
parser.add_argument("-i", '--input', nargs=1, type=argparse.FileType('r'), help="input file name")
parser.add_argument("-o", '--output', nargs=1, type=argparse.FileType('a'), help="output to specified file")
parser.add_argument('-g', '--grid', action='store_true', help="print a grid (optional)")
parser.add_argument('-d', '--dark', action='store_true', help="activate dark mode (optional)")

args = parser.parse_args()

if args.input:
	inFile = args.input[0].name
else:
	inFile = "sample_file.csv"
if args.output:
	outFile = args.output[0].name
else:
	outFile = "output.svg"

# Dark mode
if args.dark:
	print("Dark mode not yet implemented")

# read the file
df = pd.read_csv(inFile)

# Find the size of the bounding box
max_x = df.max(axis=0)["X"]
max_y = df.max(axis=0)["Y"]
min_x = df.min(axis=0)["X"]
min_y = df.min(axis=0)["Y"]
print(min_y)
print(type(min_y))
maxmin = list((max_x, max_y, abs(min_x), abs(min_y)))
print(maxmin)
true_max = math.ceil(max(maxmin))
print(true_max)

# Create SVG file
dwg = svg.Drawing(outFile)

# Add stylesheet
dwg.embed_stylesheet(".star { stroke: black; stroke-width: 0.1 } .o-star { fill: lightblue; } .b-star { fill: blue; } .a-star, .d-star { fill: white; } .f-star { fill: lightyellow; } .g-star { fill: yellow; } .k-star { fill: orange; } .m-star { fill: red; } lty-star { fill: darkred; }")


# Create grid
if args.grid:
	true_max *= 10
	hlines = dwg.add(dwg.g(id="hlines", stroke="lightgray"))
	for y in range(-true_max, true_max + 10, 10):
		hlines.add(dwg.line(start=(-true_max, y), end=(true_max, y)))
	vlines = dwg.add(dwg.g(id="vlines", stroke="lightgray"))
	for x in range(-true_max, true_max + 10, 10):
		hlines.add(dwg.line(start=(x, -true_max), end=(x, true_max)))


for index, row in df.iterrows():
	# Scale X, Y values
	x_value = 10*row["X"]
	y_value = 10*row["Y"]

	# Create star
	star = dwg.circle(center=(x_value, y_value), r="2", class_="star")

	# Determine spectral class and create stars
	spectral = row["SPECTRAL TYPE"]
	spectral = spectral[0]
	if spectral == "O":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star o-star")
	elif spectral == "B":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star b-star")
	elif spectral == "A":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star a-star")
	elif spectral == "F":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star f-star")
	elif spectral == "G":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star g-star")
	elif spectral == "K":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star k-star")
	elif spectral == "M":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star m-star")
	elif spectral == "L" or spectral == "T" or spectral == "Y":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star lty-star")
	elif spectral == "D":
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star d-star")
	else:
		star = dwg.circle(center=(x_value, y_value), r="2", class_="star g-star")

	# Add star to map
	dwg.add(star)

	# Prepare for text placement
	x_value += 3
	y_value += 3
	z_value = round(row["Z"], 0)

	# if Z is greater than 0, add a plus sign
	if z_value >= 0:
		text_to_use = row["NAME"] + " (+" + str(int(z_value)) + ")"
	else:
		text_to_use = row["NAME"] + " (" + str(int(z_value)) + ")"

	# Create text object
	text = dwg.text(text_to_use, insert=(x_value, y_value), style="font-size: 3px; font-family: sans")

	# Add text to map
	dwg.add(text)
# END LOOP
	
dwg.save() # Close the map

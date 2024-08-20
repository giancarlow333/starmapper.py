import argparse
import pandas as pd
import svgwrite as svg

parser = argparse.ArgumentParser(description="This program reads an SVG file and uses it to create a 2D star map.")
parser.add_argument("-i", '--input', nargs=1, type=argparse.FileType('r'), help="input file name")
parser.add_argument("-o", '--output', nargs=1, type=argparse.FileType('a'), help="output to specified file")

args = parser.parse_args()

if args.input:
	inFile = args.input[0].name
else:
	inFile = "sample_file.csv"
if args.output:
	outFile = args.output[0].name
else:
	outFile = "output.svg"

# read the file
df = pd.read_csv(inFile)

#print(df) # for testing

# Create SVG file
dwg = svg.Drawing(outFile)

# Add stylesheet
dwg.embed_stylesheet(".star { fill: yellow; stroke: black; stroke-width: 0.1 }")

for index, row in df.iterrows():
	# Scale X, Y values
	x_value = 10*row["X"]
	y_value = 10*row["Y"]

	# Determine spectral class
	spectral = row["SPECTRAL TYPE"]
	spectral = spectral[0]
	print(spectral)

	# Create star
	star = dwg.circle(center=(x_value, y_value), r="2", class_="star")

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

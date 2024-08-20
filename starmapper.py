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

print(df) # for testing

# Create SVG file
dwg = svg.Drawing(outFile)

# Add stylesheet
# dwg.embed_stylesheet(".star { fill: yellow; }")

for index, row in df.iterrows():
	star = dwg.circle(center=(10*row["X"], 10*row["Y"]), r="2", fill="yellow")
	dwg.add(star) # Add star to map
	
dwg.save() # Close the map

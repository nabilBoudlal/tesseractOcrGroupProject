"""Main script to be executed"""
import os.path
import parser
from ocr import text_recognition
from crafting import image_crafting

args = parser.parserprogram()
input_dir = 'input'
output_dir = 'results'

if __name__ == '__main__':
    print("Input dir: " + input_dir)
    print("Output dir: " + output_dir)

    for filename in os.listdir(input_dir):
        # crafting
        image_crafting(os.path.join(input_dir, filename))
        # ocr
        text_recognition()

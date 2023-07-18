import argparse


def parserprogram():
    parser = argparse.ArgumentParser(description='Process images with Tesseract.')
    parser.add_argument('input_folder', type=str, metavar='input_dir',
                        help='Path to the input folder containing images')
    parser.add_argument('output_folder', type=str, metavar='output_dir',
                        help='Path to the output folder for saving results')

    # Parsing degli argomenti da riga di comando
    args = parser.parse_args()

    return args

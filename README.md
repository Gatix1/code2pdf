# code2pdf
code2pdf is a Python script designed to assist students in the FBU-COMP1003 course in converting .c files into PDF format. This tool allows students to easily create PDF files from their program source code to meet the requirements for submitting answers in PDF format.

## Installation

Before using code2pdf, make sure you have the required dependencies installed by running the following command:

    pip install -r requirements.txt

## Usage

To use code2pdf, execute the following command:

    python code2pdf.py <input_folder_path> <output_folder_path>

Where:

    <input_folder_path> is the path to the folder containing .c files that you want to convert to PDF.
    <output_folder_path> is the path to the folder where the created PDF files will be saved.

Example usage:

    python code2pdf.py ./questions ./output

code2pdf will process all the .c files in the specified source code folder and generate corresponding PDF files in the specified output folder.

## Contributions

We welcome contributions to the development of the project. If you have suggestions, bug fixes, or improvements, feel free to create pull requests.

------
I hope this documentation helps you.

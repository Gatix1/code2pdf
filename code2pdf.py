import os
import sys
from fpdf import FPDF

# Function to convert a single .c file to a PDF
def convert_c_file_to_pdf(input_file, output_dir):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)

    # Read the content of the .c file
    with open(input_file, "r") as file:
        code = file.read()
        # Add the code to the PDF
        pdf.multi_cell(0, 10, code)

    # Get the base name of the input file (without the path)
    file_name = os.path.basename(input_file)

    # Output the PDF to the output directory
    output_pdf_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.pdf")
    pdf.output(output_pdf_path)

def main():
    try:
        input_directory = ""
        output_directory = ""

        # Reading arguments
        if len(sys.argv) == 3:
            input_directory = sys.argv[1]
            output_directory = sys.argv[2]
        else:
            print("Incorrect Usage!\nUsage: \"python code2pdf.py <input_folder_path> <output_folder_path>\"")
            return

        # Making output directory if it doesnt exist
        if not(os.path.exists(output_directory) and os.path.isdir(output_directory)):
            os.makedirs(output_directory)

        # List all .c files in the input directory
        c_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith(".c")]

        # Convert each .c file to a separate PDF
        for c_file in c_files:
            convert_c_file_to_pdf(c_file, output_directory)

        print("Converting finished successfully!")
    except Exception:
        print(Exception)


if __name__ == '__main__':
    main()
from win32com import client
import os


def convert_trees_to_pdf():
    file_list = os.listdir(r'C:\Users\saone\Documents\Python Stuff\prod\single_elimination_tree_generator\refined_divisions')


    for file in file_list:
        dot_index = file.index('.')
        file_name_adj = file[0:dot_index]
        pdf_string = ".pdf"
        xlsx_string = ".xlsx"

        input_base = r'C:\Users\saone\Documents\Python Stuff\prod\single_elimination_tree_generator\refined_divisions'
        input_file = os.path.join(input_base, file_name_adj + xlsx_string)

        output_base = r'C:\Users\saone\Documents\Python Stuff\prod\single_elimination_tree_generator\refined_divisions_pdfs'
        output_file = os.path.join(output_base, file_name_adj + pdf_string)

        app = client.DispatchEx("Excel.Application")
        app.Interactive = False
        app.Visible = False
        Workbook = app.Workbooks.Open(input_file)
        try:
            Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
        except Exception as e:
            print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
            print(str(e))
        finally:
            Workbook.Close()
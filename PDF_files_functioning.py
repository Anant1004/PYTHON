from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["E:/AK programs/.vscode/python/pdf_files/file_1.pdf", "E:/AK programs/.vscode/python/pdf_files/file_2.pdf", "E:/AK programs/.vscode/python/pdf_files/file_3.pdf"]:
    merger.append(pdf)

merger.write("E:/AK programs/.vscode/python/pdf_files/merged-pdf.pdf")
merger.close()
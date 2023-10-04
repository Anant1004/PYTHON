from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["file_1.pdf", "file_2.pdf", "file_3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
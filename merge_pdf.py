from pypdf import PdfMerger

pdfs = ['E:/AK programs/.vscode/python/pdf_files/do.pdf', 'E:/AK programs/.vscode/python/pdf_files/do2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
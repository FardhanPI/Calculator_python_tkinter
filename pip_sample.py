import pdfkit

# Configure the path to the wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

# Convert the web page to a PDF file
pdfkit.from_url('https://www.google.com', 'out.pdf', configuration=config)

pdfkit.from_url('https://fardhanpi.github.io/Calculator/','sample.pdf',configuration=config)

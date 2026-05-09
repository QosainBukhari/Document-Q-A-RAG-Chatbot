from src.ingestion.pdf_loader import PDFLoader

loader = PDFLoader("test/Ml_book.pdf")

text = loader.load_pdf()

print(text[:1000])
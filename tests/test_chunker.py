from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import TextChunker

loader=PDFLoader('test/Ml_book.pdf')
text = loader.load_pdf()

chunker = TextChunker()

chunks = chunker.create_chunks(text)

print(f"Total chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")
print(chunks[0])
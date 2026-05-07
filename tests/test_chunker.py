from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import TextChunker

loader=PDFLoader('data/raw/NIPS-2017-attention-is-all-you-need-Paper.pdf')
text = loader.load_pdf()

chunker = TextChunker()

chunks = chunker.create_chunks(text)

print(f"Total chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")
print(chunks[0])
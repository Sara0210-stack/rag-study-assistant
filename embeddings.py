from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

# load the PDF document 
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

model = SentenceTransformer('all-MiniLM-L6-v2')

for i,chunk in enumerate(chunks):
    embeddings = model.encode(chunk.page_content)
    print(f"\n-----Chunk {i+1} Embeddings-----")
    print(embeddings[:5])


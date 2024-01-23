from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from decouple import config
from langchain.chat_models import ChatOpenAI
KEY = config('OPENAI_API_KEY')

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=KEY)


def archive_loader_and_vectorizer():
    """ 
    This function loads txt documents from current directory 
    and vectorizes them
    """
    loader = DirectoryLoader('./', 
                            glob='**/teste.txt',
                            loader_cls=TextLoader,
                        )
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=30000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = chroma.Chroma.from_documents(docs, embedding_function)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    return retriever



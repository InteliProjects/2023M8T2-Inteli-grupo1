#! /usr/bin/env python3

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import  RunnablePassthrough
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma

from decouple import config

KEY = config('OPENAI_API_KEY')
class ChatBotModel(): 
    def __init__(self):
        self._model = ChatOpenAI(model="gpt-3.5-turbo", api_key=KEY)
        self._retriever = self.archive_loader_and_vectorizer()
        template = """Answer the questionin portuguese, and used the embeded data to answer,if you dont know the answer say youdont know, answwer based only on the following context:
        {context}
        Question: {question}
        """
        self._prompt = ChatPromptTemplate.from_template(template)

    def archive_loader_and_vectorizer(self):
        """ 
        This function loads txt documents from current directory 
        and vectorizes them
        """
        loader = DirectoryLoader('../', 
                                glob='**/teste.txt',
                                loader_cls=TextLoader,
                                show_progress=True
                            )
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=30000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = chroma.Chroma.from_documents(docs, embedding_function)
        retriever = vectorstore.as_retriever()
        return retriever
    
    def chat(self, text):
        chain = (
            {"context": self._retriever, "question": RunnablePassthrough()}
            | self._prompt
            | self._model
        )
        output_text = ""
        for s in chain.stream(text):
            output_text+=s.content
        return output_text





if __name__ == "__main__":
    llm = ChatBotModel()
    print(llm.chat("ondes esta o prego"))
    print("aa")
#! /usr/bin/env python3

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import  RunnablePassthrough
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma

import os
from dotenv import load_dotenv

load_dotenv()

class LLM_model():
    def __init__(self) -> None:
        self._model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
        self._retriever = self.archive_loader_and_vectorizer()
        template = """You are now responsible for managing a warehouse.
        I want you to respond as an expert in the field, providing short and direct answers to any questions asked of you.
        Answer the question based only on the following context:{context}, and find the right words to always choose one of the options from the context.
        Always respond in Portuguese.

        Question: {question}
        """
        self._prompt = ChatPromptTemplate.from_template(template)

    def archive_loader_and_vectorizer(self):
        """
        This function loads txt documents from current directory
        and vectorizes them
        """
        loader = DirectoryLoader('./',
                                glob='**/context.txt',
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
        return chain.invoke(text).content

#https://2023-m8-t2-grupo1-vinicioslugli.vercel.app/api/number/get/

from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrivalQA
import os
from langchain_community.llms import Ollama
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

working_dir = os.path.dirname((os.path.abspath((__file__))))

llm = Ollama(
    model="llama3:instruct",
    temprature = 0
)

embeddings = HuggingFaceEmbeddings()


def get_answer(file_name , query):

    file_path = f"{working_dir}/{file_name}"
    loader = UnstructuredFileLoader(file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(separator="/n",
                                          chunk_size=1000,
                                          chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)

    knowledge_base = FAISS.from_documents(text_chunks , embeddings)

    qa_chain = RetrivalQA.from_chain_type(
        llm,
        retriver = knowledge_base.as_retriever()
    )

    response = qa_chain.invoke({"query": query})

    return response['result']

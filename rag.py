import os
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from langchain.vectorstores import Pinecone as Pineconevs
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# pinecone
def pinecone_index(index_name="rizwan-aslam-rag-project"):
    embeddings = OpenAIEmbeddings()
    pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
    vector_store = Pineconevs.from_existing_index(index_name, embeddings)
    return vector_store
    
# gpt-4o-mini
def gpt_answer(vector_store, q, k=5):
    context = (
        "Instructions: You are a helpful assistant that answers questions based on the content of a document. "
        "The document contains information related to a person named Muhammad Rizwan Aslam"
        "Please provide a detailed and accurate response based on the content of the document. "
        "If the answer is not found in the document, kindly state that the information is not available.\n\n"
        f"Question: {q}"
    )
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.0)
    retriever = vector_store.as_retriever(search_type='similarity', search_kwards={'k': k})
    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    answer = chain.run(context)
    return answer
from dotenv import load_dotenv

load_dotenv()
import os

from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader

import pinecone

from testing_pinecone import init_pinecone

init_pinecone()

openai = OpenAI(
    model_name="text-davinci-003",
    openai_api_key=os.environ["OPENAI_API_KEY"],
)

loader = TextLoader("output.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()


index_name = "gptest"
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

query = "Who is Cezar?"
retrieved_docs = docsearch.similarity_search(query)


template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "I don't know".
Context: {context}
Question: {query}
Answer: """

prompt_template = PromptTemplate(
    input_variables=["context", "query"], template=template
)

responses = []
for doc in retrieved_docs:
    context = doc.page_content
    prompt = prompt_template.format(context=context, query=query)
    response = openai(prompt)
    responses.append(response)

print(responses)

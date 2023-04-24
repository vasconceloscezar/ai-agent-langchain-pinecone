import pinecone
from dotenv import load_dotenv

load_dotenv()
import os


def init_pinecone():
    pinecone.init(
        environment=os.environ["PINECONE_ENV"],
        api_key=os.environ["PINECONE_API_KEY"],
    )
    print("Pinecone initialized")


if __name__ == "__main__":
    init_pinecone()
    active_indexes = pinecone.list_indexes()
    print(active_indexes)

from sentence_transformers import SentenceTransformer

def search_vector(sentence):
    model = SentenceTransformer('sentence-transformers/stsb-xlm-r-multilingual')

    import pinecone
    pinecone.init(api_key='aacefed2-9c8c-437a-b8d9-31e96ba8f29a', environment='us-west1-gcp')

    index = pinecone.Index('books')

    query_sentence = sentence
    xq = model.encode(query_sentence).tolist()

    result = index.query(xq, top_k=10, includeMetadata=True)
    return result



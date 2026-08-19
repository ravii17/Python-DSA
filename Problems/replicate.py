# pipeline.py
def build_pipeline(raw_text: str) -> InMemoryVectorIndex:
    clean = load_document(raw_text)
    chunks = chunk_text(clean)
    vectors = embed_chunks(chunks)
    
    index = InMemoryVectorIndex()
    for chunk, vec in zip(chunks, vectors):
        index.add(vec, chunk)
    return index

def query_pipeline(index: InMemoryVectorIndex, question: str, top_k: int = 3) -> list[str]:
    q_vector = embed_query(question)
    return index.search(q_vector, top_k)
import ollama

def test_embedding_model(text):
    # Load the model
    embeddings = ollama.embed(
        model='nomic-embed-text:latest',
        input='Llamas are members of the camelid family',
    )
    return embeddings

if __name__ == "__main__":
    sample_text = "This is a test sentence for generating embeddings."
    embeddings = test_embedding_model(sample_text)
    print("Embeddings:", embeddings)
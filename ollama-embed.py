import ollama

def test_embedding_model(text):
    # Load the model
    model = ollama.load_model('path/to/your/model')

    # Generate embeddings for the input text
    embeddings = model.embed(text)

    return embeddings

if __name__ == "__main__":
    sample_text = "This is a test sentence for generating embeddings."
    embeddings = test_embedding_model(sample_text)
    print("Embeddings:", embeddings)
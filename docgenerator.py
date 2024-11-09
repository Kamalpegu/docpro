from nltk.tokenize import sent_tokenize

def generate_structured_content(text, keywords, document_type):
    """Generates structured content with optional section formatting"""
    sentences = sent_tokenize(text)
    keywords = [word.strip().lower() for word in keywords]

    structured_content = ""
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in keywords):
            structured_content += sentence + "\n"

    # Example: Structure based on document type 
    if document_type.lower() == "report":
        structured_content = f"## Section 1\n{structured_content}\n\n## Section 2\n{structured_content}" 
    elif document_type.lower() == "presentation":
        return structured_content

    return structured_content

from flask import Flask, render_template, request  # Flask libraries
import docgenerator  # Import your document generation module
import utils  # Import your text processing utilities

app = Flask(__name__)  # Create a Flask app object 

@app.route('/', methods=['GET', 'POST'])  # Routing for home page
def index():
    if request.method == 'POST':  # Handle POST request (form submission)
        text_input = request.form['text_input']
        keywords = request.form['keywords'].split(',') 
        document_type = request.form['document_type']
        
        cleaned_text = utils.clean_text(text_input) 
        generated_document = docgenerator.generate_structured_content(cleaned_text, keywords, document_type)
        
        # Optional: Write the document to a file (e.g., "generated_document.txt")
        # with open("generated_document.txt", "w") as file:
        #     file.write(generated_document) 

        return render_template('index.html', document=generated_document)
    
    # Render the form on initial GET request
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
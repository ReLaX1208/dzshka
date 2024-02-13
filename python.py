from docx import Document

def create_word_file(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("output.docx")

if __name__ == "__main__":
    text = input("Enter some text: ")
    create_word_file(text)
    print("Word file created successfully!")
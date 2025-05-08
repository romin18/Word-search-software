import os

def find_word_in_file(filepath, word):
    """
    Finds a word in a given file (txt, doc, pdf, or image with OCR using easyocr).
    """
    try:
        # For image files
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                import easyocr
                reader = easyocr.Reader(['en'])
                results = reader.readtext(filepath, detail=0)
                text = ' '.join(results)
                return word.lower() in text.lower()
            except ImportError:
                print("Missing 'easyocr'. Install it with: pip install --user easyocr")
                return False
            except Exception as e:
                print(f"Error processing image: {e}")
                return False

        elif filepath.lower().endswith('.txt'):
            with open(filepath, 'r', encoding="utf-8") as file:
                text = file.read()
                return word.lower() in text.lower()

        elif filepath.lower().endswith(('.doc', '.docx')):
            try:
                import docx2txt
                text = docx2txt.process(filepath)
                return word.lower() in text.lower()
            except ImportError:
                print("Missing 'docx2txt'. Install it with: pip install --user docx2txt")
                return False

        elif filepath.lower().endswith('.pdf'):
            try:
                import fitz
                doc = fitz.open(filepath)
                text = ""
                for page in doc:
                    text += page.get_text()
                return word.lower() in text.lower()
            except ImportError:
                print("Missing 'PyMuPDF'. Install it with: pip install --user pymupdf")
                return False

        else:
            print("Unsupported file type.")
            return False

    except FileNotFoundError:
        print("File not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# 🔽🔽🔽 INSERT YOUR FILE PATH AND WORD TO SEARCH HERE 🔽🔽🔽

file_path = "./example.jpg"     # ⬅️ Replace with your file path
search_word = "example"        # ⬅️ Replace with your word

# 🔍 Run search
if find_word_in_file(file_path, search_word):
    print(f"The word '{search_word}' was found in the file.")
else:
    print(f"The word '{search_word}' was not found in the file.")

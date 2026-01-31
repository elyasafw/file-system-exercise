import os

#2
def write_in_file():
    with open("./example.txt", "w", encoding="utf-8") as file:
        file.write("Hello world!")

write_in_file()


#3
def get_50_characters(file_path):
    if os.path.exists(file_path):     # פונקציה שבודקת אם הנתיב באמת קיים ומחזירה Ture או False
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read(50)
    else:
        return f"The file is not found in the path: {os.path.abspath(file_path)}"   # הופכת נתיב יחסי לנתיב אבסולוטי זה יכול לעזור להבין אם הנתבי באמת קיים או לא

characters_50 = get_50_characters("../README.md")
print(characters_50)


#4
def write_text_to_file(file_path, text):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        return True
    except Exception:
        return False

success = write_text_to_file(r"./example.txt", "The text was successfully written!")
print(f"Writing status: {success}")

failure = write_text_to_file(r"../fake_folder/failure.txt", "Writing failed..")
print(f"Writing status: {failure}")
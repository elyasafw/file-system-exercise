import shutil, string


#1
def print_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file: {file_name} not found..")

print_file(r"../README.md")


#2
def create_new_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

create_new_file(r"new_file.txt", "This is a file created in Practice Reading and Writing in Files 2")


#3
def copy_paste(source, destination):
    try:
        shutil.copyfile(source, destination)    # פונקציה המקבלת שם קובץ מקור ויעד ומעתיקה ומדביקה את התוכן (דורסת אם קיים קובץ יעד ויוצרת חדש אם לא)
        print(f"The file: '{source}' Successfully copied to: '{destination}'")
    except FileNotFoundError, PermissionError:
        print("Source file not found / no appropriate access permissions")

copy_paste(r"../README.md", r"./paste_file.txt")


#4
def count_lines(file_name):
    count = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                count = count + 1
        return count
    except FileNotFoundError:
        return "The file does not exist.."

count_readme = count_lines(r"../README.md")
print(count_readme)


#5
def count_exact_word(file_name, word_to_find):
    total_count = 0
    word_to_find = word_to_find.lower()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for char in string.punctuation:     # משתנה מחרוזת המכיל את כל תווי הסימנים
                    line = line.replace(char, " ")      # פונקציית להחלפת ערך במחזרות בערך אחר
                words_list = line.split()
                total_count += words_list.count(word_to_find)     # פונקציה המקבלת ערך לספירה
        return total_count
    except FileNotFoundError:
        return "The file does not exist.."


word_in_readme = count_exact_word(r"../README.md", "system")
print(word_in_readme)
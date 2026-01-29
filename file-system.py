import os

#1
def print_path():
    this_path = os.getcwd()    # מחזירה מחרוזת של נתיב התיקייה הנוכחי
    print(f"The current path is:  {this_path}")

print_path()


#2
def print_files():
    list_files = os.listdir()    # מחזירה רשימה של כל הקבצים בנתיב הנוכחי
    for item in list_files:
        print(f" - {item}")

print_files()


#3
def list_and_return(target_path):
    original_folder = os.getcwd()
    try:    # מנגנון בטיחות שבסוף נחזור לנתיב המקורי בסוף הריצה גם אם יש בעיה בנתיב
        os.chdir(target_path)    # משנה את תיקיית העבודה לנתיב החדש
        target_folder = os.getcwd()
        print(f"Switch to folder:  {target_folder}:")
        list_files = os.listdir()
        for item in list_files:
            print(f"- {item}")  
    finally:
        os.chdir(original_folder)
        print(f"\nWe returned to the folder:  {os.getcwd()}")

list_and_return(r"../") 


#4
def print_all_files(root_path):
    for current_root, subdirs, files in os.walk(root_path):    # עוברת על כל עץ התיקיות בנתיב ומחזירה: 1. נתיב התקייה הנוכחית, 2. תתי-התיקיות במיקום הנוכחי, 3. כל הקבצים במיקום הנוכחי
        print(f"\n-- Scanning the path:  {current_root} --")
        for filename in files:
            print(f"- {filename}")

print_all_files(r"../")


#5
def get_python_files(root_path):
    py_files = []
    for current_root, subdirs, files in os.walk(root_path):
        for filename in files:
            if filename.endswith(".py"):
                py_files.append(filename)
                
    return py_files

python_list = get_python_files(r"../")
for path in python_list:
    print(path)


#6
def count_file_extensions(root_path):
    stats = {}

    for current_root, subdirs, files in os.walk(root_path):
        for filename in files:
            extension = os.path.splitext(filename)[1].lower()    # פונקציה המפצלת את שם הקובת ל 2 חלקים: שם, סיומת כולל הנקודה
            if extension == "":
                extension = "No Extension"
            if extension in stats:
                stats[extension] += 1
            else:
                stats[extension] = 1
                
    return stats

result = count_file_extensions(r"../")
print(result)
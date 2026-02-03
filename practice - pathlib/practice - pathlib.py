from pathlib import Path


def creating_paths():
    current_dir = Path.cwd()
#a
    print(f"- a.  Current folder: {current_dir}")
    folder = current_dir / 'files'
    folder.mkdir(exist_ok=True)
#b
    file_path = folder / 'data.txt'
    file_path.touch()
    print(f"- b.  File created")
#c
    print(f"- c. The path of the folder: {file_path.parent}")
#d
    print(f"- d. the home folder: {Path.home()}")

creating_paths()


#2
def handle_notes_file(file_name):
    file_path = Path(file_name)
    if file_path.exists():
        print("The file exists!")
    else:
        file_path.write_text('This is a new file created by pathlib', encoding="utf-8")
    content = file_path.read_text(encoding="utf-8")
    print(f"New file content:\n{content}")

handle_notes_file("notes.txt")


#3
def analyze_path(path_str):
    path = Path(path_str)
    print(f"• File name with extension: {path.name}")
    print(f"• File name without extension: {path.stem}")
    print(f"• The file extension {path.suffix}")
    print(f"• Parent folder: {path.parent}")
    
    print("• All folders in the path (parents):")
    for p in path.parents:
        print(f"  - {p}")

analyze_path('documents/reports/annual_report.pdf')
# הקובץ לא צריך להיות קיים. pathlib מבצעת ניתוח טקסטואלי של הנתיב כאובייקט, ללא קשר לתוכן הדיסק.


#4
def list_directory_contents():
    current_path = Path.cwd()
    dir_count = 0
    file_count = 0
    for item in current_path.iterdir():
        if item.is_dir():
            print(f"📁 [{item.name}]")
            dir_count += 1
        elif item.is_file():
            print(f"📄 [{item.name}]")
            file_count += 1
            
    print(f"\Found: {dir_count} folders | {file_count} files")

list_directory_contents()
#1
def get_lines_starting_with(file_path, search_prefix):
    prefix_matching = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(search_prefix):
                    prefix_matching.append(line.rstrip('\n'))  # ניקוי של \n בסוף שורה          
        return prefix_matching
    except Exception:
        return []

result = get_lines_starting_with(r"./exemple_files_2.txt", "Hello")
print(result) 


#2
def print_file_with_metadata(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.rstrip('\n')
                line_length = len(clean_line)
                print(f"{line_length} ** {clean_line} **")     
    except Exception as error:
        print(f"{error}")

print_file_with_metadata(r"./example_files_2.txt")
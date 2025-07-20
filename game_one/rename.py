import os

files_names = os.listdir("png")
for f_n in files_names:
    file_name = f_n.replace(" ", "")
    file_name = file_name.replace("(", "")
    file_name = file_name.replace(")", "")
    os.rename(f"png/{f_n}", f"png/{file_name}")

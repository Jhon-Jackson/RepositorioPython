import os
import shutil

folder_path = r"D:\jhow arquivos\Videos PvPs\Músicas Eletrônicas"

file_types = {
    "imagens" : [".jpg", ".jpeg", ".png", ".gif"],
    "Documents" : [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos" : [".mp4", ".mkv", ".mov"],
    "Music" : [".mp3", ".wav"],
    "Archives" : [".zip", ".rar", ".tar", ],
    "Projetos" : [".xcf"]
}

def organize_files():
    for file in os.listdir(folder_path):
        filename, ext = os.path.splitext(file)
        ext = ext.lower()

        for category, extensions in file_types.items():
           if ext in extensions:
               category_path = os.path.join(folder_path, category)
               if not os.path.exists(category_path):
                   os.mkdir(category_path)
               shutil.move(
                   os.path.join(folder_path, file),
                   os.path.join(category_path, file)
               )
               break
    print("Files organized successfully!")


organize_files()

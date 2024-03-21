import pandas as pd
import os
import glob

# caminho para ler os arquivos
folder_path = 'source\\raw_data\\'

# lista todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path , '*.xlsx'))

print(excel_files)
import pandas as pd
import os
import glob

# caminho para ler os arquivos
folder_path = 'source\\raw_data\\'

# lista todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path , '*.xlsx'))

# aqui printamos o arquivo, podemos ver que é um array completo
print(excel_files)

# aqui verificamos se or arquivos estão dentro do excel_files, caso não o arquivo não será encontrado
if not excel_files:
    print("Não arquivo não encontrado")
else:
# Aqui começamos o código, o dataframe irá receber nossas modificações e salva-lás
    new_dataframe = []    
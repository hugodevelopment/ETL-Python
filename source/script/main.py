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

# Aqui ele percorre os arquivos em excel no array excel_files
    for files in excel_files:
        try:
            # lendo os aquivos
            df_temp = pd.read_excel(files)
            # print("oi",df_temp)
            # pegando os nomes dos arquivos
            file_name = os.path.basename(files)
            print(file_name)

            if "brasil" in file_name.lower():
                df_temp["location"] =  "br"
            elif "france" in file_name.lower():
                df_temp["location"] =  "fr"
            elif "italia" in file_name.lower():
                df_temp["location"] in file_name.lower()

        except:
            print("sem arquivo")    

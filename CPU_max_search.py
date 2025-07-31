import pandas as pd
import numpy as np


        
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")

data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')

split_data_read = data["message"].str.split(';', expand=True)
navi_cpu_read = split_data_read.apply(lambda row: next((cell.strip() for cell in row if isinstance(cell, str) and 'navi=' in cell), None), axis=1)


navi_first_value = navi_cpu_read.str.extract(r'navi\s*=\s*([\d.]+)')
navi_first_value = navi_first_value.astype(float)
navi_max = np.max(navi_first_value)


print(f"max : {navi_max}")







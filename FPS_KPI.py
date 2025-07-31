import pandas as pd
import re
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


fps_parser_1 = data[data['ROW'].str.contains('[John1] fps', na=False, regex=False)].copy()
fps_parser_1['Extracted'] = fps_parser_1['ROW'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_3 = data[data['ROW'].str.contains('[John3] fps', na=False, regex=False)].copy()
fps_parser_3['Extracted'] = fps_parser_3['ROW'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_5 = data[data['ROW'].str.contains('[John5] fps', na=False, regex=False)].copy()
fps_parser_5['Extracted'] = fps_parser_5['ROW'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_8 = data[data['ROW'].str.contains('[John8] fps', na=False, regex=False)].copy()
fps_parser_8['Extracted'] = fps_parser_8['ROW'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)

John1_avg = fps_parser_1['Extracted'].mean()
John3_avg = fps_parser_3['Extracted'].mean()
John5_avg = fps_parser_5['Extracted'].mean()
John8_avg = fps_parser_5['Extracted'].mean()


print(f"John1 : {John1_avg}")
print(f"John3 : {John3_avg}")
print(f"John5 : {John5_avg}")
print(f"John8 : {John8_avg}")




    


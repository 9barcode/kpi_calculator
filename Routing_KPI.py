import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')

sentence_start = data[data['Row_1'].str.contains('Voice:', na=False)]

sentence_data = data[data['Row_1'].str.contains(r'\[ABC\] DEF\[ 0 \] : Hello', na=False)]

upstream_data = data[data['Row_1'].str.contains(r'#AD.*john', regex=True, na=False)]

BE_ID_data = data[data['Row_1'].str.contains(r'YD.*AB.*ID', regex=True, na=False)]








if not sentence_start.empty and not sentence_data.empty and not upstream_data.empty and not BE_ID_data.empty :
    first_sentence_start = sentence_start.iloc[0]['Row_2']
    first_sentence_data = sentence_data.iloc[0]['Row_2']
    first_upstream_data = upstream_data.iloc[0]['Row_2']

    first_BE_ID_data = BE_ID_data.iloc[0]['Row_2']

    
    time_diff_sentence = float(first_sentence_data) - float(first_sentence_start) # 완료 
    time_diff_upstream_BE_ID = float(first_BE_ID_data) - float(first_upstream_data) #완료

    print(f"Import Finish(Upstream - BE_ID):{time_diff_upstream_BE_ID}")

    print(f"Voice:{time_diff_sentence}")
    
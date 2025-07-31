import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')

search_start = data[data['Payload'].str.contains('NAV_SE_runQuery', na=False)]
search_end = data[data['Payload'].str.contains('NAV_SE_queryEntries', na=False)]


if not search_start.empty and not search_end.empty :
    first_search_start = search_start.iloc[0]['Timestamp']
    first_search_end = search_end.iloc[0]['Timestamp']
    
    
    time_diff_search_engine = float(first_search_end) - float(first_search_start)
    
    print(f"Search_engine: {time_diff_search_engine}")
    
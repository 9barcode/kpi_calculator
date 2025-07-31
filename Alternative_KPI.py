import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')

sentence_start = data[data['Row_1'].str.contains('fetduide:1234', na=False)]
# print(sentence_start['Timestamp'])
sentence_data = data[data['Row_1'].str.contains(r'\[ab\] cd\[ 0 \] : calculated', na=False)]
# print(sentence_data['Timestamp'])
upstream_data = data[data['Row_1'].str.contains(r'#fg.*df', regex=True, na=False)]
# print(upstream_data['Timestamp'])
BE_ID_data = data[data['Row_1'].str.contains(r'dg.*INFO.*sdf', regex=True, na=False)]
# print(BE_ID_data['Timestamp'])
search_start = data[data['Row_1'].str.contains('runQuery', na=False)]
search_end = data[data['Row_1'].str.contains('queryEntries', na=False)]

def safe_diff(a, b):
    try:
        diff = float(a or 0) - float(b or 0)  # None을 0으로 처리하고 뺄셈
        if diff < 0:  # 음수인 경우는 이상값으로 간주해 0 반환
            return 0
        return diff  # 양수이거나 0이면 정상값으로 반환
    except (ValueError, TypeError):  # 숫자 변환 실패 시
        return 0

if not sentence_start.empty and not sentence_data.empty and not upstream_data.empty and not BE_ID_data.empty:
    try:
        first_sentence_start = sentence_start.iloc[0]['Row_2'] 
    except IndexError:
        first_sentence_start = None
    try:
        first_sentence_data = sentence_data.iloc[0]['Row_2'] 
    except IndexError:
        first_sentence_data = None
    try:
        first_upstream_data = upstream_data.iloc[0]['Row_2'] 
    except IndexError:
        first_upstream_data = None
    try:    
        second_upstream_data = upstream_data.iloc[1]['Row_2'] 
    except IndexError: 
        second_upstream_data = None
    try:    
        third_upstream_data = upstream_data.iloc[2]['Row_2'] 
    except IndexError:
        third_upstream_data = None
    try: 
        forth_upstream_data = upstream_data.iloc[3]['Row_2'] 
    except IndexError:
        forth_upstream_data = None
    try :    
        first_BE_ID_data = BE_ID_data.iloc[0]['Row_2'] 
    except IndexError:
        first_BE_ID_data = None
    try :    
        second_BE_ID_data = BE_ID_data.iloc[1]['Row_2'] 
    except IndexError:
        second_BE_ID_data = None
    try:    
        third_BE_ID_data = BE_ID_data.iloc[2]['Row_2'] 
    except IndexError:
        third_BE_ID_data = None
    try:    
        forth_BE_ID_data = BE_ID_data.iloc[3]['Row_2'] 
    except IndexError:
        forth_BE_ID_data = None

# 이후 계산
time_diff_sentence = safe_diff(first_sentence_data, first_sentence_start)
first_upstream_BE_ID = safe_diff(first_BE_ID_data, first_upstream_data)
second_upstream_BE_ID = safe_diff(second_BE_ID_data, second_upstream_data)
third_upstream_BE_ID = safe_diff(third_BE_ID_data, third_upstream_data)
forth_upstream_BE_ID = safe_diff(forth_BE_ID_data, forth_upstream_data)


values = [
    first_upstream_BE_ID,
    second_upstream_BE_ID,
    third_upstream_BE_ID,
    forth_upstream_BE_ID
]

sum_of_routing_data = sum(values)

    
    
print(f"sum_of_routing_data:{sum_of_routing_data}")
print(f"voice:{time_diff_sentence}")
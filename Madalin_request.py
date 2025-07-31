import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


upstream_data = data['Row_1'].str.contains(r'#AD.*navi', regex=True, na=False)]

BE_ID_data = data[data['Row_1'].str.contains(r'DDP.*INFO.*BE_ID', regex=True, na=False)]

Route_calculation_start = data[data['Row_1'].str.contains(r'Marker.*Start_time', na=False)]
Route_calculation_finished = data[data['Row_1'].str.contains(r'Marker.*Finish_time', na=False)]
Route_calculation_changed = data[data['Row_1'].str.contains(r'\[WIN1\].*Change_time', na=False)]
downstream_first = data[data['Row_1'].str.contains(r'#Down.*waypoint', regex=True, na=False)]

print(f"Route_Calculation_Started : {Route_calculation_start.iloc[0]["Row_2"]}")
print(f"Route_Calculation_Finished : {Route_calculation_finished.iloc[0]["Row_2"]}")
print(f"Route has been changed_first : {Route_calculation_changed.iloc[0]["Row_2"]}")
print(f"upstream : {upstream_data.iloc[0]["Row_2"]}")
print(f"downstream : {downstream_first.iloc[0]["Row_2"]}")
print(f"BE_ID : {BE_ID_data.iloc[0]["Row_2"]}")
print(f"Route has been changed_second : {Route_calculation_changed.iloc[1]["Row_2"]}")








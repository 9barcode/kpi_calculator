import pandas as pd
import numpy as np
from pydlt import DltFileReader
import os

dlt_file_path = input("dlt 파일들이 저장된 경로를 입력하세요 : ").strip()
csv_file_path = input("csv 파일을 저장할 경로를 입력하세요 : ").strip()

result = []

# 모든 .dlt 파일 반복
for file_name in os.listdir(dlt_file_path):
    if file_name.endswith(".dlt"):
        full_path = os.path.join(dlt_file_path, file_name)
        print(f"converting...: {file_name}")
        
        try:
            for dlt in DltFileReader(full_path):
                if "cgroup cpu usage" in str(dlt.payload):
                    result.append({
          
                    "message": dlt.payload
                })
        finally:
            print("파일 처리 끝났습니다.")

dlt_parser = pd.DataFrame(result)
csv_convert = dlt_parser.to_csv(csv_file_path)

        
# file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
# file_name = input("파일명?.csv까지 붙여서: ")

# data = pd.read_csv(f"{file_path}/{file_name}", encoding='ISO-8859-1')
# # print(data.head(10))
# cpu_read = data[data['Payload'].str.contains(r'cgroup cpu usage', regex=True, na=False)]
# split_cpu_read = cpu_read['Payload'].str.split(';', expand=True)
# navi_cpu_read = split_cpu_read.apply(lambda row: next((cell.strip() for cell in row if isinstance(cell, str) and 'navi=' in cell), None), axis=1)
# # print(navi_cpu_read)
# navi_first_value = navi_cpu_read.str.extract(r'navi\s*=\s*([\d.]+)')
# navi_max = np.max(navi_first_value)


# print(f"max : {navi_max}")






# # print(cpu_read)









# if not upstream_data.empty and not BE_ID_data.empty and not Route_calculation_start.empty and not Route_calculation_finished.empty and not Route_calculation_changed.empty:
#     first_upstream_data = upstream_data.iloc[0]['Timestamp']
#     first_downstream_data = downstream_first.iloc[0]['Timestamp']
#     first_BE_ID_data = BE_ID_data.iloc[0]['Timestamp']
#     first_route_start = Route_calculation_start.iloc[0]['Timestamp']
#     first_route_finished = Route_calculation_finished.iloc[0]['Timestamp']
#     first_route_changed = Route_calculation_changed.iloc[0]['Timestamp']
#     Second_route_changed = Route_calculation_changed.iloc[1]['Timestamp']
    
 
#     time_diff_upstream_BE_ID = float(first_BE_ID_data) - float(first_upstream_data) #완료
#     time_diff_onboard_calculation = float(first_route_finished) - float(first_route_start) #완료
#     time_diff_display_onboard_route = float(first_route_changed) - float(first_route_finished) #완료
#     time_diff_BE_calculation_Time = float(first_downstream_data) - float(first_upstream_data) #완료
#     time_diff_show_be_route = float(Second_route_changed)-float(first_BE_ID_data) #완료 
    
    
# print(f"Onboard Calculation Time:{time_diff_onboard_calculation}")
# print(f"Display Onboard Route : {time_diff_display_onboard_route}")
# print(f"BE Calculation Time : {time_diff_BE_calculation_Time}")
# print(f"Import Finish(Upstream - BE_ID):{time_diff_upstream_BE_ID}")
# print(f"Show BE Route:{time_diff_show_be_route}")
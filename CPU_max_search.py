import pandas as pd
import numpy as np


        
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")

data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')
# print(data.head(10))
# cpu_read = data[data['Payload'].str.contains(r'cgroup cpu usage', regex=True, na=False)]
split_data_read = data["message"].str.split(';', expand=True)
navi_cpu_read = split_data_read.apply(lambda row: next((cell.strip() for cell in row if isinstance(cell, str) and 'navi=' in cell), None), axis=1)
# print(navi_cpu_read)

navi_first_value = navi_cpu_read.str.extract(r'navi\s*=\s*([\d.]+)')
navi_first_value = navi_first_value.astype(float)
navi_max = np.max(navi_first_value)


print(f"max : {navi_max}")






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
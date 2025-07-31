import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


upstream_data = data[data['Payload'].str.contains(r'#UPSTREAM.*navigation', regex=True, na=False)]
# print(upstream_data['Timestamp'])
BE_ID_data = data[data['Payload'].str.contains(r'RoutingSuccess.*INFO.*BE_ID', regex=True, na=False)]
# print(BE_ID_data['Timestamp'])
Route_calculation_start = data[data['Payload'].str.contains(r'KPI_MARKER.*NAV_Route_Calculation_Started', na=False)]
Route_calculation_finished = data[data['Payload'].str.contains(r'KPI_MARKER.*NAV_Route_Calculation_Finished', na=False)]
Route_calculation_changed = data[data['Payload'].str.contains(r'\[WIN1\].*Route has been changed', na=False)]
downstream_first = data[data['Payload'].str.contains(r'#DOWNSTREAM.*routeWaypoint', regex=True, na=False)]

print(f"NAV_Route_Calculation_Started : {Route_calculation_start.iloc[0]["Timestamp"]}")
print(f"NAV_Route_Calculation_Finished : {Route_calculation_finished.iloc[0]["Timestamp"]}")
print(f"Route has been changed_first : {Route_calculation_changed.iloc[0]["Timestamp"]}")
print(f"upstream : {upstream_data.iloc[0]["Timestamp"]}")
print(f"downstream : {downstream_first.iloc[0]["Timestamp"]}")
print(f"BE_ID : {BE_ID_data.iloc[0]["Timestamp"]}")
print(f"Route has been changed_second : {Route_calculation_changed.iloc[1]["Timestamp"]}")







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


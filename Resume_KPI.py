import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명?: ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


NAV_Map_Route_Finished = data[data['Payload'].str.contains('NAV_MAP_Route_Render_Finished', na=False)]



if not NAV_Map_Route_Finished.empty:
    maprendering = float(NAV_Map_Route_Finished.iloc[-1]['Timestamp'])
else:
    maprendering = None


    

    
print(f"NAV_MAP_Route_Render_Finished : {maprendering}")
    
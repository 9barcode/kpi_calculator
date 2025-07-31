import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


NAV_MapInitialRenderingFinished = data[data['Payload'].str.contains('NAV_MapInitialRenderingFinished_0', na=False)]
NAV_DestinationInput = data[data['Payload'].str.contains('NAV_DestinationInput', na=False)]
fullcontents = data[data['Payload'].str.contains('NVMD_NAV_Full_Contents_Display', na=False)]


if not NAV_MapInitialRenderingFinished.empty:
    maprendering = float(NAV_MapInitialRenderingFinished.iloc[0]['Timestamp'])
else:
    maprendering = None

if not NAV_DestinationInput.empty:
    destinationinput = float(NAV_DestinationInput.iloc[0]['Timestamp'])
else:
    destinationinput = None

if not fullcontents.empty:
    fullcontents_POI = float(fullcontents.iloc[0]['Timestamp'])
else:
    fullcontents_POI = None

    

    
    
    
    print(f"NAV_MapInitialRenderingFinished : {maprendering}")
    print(f"NVMD_NAV_Full_Contents_Display: {fullcontents_POI}")
    print(f"NAV_DestinationInput: {destinationinput}")
    
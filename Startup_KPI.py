import pandas as pd
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


NAV_MapInitialRenderingFinished = data[data['Row_1'].str.contains('Content_1', na=False)]
NAV_DestinationInput = data[data['Row_1'].str.contains('Content_2', na=False)]
fullcontents = data[data['Row_1'].str.contains('Content_3', na=False)]


if not NAV_MapInitialRenderingFinished.empty:
    maprendering = float(NAV_MapInitialRenderingFinished.iloc[0]['Row_2'])
else:
    maprendering = None

if not NAV_DestinationInput.empty:
    destinationinput = float(NAV_DestinationInput.iloc[0]['Row_2'])
else:
    destinationinput = None

if not fullcontents.empty:
    fullcontents_POI = float(fullcontents.iloc[0]['Row_2'])
else:
    fullcontents_POI = None

    

    
    
    
    print(f"Content_1 : {maprendering}")
    print(f"Content_2: {fullcontents_POI}")
    print(f"Content_3: {destinationinput}")
    
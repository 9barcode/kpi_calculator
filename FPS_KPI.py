import pandas as pd
import re
file_path = input("CSV 파일이 있는 폴더의 경로를 입력하세요: ")
file_name = input("파일명? : ")
data = pd.read_csv(f"{file_path}/{file_name}.csv", encoding='ISO-8859-1')


fps_parser_1 = data[data['Payload'].str.contains('[WIN1] fps', na=False, regex=False)].copy()
fps_parser_1['Extracted'] = fps_parser_1['Payload'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_3 = data[data['Payload'].str.contains('[WIN3] fps', na=False, regex=False)].copy()
fps_parser_3['Extracted'] = fps_parser_3['Payload'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_5 = data[data['Payload'].str.contains('[WIN5] fps', na=False, regex=False)].copy()
fps_parser_5['Extracted'] = fps_parser_5['Payload'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)
fps_parser_8 = data[data['Payload'].str.contains('[WIN8] fps', na=False, regex=False)].copy()
fps_parser_8['Extracted'] = fps_parser_8['Payload'].str.extract(r'\(\s*([0-9.]+)\s*\)').astype(float)

win1_avg = fps_parser_1['Extracted'].mean()
win3_avg = fps_parser_3['Extracted'].mean()
win5_avg = fps_parser_5['Extracted'].mean()
win8_avg = fps_parser_5['Extracted'].mean()


print(f"WIN1 : {win1_avg}")
print(f"WIN3 : {win3_avg}")
print(f"WIN5 : {win5_avg}")
print(f"WIN8 : {win8_avg}")




# if not NAV_MapInitialRenderingFinished.empty:
#     maprendering = float(NAV_MapInitialRenderingFinished.iloc[0]['Timestamp'])
# else:
#     maprendering = None

# if not NAV_DestinationInput.empty:
#     destinationinput = float(NAV_DestinationInput.iloc[0]['Timestamp'])
# else:
#     destinationinput = None

# if not fullcontents.empty:
#     fullcontents_POI = float(fullcontents.iloc[0]['Timestamp'])
# else:
#     fullcontents_POI = None

    

    
    
    
    # print(f"NAV_MapInitialRenderingFinished : {maprendering}")
    # print(f"NVMD_NAV_Full_Contents_Display: {fullcontents_POI}")
    # print(f"NAV_DestinationInput: {destinationinput}")
    
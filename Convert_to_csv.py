import pandas as pd
import numpy as np
from pydlt import DltFileReader
import os

dlt_file_path = input("Worst case test 후 받은 dlt 경로를 입력하세요 : ").strip()
csv_file_path = input("csv 파일을 저장할 경로를 입력하세요 : ").strip()
csv_file_name = os.path.join(csv_file_path, "result.csv")

result = []

# .dlt 파일 목록 추출
dlt_files = [f for f in os.listdir(dlt_file_path) if f.endswith(".dlt")]
total_files = len(dlt_files)

# 모든 .dlt 파일 반복 + 진행률 출력
for idx, file_name in enumerate(dlt_files, start=1):
    full_path = os.path.join(dlt_file_path, file_name)
    progress = (idx / total_files) * 100
    print(f"[{idx}/{total_files}] ({progress:.1f}%) converting...: {file_name}")

    try:
        for dlt in DltFileReader(full_path):
            if "cgroup cpu usage" in str(dlt.payload):
                result.append({
                    "message": dlt.payload
                })
    finally:
        print("파일 처리 끝났습니다.")

# 결과 저장
dlt_parser = pd.DataFrame(result)
dlt_parser.to_csv(csv_file_name, index=False)
print(f"CSV 저장 완료: {csv_file_name}")

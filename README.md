#  KPI 자동화 계산기 (KPI Calculator Tool)

자동차 소프트웨어 테스트 업무 중 반복되는 KPI 계산, 결과 정리에 소요되는 시간을 절감하기 위해 개발한 Python 기반 자동화 도구입니다.  
Pandas 등 실무에서 사용하는 주요 기술을 적용하여 실제 업무에 투입 가능한 수준으로 구현되었습니다.


---

## 주요 기능

- ✔️ Excel/CSV 기반 KPI 자동 계산
- ✔️ 로그 정제 및 조건 필터링 기능
- ✔️ 계산 반복작업 자동화
- ✔️ GUI 없이 BAT 파일로 간단히 실행

---

## 🛠️ 사용 기술

| 분류 | 내용 |
|------|------|
| 언어 | Python 3.13 |
| 라이브러리 | Pandas, openpyxl, Pydlt |
| 배포 환경 | GitHub (Windows 기준 테스트) |
Alternative_KPI.py | 대체경로 시 경로계산 start - end 로그가 발생한 시간을 pandas로 추출하여 계산
Convert_to_csv.py | dlt log 전체를 한꺼번에 여는 경우에 viewer 프로그램이 터지는 경우가 있어 dlt log들을 전부 모아 필요한 값만 필터링하여 csv 형식으로 변경
CPU_max_search.py | convert_to_csv를 실행시켜 얻은 csv에서 cpu max에 대한 로그 필터를 적용 시켜 데이터 값 확인
KPI_calculator_endspec.bat | py 파일을 일일히 실행시키기 번거로워 bat 파일로 통합하여 간단하게 수행
Madalin_request.py | dlt log에서 특정한 로그에 대한 시간값에 대해 추출
mean.py | 각 테스트 항목에 대해 3~5번 이상 수행하여 평균값이 필요하므로 그에 필요한 평균 계산기
Resume_KPI.py | 특정 로그에 대한 시간값 측정
Routing_KPI.py | 경로 계산 start - end의 로그의 시간값을 추출하고 계산
Search_KPI.py | 검색 start - end의 로그를 필터하고 시간값을 추출하여 계산
Startup_KPI.py | 내비게이션 시작 시 로그를 필터하고 시간값 추출

---

## 📂 폴더 구조

```plaintext
kpi_calculator/
├── Alternative_KPI.py
├── Convert_to_csv.py
├── CPU_max_search.py
├── KPI_calculator_endspec.bat
├── Madalin_request.py
├── mean.py
├── Resume_KPI.py
├── Routing_KPI.py
├── Search_KPI.py
├── Startup_KPI.py
└── README.md
```


🎯 개발 배경
해당 도구는 실제 차량 내비게이션 QA 업무 중
KPI 계산, 반복 데이터 필터링 및 보고서 생성의 반자동화를 위해 개발되었습니다.
테스트 자동화 전환 및 데이터 기반 업무 개선을 위한 개인 역량 강화 프로젝트로 활용되었습니다.
실제 dlt log 내용을 넣지 않고 dummy 값들을 넣었습니다. 

🙋‍♂️ 개발자 정보
이름: Hyeongju Kwon

경력: 자동차 내비게이션 소프트웨어 QA

관심 분야: QA 자동화, Python 기반 도구 개발, 차량 소프트웨어 테스트

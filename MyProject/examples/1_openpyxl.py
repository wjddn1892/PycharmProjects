import openpyxl

# 엑셀파일 열기
wb = openpyxl.load_workbook('score.xlsx')

# 현재 Active Sheet 얻기
ws = wb.active  # 보통 첫번째 Sheet 은 Active Sheet, 이전 저장시 마지막에 선택된 것이 Active Sheet
# ws = wb.get_sheet_by_name("Sheet1")   # 더 안전

# 국영수 점수를 읽기
for r in ws.rows:
    row_index = r[0].row  # 행 인덱스
    kor = r[1].value
    eng = r[2].value
    math = r[3].value
    sum = kor + eng + math

    # 합계 쓰기
    ws.cell(row=row_index, column=5).value = sum

    print(kor, eng, math, sum)

# 엑셀 파일 저장
wb.save("score2.xlsx")
wb.close()
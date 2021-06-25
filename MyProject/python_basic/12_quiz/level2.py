names = ["이정우", "전시우", "유튜버1", "유튜버2"]

for name in names:
    with open(f"{name}.txt", "w", encoding="utf-8") as r:
        r.write(f"""안녕하세요 {name}님.

(주)정우출판 편집자입니다.

좋은 하루 보내세요.^^

감사합니다.""")
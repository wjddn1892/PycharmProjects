# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email import encoders
#
#
# # 보내는 사람 정보
# me = "wjddn1892@gmail.com"
# my_password = "powercable"
#
# # 로그인하기
# s = smtplib.SMTP_SSL('smtp.gmail.com')
# s.login(me, my_password)
#
# # 받는 사람 정보
# you = "wjddn1892@naver.com"
#
# # 메일 기본 정보 설정
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "제목입니다."
# msg['From'] = me
# msg['To'] = you
#
# # 메일 내용 쓰기
# content = "안녕하세요? 파이썬으로 보낸 메일입니다."
# part2 = MIMEText(content, 'plain')
# msg.attach(part2)
#
# # 메일 보내고 서버 끄기
# s.sendmail(me, you, msg.as_string())
# s.quit()


# 여러사람에게 메일 보내기
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "wjddn1892@gmail.com"
my_password = "powercable"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
email_list = ["wjddn1892@naver.com", "wjddn1892@naver.com"]

for you in email_list:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "추석기사 첨부"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "추석기사 첨부합니다."
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("../articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내기
    s.sendmail(me, you, msg.as_string())

# 다 끝나고 닫기
s.quit()
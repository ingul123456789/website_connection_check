from requests import get

websites = []
while True:
  y = input("연결 상태를 체크하기를 원하는 웹사이트 주소를 입력해주세요 그만 입력 하고 싶으시면 '정지'를 입력해주세요")
  if y == "정지":
    break
  else:
    websites.append(y)
results = {}
x = 0
response = 0
for website in websites:
  if not website.startswith("https://"):
    x = website
    website = f"https://{website}"
    print(f"{x}는 {website}로 수정되었습니다")
  response = get(website)
  print(response)
  if response.status_code == 200:
    results[website] = "ok"
  else:
    results[website] = "FAILED"

print(results)

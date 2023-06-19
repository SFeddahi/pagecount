from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

domain = "https://yourdomain.com/"

search = f"site:{domain}"

URL = f"https://www.google.com/search?q={search}"

result = requests.get(URL, headers = headers)    

soup = BeautifulSoup(result.content, 'html.parser')

total_results_text = soup.find("div", {"id": "result-stats"}).find(text = True, recursive = False)

results_num = ''.join([num for num in total_results_text if num.isdigit()])

print(results_num)

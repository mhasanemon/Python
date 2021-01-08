import requests
import bs4
data = requests.get('http://www.jnu.ac.bd/dept/portal/faculty/cse/faculty_members.html')

if data.status_code == requests.codes.ok:
    soup = bs4.BeautifulSoup(data.content,'html.parser')

    head = soup.select(".table.table-bordered.table-striped tr")
    print(head[0].get_text().strip())
   




from bs4 import BeautifulSoup
import requests
import csv

date = input("Enter the date in MM/DD/YYYY format : ")
url = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    
    championships = soup.find_all("div", {"class": "matchCard"})
    
    headers = ("البطولة","صاحب الأرض","الضيف","الوقت","النتيجة")    

    match_details = []

    def get_match_info(championship):

        championship_title = championship.find('h2').text.strip()

        teams = championship.find_all("p")
        times = championship.find_all("span" , {"class" : "time"})        
        scores = championship.find_all("span" , {"class" : "score"})

        for i in range(0, len(scores), 2):
            team1 = teams[i].text.strip()
            team2 = teams[i + 1].text.strip() if i + 1 < len(teams) else ""
            time = times[i // 2].text.strip() if (i // 2) < len(times) else ""
            score1 = scores[i].text.strip() if (i // 2) < len(scores) else ""
            score2 = scores[i+1].text.strip() if (i // 2) < len(scores) else ""

            match_details.append({
                "البطولة": championship_title,
                "صاحب الأرض": team1,
                "الضيف": team2,
                "الوقت": time,
                "النتيجة": f"{score1}-{score2}"
            })

    for championship in range (len(championships)):
        get_match_info(championships[championship])
        
    with open('D:\Documents\pyscrap\yallakora.csv', 'w', newline='', encoding='utf-8') as output:
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(match_details)
        print("file created")
    
main(url)

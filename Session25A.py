import requests
from bs4 import BeautifulSoup

# URL of the cricket data page
# url = "https://www.espncricinfo.com/"
url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/points-table-standings"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

teams = soup.find_all('span', class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.find_all('td', class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")

# List of Dictionaries
data = []

for idx in range(10):
    team_data = []
    data.append(team_data)

print("data:", data)

idx = 0
for team in teams:
    title = team.text.strip()
    data[idx].append(title)
    idx += 1
    # print(title)

print("data:", data)


team_idx = 0
idx = 0

for win in wins:
    num = win.text.strip()
    print(num)

    # identify and fix :)
    # if idx % 5 != 0:
    #     data[team_idx]['stats'].append(num)

    data[team_idx].append(num)
    idx += 1

    if idx % 8 == 0:
        print("Wow...")
        team_idx += 1

print("data finally:", data)


file = open("ipl-data-2022.csv", "a")
header = "TEAMS,M,W,L,T,N/R,NRR,For,Against\n"
file.write(header)

for info in data:

    csv = "{},{},{},{},{},{},{},{},{}\n"\
        .format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])

    file.write(csv)

    print(csv)

print("Check the File...")




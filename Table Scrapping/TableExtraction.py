import pandas as pd
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor
import requests

response = open('html_table.html','r').read()
# response = requests.get('URL')

# Way 1
soup = BeautifulSoup(response,'lxml')
table_chunk = soup.select('.tg')[0]
extractor = Extractor(table_chunk).parse()
extractor.write_to_csv(filename="DataExport.csv")

# df = pd.DataFrame(extractor.return_list()[1:],columns=extractor.return_list()[0])
# df.Robert = df.Robert.astype(int) + 10
# df.to_csv("DataExport.csv",index=False)


#Way 2
table_data = []
for tr_tags in table_chunk.find_all('tr'):
    td_data = []
    for td_tags in tr_tags.find_all('td'):
        td_data.append(td_tags.text.strip())
    table_data.append(td_data)
df = pd.DataFrame(table_data[1:],columns=table_data[0])
df.Robert = df.Robert.astype(int) + 10
df.to_csv("DataExport.csv",index=False)
df.to_csv("DataExport_withoutheader.csv",index=False,header=False)


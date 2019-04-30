from  bs4 import BeautifulSoup
soup_chunk = '''<div class="opskriften">
<p class="h3">Ingrediensliste</p>
<p></p>
<p><strong>Påskeæg med nougat (6 stk)</strong><br>150 g. marcipan <br>ca. 40 g. nougat<br>150 g. mørk chokolade <br>50 g. lys chokolade &nbsp;</p>'''

soup = BeautifulSoup(soup_chunk,'lxml')
requiredData = []
for tags in soup.find_all('p'):
    if tags.select('br'):
        contents = {}
        contents['MainItem'] = tags.select('strong')[0].text
        [i.decompose() for i in tags.select('strong')]
        contents['SubItems'] = [i.strip().replace("</p>",'') for i in str(tags).split("<br/>") if "<p>" not in i]
        requiredData.append(contents)
print(requiredData)

#[{'MainItem': 'Påskeæg med nougat (6 stk)', 'SubItems': ['150 g. marcipan', 'ca. 40 g. nougat', '150 g. mørk chokolade', '50 g. lys chokolade \xa0']}]

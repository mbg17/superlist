import requests
import re
r = requests.get(
    'https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
)
r.encoding = 'utf-8'
text = r.text
#print(text)
fi = re.finditer(
    r'<a class=".*?" href="(?P<url>[https:http]+://[www|*]+.\w+.[com|org|cn]+\w?).*?" target="_blank">(?P<text>\w+).*?</a>',
    #r'<div class="p-name"><a target="_blank" title="(?P<text>\w+).?*" href="(?P<url>.*).*?"><em>.*?</em><i class="promo-words">.*?</i></a></div>',
    text)
for i in fi:
    print(i.group('url'), i.group('text'))

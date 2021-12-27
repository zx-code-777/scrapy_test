import re

# .*贪婪匹配  .*?非贪婪匹配
# content = 'hello 1234567 world_this is a regex demp'
# # result = re.match('^he.*(\d+).*demp', content)
# result = re.match('^he.*?(\d+).*demp', content)
# print(result)
# print(result.group(1))

content = '''hello 1234567 
          world_this is a regex demp
          '''
# result = re.match('^he.*(\d+).*demp', content)
# result = re.match('^he.*?(\d+).*demp', content, re.S)
# print(result)
# print(result.group(1))

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# search方法返回第一个符合条件的目标
#result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result.group(1))
# print(result.group(2))

# findall方法全部符合条件的
#results = re.findall('<a.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# results = re.findall('<a.*?>?(\w+)</a>', html, re.S)
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])

# sub
context = 'sdsada231ft234124tg45a241'
context = re.sub('\d+', '',context)
print(context)




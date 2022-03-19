>>> dt = r.html.find('script[id="__state"]', first=True).text
>>> raw = dt.replace('os.__STATE=', '')
>>> data = json.loads(raw)
>>> data['PostStore']
start_point = response.css('script[id="__state"]').get()

start = start_point[32:]
data = json.loads(start[:22973])

country = response.css('img.inline.vMiddle.mr8').attrib['alt']
city = response.css('div.osBlack.block::text').getall()[2]
category = response.css('a.osBlack.block::text').getall()[2]
name = data['PostStore']['_post']['member']['full_name']
<!-- phone = data['PostStore']['_post']['local_phone'] -->
phone = data['PostStore']['_post']['member']['international_phone_number']

>>> data['PostStore']['_post']

.active > span:nth-child(1)
count = response.css('span.inline.mr15::text').getall()
"".join(count).split()[5]
response.css('.next ::attr(onclick)').get().split('?')[1].split('&')[0] # ?page=2

# if ad_selector:
        #     try:
        #         next_page = response.css('.next ::attr(onclick)').get().split('?')[1].split('&')[0]
        #         if next_page is not None:
        #             next_page = response.urljoin('?'+next_page)
        #             yield response.follow(url=next_page, headers = self.desktop_header, callback=self.parse_categories)
        #     except:
        #         next_page = response.css('.next ::attr(href)').get().split('?')[1].split('&')[0]
        #         if next_page:
        #             next_page = response.urljoin('?'+next_page)
        #             yield response.follow(url=next_page, headers = self.desktop_header, callback=self.parse_categories)
.pagination

eg = response.css('span.block.postLink.postSpanTitle.noEmojiText::attr(data-href)').getall()



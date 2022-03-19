import json
from datetime import datetime

import scrapy


class OpensooqSpiderSpider(scrapy.Spider):
    name = "opensooq-spider"
    mobile_header = {
    'authority': 'ae.opensooq.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'PHPSESSID=b1d395a38db616789bafae0fa32cff01; frf_cookie=1; at0=0fff83543f588f861d4b766d3412509ef72934c1c21e3e2ed235841c48f9807da%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22at0%22%3Bi%3A1%3Bi%3A1647292471%3B%7D; country=be22aadbf049a2fafbfe8fc58de444c99688c442d6f5eae5a4cce1bbe1c7a7d5a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22country%22%3Bi%3A1%3Bs%3A2%3A%22ae%22%3B%7D; _csrf=af9c3c684ba39a733e4b0fe593d73821bd6aec7fee7dc540ae96b4211b60115aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22iypePyybACo5UmAnjrPgG7UyNs2C7mRM%22%3B%7D; userInfo=j%3A%7B%22phone_number%22%3A%22%22%2C%22first_name%22%3A%22%22%2C%22M_email%22%3A%22%22%2C%22member_verification%22%3A0%2C%22id%22%3A0%2C%22isGuest%22%3Atrue%7D; tgt_ticket=4f24511657fe681469dd6efccc245dd0308e5534e6d325d4a6a7c2799c6da04e; tgt_timestamp=1647292101; device_uuid=a1789947-38c0-48d2-b8fb-805b74cb2bc7; countryAbbrv=ae; first_time_visit=dbe227f33a791522a308a1b922497131f14ce1a90b6b6401ff229fb557f07836a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22first_time_visit%22%3Bi%3A1%3Bb%3A1%3B%7D; ss_pulse=a8f5f0d4091ea53b9be799e64d341242eb5725f2a494aa1337f0c19ccd85568fa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22ss_pulse%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D',
}
    desktop_header = {
    'authority': 'ae.opensooq.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'frf_cookie=1; country=be22aadbf049a2fafbfe8fc58de444c99688c442d6f5eae5a4cce1bbe1c7a7d5a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22country%22%3Bi%3A1%3Bs%3A2%3A%22ae%22%3B%7D; userInfo=j%3A%7B%22phone_number%22%3A%22%22%2C%22first_name%22%3A%22%22%2C%22M_email%22%3A%22%22%2C%22member_verification%22%3A0%2C%22id%22%3A0%2C%22isGuest%22%3Atrue%7D; tgt_ticket=4f24511657fe681469dd6efccc245dd0308e5534e6d325d4a6a7c2799c6da04e; tgt_timestamp=1647292101; device_uuid=a1789947-38c0-48d2-b8fb-805b74cb2bc7; countryAbbrv=ae; first_time_visit=dbe227f33a791522a308a1b922497131f14ce1a90b6b6401ff229fb557f07836a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22first_time_visit%22%3Bi%3A1%3Bb%3A1%3B%7D; ss_pulse=a8f5f0d4091ea53b9be799e64d341242eb5725f2a494aa1337f0c19ccd85568fa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22ss_pulse%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; PHPSESSID=12ca288fe7b61bdb746ddbd7e0b23fca; at0=6a79b18c74b40c560306f5a17c7839e84d5ad3d49f0f35be57383caa7132a8b1a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22at0%22%3Bi%3A1%3Bi%3A1647627319%3B%7D; _csrf=1ecb7c0f514e3a8476fb18984b55fb9f7826888b8fdd9b042c96b795e895a98ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22tN3eQsfAhKE7aYhkDWuIefZilJNxo8hA%22%3B%7D; RVP=173940653,0; RVPTime={"173940653":"3/18/2022, 9:15:31 PM"}',
    'if-none-match': 'W/"22985-AybHe9V/JH1w78U8GUNzOberVFA"',
}

    def __init__(self):
        self.listing_count = ""

    def start_requests(self):
        url = "https://www.opensooq.com/en?ref=change_country_sa"

        yield scrapy.Request(
            url,
            headers=self.desktop_header,
            callback=self.parse_countries,
        )

    def parse_countries(self, response):
        countries_selector = response.css("a.block")
        country_list = [c.attrib["href"] + "/find" for c in countries_selector]
        if 'https://www.opensooq.com/find' in country_list:
                country_list.remove('https://www.opensooq.com/find')
        for country in country_list:
            yield scrapy.Request(
                country,
                headers=self.desktop_header,
                callback=self.parse_categories,
            )

    def parse_categories(self, response):
        ad_list = []
        ad_selector = response.css('a.block.postLink.notEg.postSpanTitle.noEmojiText::attr(href)').getall()
        eg_ad_selector = response.css('span.block.postLink.postSpanTitle.noEmojiText::attr(data-href)').getall()
        if ad_selector:
            for links in ad_selector:
                ad_list.append(response.urljoin(links))
        else:
            for links in eg_ad_selector:
                ad_list.append(response.urljoin(links))
        count = response.css('span.inline.mr15::text').getall()
        self.listing_count = "".join(count).split()[5]
        current_page = response.css('.active ::text').get()
        total_pages = 50

        if current_page:
            if int(current_page) == 1:
                for i in range(2, total_pages):
                    yield response.follow(
                        url=response.url + f"?sort=record_posted_date.desc&page={i}&per-page=30",
                        headers=self.desktop_header,
                        callback=self.parse_categories,
                    )
        for ad in ad_list:
            yield scrapy.Request(
                ad,
                headers=self.mobile_header,
                callback=self.parse_listings,
            )

        

    def parse_listings(self, response):
        item = {}
        item["country"] = response.css("img.inline.vMiddle.mr8").attrib["alt"]
        item["city"] = response.css("div.block:nth-child(2)::text").get()
        item["category"] = response.css(
            "ul.customParams:nth-child(2) > li:nth-child(3) > a:nth-child(2)::text"
        ).get()
        item["listing_count"] = self.listing_count
        selector = response.css('script[id="__state"]').get()
        cleaned_data = selector.replace('<script id="__state">os.__STATE=', "").replace(
            "</script>", ""
        )
        data = json.loads(cleaned_data)
        try:
            item["phone_number"] = data["PostStore"]["_post"]["phone"]
            item["ad_owner_name"] = data["PostStore"]["_post"]["member"]["full_name"]
            item["listing_title"] = data["PostStore"]["_post"]["title"]
            dt_obj = data["PostStore"]["_post"]["record_posted_date_timestamp"]
            item["listing_date"] = datetime.fromtimestamp(dt_obj).strftime("%d-%m-%y")
        except:
            item["phone_number"] = ""
            item["ad_owner_name"] = ""
            item["listing_title"] = ""
            item["listing_date"] = ""

        yield item

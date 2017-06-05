class BillSpider(scrapy.Spider):
    name = "bills"
    start_urls = [
        'http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180AB378',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

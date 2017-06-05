import scrapy


class VotesSpider(scrapy.Spider):
    name = "votes"

    def start_requests(self):
        urls = [
            'http://leginfo.legislature.ca.gov/faces/billVotesClient.xhtml?bill_id=201720180AB378',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        bill_query = response.url.split("?")[1]
        bill_id = bill_query.split('=')[1]
        filename = 'votes-bill-id-%s.html' % bill_id
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
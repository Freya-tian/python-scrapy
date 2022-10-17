import scrapy
from articleSpider.items import HabrItem

class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/search/page1/?q=react&target_type=posts&order=relevance']

    def parse(self, response):
        filename = 'habr.html'
        open(filename,'wb+').write(response.body)
        for each in response.xpath("//div[@class='tm-articles-list']/article"):
            item=HabrItem()
            publisher=each.xpath("div[@class='tm-article-snippet']//a[@class = 'tm-user-info__username']/text()").extract()[0]
            titlecontainer=each.xpath("div[@class='tm-article-snippet']/h2/a/span")
            title = titlecontainer[0].xpath('string(.)').extract()[0]
            cuttextcontainer = each.xpath("div[@class='tm-article-snippet']/div[@class='tm-article-body tm-article-snippet__lead']/div")
            cuttext = cuttextcontainer[0].xpath('string(.)').extract()[0]
            link = each.xpath("div[@class='tm-article-snippet']/h2/a/@href").extract()[0]
            item['publisher']=publisher
            item['title']=title
            item['cuttext']=cuttext
            item['link']=link
            yield item 
            try:
               for i in range(2,50):
                     yield scrapy.Request(url='https://habr.com/ru/search/page'+str(i)+"/?q=react&target_type=posts&order=relevance",callback = self.parse)
            except:
               print("downloaded...")


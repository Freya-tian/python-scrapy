import scrapy
from articleSpider.items import ArticlespiderItem 

class CyberleninkSpider(scrapy.Spider):
    name= 'cyberlenink'
    allowed_domains = ['cyberleninka.ru']
    start_urls = ('https://cyberleninka.ru/article/c/computer-and-information-sciences',)

    def parse(self, response):
        items=[]
        '''filename = 'text.html'
        open(filename,'wb+').write(response.body)
        '''
        for each in response.xpath("//ul[@class='list']/li"):
                item=ArticlespiderItem()
                name=each.xpath("a/div[@class='title']/text()").extract()[0]
                writerandTime=each.xpath("a/span/text()").extract()[0]
                listTandW = writerandTime.split('/',1)
                writer = listTandW[1]
                time=listTandW[0]
                url="https://cyberleninka.ru/article/" + each.xpath("a/@href").extract()[0]
                item['articleName']=name
                item['articleWriter']=writer
                item['articleTime']=time
                item['articleUrl']=url
                yield item 
        try:
           for i in range(2,3530):
             yield scrapy.Request(url='https://cyberleninka.ru/article/c/computer-and-information-sciences/'+ str(i),callback = self.parse)
        except:
           print("downloaded...")
       
        
        
       
        

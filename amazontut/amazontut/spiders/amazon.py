import scrapy
from ..items import AmazontutItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page=2
    start_urls = ['https://www.amazon.com/s?bbn=17&rh=n%3A17%2Cp_n_publication_date%3A1250226011&dc&qid=1619244512&rnid=1250225011&ref=lp_17_nr_p_n_publication_date_0'
                  
                  ]

    def parse(self, response):
        items=AmazontutItem()
        book=response.css(".a-color-base.a-text-normal::text").extract()
        author=response.css(".a-color-secondary .a-row span.a-size-base+ .a-size-base").css("::text").extract()
        price=response.css(".a-spacing-top-small .a-price-whole").css("::text").extract()
        image=response.css(".s-image::attr(src)").extract()

        items["book"]=book
        items["author"]=author
        items["price"]=price
        items["image"]=image

        yield items
        next_page="https://www.amazon.com/s?i=stripbooks&bbn=17&rh=n%3A17%2Cp_n_publication_date%3A1250226011&dc&page="+str(AmazonSpider.page)+"&qid=1619247773&rnid=1250225011&ref=sr_pg_2"
        if AmazonSpider.page<4:
            AmazonSpider.page+=1
            yield response.follow(next_page,callback=self.parse) 
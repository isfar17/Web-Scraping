import scrapy
from ..items import TutorialItem

class Scrape(scrapy.Spider):
    name="quotes"
    page=2
    start_urls=[
        "https://quotes.toscrape.com/"
        ]

    def parse(self,response):
        items=TutorialItem()
        all_quote=response.css("div.quote")
        for quote in all_quote:
            text=quote.css(".text::text").extract()
            author=quote.css(".author::text").extract()
            tag=quote.css(".tag::text").extract()
                #if you dont want to see title tag write "title::text"in the parenthesis
            items["text"]=text
            items["author"]=author
            items["tag"]=tag

            # yield {
            # # "all_quotes":all_quote
            # "text":text,
            # "author":author,
            # "tag":tag
            # }
            yield items

        next_page="https://quotes.toscrape.com/page/"+str(Scrape.page)+"/"
        if Scrape.page <11:
            Scrape.page+=1
            yield response.follow(next_page,callback=self.parse)


        # next_page=response.css("li.next a::attr(href)").get()

        # print(next_page)
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)
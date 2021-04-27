import scrapy
from scrapy.utils.response import open_in_browser
from ..items import TutorialItem
from scrapy.http import FormRequest
class Scrape(scrapy.Spider):
    name="quotes"
    page=2
    start_urls=[
        "https://quotes.toscrape.com/login"
        ]

    def parse(self,response):

        csrf_token=response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response,formdata={
            "csrf_token":csrf_token,
            "username":"sdsdsd",
            "password":"1234"},#must be a string
            callback=self.scrap)
    def scrap(self,response):
        open_in_browser(response)
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
            yield items

        next_page="https://quotes.toscrape.com/page/"+str(Scrape.page)+"/"
        if Scrape.page <11:
            Scrape.page+=1
            yield response.follow(next_page,callback=self.scrap)        
        


import scrapy
import requests

class GithubSpider(scrapy.Spider):
    name = "github"
    def start_requests(self):
        urls = []

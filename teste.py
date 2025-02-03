from web_scrap import WebScrapingImages, WebScrapingText, WebScrapingLink


urls = input("Enter the URL: ")

# result = WebScrapingImages(url=urls).get_images()
# result1 = WebScrapingText(url=urls).get_text()
result2 = WebScrapingLink(url=urls).get_links()
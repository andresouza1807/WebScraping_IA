from web_scrap import WebScrapingImages, WebScrapingText, WebScrapingLink


urls = input("Enter the URL: ")


# result = WebScrapingImages(url=urls).get_images(output_file='output_file_images.txt')
result1 = WebScrapingText(url=urls).get_text(output_file='output_file_text.txt')
# result2 = WebScrapingLink(url=urls).get_links(output_file='output_file_links.txt')
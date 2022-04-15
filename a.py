# import requests
# from bs4 import BeautifulSoup

# #array of just crypto names
# names = []

# #gets content from site
# site = requests.get("https://cryptopanic.com/news/bitcoin/")

# #opens content from site
# info = site.content
# soup = BeautifulSoup(info,"html.parser")

# #class ID for name of crypto
# type_name = 'new'

# #crypto names + other unnecessary info
# names_raw = soup.find_all('p', attrs={'class': 'sc-1eb5slv-0 iJjGCS'})

# for type_name in names_raw:
#     print(type_name.text, type_name.next_sibling)



from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["₹58,400","New Apple iPhone 11 (128GB) - Black"]
scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)

scraper.get_result_similar(amazon_url,grouped=True)
scraper.set_rule_aliases({'rule_aru8':'Title','rule_9cdc':'Price'})
scraper.keep_rules(['rule_aru8','rule_9cdc'])
scraper.save('amazon-search')
results=scraper.get_result_similar('https://www.amazon.in/s?k=mi+phones+under+15000',group_by_alias=True)

results['Price']
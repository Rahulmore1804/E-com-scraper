



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

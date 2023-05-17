import scrapermain

brand = input("Enter the Brand of the Product (or press enter to leave it blank) : ")
product = input("Enter the Name of the Product : ")

scrapermain.StartScraper(brand,product)

print ("------------------")
print ("Scraping Completed")
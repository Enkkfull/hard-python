import wikipediaapi


def main(): 

	wiki = wikipediaapi.Wikipedia('en')
	
	# generate pages to scrape
	months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	
	years = [x for x in range(1992, 2022)]
	
	# list of all pages
	pages = []
	
	for year in years:
	  for month in months:
	   pages.append('Deaths_in_'+month+"_"+str(year))

	page = wiki.page(pages[0])
	print(page.text)



# Checks if the pages in a list exists
def check_pages(wiki, pages):
	existence = []

	for page in pages:
		page_py = wiki.page(page)
		existence.append(page_py.exists())
		print(page_py.title)



if __name__ == "__main__":
    main()
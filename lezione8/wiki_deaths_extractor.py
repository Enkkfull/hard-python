import wikipediaapi


def main(): 

	wiki = wikipediaapi.Wikipedia('en')
	
	# generate pages to scrape
	months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	
	years = [x for x in range(1992, 2022)]
	
	# list of all pages
	pages_names = []
	
	for year in years:
	  for month in months:
	   pages_names.append('Deaths_in_'+month+"_"+str(year))

	page = wiki.page(pages_names[0])
	#print(page.text)
	parse_page(page.text, month, year)



# Checks if the pages in a list exists
def check_pages(wiki, pages):
	existence = []

	for page in pages:
		page_py = wiki.page(page)
		existence.append(page_py.exists())
		print(page_py.title)


# Parse the page
def parse_page(text, month, year):

	day_to_deaths = {}
	day = 1
	# find where the doc with deaths starts: month + year
	text_divided = text.split("\n")
	parsing_day = False
	for line in text_divided:
		print("Processing line ", line)
  # find the first day -> 1
		if line == str(day):
			day_to_deaths[day] = []
			day += 1
			parsing_day = True
  # until we find the n2, parse the line
		elif line != "" and not line.startswith("=") and parsing_day:	
			day_to_deaths[day-1].append(parse_line(line))	

	print(day_to_deaths)
	# proceed for all days untile end doc

def parse_line(line):
	return {"name": }

if __name__ == "__main__":
    main()
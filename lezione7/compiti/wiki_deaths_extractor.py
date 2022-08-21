# install and import wiki api library
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('November_7')

print(page_py.summary)

# generate links to  scrape
months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#verify if the links exists, and evaluate next steps
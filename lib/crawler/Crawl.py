
from .searchengine.SearchParser import SearchParser

class Crawl():
	def __init__(self):
		print "something"

if __name__ == "main":
	dat = SearchParser("google", "This is a source code")
	print dat.parse()
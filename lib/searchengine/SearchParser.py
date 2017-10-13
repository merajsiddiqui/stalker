from parser.Google import Google


class SearchParser():

	search_engine_list = [
		"Google",
		"Yahoo",
		"Bing"
	]

	def __init__(self, searchengine, pageSourceCode):
		searchengine = searchengine.title()
		if searchengine in self.search_engine_list:
			self.parserHandler = eval(searchengine+"()")
			self.pageSourceCode = pageSourceCode
		else:
			self.error = "Invalid Search Engine Provided"

	def parse(self):
		self.parserHandler.pageSourceCode = self.pageSourceCode
		data = self.parserHandler.parsePage()
		return data

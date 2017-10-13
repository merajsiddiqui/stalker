import sys
sys.path.append("..")
from searchengine.SearchParser import SearchParser

dat = SearchParser("google", "This is a source code")
print dat.parse()
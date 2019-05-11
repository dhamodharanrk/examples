'''Its an collection of usefull/repeated functions. It has traditional funcction as well as lambda'''

# =================LIST OPERATIONS===================#

def findDiff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


# findDiff = lambda first, second: [item for item in first if item not in second]

def findDuplicates(x):
    import collections
    return [item for item, count in collections.Counter(x).items() if count > 1]


# findDuplicates = lambda source_list: [item for item, count in collections.Counter(source_list).items() if count > 1]

# =========================String========================#

def concateString(source_list, separator):
    return separator.join(source_list)


# concateString = lambda source_list,separator: str(separator).join(source_list)

print(concateString(["Heloo", "World!"], " "))

#====================OTHERS==============================#
#Extracting domain information from URL
import tldextract
def extractDomain(url):
	if "http" in str(url) or "www" in str(url):
		parsed = tldextract.extract(url)
		parsed = ".".join([i for i in parsed if i])
		return parsed
	else: return "NA"
print(extractDomain("https://google.co.uk?link=something"))

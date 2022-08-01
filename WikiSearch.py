import wikipedia

def Search(SearchText):
    try:
        WikiQuery = SearchText.split('for')[1]
        print(WikiQuery)
        return(wikipedia.summary(WikiQuery, sentences=2))
    except:
        return("Unable to search Wiki")
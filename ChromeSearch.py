import webbrowser as WB

def SearchChrome(SearchContents):
    ChromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    WB.get(ChromePath).open_new_tab(SearchContents + ".com")
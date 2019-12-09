import autoit

google_chrome_pid = autoit.run('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"', show_flag=3) # run in incognito mode, start maximized
url = "pune.vaultize.com"
autoit.win_wait_active("New Tab - Google Chrome")
print "{}".format(url)
autoit.send("pune.vaultize.com")
autoit.send("{Enter}")

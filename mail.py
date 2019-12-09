import autoit

autoit.run("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#autoit.win_activate("Chrome")
autoit.win_wait("New Tab - Google Chrome")
autoit.send("gmail.com")
autoit.send("{Enter}")
autoit.win_wait_active("Inbox")
autoit.control_click("Inbox")

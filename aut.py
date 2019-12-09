import autoit
import random

autoit.run("notepad.exe")
autoit.win_wait_active("Untitled - Notepad")
#print 'Check',autoit.win_wait_active("Untitled - Notepad")
autoit.send("Omkar")
autoit.win_wait_active("*Untitled - Notepad")
autoit.win_close("*Untitled - Notepad")
autoit.win_wait_active("Notepad")
#autoit.control_click("[Class:#32770]", "Button1")
autoit.send("{Enter}")
autoit.win_wait_active("Save As")
stg = "Omkar"+str(random.random())
autoit.send(stg)
autoit.send("{Enter}")
print autoit.win_exists("Confirm Save As")
if (autoit.win_exists("Confirm Save As")):
    autoit.send("{LEFT}")
    autoit.send("{Enter}")
else:
    pass
#autoit.control_click("[class:#32770]","Button")
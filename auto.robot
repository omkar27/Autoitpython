*** Settings ***
Library           AutoItLibrary
Library           OperatingSystem
Library           PyAutoIt
*** Variables ***

*** Test Cases ***
First
	#${Version}  Get Auto It Version
	#Log To Console  \n ${Version}

	AutoItLibrary.Run  notepad.exe
	#Win Minimize All
	#Win Activate    Untitled - Notepad    OMKAR
	#Send     1234
	Win Wait Active     Untitled - Notepad
	Send    Omkar
	#Win Menu Select Item    Untitled - Notepad  1234        &File   Save &As
	Win Close       *Untitled - Notepad
	Send    ${"Enter"}
	Pr
   # AutoItLibrary.ControlClick("Calculator", "", "Button5", "Left") ;Click the number 1
    #${X-Pos}  Mouse Get Pos X
	#${Y-Pos}  Mouse Get Pos Y
	#Mouse Click  strButton=LEFT, nX=${X-Pos}, nY=${Y-Pos} , nClicks=2, nSpeed=-1
*** Keywords ***

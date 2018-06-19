import webbrowser

print "Open both cameras. Enter 'both'"
if raw_input("> ") == "both": #opens both cameras
    webbrowser.open('http://192.168.21.181/top.htm')
    webbrowser.open('http://192.168.21.182/top.htm')
else:
    print "Bruh you messed up try again"

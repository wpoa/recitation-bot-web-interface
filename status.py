import cgi
import cgitb
import os
import sys
sys.path.append('/data/project/recitation-bot/')
import shutdown_bot_hack

cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<TITLE>control recitation-bot</TITLE>"
print "<H1>control recitation-bot</H1>"
print "<html>"
print "<body>"

# standard single line text field
print "<form method='post'>"
actions = ['status', 'shutdown', 'shutdown_hard', 'start']
actions_text = ['show status', 'shutdown bot', 'shutdown bot HARD', 'start bot']
for var, text in zip(actions, actions_text):
    print "<input type='radio' name='%s' />%s" % (var, text)
print ".<br /><input type='submit' value='execute' />"
print "</form>"
form = cgi.FieldStorage()

def wrap_pre(sidefun):
    print '<pre>'
    sidefun()
    print '</pre>'

if 'status' in form:
    wrap_pre(shutdown_bot_hack.qstat_simple)
if 'shutdown' in form:
    wrap_pre(shutdown_bot_hack.qdel_python_method)
if 'shutdown_hard' in form:
    wrap_pre(shutdown_bot_hack.do_suite)
if 'start' in form:
    wrap_pre(shutdown_bot_hack.start_it)

print "</ul>"
print "</body>"
print "</html>"

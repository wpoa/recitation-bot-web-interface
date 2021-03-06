import cgi
import cgitb
import os
import sys
sys.path.append('/data/project/recitation-bot/recitation-bot/recitation-bot/')
import status_page

cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<TITLE>jump a doi to the front of the queue</TITLE>"
print "<H1>jump a doi to the front of the queue</H1>"
print "<html>"
print "<body>"

# standard single line text field
print "<form method='post'>"
print "Enter a doi (don't include 'http://dx.doi.org/'):"
print "<input type='text' name='doi' value='' /><BR/>"
print "If DOI already uploaded, force reupload of "
reupload_vars = ['reupload_text', 'reupload_images', 'reupload_equations', 'reupload_tables']
reupload_text = ['text', 'images', 'equations', 'tables']
for var, text in zip(reupload_vars, reupload_text):
    print "<input type='checkbox' name='%s' />%s" % (var, text)
print ".<br /><input type='submit' value='submit form' />"
print "</form>"
form = cgi.FieldStorage()

reupload = []
doi_plain = ''

#print form
for field_name in form:
    field=form[field_name]
    for check in reupload_vars:
        if field.name == check:
            if form[check].value == 'on':
                print "<p>%s : %s</p>" % (check, form[check].value)
                reupload.append(check)
    if field.name == 'doi':
        doi_plain = field.value
        doi_safe = cgi.escape(repr(doi_plain))

if doi_plain:
    #write to log
    dequeue = open('/data/project/recitation-bot/recitation-bot/jump_the_queue.log','a')
    dequeue.write(doi_plain+'\t'+str(reupload)+'\n')
    dequeue.close()
    
    #show the user
    print "<p>%s will be uploaded shortly</p>" % doi_safe
    url = 'http://tools.wmflabs.org/recitation-bot/' + doi_plain + '.html'
    print "<p>Follow the upload status at <a href='%s'>%s</a> </p>" % (url, url)
    status_page.make_status_page(doi=doi_plain, success=None, error_msg=None,ja=None, inqueue=True)


print "</ul>"
print "</body>"
print "</html>"

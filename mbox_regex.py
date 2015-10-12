#!/usr/bin/python
# Deepak Ramanath

# Python program to process a mail interaction file using regex

import re

# Regex compile for email and name
emailCompile = re.compile(r'\w+:[ ]?(?P<email>\w+[\.]?\w+\@[a-zA-z0-9\.?]+)')
nameCompile = re.compile(r'\w+:[ ]?(?P<name>\w+[\.]?\w+)')
nameCompleEmail = re.compile(r'(?P<name2>\w+[\.]?\w+)')

# Empty lists
Emails = []
Names = []
Names2 = []

# Regex search on the file
with open('mbox.txt', 'r') as mboxData:
    for line in mboxData:
        if "From:" in line:
            emailSearch = emailCompile.search(line.rstrip())
            nameSearch = nameCompile.search(line.rstrip())
            email = emailSearch.group('email')
            name = nameSearch.group('name')
            # Name search from email address
            name2Search = nameCompleEmail.search(email)
            name2 = name2Search.group('name2')
            Emails.append(email)
            Names.append(name)
            Names2.append(name)
            
if Names == Names2:
    print "Name search matches both regex methods"
else:
    print "Check your code"

# Final name and email lists
finalEmails = []
finalNames = []

# Checking fo duplicates
for Email in Emails:
	if not Email in finalEmails:
		finalEmails.append(Email)

for Name in Names:
    if not Name in finalNames:
        finalNames.append(Name)

# making a tuple of lists
NamesEmails = zip(finalNames, finalEmails)

# Printing the final list of names and email address
for N, E in NamesEmails:
    print "Name: %s\t\t Email: %s" % (N, E)

"""Lesson 4.6 Validation
"Verifying on the server-side that what was received is what was expected"
"""

# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    if str.capitalize(month) in months:
        return str.capitalize(month)
    else:
        return None

# print valid_month("january")
# => "January"
# print valid_month("January")
# => "January"
# print valid_month("foo")
# => None
# print valid_month("")
# => None

"""Instructor version:
def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month

OR

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
"""

# -----------
# User Instructions
#
# Modify the valid_day() function to verify
# whether the string a user enters is a valid
# day. The valid_day() function takes as
# input a String, and returns either a valid
# Int or None. If the passed in String is
# not a valid day, return None.
# If it is a valid day, then return
# the day as an Int, not a String. Don't
# worry about months of different length.
# Assume a day is valid if it is a number
# between 1 and 31.
# Be careful, the input can be any string
# at all, you don't have any guarantees
# that the user will input a sensible
# day.
#
# Hint: The string function isdigit() might be helpful.


def valid_day(day):
    if day.isdigit():
        if 1 <= int(day) <= 31:
            return int(day)

# valid_day('0')
# => None
# valid_day('1')
# => 1
# valid_day('15')
# => 15
# valid_day('500')
# => None

"""Instructor Version:
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
"""

# -----------
# User Instructions
#
# Modify the valid_year() function to verify
# whether the string a user enters is a valid
# year. If the passed in parameter 'year'
# is not a valid year, return None.
# If 'year' is a valid year, then return
# the year as a number. Assume a year
# is valid if it is a number between 1900 and
# 2020.
#


def valid_year(year):
    if year.isdigit():
        year = int(year)
        if 1900 <= year <= 2020:
            return year

# print valid_year('0')
# => None
# print valid_year('-11')
# => None
# print valid_year('1950')
# => 1950
# print valid_year('2000')
# => 2000

"""Instructor version:
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= 2020:
            return year
"""

"""Verification Steps:
1. Verify the user's input.
2. Detect if it is an error and render form again if it is.
3. Include an error message.
"""

"""String Substitution:
"<b>some bold text"

"<b>%s<b>" %string_automatically_replaced

OR

a = string_automatically_replaced
<b>%s<b>" % a

RESULTS

<b>string_automatically_replaced</b>
"""

# User Instructions
#
# Write a function 'sub1' that, given a
# string, embeds that string in
# the string:
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given
# string.
# The function should return the new string.

given_string = "I think %s is a perfectly normal thing to do in public."


def sub1(s):
    string = given_string.replace("%s", s)
    return string

"""Instructor Version:
def sub1(s)
    return given_string % s
"""

#print sub1("running")
# => "I think running is a perfectly normal thing to do in public."
#print sub1("sleeping")
# => "I think sleeping is a perfectly normal thing to do in public."

# User Instructions
#
# Write a function 'sub2' that, given two
# strings, embeds those strings in the string:
# "I think X and Y are perfectly normal things to do in public."
# where X and Y are replaced by the given
# strings.
# The function should return the new string.

given_string2 = "I think %s and %s are perfectly normal things to do in public."


def sub2(s1, s2):
    return given_string2 % (s1, s2)

print sub2("running", "sleeping")
# => "I think running and sleeping are perfectly normal things to do in public."
print sub2("sleeping", "running") 
# => "I think sleeping and running are perfectly normal things to do in public."

"""Optional Parameter: set it equal to ""

You can keep track of multiple varies or use the same variable more than
once by creating a dictionary for the substitution and keying it to your
variables.

You need the %(variable)s
"""

# User Instructions
#
# Write a function 'sub_m' that takes a
# name and a nickname, and returns a
# string of the following format:
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
#

given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."


def sub_m(name, nickname):
    return given_string3 % {"name": name, "nickname": nickname}

# print sub_m("Mike", "Goose")
# => "I'm Goose. My real name is Mike, but my friends call me Goose."

"""Input Values
<input type="test" value="cool> sets "cool" as the default value

<input name="month" value"%(month)s> preserves user input
"""

# User Instructions
#
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#


def escape_html(s):
    string = s
    string.replace('>', '&gt;')
    string.replace('<', '&lt;')
    string.replace('"', '&quot;')
    string.replace('&', '&amp;')
    return string

print escape_html('>')
print escape_html('<')
print escape_html('"')
print escape_html("&")

"""Instructor Version:
def escape_html(s):
    for (i, o) in (("&", "&amp;"),
                   (">", "&gt;"),
                   ("<", "&lt;"),
                   ('"', "&quot;")):
        s = s.replace(i,o)
    return s

OR

import cgi
def escape.html(s):
    return cgi.escape(s, quote = True)
"""

"""Redirection:
Can't share success link?
Can't reload the page without the form resubmission?

Redirect them to a new page!
- Make a handler
- Add the URL
- Redirect to the URL
"""

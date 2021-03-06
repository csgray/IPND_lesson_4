"""Databases
"Programs that stores and retrieves (large amounts of structured) data."
Or the machine(s) running the program.

Tables
    type: what the table covers
    columns: the properties that make up a particular type
    rows: the entries; one instance of an element

Almost every table has an ID column to identify the rows
"""

from collections import namedtuple
import sqlite3

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties.
# For example, a Link's number of votes can be accessed by link.votes if
# "link" is a Link.

# make the function query() return the number of votes for the link
# whose ID is 15

# def query(q):
#    for n in links:
#        if n.id == q:
#            return n.votes

# make the function query() return a list of Links submitted by user 62443, by
# submission time ascending

# def query():
#     results = []
#     for n in links:
#         if n.submitter_id == 62443:
#             results.append(n)
#     results = sorted(results, key=lambda n: n.submitted_time)
#     return results

"""
Downsides of querying data by hand:
    error-prone
    tedious
    slow

Types of Databases
    Relational (SQL: Postgresql, MySQL, SQLite, Oracle)
    Datastore (Google App Engine)
    Dynamo (Amazon)
    NoSQL (Mongo, Couch)

SQL: Structured Query Language
    Used to ask the database questions
    Invented in the 1970s

SELECT * FROM links WHERE id = 5;
"fetch data" "all columns" FROM "table" WHERE "constraint"

cursor: position within the database
"""

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('create table links ' +
           '(id integer, submitter_id integer, submitted_time integer, ' +
           'votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

# db is an in-memory sqlite database that can respond to sql queries using the
# execute() function.
#
# For example. If you run
#
# c = db.execute("select * from links")
#
# c will be a "cursor" to the results of that query. You can use the fetchmany()
# function on the cursor to convert that cursor into a list of results. These
# results won't be Links; they'll be tuples, but they can be passed turned into
# a Link.
#
# For example, to print all the votes for all of the links, do this:
#
# c = db.execute("select * from links")
# for link_tuple in c:
#     link = Link(*link_tuple)
#     print link.votes
#
# QUIZ - make the function query() return the number of votes the link with ID = 2 has


# def query():
#     c = db.execute("SELECT * FROM links WHERE id=2")
#     link = Link(*c.fetchone())
#     return link.votes

"""
SELECT * FROM links WHERE submitter_id=5 AND votes > 23
                                         OR votes > 23
"""

# QUIZ - make the function query() return the ID of the link that was
# submitted by user 62443 and has > 1000 votes.


# def query():
#     c = db.execute("SELECT * FROM links WHERE submitter_id=62443 \
#                     AND votes > 1000")
#     link = Link(*c.fetchone())
#     return link.id

"""
SELECT * FROM links
         WHERE votes > 10
         ORDER BY votes

Defaults to ascending but can specify with ASC or DESC
"""
# QUIZ - make the function query() return a list of the IDs of the links
# that were submitted by user 62443 sorted by submission time ascending.
#
# def query():
#     c = db.execute("SELECT * FROM links WHERE submitter_id=62443 \
#                    ORDER BY submitted_time ASC")
#     results = []
#     for link_tuple in c:
#         link = Link(*link_tuple)
#         results.append(link.id)
#     return results

# Better version:
#
# def query():
#     c = db.execute("SELECT id FROM links WHERE submitter_id=62443 \
#                    ORDER BY submitted_time ASC")
#     results = [t[0] for t in c]
#     return results

"""
JOINS: type of SQL query involving multiple Tables

SELECT id FROM user WHERE name="spez"
SELECT * FROM link WHERE user_id=22

vs

SELECT link.* FROM link,user WHERE link.user_id=user.id AND user.name="spez"

-----------------------

INDEX: increases the speed of queries by keying items

sequential scan: going over a list of things one-by-one in order
"""

# QUIZ - implement the function link_by_id() that takes a link's ID and returns
# the Link object itself

# My version
# def link_by_id(link_id):
#    c = db.execute("SELECT * FROM links WHERE id=?", (link_id,))
#    return c.fetchone()

"""
Not a SQL question, but a Python question!
Instructor version:


def link_by_id(link_id):
    for l in links:
        if l.id == link_id:
            return l
"""

# QUIZ - implement the function build_link_index() that creates a python
# dictionary the maps a link's ID to the link itself


def build_link_index():
    index = {}
    for l in links:
        index[l.id] = l
    return index

link_index = build_link_index()

def link_by_id(link_id):
    return link_index.get(link_id)

# QUIZ - implement the function add_new_link() that both adds a link to
# the "links" list and updates the link_index dictionary.


def add_new_link(link):
    links.append(link)
    link_index[link.id] = link

"""
Indexes increase the speed of database reads,
but they decrease the speed of database inserts

Indexes for Sorting
hashtable: Not sorted! Constant (always takes the same) Time Lookup.
    Just key:value pairs. New elements go wherever there is room for it.
tree: Sorted! But lookups are slower since time is log (n) of elements

Big_O Notation
https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/

ACID
Atomicity - all parts of a transaction succeed or fail together
Consistency - the database will not have random or invalid changes
Isolation  - no transaction can interfere with another's
Durability - once a transaction is comitted, it won't be lost

transaction: a group of statements
locking: only transaction can change a row at a time (row is locked)

Google App Engine Datastore
tables -> entities
    - columns are not fixed and can be changed on the fly
    - all entities have an ID
    - entities can have parents/ancestors and children/descendents

Regular Expressions (Regex)
    from regexone.com
Matches alphanumeric and special characters in any position.
\ escapes special characters like those below
. is a wildcard for any single characters
\d is a wildcard for any digit
[abc] matches specific characters (in this case a, b, and c)
[^xyz] excludes specific character (match everything except x, y, and z)
[a-d] matches sequential characters (a, b, c, and d)
\w is the same as [A-Za-z0-9_] (alphanumeric) for English-language matching
a{3} means three 'a' charactes: aaa
* means 'zero or more' of whatever it follows
+ means 'one or more' of whatever it follows
? means that whatever it follows is optional
\s matches any whitespace
_ is a single space
\t is a tab
\n is a new line
\r is a carriage return (from Windows)
^ means to only match lines that start with the expression
$ marks where the line should end
(stuff) restricts what is captured to what is inside the parantheses
    so you can do a search with more parameters but only keep some of it
You can (nest(capture groups)) so that you capture both separately
| means logical OR as in cats|dogs to capture both
You can reverse the meaning of special characters by capitalizing them
    \D means any non-digit character
    \S means any non-whitespace character
    \W means any non-alphanumeric character (like punctuation)
\b means the boundary between a word and a non-word character
    so you can use it to isolate words like \w+\b
    but spaces count as word characters

Uniform Resource Identifiers
protocol://host:port(optional)/resource_path
such as http://regexone.com:80/page

"""

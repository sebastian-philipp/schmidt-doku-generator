#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom

def prettyPrint(xmlString):
	x = xml.dom.minidom.parseString(xmlString)
	return x.toprettyxml()

def elem(e, t, attr = {}):
	attr = " ".join(['%s="%s"'%(k, v) for (k,v) in attr.items()])
	return "<%s %s>%s</%s>\n" % (e, attr, t, e) if len(attr) else  "<%s>%s</%s>\n" % (e, t, e)

def toA(n, href):
	return elem("a", n, {"href": href})

def toUl(l):
	return elem("ol", "".join([elem("li", x) for x in l]))

def toP(c):
	return elem("p", c)

def write(name, content):
	print "writing", name
	with open(name, "w") as f:
		f.write(content)
		
def navigation(meta, l, r = None):
	"""eg navigation(meta, ("<< Prev", "foo.html"))"""
	l = [
			(meta["seminarSubject"], meta["seminarLink"]),
			(meta["seminar"], "index.html"),
			l
		]
	if r is not None:
		l.append(r)
	bareList = [ "[ %s ]" % toA(n, l) for (n,l) in l]
	bare = "<hr /> ... %s ... <hr />" % " ... ".join(bareList)
	return elem("div", bare)

def sectionToNaviElem(section, prefix = "", postfix = ""):
	return (prefix + section["name"] + postfix, sectionToFileName(section))
		
def sectionToFileName(section):
	return section["name"].lower() + ".html"

def head(meta):
	return """
<head>
	<title>Seminar - %(seminar)s</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="author" content="%(author)s" />
	<style type="text/css"><!--
	p {width:50em;}
	--!></style>
</head>""" % meta


# index

def frameIndex(meta):
	"""usage {"seminar": seminar, "desc": desc, "author":author}"""
	meta["navi"] = navigation(meta, ("Inhaltsverzeichnis", "contents.html"))
	meta["head"] = head(meta)
	return """
<html>
%(head)s
<body>
	<a name="top"></a>
	<div align="center">
		<h1>%(seminar)s</h1>
	</div>
%(navi)s
	<div align="center">
		<h1>%(seminar)s</h1>
		<p>%(desc)s</p>
		<p>%(author)s</p>
	</div>
%(navi)s
</body>	
</html>
""" % meta 

# contents

def frameContents(meta, content):
	meta["navi"] = navigation(meta, ("<< Startseite", "index.html"), sectionToNaviElem(content[0], "", " >>"))
	meta["head"] = head(meta)
	meta["toContentsList"] = toContentsList(content)
	return """
<html>
%(head)s
<body>
	<a name="top"></a>
	<div align="center">
		<h1>Inhaltsverzeichnis</h1>
	</div>
%(navi)s
	<div>
%(toContentsList)s
	</div>
%(navi)s
</body>	
</html>"""% meta

def sectiontoUl(section):
	sectionLinkName = sectionToFileName(section)
	def dictToName(subSection):
	#	print "subSection", subSection
		return subSection["name"]
	#print "section", section
	names = map(dictToName,section["content"])
	for i in range(len(names)):
		names[i] = toA(names[i], sectionLinkName + "#" + str(i))
	return toA(section["name"], sectionLinkName) + toUl(names)

def toContentsList(content):
	return toUl(map(sectiontoUl, content))

# section.html

def writeSubSections(meta, content):
	contentNaviElem = ("Inhaltsverzeichnis", "contents.html")
	
	for i in range(len(content)):
		prev = sectionToNaviElem(content[i-1], "<< ", "") if i > 0 else contentNaviElem
		next = sectionToNaviElem(content[i+1], "", " >>") if i < (len(content)-1) else contentNaviElem
		write(sectionToFileName(content[i]), frameSubSection(meta, prev, next, content[i]))

def frameSubSection(meta, prev, next, subSection):
	subSection["head"] = head(meta)
	subSection["navi"] = navigation(meta, prev, next)
	subSection["desc"] = toP(subSection["desc"])
	subSection["subSections"] = ""
	for i in range(len(subSection["content"])):
		subSection["subSections"] += toSubSection(i, subSection["content"][i])

	return """
<html>
%(head)s
<body>
	<a name="top"></a>
	<div align="center">
		<h1>%(name)s</h1>
	</div>
%(navi)s
	<div>
%(desc)s
%(subSections)s
	</div>
%(navi)s
</body>	
</html>
""" % subSection

def prettyText(text):
	def handlePrefix(l):
		if l.startswith("\\h4"):
			return elem("h4", l[3:])
		elif l.startswith("\\a"):
			return toA(l[2:], l[2:]) + "<br>"
		else:
			return l + "<br>"
	return "\n".join(map(handlePrefix, text.splitlines()))

def toSubSection(number, subSection):
	subSection["number"] = number
	subSection["content"] = toP(prettyText(subSection["content"]))
	return """
		<h2><a name="%(number)s">%(name)s</a></h2>
%(content)s
""" % subSection

def main(meta, content):
	write("index.html", frameIndex(meta))
	write("contents.html", frameContents(meta, content))
	writeSubSections(meta, content)






#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dokuGenerator


def main():
	meta = {
		"seminarSubject": "Programmiersprachen und Sprachsysteme",
		"seminarLink": "http://www.fh-wedel.de/~si/seminare/ss13/Termine/Themen.html",
		"seminar": "Beispiel Seminar",
		"desc": "Untertitel",
		"author":"Sebastian Philipp"}
	
	content = [
		{ # section
			"name": "Beispiel1",
			"desc": """
Vor der ersten Überschrift
""",
			"content": [
				{ # subSection
					"name": "Überschrift",
					"content": """
Inhalt

<b>HTML-Tags gehen</b>

\\ahttp://spezielle.link/syntax

Dies ist ein \\a-section{Patches} interner link

Inline \\a{http://link.syntax/} gehen auch 


\\h4 Geht auch für Unterüberschriften
"""
				},
				{ # subSection
					"name": "Noch ein Beispiel",
					"content": """
Neue
Zeilen
werten
umgebrochen
\\code-ruby{
# Inklusive Syntax highlightning
class Id
	def initialize(lam)
		@v = lam
	end

	def force # :: Id a -> a
		@v[]
	end

	def self.unit # a -> Id a
		lambda {|x| Id.new(lambda { x })}
	end

	def bind # :: Id a -> (a -> Id b) -> Id b
		x = self
		lambda {|f| f[x.force]}
	end
end
\\code}
"""
				}
			]
		},
		{ # section
			"name": "Patches",
			"desc": """kann ich gebrauchen""",
			"content": [
				{ # subSection
					"name": "Blah",
					"content": """
Foo"""
				},
				{ # subSection
					"name": "Bar",
					"content": """
Text
<ul><li>a</li></ul>
Text
Baaz"""
				}
			]
		}
		
	]
				
	dokuGenerator.main(meta, content)

if __name__ == "__main__":
	main()






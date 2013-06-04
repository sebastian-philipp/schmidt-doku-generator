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
Baaz"""
				}
			]
		}
		
	]
				
	dokuGenerator.main(meta, content)

if __name__ == "__main__":
	main()






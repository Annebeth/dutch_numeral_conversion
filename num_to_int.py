import csv, re

SIMPLE_NUMERALS = {
	u"nul"			: 0,
    u"een"   		: 1,
    u'\xe9\xe9n'	: 1,
    u"twee"  		: 2,
    u"drie"  		: 3,
    u"vier"  		: 4,
    u"vijf"  		: 5,
    u"zes"   		: 6,
    u"zeven" 		: 7,
    u"acht"  		: 8,
    u"negen" 		: 9,
    u"tien"			: 10,
    u"elf"			: 11,
    u"twaalf"		: 12,
    u"dertien"		: 13,
    u"veertien"		: 14
}

TENS = {
    u"twintig"   : 20,
    u"dertig"    : 30,
    u"veertig"   : 40,
    u"vijftig"   : 50,
    u"zestig"    : 60,
    u"zeventig"  : 70,
    u"tachtig"   : 80,
    u"negentig"  : 90
}

MULTS = {
	"honderd"	: 10**2,
	"duizend"	: 10**3,
	"miljoen"	: 10**6,
	"miljard"	: 10**9,
	"biljoen"	: 10**12,
	"biljard"	: 10**15
}

MULTS_LIST = [k for (k,v) in sorted(MULTS.items(), key=lambda t: t[1], reverse = True)]

def under_100(numb):
	numb = numb.decode('utf-8')
	# If already a numeral
	x = re.match("^\d+\s*$", numb)
	if x:
		return int(numb)
	# Simple numerals 1-9
	elif numb in SIMPLE_NUMERALS:
		return SIMPLE_NUMERALS[numb]
	# Simple tens
	elif numb in TENS:
		return TENS[numb]
	else:
		count = None
		for n in SIMPLE_NUMERALS:
			for t in TENS:
				# For -tens
				if re.match("^" + n + "tien$", numb):
					count = SIMPLE_NUMERALS[n] + 10
					return count
				# For 21 to 99
				elif re.match("^" + n + "en" + t + "$", numb):
					count = SIMPLE_NUMERALS[n] + TENS[t]
					return count
		return None

def number_finder(numb):
	numb = numb.replace(" ", "")	
	n = under_100(numb)
	if n is not None:
		return n
	else:
		for m in MULTS_LIST:
			x = re.match("(^.*)" + m + "(.*)", numb)
			if not x is None:
				nbefore = number_finder(x.group(1)) if x.group(1) else 1
				nafter = number_finder(x.group(2)) if x.group(2) else 0
				return nbefore * MULTS[m] + nafter
		print 'Error: This number could not be parsed!'

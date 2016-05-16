def con(w, text, i, d):
	izquierda = "\w+\s"*i
	derecha = "\s\w+"*d
	exp = re.compile("({}){}(?=({}))".format(izquierda,w,derecha))
	return re.findall(exp, text)

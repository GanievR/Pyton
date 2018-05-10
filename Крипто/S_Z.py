
# Шифрование
text="fwjhgfkashf"
keys={
	'a':'!',  'b':'@',  'c':'#',
	'd':'$',  'e':'%',  'f':'^',
	'g':'&',  'h':'*',  'i':'(',
	'j':')',  'k':'-',  'l':'=',
	'm':'+',  'n':'?',  'o':':',
	'p':';',  'q':'<',  'r':'>',
	's':'/',  't':'[',  'u':']',
	'v':'{',  'w':'}',  'x':'|',
	'y':'.',  'z':',',  ' ':'~'
}
crypt=""
for i in text:
	if i in keys:
		crypt+=keys[i]
print("Crypted text:\n"+crypt+"\n")

# Расшифрование
text=crypt
keys={
	'!':'a',  '@':'b',  '#':'c',
	'$':'d',  '%':'e',  '^':'f',
	'&':'g',  '*':'h',  '(':'i',
	')':'j',  '-':'k',  '=':'l',
	'+':'m',  '?':'n',  ':':'o',
	';':'p',  '<':'q',  '>':'r',
	'/':'s',  '[':'t',  ']':'u',
	'{':'v',  '}':'w',  '|':'x',
	'.':'y',  ',':'z',  '~':' '
}
decrypt=""
for i in text:
	if i in keys:
		decrypt+=keys[i]
print("Decrypted text:\n"+decrypt)
decrypt_r=open("text_crypt.txt","w")

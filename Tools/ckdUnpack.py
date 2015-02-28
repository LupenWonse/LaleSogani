# CKD Expander Script
# By Ahmet Gencoglu
# Bu script LaleSavascilari oyun dosya paketleri CKD dosyalarinin
# otomatik olarak acilmasi icin yaratildi.
# Kullanimi, kopyalanmasi, dagitilmasi falan serbesttir.

print "Hello World - CKD Expander for Lale Savascilari"

# Regular Expressions kutuphanesini alalim
import re
import sys

for currentFile in sys.argv[1:]:

# Istedigimiz dosyayi acalim hemen
	with open(currentFile,"rb") as ckdFile:
	# Butun datayi bi kerede alalim (Herhalde RAMi zorlayacak kadar buyuk dosylara
	# denk gelmeyiz
	data = ckdFile.read()

# RegEx mucizesi (Buraya bu satiri anlatan yorum yazsam iyi olur
allFileData = re.findall(b'\x46\x69\x4c\x45[\s\S]*?(?=\x46\x69\x4c\x45|$)',data)

# Buldugumuz butun dosyalari tek tek dosyalara koyalim
for currentFileData in allFileData:

#Check if the data is longer than 65 bytes
#At the end of the file every file signature is repeated therefore we need this step
	if len(currentFileData) <= 65:
		continue
	
	# Dosya istimini bulalim
	filename = re.search(b'\x46\x69\x4c\x45.*?\....', currentFileData).group()
	# Datayi (ilk 65 byte i almadan) dosyalara paketleyelim	
	with open(filename,"wb") as outputFile:
		outputFile.write(currentFileData[65:])
		# Hava atma zamani
		print "File Created:" + filename
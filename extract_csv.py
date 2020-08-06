#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  extract_csv.py
#
#  Copyright 2020 Ali Lahbabi <ali.lahbabi@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from pymongo import MongoClient


def main(args):
	client = MongoClient("mongodb://localhost:27017/")
	database = client["dbanef"]
	collection = database["usager"]

	# Prepare usager request
	query = {}
	projection = {}
	_f = open("usager_fields.ini","r")
	for ch_ in _f:
		ch_ = ch_[:-1]
		if ch_ != "":
			try:
				#projection[ch_] = u"$"+ch_
				projection[ch_] = 1
			except:
				print("Error field")
	print(projection,len(projection))
	print(">>>>>>>>>>>>>>>>>")
	#projection["langues.code"] = u"$langues.code"
	#projection["doc_version"] = u"$doc_version"

	#cursor = collection.find(query, projection = projection)
	cursor = collection.find({}, projection)
	_f.close()
	try:
		_f = open("usager_fields.ini", "r")
		head_ = ""
		for ch_ in _f:
			ch_ = ch_[:-1]
			if ch_ == "" :  break
			if head_ != "":
				head_ = head_ + "," + ch_
			else:
				head_ = ch_
		_o = open("usager_ano.csv", "w")
		_o.write(head_+"\n")
		_f.close()
		for doc in cursor:
			try:
				print(doc, type(doc), len(doc))
				# #print(len(doc['langues']),doc['langues'][0]['code'][0],doc['doc_version'])
				# str_ = ""
				# for i_ in arr_:
				# 	if type(doc[i_]) is list:
				# 		print(i_,type(doc[i_]),doc[i_],len(doc[i_]))
				# 	else:
				# 		print(i_, type(doc[i_]), doc[i_])
				if input("Continuer ? ")== "n" : return 0
			except:
				print(">>")
			# try:
			# 	str_ =""
			# 	for ch_ in _f:
			# 		ch_ = ch_[:-1]
			# 		#print(ch_)
			#
			# 		#ch_ = "'"+ch_+"'"
			# 		try:
			# 			print(ch_)
			# 			print(doc.get[ch_])
			# 			#str_ = str(doc[ch_])+','+str_
			# 		except:
			# 			print("<")
			# 			# >>
			# 		else:
			# 			str_ = ch_ + ',' + str_
			# 		#print(str_)
			# 		#print(doc['_id'],doc['doc_version'])
			# 	#print(doc['langues'][0],len(doc['langues'][0]['code']))
			# except:
			# 	print(">")

	finally:
		client.close()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

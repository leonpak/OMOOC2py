# -*- coding:utf-8 -*-
from sys import *
from os.path import exists


def main():
	print "简单日记：R.查阅日记 W.写日记  Q.退出"
	choose = raw_input("EasyDiary>>>")
	if choose.lower() == 'r':
		print_history()
	elif choose.lower()== 'w':
		write_Diary()
	elif choose.lower()== 'q':
		exit(0)
	else:
		print "请重新选择!!!"
		main()



def print_history():

	if exists("diary.txt") :
		print "历史记录："
		print 30 * '@'
		target = open('diary.txt','r')
		print target.read()
		print 30 * '@'
		target.close()
		
	else:
		print "记录为空!!!请写日记（W）或退出(Q)"
		main()
	
		

def write_Diary():

	print "请在提示符后记录你的内容",
	target = raw_input("Write: ")
	filename = open("diary.txt",'a')
	filename.write(target + "\n")
	filename.close()
	print "WellDone!保存."
	
	
if __name__ == '__main__':
	main()
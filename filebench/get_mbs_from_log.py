import sys
# print(sys.argv[1])

mbs=0


# get the mb/s values from filebench log file
f=open("./log/%s_%s_filebench_log.txt" % (sys.argv[1], sys.argv[2]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('rd/wr') != -1:
         mbs=float((contents[contents.find('rd/wr')+len('rd/wr'):contents.find('mb/s')]).replace(" ", ""))
print 'ext4_varmail_mb/s = %.1f' % (mbs)
f.close()














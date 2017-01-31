import sys
# print(sys.argv[1])





# get the mb/s from log file
f=open("./log/%s_postmark_log.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('megabytes read (') != -1:
         read_mbs = float(contents[contents.find('megabytes read (')+len('megabytes read ('):contents.find(' megabytes per second)')])
     if contents.find('megabytes written (') != -1:
         write_mbs = float(contents[contents.find('megabytes written (')+len('megabytes written ('):contents.find(' megabytes per second)')]) 
print '%s_read_mb/s = %.2f' % (sys.argv[1], read_mbs)
print '%s_write_mb/s = %.2f' % (sys.argv[1], write_mbs)
f.close()




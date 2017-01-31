import sys
# print(sys.argv[1])





# get iops from 1st sequential write log
f=open("./log/%s_1st_sequential_write_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 1st sequential write iops = %d' % (total_of_iops)
f.close()





# get iops from 2st sequential write log
f=open("./log/%s_2nd_sequential_write_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 2nd sequential write iops = %d' % (total_of_iops)
f.close()







# get iops from 3rd random write log
f=open("./log/%s_3rd_random_write_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 3rd random write iops = %d' % (total_of_iops)
f.close()







# get iops from 4th sequential write log
f=open("./log/%s_4th_sequential_write_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 4th sequential write iops = %d' % (total_of_iops)
f.close()





# get iops from 5th random read log
f=open("./log/%s_5th_random_read_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 5th random read iops = %d' % (total_of_iops)
f.close()






# get iops from 6th sequential read log
f=open("./log/%s_6th_sequential_read_log.txt" % (sys.argv[1]), 'r')
total_of_iops = 0
num_of_iops = 0
while True:
     contents = f.readline()
     if not contents: break
     if contents.find(', iops=') != -1:
         # print(contents[contents.find('iops='):contents.find(',runt')])
         iops = int(contents[contents.find(', iops=')+len(', iops='):contents.find(', runt')])
         total_of_iops = total_of_iops + iops
         # num_of_iops = num_of_iops + 1
         # print(iops)
         # print(total_of_iops)
	 # print(num_of_iops)
         # print
print '     *** 6th sequential read iops = %d' % (total_of_iops)
f.close()


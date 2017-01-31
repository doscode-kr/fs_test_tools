
ext4_random_write_iops=0
ext4_sequential_write_iops=0;
ext4_random_read_iops=0;
ext4_sequential_read_iops=0;
ext4_random_write_waf=0;
ext4_sequential_wrtie_waf=0;

f2fs_random_write_iops=0
f2fs_sequential_write_iops=0;
f2fs_random_read_iops=0;
f2fs_sequential_read_iops=0;
f2fs_random_write_waf=0;
f2fs_sequential_wrtie_waf=0;

alfs_random_write_iops=0
alfs_sequential_write_iops=0;
alfs_random_read_iops=0;
alfs_sequential_read_iops=0;
alfs_random_write_waf=0;
alfs_sequential_wrtie_waf=0;





##################################################
# read
##################################################




# read ext4 iops and waf from log files
f=open("./log/ext4_iops.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('3rd random write iops = ') != -1:
         ext4_random_write_iops = int(contents[contents.find('3rd random write iops = ')+len('3rd random write iops = '):-1])
     if contents.find('4th sequential write iops = ') != -1:
         ext4_sequential_write_iops = int(contents[contents.find('4th sequential write iops = ')+len('4th sequential write iops = '):-1])
     if contents.find('5th random read iops = ') != -1:
         ext4_random_read_iops = int(contents[contents.find('5th random read iops = ')+len('5th random read iops = '):-1])
     if contents.find('6th sequential read iops = ') != -1:
         ext4_sequential_read_iops = int(contents[contents.find('6th sequential read iops = ')+len('6th sequential read iops = '):-1])
print ' *** ext4_random_write_iops = %d' % (ext4_random_write_iops)
print ' *** ext4_sequential_write_iops = %d' % (ext4_sequential_write_iops)
print ' *** ext4_random_read_iops = %d' % (ext4_random_read_iops)
print ' *** ext4_sequential_read_iops = %d' % (ext4_sequential_read_iops)
f.close()





#read ext4 waf from log files
f=open("./log/ext4_waf.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('third_WAF = ') != -1:
         ext4_random_write_waf = float(contents[contents.find('third_WAF = ')+len('third_WAF = '):-1])
     if contents.find('fourth_WAF = ') != -1:
         ext4_sequential_write_waf = float(contents[contents.find('fourth_WAF = ')+len('fourth_WAF = '):-1])
print ' *** ext4_random_write_waf = %.4f' % (ext4_random_write_waf)
print ' *** ext4_sequential_write_waf = %.4f' % (ext4_sequential_write_waf)
f.close()






# read f2fs iops and waf from log files
f=open("./log/f2fs_iops.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('3rd random write iops = ') != -1:
         f2fs_random_write_iops = int(contents[contents.find('3rd random write iops = ')+len('3rd random write iops = '):-1])
     if contents.find('4th sequential write iops = ') != -1:
         f2fs_sequential_write_iops = int(contents[contents.find('4th sequential write iops = ')+len('4th sequential write iops = '):-1])
     if contents.find('5th random read iops = ') != -1:
         f2fs_random_read_iops = int(contents[contents.find('5th random read iops = ')+len('5th random read iops = '):-1])
     if contents.find('6th sequential read iops = ') != -1:
         f2fs_sequential_read_iops = int(contents[contents.find('6th sequential read iops = ')+len('6th sequential read iops = '):-1])
print ' *** f2fs_random_wrtie_iops = %d' % (f2fs_random_write_iops)
print ' *** f2fs_sequential_wrtie_iops = %d' % (f2fs_sequential_write_iops)
print ' *** f2fs_random_read_iops = %d' % (f2fs_random_read_iops)
print ' *** f2fs_sequential_read_iops = %d' % (f2fs_sequential_read_iops)
f.close()



#read f2fs waf from log files
f=open("./log/f2fs_waf.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('third_WAF = ') != -1:
         f2fs_random_write_waf = float(contents[contents.find('third_WAF = ')+len('third_WAF = '):-1])
     if contents.find('fourth_WAF = ') != -1:
         f2fs_sequential_write_waf = float(contents[contents.find('fourth_WAF = ')+len('fourth_WAF = '):-1])
print ' *** f2fs_random_write_waf = %.4f' % (f2fs_random_write_waf)
print ' *** f2fs_sequential_write_waf = %.4f' % (f2fs_sequential_write_waf)
f.close()



# read alfs iops and waf from log files
f=open("./log/alfs_iops.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('3rd random write iops = ') != -1:
         alfs_random_write_iops = int(contents[contents.find('3rd random write iops = ')+len('3rd random write iops = '):-1])
     if contents.find('4th sequential write iops = ') != -1:
         alfs_sequential_write_iops = int(contents[contents.find('4th sequential write iops = ')+len('4th sequential write iops = '):-1])
     if contents.find('5th random read iops = ') != -1:
         alfs_random_read_iops = int(contents[contents.find('5th random read iops = ')+len('5th random read iops = '):-1])
     if contents.find('6th sequential read iops = ') != -1:
         alfs_sequential_read_iops = int(contents[contents.find('6th sequential read iops = ')+len('6th sequential read iops = '):-1])
print ' *** alfs_random_wrtie_iops = %d' % (alfs_random_write_iops)
print ' *** alfs_sequential_wrtie_iops = %d' % (alfs_sequential_write_iops)
print ' *** alfs_random_read_iops = %d' % (alfs_random_read_iops)
print ' *** alfs_sequential_read_iops = %d' % (alfs_sequential_read_iops)
f.close()


#read alfs waf from log files
f=open("./log/alfs_waf.txt", 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('third_WAF = ') != -1:
         alfs_random_write_waf = float(contents[contents.find('third_WAF = ')+len('third_WAF = '):-1])
     if contents.find('fourth_WAF = ') != -1:
         alfs_sequential_write_waf = float(contents[contents.find('fourth_WAF = ')+len('fourth_WAF = '):-1])
print ' *** alfs_random_write_waf = %.4f' % (alfs_random_write_waf)
print ' *** alfs_sequential_write_waf = %.4f' % (alfs_sequential_write_waf)
f.close()






##################################################
# write
##################################################


# write the random write iops data file for gnuplot graph
f=open("./gnuplot/random_write_iops_data.gp", "w")
write_data = "0 EXT4 %d\n1 F2FS %d\n2 ALFS %d\n" % (ext4_random_write_iops, f2fs_random_write_iops, alfs_random_write_iops)
f.write(write_data)
f.close()


# write the sequential write iops data file for gnuplot graph
f=open("./gnuplot/sequential_write_iops_data.gp", "w")
write_data = "0 EXT4 %d\n1 F2FS %d\n2 ALFS %d\n" % (ext4_sequential_write_iops, f2fs_sequential_write_iops, alfs_sequential_write_iops)
f.write(write_data)
f.close()


# write the random read iops data file for gnuplot graph
f=open("./gnuplot/random_read_iops_data.gp", "w")
write_data = "0 EXT4 %d\n1 F2FS %d\n2 ALFS %d\n" % (ext4_random_read_iops, f2fs_random_read_iops, alfs_random_read_iops)
f.write(write_data)
f.close()


# write the sequential read iops data file for gnuplot graph
f=open("./gnuplot/sequential_read_iops_data.gp", "w")
write_data = "0 EXT4 %d\n1 F2FS %d\n2 ALFS %d\n" % (ext4_sequential_read_iops, f2fs_sequential_read_iops, alfs_sequential_read_iops)
f.write(write_data)
f.close()


# write the random write waf data file for gnuplot graph
f=open("./gnuplot/random_write_waf_data.gp", "w")
write_data = "0 EXT4 %.4f\n1 F2FS %.4f\n2 ALFS %.4f\n" % (ext4_random_write_waf, f2fs_random_write_waf, alfs_random_write_waf)
f.write(write_data)
f.close()


# write the sequential write waf data file for gnuplot graph
f=open("./gnuplot/sequential_write_waf_data.gp", "w")
write_data = "0 EXT4 %.4f\n1 F2FS %.4f\n2 ALFS %.4f\n" % (ext4_sequential_write_waf, f2fs_sequential_write_waf, alfs_sequential_write_waf)
f.write(write_data)
f.close()









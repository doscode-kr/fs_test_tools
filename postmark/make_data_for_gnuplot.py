import sys

ext4_read_mbs=0
ext4_write_mbs=0
ext4_waf=0
f2fs_read_mbs=0
f2fs_write_mbs=0
f2fs_waf=0
alfs_read_mbs=0
alfs_write_mbs=0
alfs_waf=0

#######################
# read the mb/s
#######################

f=open("./log/ext4_mbs.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('ext4_read_mb/s = ') != -1:
        ext4_read_mbs = float(contents[contents.find('ext4_read_mb/s = ')+len('ext4_read_mb/s = '):-1])
    if contents.find('ext4_write_mb/s = ') != -1:
        ext4_write_mbs = float(contents[contents.find('ext4_write_mb/s = ')+len('ext4_write_mb/s = '):-1])
# print '%.2f' % (ext4_read_mbs)
# print '%.2f' % (ext4_write_mbs)
f.close()

f=open("./log/f2fs_mbs.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('f2fs_read_mb/s = ') != -1:
        f2fs_read_mbs = float(contents[contents.find('f2fs_read_mb/s = ')+len('f2fs_read_mb/s = '):-1])
    if contents.find('f2fs_write_mb/s = ') != -1:
        f2fs_write_mbs = float(contents[contents.find('f2fs_write_mb/s = ')+len('f2fs_write_mb/s = '):-1])
# print '%.2f' % (f2fs_read_mbs)
# print '%.2f' % (f2fs_write_mbs)
f.close()

f=open("./log/alfs_mbs.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('alfs_read_mb/s = ') != -1:
        alfs_read_mbs = float(contents[contents.find('alfs_read_mb/s = ')+len('alfs_read_mb/s = '):-1])
    if contents.find('alfs_write_mb/s = ') != -1:
        alfs_write_mbs = float(contents[contents.find('alfs_write_mb/s = ')+len('alfs_write_mb/s = '):-1])
# print '%.2f' % (alfs_read_mbs)
# print '%.2f' % (alfs_write_mbs)
f.close()




#######################
# read the waf
#######################

f=open("./log/ext4_waf.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('postmark_WAF = ') != -1:
        ext4_waf = float(contents[contents.find('postmark_WAF = ')+len('postmark_WAF = '):-1])
# print '%.4f' % (ext4_waf)
f.close()

f=open("./log/f2fs_waf.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('postmark_WAF = ') != -1:
        f2fs_waf = float(contents[contents.find('postmark_WAF = ')+len('postmark_WAF = '):-1])
# print '%.4f' % (f2fs_waf)
f.close()

f=open("./log/alfs_waf.txt", 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('postmark_WAF = ') != -1:
        alfs_waf = float(contents[contents.find('postmark_WAF = ')+len('postmark_WAF = '):-1])
# print '%.4f' % (alfs_waf)
f.close()





#######################
# write
#######################

# write the read mb/s
f=open("./gnuplot/read_mbs_data.gp", "w")
write_data = "0 EXT4 %.2f\n1 F2FS %.2f\n2 ALFS %.2f\n" % (ext4_read_mbs, f2fs_read_mbs, alfs_read_mbs)
f.write(write_data)
f.close()

# write the write mb/s
f=open("./gnuplot/write_mbs_data.gp", "w")
write_data = "0 EXT4 %.2f\n1 F2FS %.2f\n2 ALFS %.2f\n" % (ext4_write_mbs, f2fs_write_mbs, alfs_write_mbs)
f.write(write_data)
f.close()

# write the waf
f=open("./gnuplot/waf_data.gp", "w")
write_data = "0 EXT4 %.4f\n1 F2FS %.4f\n2 ALFS %.4f\n" % (ext4_waf, f2fs_waf, alfs_waf)
f.write(write_data)
f.close()










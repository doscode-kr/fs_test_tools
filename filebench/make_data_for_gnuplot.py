import sys
# print '%s' % (sys.argv[1]) # sys.argv[1] should mean used workload

ext4_mbs=0
ext4_waf=0
f2fs_mbs=0
f2fs_waf=0
alfs_mbs=0
alfs_waf=0

#######################
# read the mb/s
#######################

f=open("./log/ext4_%s_mbs.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('mb/s = ') != -1:
        ext4_mbs = float(contents[contents.find('mb/s = ')+len('mb/s = '):-1])
# print '%.1f' % (ext4_mbs)
f.close()


f=open("./log/f2fs_%s_mbs.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('mb/s = ') != -1:
        f2fs_mbs = float(contents[contents.find('mb/s = ')+len('mb/s = '):-1])
# print '%.1f' % (f2fs_mbs)
f.close()


f=open("./log/alfs_%s_mbs.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('mb/s = ') != -1:
        alfs_mbs = float(contents[contents.find('mb/s = ')+len('mb/s = '):-1])
# print '%.1f' % (alfs_mbs)
f.close()

#######################
# read the waf
#######################

f=open("./log/ext4_%s_waf.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('filebench_WAF = ') != -1:
        ext4_waf = float(contents[contents.find('filebench_WAF = ')+len('filebench_WAF = '):-1])
# print '%.4f' % (ext4_waf)
f.close()


f=open("./log/f2fs_%s_waf.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('filebench_WAF = ') != -1:
        f2fs_waf = float(contents[contents.find('filebench_WAF = ')+len('filebench_WAF = '):-1])
# print '%.4f' % (f2fs_waf)
f.close()


f=open("./log/alfs_%s_waf.txt" % (sys.argv[1]), 'r')
while True:
    contents = f.readline()
    if not contents: break
    if contents.find('filebench_WAF = ') != -1:
        alfs_waf = float(contents[contents.find('filebench_WAF = ')+len('filebench_WAF = '):-1])
# print '%.4f' % (alfs_waf)
f.close()

#######################
# write
#######################

f=open('./gnuplot/%s_mbs_data.gp' % (sys.argv[1]), 'w')
write_data = "0 EXT4 %.1f\n1 F2FS %.1f\n2 ALFS %.1f\n" % (ext4_mbs, f2fs_mbs, alfs_mbs)
f.write(write_data)
f.close()

f=open('./gnuplot/%s_waf_data.gp' % (sys.argv[1]), 'w')
write_data = "0 EXT4 %.4f\n1 F2FS %.4f\n2 ALFS %.4f\n" % (ext4_waf, f2fs_waf, alfs_waf)
f.write(write_data)
f.close()











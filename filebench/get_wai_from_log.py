import sys
# print(sys.argv[1])




# get wai values from after 0-2nd mounting file system
f=open("../%s_get_wai_log_after_0-2nd_mounting_file_system.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         after_mounting_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         after_mounting_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** after_mounting_dataUnitWrite = %d, after_mounting_controllerDataUnitsWritten = %d' % (after_mounting_dataUnitWrite,after_mounting_controllerDataUnitsWritten)
if after_mounting_dataUnitWrite != 0:
     after_mounting_waf=after_mounting_controllerDataUnitsWritten/after_mounting_dataUnitWrite
     print '     *** after_mounting_WAF = %.10f' % (after_mounting_waf)
else :
     print '     *** after_mounting_WAF = Error(division by zero)'
f.close()





# get wai values from after 1st sequential write log
f=open("./log/%s_%s_get_wai_log_after_1st_sequential_write.txt" % (sys.argv[1], sys.argv[2]) , 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         first_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         first_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** first_dataUnitWrite = %d, first_controllerDataUnitsWritten = %d' % (first_dataUnitWrite,first_controllerDataUnitsWritten)
if (first_dataUnitWrite-after_mounting_dataUnitWrite) != 0:
     first_waf=(first_controllerDataUnitsWritten-after_mounting_controllerDataUnitsWritten)/(first_dataUnitWrite-after_mounting_dataUnitWrite)
     print '     *** first_WAF = %.10f' % (first_waf)
else :
     print '     *** first_WAF = Error(division by zero)'
f.close()





# get wai values from after 2nd sequential write log
f=open("./log/%s_%s_get_wai_log_after_2nd_sequential_write.txt" % (sys.argv[1], sys.argv[2]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         second_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         second_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** second_dataUnitWrite = %d, second_controllerDataUnitsWritten = %d' % (second_dataUnitWrite,second_controllerDataUnitsWritten)
if (second_dataUnitWrite-first_dataUnitWrite) != 0:
     second_waf=(second_controllerDataUnitsWritten-first_controllerDataUnitsWritten)/(second_dataUnitWrite-first_dataUnitWrite)
     print '     *** second_WAF = %.10f' % (second_waf)
else :
     print '     *** second_WAF = Error(division by zero)'
f.close()





# get wai values from after running the filebench
f=open("./log/%s_%s_get_wai_log_after_run_the_filebench.txt" % (sys.argv[1], sys.argv[2]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         filebench_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         filebench_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** filebench_dataUnitWrite = %d, filebench_controllerDataUnitsWritten = %d' % (filebench_dataUnitWrite,filebench_controllerDataUnitsWritten)
if (filebench_dataUnitWrite-second_dataUnitWrite) != 0:
     filebench_waf=(filebench_controllerDataUnitsWritten-second_controllerDataUnitsWritten)/(filebench_dataUnitWrite-second_dataUnitWrite)
     print '     *** filebench_WAF = %.10f' % (filebench_waf)
else :
     print '     *** filebench_WAF = Error(division by zero)'
f.close()







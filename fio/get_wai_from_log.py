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
     print '     *** after_mounting_WAF = %.4f' % (after_mounting_waf)
else :
     print '     *** after_mounting_WAF = Error(division by zero)'
f.close()





# get wai values from after 1st sequential write log
f=open("./log/%s_get_wai_log_after_1st_sequential_write.txt" % (sys.argv[1]), 'r')
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
     print '     *** first_WAF = %.4f' % (first_waf)
else :
     print '     *** first_WAF = Error(division by zero)'
f.close()





# get wai values from after 2nd sequential write log
f=open("./log/%s_get_wai_log_after_2nd_sequential_write.txt" % (sys.argv[1]), 'r')
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
     print '     *** second_WAF = %.4f' % (second_waf)
else :
     print '     *** second_WAF = Error(division by zero)'
f.close()





# get wai values from after 3rd random write log
f=open("./log/%s_get_wai_log_after_3rd_random_write.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         third_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         third_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** third_dataUnitWrite = %d, third_controllerDataUnitsWritten = %d' % (third_dataUnitWrite,third_controllerDataUnitsWritten)
if (third_dataUnitWrite-second_dataUnitWrite) != 0:
     third_waf=(third_controllerDataUnitsWritten-second_controllerDataUnitsWritten)/(third_dataUnitWrite-second_dataUnitWrite)
     print '     *** third_WAF = %.4f' % (third_waf)
else :
     print '     *** third_WAF = Error(division by zero)'
f.close()





# get wai values from after 4th sequential write log
f=open("./log/%s_get_wai_log_after_4th_sequential_write.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         fourth_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         fourth_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** fourth_dataUnitWrite = %d, fourth_controllerDataUnitsWritten = %d' % (fourth_dataUnitWrite,fourth_controllerDataUnitsWritten)
if (fourth_dataUnitWrite-third_dataUnitWrite) != 0:
     fourth_waf=(fourth_controllerDataUnitsWritten-third_controllerDataUnitsWritten)/(fourth_dataUnitWrite-third_dataUnitWrite)
     print '     *** fourth_WAF = %.4f' % (fourth_waf)
else :
     print '     *** fourth_WAF = Error(division by zero)'

f.close()





# get wai values from after 5th random read log
f=open("./log/%s_get_wai_log_after_5th_random_read.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         fifth_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         fifth_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** fifth_dataUnitWrite = %d, fifth_controllerDataUnitsWritten = %d' % (fifth_dataUnitWrite,fifth_controllerDataUnitsWritten)
if (fifth_dataUnitWrite-fourth_dataUnitWrite) != 0:
     fifth_waf=(fifth_controllerDataUnitsWritten-fourth_controllerDataUnitsWritten)/(fifth_dataUnitWrite-fourth_dataUnitWrite)
     print '     *** fifth_WAF = %.4f' % (fifth_waf)
else :
     print '     *** fifth_WAF = Error(division by zero)'
f.close()





# get wai values from after 6th sequential read log
f=open("./log/%s_get_wai_log_after_6th_sequential_read.txt" % (sys.argv[1]), 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         sixth_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         sixth_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** sixth_dataUnitWrite = %d, sixth_controllerDataUnitsWritten = %d' % (sixth_dataUnitWrite,sixth_controllerDataUnitsWritten)
if (sixth_dataUnitWrite-fifth_dataUnitWrite) != 0:
     sixth_waf=(sixth_controllerDataUnitsWritten-fifth_controllerDataUnitsWritten)/(sixth_dataUnitWrite-fifth_dataUnitWrite)
     print '     *** sixth_WAF = %.4f' % (sixth_waf)
else :
     print '     *** sixth_WAF = Error(division by zero)'
f.close()



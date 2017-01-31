import sys
# print(sys.argv[1]) # file system

# get wai values after 0-2nd mounting file system
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

# get wai values after running the dd command
f=open("./log/%s_get_wai_log_after_dd_command.txt" % (sys.argv[1]) , 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         after_dd_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         after_dd_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** after_dd_dataUnitWrite = %d, after_dd_controllerDataUnitsWritten = %d' % (after_dd_dataUnitWrite,after_dd_controllerDataUnitsWritten)
if (after_dd_dataUnitWrite-after_mounting_dataUnitWrite) != 0:
     after_dd_waf=(after_dd_controllerDataUnitsWritten-after_mounting_controllerDataUnitsWritten)/(after_dd_dataUnitWrite-after_mounting_dataUnitWrite)
     print '     *** after_dd_WAF = %.10f' % (after_dd_waf)
else :
     print '     *** after_dd_WAF = Error(division by zero)'
f.close()


# get wai values after running the postmark
f=open("./log/%s_get_wai_log_after_run_the_postmark.txt" % (sys.argv[1]) , 'r')
while True:
     contents = f.readline()
     if not contents: break
     if contents.find('te.dw : ') != -1:
         # print(int((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", "")))
         pm_dataUnitWrite=float((contents[contents.find('te.dw : ')+len('te.dw : '):contents.find(' / ')]).replace(",", ""))
     if contents.find('tten.dw : ') != -1:
         # print(int((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", "")))
         pm_controllerDataUnitsWritten=float((contents[contents.find('tten.dw : ')+len('tten.dw : '):-1]).replace(",", ""))
print '     *** postmark_dataUnitWrite = %d, postmark_controllerDataUnitsWritten = %d' % (pm_dataUnitWrite,pm_controllerDataUnitsWritten)
if (pm_dataUnitWrite-after_dd_dataUnitWrite) != 0:
     pm_waf=(pm_controllerDataUnitsWritten-after_dd_controllerDataUnitsWritten)/(pm_dataUnitWrite-after_dd_dataUnitWrite)
     print '     *** postmark_WAF = %.10f' % (pm_waf)
else :
     print '     *** postmark_WAF = Error(division by zero)'
f.close()




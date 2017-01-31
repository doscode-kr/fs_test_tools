
Written by Changhun Jung, Hyunyoung Lee, DongOh Shin from SK Hynix Memory Solutions.
If you have any question or report about this, please don't hesitate to contact to
Changhun Jung <jcptk677@gmail.com>

This is a test tool to measure the performance of EXT4, F2FS and ALFS(modified F2FS)
file system with SK hynix PE3110 specific. For this test, we used the fio,
postmark and filebench benchmark tools on Kernel 4.8.1, Cent OS 7.2.
The fio's version is 2.2.8, postmark's version is 1.5 and
filebench's version is 1.5-alpha3.

From now on, we will explain the usage of shell, python and gnuplot scripts
that are located in [fs_test_tool] directory. before using these,
you have to set the absolute path of file or directory on scripts
to depend on your path.

<mount usage>
1. cd fs_test_tool
2. ./mount.sh <ext4 or f2fs or alfs>
   When running the mount.sh, you have to specify file system name that you want to mount
   on nvme driver. The mount.sh has a nvme driver format, file system making and mounting
   funtions. After running the mount.sh, [get_wai_log_after_0-1st_driver_format.txt]
   log file will be created in current directory, this log have a
   WAI(Write Amplification Information) values after format the nvme driver.
   This WAI can be used to calculate the WAF(Write Amplification Factor).
   Also, [<filesystem>_get_wai_log_after_0-2_mounting_file_system.txt] will be created
   in current directory, this log have a WAI values after mounting the file system.

<fio usage>
1. cd fs_test_tool/fio
2. ./fio.sh <ext4 or f2fs or alfs>
   When running the fio.sh, you have to specify file system name that is mounted
   on nvme driver as a parameter. The fio.sh consists of the 6 fio funtions
   in the order SW(Sequential Write), SW, RW(random write), SW, RR(Random Read)
   and SR(Sequential Read). First SW and Second SW are in charge of pre-condition.
   You can modify the detailed fio options on [fio.sh] file.
   After running each fio funtions, fio log files and wai log files are created
   in [log] directory like these [ext4_3rd_random_write_log.txt] and
   [ext4_get_wai_log_after_3rd_random_write.txt], these files are raw data.
   [ext4_3rd_random_write_log.txt] has a result of fio like IOPS,
   and [ext4_get_wai_log_after_3rd_random_write.txt] has a WAI value
   to calculate the WAF. Also, fio.sh makes the processed data from raw data
   in [log] directory by using the [get_iops_from_log.py] and [get_wai_from_log.py]
   (We used the python version 2.7.5). The processed data's file name will be
   [<filesystem>_iops.txt] and [<filesystem>_waf.txt].
3. python make_data_for_gnuplot.py
   This command makes the [*_data.gp] files from processed data for gnuplot
   in [gnuplot] directory. Before running this command, you should have ext4, f2fs
   and alfs file system test result log files.
4. cd gnuplot
5. ./gnuplot.sh
   This command makes the graph files using the gnuplot, [*_conf.gp] and [*_data.gp]
   (We used the gnuplot version 4.6). You can check the graph files with IOPS and WAF
   in [graph] directory.

<postmark usage>
1. cd fs_test_tool/postmark
2. ./postmark.sh <ext4 or f2fs or alfs>
   When running the postmark.sh, you have to specify file system name that is mounted
   on nvme driver as a parameter. This command runs the dd-pre-condition and
   postmark by using the [postmark.conf] file that is located in [postmark_files] directory.
   You can modify the detailed option of dd-pre-condition and postmark
   on [postmark.sh] and [postmark.conf] file respectively.
   After running the postmark, the dd-pre-condition and postmark log file will be created
   in [log] directory as named [<filesystem>_dd_log.txt] and [<filesystem>_postmark_log.txt]
   respectively. Also, [<filesystem>_get_wai_log_after_dd_command.txt] and 
   [<filesytsem>_get_wai_log_after_run_the_postmark.txt] will be created in [log] directory,
   this wai logs have a WAI values to calculate the WAF value. All of these are raw data.
   Then processed data files will be created from raw data files as named
   [<filesystem>_mbs.txt] and [<filesystem>_waf.txt] in [log] directory
   using [get_mbs_from_log.py] and [get_wai_from_log.py].
3. python make_data_for_gnuplot.py
   This command makes the [*_data.gp] files from processed data for gnuplot
   in [gnuplot] directory. Before running this command, you should have ext4, f2fs
   and alfs file system test result log files.
4. cd gnuplot
5. ./gnuplot.sh
   This command makes the graph files using the gnuplot, [*_conf.gp] and [*_data.gp].
   You can check the graph files with MB/S and WAF in [graph] directory.

<filebench usage>
1. cd fs_test_tool/filebench
2. ./filebench <ext4 or f2fs or alfs> <videoserver or varmail or fileserver or oltp>
   This command runs the fio-pre-condition and filebench by using workloads.
   When running the filebench, you have to specify file system name that
   is mounted on nvme driver as a parameter, also you have to specify workload name
   that you want to use as a parameter. The workloads are provided by filebench tool
   and located in [filebench_files/workloads_2] directory. You can modify the
   detailed option of filebench workload. In addtion, you can modify the detaild
   option of fio-pre-condition on [fio-pre-condition.sh].
   After running the filebench, fio-pre-condition, result of filebench,
   wai values log files are created in [log] directory. These are raw data.
   Then processed data files will be created from raw data files as named 
   [<filesystem>_<workload>_mbs.txt] and [<filesystem>_<workload>_waf.txt]
   in [log] directory using [get_mbs_from_log.py] and [get_wai_from_log.py].
3. python make_data_for_gnuplot.py <videoserver or varmail or fileserver or oltp>
   When running this command, you have to specify the used workload as a parameter.
   This command makes the [*_data.gp] files from processed data for gnuplot
   in [gnuplot] directory. Before running this command, you should have ext4, f2fs
   and alfs file system test result log files for one workload.
4. cd gnuplot
5. ./gnuplot.sh <videoserver or varmail or fileserver or oltp>
   When running this command, you have to specify the used workload as a parameter.
   This command makes the graph files using the gnuplot, [*_conf.gp] and [*_data.gp].
   You can check the graph files with MB/S and WAF in [graph] directory.


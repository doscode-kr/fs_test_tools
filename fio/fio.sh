#!/bin/sh
filesystem=$1 # file system (ext4 or f2fs or alfs)
basic_path=/home/mizno
mounting_path=/mounting_point
nvme_cli_path=/nvme-cli
nvme_driver=/dev/nvme0n1
fio_total_size=800G
# temp1=5
# temp2=10
# temp3=$(($temp1+$temp2))
# echo $temp3
# temp4=5.12321313
# temp5=1.21212969
# temp6=$(echo "scale=10; $temp4 / $temp5" | bc)
# echo $temp6



if [ $# = 0 ]
then
        echo "usage : ./fio.sh <ext4 or f2fs or alfs>"
        exit
fi






if [ "$filesystem" = "ext4" ]
then
	filesystem=$1
elif [ "$filesystem" = "f2fs" ]
then
	filesystem=$1
elif [ "$filesystem" = "alfs" ]
then
	filesystem=$1
else
	echo "usage : ./fio.sh <ext4 or f2fs or alfs>"
        exit
fi





# 1st sequential write with fio(pre-condition)
echo " *** 1st sequential write with fio(pre-condition)"
first_sequential_write_log_file_name="$filesystem"_1st_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$first_sequential_write_log_file_name





# vu cmd after 1st sequential write with fio(pre-condition)
echo " *** vu cmd after 1st sequential write with fio(pre-condition)"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_1st_sequential_write.txt





# 2nd sequential write with fio(pre-condition)
echo " *** 2nd sequential write with fio(pre-condition)"
second_sequential_write_log_file_name="$filesystem"_2nd_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$second_sequential_write_log_file_name





# vu cmd after 2nd sequantial write with fio(pre-condition)
echo " *** vu cmd after 2nd sequantial write with fio(pre-condition)"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_2nd_sequential_write.txt





# 3rd random write with fio
echo " *** 3rd random write with fio"
third_random_write_log_file_name="$filesystem"_3rd_random_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$third_random_write_log_file_name





# vu cmd after 3rd random write with fio
echo " *** vu cmd after 3rd random write with fio"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_3rd_random_write.txt





# 4th sequential write with fio
echo " *** 4th sequential write with fio"
fourth_sequential_write_log_file_name="$filesystem"_4th_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=write \
 --bs=128k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$fourth_sequential_write_log_file_name





# vu cmd after 4th sequential write with fio
echo " *** vu cmd after 4th sequential write with fio"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_4th_sequential_write.txt





# 5th random read with fio
echo " *** 5th random read with fio"
fifth_random_read_log_file_name="$filesystem"_5th_random_read_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=randread \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$fifth_random_read_log_file_name





# vu cmd after 5th random read with fio
echo " *** vu cmd after 5th random read with fio"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_5th_random_read.txt





# 6th sequential read with fio
echo " *** 6th sequential read with fio"
sixth_sequential_read_log_file_name="$filesystem"_6th_sequential_read_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=read \
 --bs=128k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=$fio_total_size \
> ./log/$sixth_sequential_read_log_file_name





# vu cmd after 6th sequential read with fio
echo " *** vu cmd after 6th sequential read with fio"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$filesystem"_get_wai_log_after_6th_sequential_read.txt





# get the iops from log files
echo " *** get the iops from write and read log files"
sudo python get_iops_from_log.py $filesystem > ./log/"$filesystem"_iops.txt





# get the waf from log files
echo " *** get the waf from log files"
sudo python get_wai_from_log.py $filesystem > ./log/"$filesystem"_waf.txt








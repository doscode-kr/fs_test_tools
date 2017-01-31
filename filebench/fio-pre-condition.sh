#!/bin/sh
argv1=$1 # file system (ext4 or f2fs or alfs)
argv2=$2 # filebench workload (videoserver or varmail or fileserver or oltp)
basic_path=/home/mizno
mounting_path=/mounting_point
nvme_cli_path=/nvme-cli
nvme_driver=/dev/nvme0n1
# temp1=5
# temp2=10
# temp3=$(($temp1+$temp2))
# echo $temp3
# temp4=5.12321313
# temp5=1.21212969
# temp6=$(echo "scale=10; $temp4 / $temp5" | bc)
# echo $temp6





# 1st sequential write with fio(pre-condition)
echo " *** 1st sequential write with fio(pre-condition)"
first_sequential_write_log_file_name="$argv1"_"$argv2"_1st_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=4k \
> ./log/$first_sequential_write_log_file_name





# vu cmd after 1st sequential write with fio(pre-condition)
echo " *** vu cmd after 1st sequential write with fio(pre-condition)"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$argv1"_"$argv2"_get_wai_log_after_1st_sequential_write.txt





# 2nd sequential write with fio(pre-condition)
echo " *** 2nd sequential write with fio(pre-condition)"
second_sequential_write_log_file_name="$argv1"_"$argv2"_2nd_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path$mounting_path/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=4k \
> ./log/$second_sequential_write_log_file_name





# vu cmd after 2nd sequantial write with fio(pre-condition)
echo " *** vu cmd after 2nd sequantial write with fio(pre-condition)"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > ./log/"$argv1"_"$argv2"_get_wai_log_after_2nd_sequential_write.txt









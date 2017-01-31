#!/bin/sh
basic_path=/home/mizno
nvme_driver=/dev/nvme0n1
filesystem=$1

# 1st sequential write with fio(pre-condition)
echo " *** 1st sequential write with fio(pre-condition)"
first_sequential_write_log_file_name=1st_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path/mounting_point/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100M \
> ./log/$first_sequential_write_log_file_name

# vu cmd after 1st sequential write with fio(pre-condition)
echo " *** vu cmd after 1st sequential write with fio(pre-condition)"

# 2nd sequential write with fio(pre-condition)
echo " *** 2nd sequential write with fio(pre-condition)"
second_sequential_write_log_file_name=2nd_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path/mounting_point/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100M \
> ./log/$second_sequential_write_log_file_name

# vu cmd after 2nd sequantial write with fio(pre-condition)
echo " *** vu cmd after 2nd sequantial write with fio(pre-condition)"

# 3rd random write with fio
echo " *** 3rd random write with fio"
third_random_write_log_file_name=3rd_random_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path/mounting_point/fio_test \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100M \
> ./log/$third_random_write_log_file_name

# vu cmd after 3rd sequantial write with fio
echo " *** vu cmd after 3rd sequantial write with fio"

# 4th sequential write with fio
echo " *** 4th sequential write with fio"
fourth_sequential_write_log_file_name=4th_sequential_write_log.txt
sudo fio --name=fio_test \
 --filename=$basic_path/mounting_point/fio_test \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100M \
> ./log/$fourth_sequential_write_log_file_name

# vu cmd after 4th sequential write with fio
echo " *** vu cmd after 4th sequential write with fio"

# get the iops from log files
first_sequential_write_iops=$(python get_iops_from_log.py ./log/$first_sequential_write_log_file_name)
second_sequential_write_iops=$(python get_iops_from_log.py ./log/$second_sequential_write_log_file_name)
third_random_write_iops=$(python get_iops_from_log.py ./log/$third_random_write_log_file_name)
fourth_sequential_write_iops=$(python get_iops_from_log.py ./log/$fourth_sequential_write_log_file_name)
echo $first_sequential_write_iops
echo $second_sequential_write_iops
echo $third_random_write_iops
echo $fourth_sequential_write_iops
















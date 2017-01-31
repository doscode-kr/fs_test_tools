#!/bin/sh
filesystem=$1 # file system (ext4 or f2fs or alfs)
basic_path=/home/mizno
mounting_path=/mounting_point


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

echo " *** run the pre-condition command"
sudo dd if=/dev/zero of=/home/mizno/mounting_point/dd bs=1G count=821 > ./log/"$filesystem"_dd_log.txt 2>&1

echo " *** vu cmd after running the dd command"
sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > ./log/"$filesystem"_get_wai_log_after_dd_command.txt

echo " *** run the postmark"
./postmark_files/postmark ./postmark_files/postmark.conf > ./log/"$filesystem"_postmark_log.txt

echo " *** vu cmd after running the postmark"
sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > ./log/"$filesystem"_get_wai_log_after_run_the_postmark.txt

# get the mb/s from log file
sudo python get_mbs_from_log.py $filesystem > ./log/"$filesystem"_mbs.txt

# get the wai from log file
sudo python get_wai_from_log.py $filesystem > ./log/"$filesystem"_waf.txt


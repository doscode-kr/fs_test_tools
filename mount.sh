#!/bin/sh
basic_path=/home/mizno
mounting_path=/mounting_point
nvme_cli_path=/nvme-cli
nvme_driver=/dev/nvme0n1
filesystem=$1
if [ $# = 0 ]
then
	echo "usage : ./mount.sh <ext4 or f2fs or alfs>"
	exit
fi




# format the nvme driver
echo " *** format the nvme driver"
sudo $basic_path$nvme_cli_path/nvme format $nvme_driver
# sleep 1





# vu cmd after driver format
echo " *** vu cmd after driver format"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > get_wai_log_after_0-1st_driver_format.txt
# sleep 1





# make the file system
echo " *** make the file system"
if [ "$filesystem" = "ext4" ]
then
        sudo mkfs -t ext4 -b 4096 $nvme_driver
elif [ "$filesystem" = "f2fs" ]
then
	sudo insmod $basic_path/f2fs481/f2fs.ko
	sudo $basic_path/f2fs481/tools/f2fs-tools/mkfs/mkfs.f2fs -s 8 -a 0 -d 1 -l F2FS $nvme_driver
elif [ "$filesystem" = "alfs" ]
then
	sudo insmod $basic_path/alfs20170113/fix-risa-read-chkpoint/f2fs.ko
	sudo $basic_path/alfs20170113/fix-risa-read-chkpoint/tools/mkfs/mkfs.f2fs -s 8 -a 0 -d 1 -l ALFS $nvme_driver
else
	echo "usage : ./mount.sh <ext4 or f2fs or alfs>"
	exit 1
fi 
# sleep 1





# mount the file system
echo " *** mount the file system"
if [ "$filesystem" = "ext4" ]
then
        sudo mount -t ext4 -o discard $nvme_driver $basic_path$mounting_path/
elif [ "$filesystem" = "f2fs" ]
then
	sudo mount -t f2fs -o discard $nvme_driver $basic_path$mounting_path/
elif [ "$filesystem" = "alfs" ]
then
	sudo mount -t f2fs -o discard $nvme_driver $basic_path$mounting_path/
else
	echo "usage : ./mount.sh <ext4 or f2fs or alfs>"
	exit 1
fi 
# sleep 1





# vu cmd after mouting file system
echo " *** vu cmd after driver format"
sudo $basic_path$nvme_cli_path/nvme get-wai $nvme_driver > "$filesystem"_get_wai_log_after_0-2nd_mounting_file_system.txt





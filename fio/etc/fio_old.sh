sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > get_wai_log_0_mounting.txt

echo " *** start the 1st 4k 1000G random write"

fio --name=fio \
 --filename=/home/mizno/mounting_point/fio \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --thread \
 --direct=1 \
 --size=836G \

echo " *** end the 1st 4k 1000G random write"

sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > get_wai_log_1st_4k_1000G_random_write.txt

echo " *** start the 2st 4k 1000G random write"

fio --name=fio \
 --filename=/home/mizno/mounting_point/fio \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --thread \
 --direct=1 \
 --size=836G \

echo " *** end the 2st 4k 1000G random write"

sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > get_wai_log_2st_4k_1000G_random_write.txt



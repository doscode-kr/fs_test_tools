
sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1

echo "write the fio1"

fio --name=fio1 \
 --filename=/home/mizno/fs_test/fio1 \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100G \

sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1

echo "delete the fio1"

sudo rm -rf /home/mizno/fs_test/fio1

sleep 3

sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1

echo "write the fio2"

fio --name=fio2 \
 --filename=/home/mizno/fs_test/fio2 \
 --rw=write \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100G \

sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1

echo "delete the fio2"

sudo rm -rf /home/mizno/fs_test/fio2

sleep 3

sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1

echo "write the fio3"

fio --name=fio3 \
 --filename=/home/mizno/fs_test/fio3 \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=1 \
 --iodepth=128 \
 --direct=1 \
 --thread \
 --size=100G \

sudo /home/mizno/nvme-cli/nvme smart-log /dev/nvme0n1



fio --name=fio \
 --filename=/home/mizno/mounting_point/fio \
 --rw=randwrite \
 --bs=4k \
 --ioengine=libaio \
 --numjobs=8 \
 --iodepth=128 \
 --thread \
 --direct=1 \
 --size=1000G \



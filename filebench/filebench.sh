#!/bin/sh
argv1=$1
argv2=$2
filesystem=""
workload=""
if [ $# = 0 ]
then
        echo "usage : ./filebench.sh <ext4 or f2fs or alfs> <videoserver or varmail or fileserver or oltp>"
        exit
fi

if [ "$argv1" = "ext4" ]
then
	filesystem=$argv1
elif [ "$argv1" = "f2fs" ]
then
	filesystem=$argv1
elif [ "$argv1" = "alfs" ]
then
	filesystem=$argv1
else
	echo "usage : ./filebench.sh <ext4 or f2fs or alfs> <videoserver or varmail or fileserver or oltp>"
        exit
fi

if [ "$argv2" = "videoserver" ]
then
	workload=$argv2
elif [ "$argv2" = "varmail" ]
then
	workload=$argv2
elif [ "$argv2" = "fileserver" ]
then
	workload=$argv2
elif [ "$argv2" = "oltp" ]
then
	workload=$argv2
else
        echo "usage : ./filebench.sh <ext4 or f2fs or alfs> <videoserver or varmail or fileserver or oltp>"
        exit
fi

# run the fio-pre-condition
sudo ./fio-pre-condition.sh $argv1 $argv2



# echo $workload".f"

echo " *** run the filebench "$argv2" on the "$argv1

./filebench_files/filebench -f ./filebench_files/workloads_2/"$workload".f > ./log/"$argv1"_"$argv2"_filebench_log.txt

echo " *** vu cmd after filebench "$argv2" on the "$argv1

sudo /home/mizno/nvme-cli/nvme get-wai /dev/nvme0n1 > ./log/"$argv1"_"$argv2"_get_wai_log_after_run_the_filebench.txt


# run the get_wai_from_log.py
sudo python get_wai_from_log.py $argv1 $argv2 > ./log/"$argv1"_"$argv2"_waf.txt

# run the get_mbs_from_log.py
sudo python get_mbs_from_log.py $argv1 $argv2 > ./log/"$argv1"_"$argv2"_mbs.txt








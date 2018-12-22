#!/bin/sh
i=0
while [ $i -le 255 ]
do
	myip=192.168.7.$i
	ping -c 1 $myip
	if ($?);then
		echo "$myip" >> /home/dange/ip.txt
	fi
	i=`expr $i + 1`;
done

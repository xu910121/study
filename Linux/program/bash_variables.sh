#!/bin/bash
i=0;
while [ $i -lt 4 ];
do
  echo $i;
  i=`expr $i + 1`;
  # let i+=1;
  # ((i++));
  # i=$[$i+1];
  # i=$(( $i + 1 ))
done

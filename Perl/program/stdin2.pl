#!/bin/perl
chomp(@lines = <STDIN>);
for($i=0;$i<5;$i++){
	print "$lines[$i]\n";
}

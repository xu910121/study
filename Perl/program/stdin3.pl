#!/bin/perl
use feature 'say';
while (1)
{
	chomp($lines = <STDIN>);
	if (!defined($lines)){
		print "\$lines is null\n";
	}else{
		say "$lines ??";
	}
}

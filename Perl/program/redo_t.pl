#!/usr/bin/perl
use strict;
use warnings;

open(Test_t,'<',"E:/test.txt") or die "Can not open file!";
while (<Test_t>) {
	print "1\n";
	chomp;
	if (s/\\$//) {
		$_ .= <Test_t>;
		print $_;
		redo unless eof; 
	}
}
close(Test_t);
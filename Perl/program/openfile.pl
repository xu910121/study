#!/usr/bin/perl -w
use strict;
open my $test,'<', "test.pl" or die "$!";
while (<$test>) {
	print "$_\n";
}
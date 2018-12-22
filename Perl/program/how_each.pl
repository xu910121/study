#!/bin/perl
@rocks = qw/bedrock slate rubble granite /;
foreach $index ( 0 .. $#rocks ) {
	print "$index: $rocks[$index]\n"
}

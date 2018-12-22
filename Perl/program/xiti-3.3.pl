#!/bin/perl
@names = qw/ fred betty barney dino wilma pebbles bamm-bamm /;
chomp(@lines = <STDIN>);
for($i = 0;$i <= $#lines;$i++)
{
	print "$names[$lines[$i]-1]\n";
}

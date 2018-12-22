#!/bin/perl
chomp(@lines = <STDIN>);
@rev = reverse @lines ;
for($i = 0;$i <= $#rev;$i++)
{
	print "$rev[$i]\n";
}

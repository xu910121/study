#!/usr/bin/perl

sub add {
	$sum = $_[0] +$_[1];
	print $sum . "\n";
}

$test = \&add;
$test->(2,3);
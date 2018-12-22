#!/usr/bin/perl
#sub test_sort { $arr{$a} <=> $arr{$b} };
@arr = qw/5 9 3 8 2 1 0 7 92 5 6/;
my @result = sort {$a <=> $b} @arr;
print "@result" . "\n";


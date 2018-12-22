#!/usr/bin/perl -w

$test = "abcda";
($result = $test) =~ s/a/11/g;
print "$test\n";
print "$result";

($result = $test) =~ tr/ab/11/;
print "$test\n";
print "$result";
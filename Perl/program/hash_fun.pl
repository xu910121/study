#!/bin/perl
my %hash = ('a' => 1,'b' => 2,'c' => 3);
my @k = keys(%hash);
my @v = values(%hash);
print "@k\n";
print "@v\n";
while (($key,$value) = each(%hash)){
	print "$key => $value\n";
}

if (exists $hash{"a"}){
	print "exists!!!!!!!\n";
}
print "PATH is $ENV{PATH}\n";

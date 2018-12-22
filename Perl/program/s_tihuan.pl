#!/usr/bin/perl
$_ = "He's out bowling with Barney tonight.";
s/Barney/Fred/;
print "$_\n";
s/with (\w+)/against $1's team/;
print "$_\n";

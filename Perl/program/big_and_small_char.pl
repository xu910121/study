#!/usr/bin/perl
$_ = "I saw Barney with Fred.";
s/(fred|barney)/\U$1/gi;
print "$_\n";

s/(fred|barney)/\L$1/gi;
print "$_\n";

s/(fred|barney)/\u\L$1/ig;
print "$_\n";


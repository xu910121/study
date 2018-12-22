#!/usr/bin/perl
$_ = "I'm much better \nthan Barney is \nat bowling,\nWilma.\n";
print "Found ‘wilma’ at start of line\n" if /^Wilma\b/im;

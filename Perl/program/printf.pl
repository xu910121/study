#!/bin/perl
my @items = qw( wilma dino pebbles );
my $format = "The items are :\n" . ("%10s\n" x @items);
print $format,@items;
printf "The items are:\n".("%10s\n" x @items),@items;

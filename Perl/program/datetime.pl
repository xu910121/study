#!/usr/bin/perl

use DateTime;

my $dt = DateTime->from_epoch( epoch => time);

printf '%4d%02d%02d',$dt->year,$dt->month,$dt->day;

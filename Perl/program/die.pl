#!/bin/perl
if (!open LOG,'</var/log/dmesg'){
	die "Cannot open log:$!";
}

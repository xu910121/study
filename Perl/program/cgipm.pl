#!/usr/bin/perl
use CGI qw(:all);

print header("text/plain");
foreach $param ( param() ) {
	print "$param:" . param($sparm) . "\n";
}

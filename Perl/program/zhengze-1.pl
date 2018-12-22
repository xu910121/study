#!/bin/perl
use 5.010;
print "Do you like Perl?";
my $likes_perl = (<STDIN> =~ /\byes\b/i);
if ($likes_perl){
	print "You said earlier that you like Perl,so...\n";
}

my $names = 'Fred or Barney';
if ( $names =~ m/(\w+) (and|or) (\w+)/){	
	say "I saw $1 and $2";
}

if ("Hello there, neighbor" =~ /\s(\w+),/){
	print "That \$& matched '$&'.\n";
	print "That \$1 matched '$1'.\n";
	print "That \$` is $`.\n";
	print "That \$' is $'.\n";
}

if ("Hello there, neighbor" =~ /\s(\w+),/p){
		print "That actually matched '${^MATCH}'.\n";
	}
if ("Hello there, neighbor" =~ /\s(\w+),/p){
		print "That was (${^PREMATCH}) (${^MATCH}) (${^POSTMATCH}).\n";
}

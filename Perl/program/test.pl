#!/bin/perl
#use feature 'say';
#while (<>)
#{
#	say "$_";
#}

#open CONFIG,'<:encoding(UTF-8)',"test.pl";
#while (<CONFIG>)
#{
#	print "$_";
#}

$result = "fred xxxxxxxxx barney";
print $result . "\n";
$result =~ s/x+//;#$result =~ s/x*//是达不到效果的。
print $result . "\n";

#x操作符
$tab = 64;
print '-' x 80;
print "\t" x ($tab/8), ' '  x ($tab%8);
print "***********\n";

while (<>) {
	chomp;
	last unless -f $_;
	print "exits";
}

$paragrapth = "perlfdkjlgdfaperlfdksfjperldjflds";
if ( @perls = $paragrapth =~ /perl/gi ) {
	print "\$paragrapth = $paragrapth\n";
	printf "Perl mentioned %d times.\n", scalar @perls;
}
print "test!" . "\n";
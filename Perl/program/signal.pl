#!/usr/bin/perl
my $int_count = 0;
sub my_int_handler { $int_count++ }
$SIG{'INT'} = 'my_int_handler';
open my $find_fh,'-|','find',qw(/ -atime +90 -size +1000 -print) or die "fork:$!";
while (<$find_fh>) {
	chomp;
	print "%s size %dk last accessed %.2f days ago\n",$_,(1023 + -s $_)/1024, -A $_;
}
if ($int_count) {
	print "[processint interrupted ...]\n";
}
print "over!!!!!!!!!!\n";

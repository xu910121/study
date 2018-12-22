#!/usr/bin/perl
foreach my $file (glob "*.old") {
	print $file . "\n";
	my $newfile = $file;
	$newfile =~ s/\.old$/.new/;
	print $newfile . "\n";
	if (-e $newfile) {
		warn "can't rename $file to $newfile:$namefile exists \n";
	} elsif (rename $file => $newfile){
		#
	} else {
		warn "rename $file to $newfile failed:$!\n";
	}
}

#!/usr/bin/perl
foreach my $person (qw/ fred Wilma betty barney dino pebbles /) {
	eval {
		open my $fh, '<', $person
			or die "Can't open file '$person': $!";
		my($total, $count);
		while (<$fh>) {
			$total += $_;
			$count++;
		}
		print "\$total = $total\n";
		print "\$count = $count\n";
		my $average = eval { $total/$count } // 'NaN';
		print "Average for file $person was $average\n";
		#&do_something($person, $average);
	};
	if ($@) {
		print "An error occurred ($@), continuing\n";
	}
}

#!/bin/perl
$_ = "yabba dabba doo";
if (/abba/){
	print "It matched!\n";
}
if (/y(....) d\1/){
	print "It matched the same after y and d!\n";
}
if (/\p{Space}/){
	print "The string has some whitespace.\n";
}
if (/\p{Digit}/){
	print "The string has a digit.\n";
}else{
	print "The string has no digit\n";
}
if (/y(.)(.)\2\1/){
	print "It matched after the y!\n";
}
if (/y((.)(.)\3\2) d\1/){
	print "It matched!\n";
}




$_ = "aa11bb";
if (/(.)\111/){
	print "It matched!\n";
}
$_ = "fredfred barney";
if (/fred+barney/){
	print "It matched!!!!!!!\n";
}
$_ = "abba";
if (/(.)\1/){
	print "It matched same character next to itself\n";
}

$_ = "The HAL-9000 requires authorization to continue.";
if (/HAL-[0-9]+/){
	print "The string mentions some model of HAL computer.\n";
}

print "Would you like to play a game?";
chomp($_ = <STDIN>);
if (/yes/i){
	print "In that case,I recommend that you go bowling.\n";
}

$_ = "I saw Barney\ndown at the bowling allen\nwith Fred\nlast night.\n";
if (/Barney.*Fred/s){
	print "That string mentions Fred after Barney!\n";
}


my $what = "larry";
while (<>){
	print "??????????????????";
	if (/\A($what)/){
		print "We saw $what in beginning of $_";
	}
	last;
}

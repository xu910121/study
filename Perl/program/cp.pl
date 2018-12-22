#!/bin/perl
open CP,"/bin/cp.exe";
open STDOUT,'>',"cp.exe";
while (<CP>)
{
	print "$_" ;
}

#!/bin/perl
use 5.010;
%some_hash = ('foo',35,'bar',12.4,2.5,'hello','wilma',1.72e30,'betty',"bye\n");
@any_array = %some_hash;
say "@any_array\n";
print "$some_hash{'foo'}";

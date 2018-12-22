#!/usr/bin/perl

$Price = 2123.5;
print <<EOF;
The price is $Price.
EOF

print <<"EOF";
The prince is $Price;
EOF

print <<'EOF';
The price is $Price;
EOF

print << x 10;
The Camels are coming! Huarrh! Huarrh!

#上面不加新的空行将会报错。

print <<" " x 10;
The Camels are coming! Huarrh! Huarrh!
 
#上面空行开始处有一个空格，一定要有的，不然报错。

print <<`EOF`;
echo hi there
echo lo there
EOF

print <<"dromedary", <<"camelid";
I said bactrian.
dromedary
She said llama.
camelid

print(<<"THIS",23,<<'THAT');
Here's a lie
or two.
THIS
And here's another.
THAT

($quote = <<'QUOTE') =~ s/^s+//gm;
	The Road goes over on and on,
	down from the door where it began.
QUOTE
print $quote;

@sauces = <<End_Lines =~ m/(\S.*\S)/g;
	normal tomato
	spicy tomate
	green chile 
	pesto
	white wine
End_Lines
print @sauces;

#!/usr/bin/perl

open(FF,"input_file.txt");
while(<FF>)
{
	$f2 = (split/,/)[2];
	print "$f2\n";
}
close(FF);

#!/usr/bin/perl

open(FF,"input_file.txt");
while(<FF>)
{
    @l=split/,/;
    print $l[2],"\n";
}
close(FF);

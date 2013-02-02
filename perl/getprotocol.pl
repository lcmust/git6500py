#!/usr/bin/perl -w
use Socket;
my $protocol = getprotobyname("tcp");
print "$protocol\n";

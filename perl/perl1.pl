#!/usr/bin/perl
#
$str="string";
for($i=1;$i<150;$i++)
{
    $st=sprintf("string%d", $i);
    $str=$str.",$st";
}
for($i=0;$i<50000;$i++)
{
    print "$str\n";
}

.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _extract-kernel-doc:

=========================
extract the documentation
=========================

.. todo::

   description how to extract kernel-doc documentation


..
   If you just want to read the ready-made books on the various
   subsystems (see Documentation/DocBook/*.tmpl), just type 'make
   psdocs', or 'make pdfdocs', or 'make htmldocs', depending on your
   preference.  If you would rather read a different format, you can type
   'make xmldocs' and then use DocBook tools to convert
   Documentation/DocBook/*.xml to a format of your choice (for example,
   'db2html ...' if 'make htmldocs' was not defined).

   If you want to see man pages instead, you can do this:

   $ cd linux
   $ scripts/kernel-doc -man $(find -name '*.c') | split-man.pl /tmp/man
   $ scripts/kernel-doc -man $(find -name '*.h') | split-man.pl /tmp/man

   Here is split-man.pl:

   -->
   #!/usr/bin/perl

   if ($#ARGV < 0) {
      die "where do I put the results?\n";
   }

   mkdir $ARGV[0],0777;
   $state = 0;
   while (<STDIN>) {
       if (/^\.TH \"[^\"]*\" 9 \"([^\"]*)\"/) {
           if ($state == 1) { close OUT }
           $state = 1;
           $fn = "$ARGV[0]/$1.9";
           print STDERR "Creating $fn\n";
           open OUT, ">$fn" or die "can't open $fn: $!\n";
           print OUT $_;
       } elsif ($state != 0) {
           print OUT $_;
       }
   }

   close OUT;
   <--

   If you just want to view the documentation for one function in one
   file, you can do this:

   $ scripts/kernel-doc -man -function fn file | nroff -man | less

   or this:

   $ scripts/kernel-doc -text -function fn file






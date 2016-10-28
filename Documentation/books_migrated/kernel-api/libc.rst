.. -*- coding: utf-8; mode: rst -*-

.. _libc:

*************************
Basic C Library Functions
*************************

When writing drivers, you cannot in general use routines which are from
the C Library. Some of the functions have been found generally useful
and they are listed below. The behaviour of these functions may vary
slightly from those defined by ANSI, and these deviations are noted in
the text.


String Conversions
==================


.. kernel-doc:: lib/vsprintf.c
    :man-sect: 9
    :export:


.. kernel-doc:: include/linux/kernel.h
    :man-sect: 9
    :functions: kstrtol


.. kernel-doc:: include/linux/kernel.h
    :man-sect: 9
    :functions: kstrtoul


.. kernel-doc:: lib/kstrtox.c
    :man-sect: 9
    :export:


String Manipulation
===================


.. kernel-doc:: lib/string.c
    :man-sect: 9
    :export:


Bit Operations
==============


.. kernel-doc:: arch/x86/include/asm/bitops.h
    :man-sect: 9
    :internal:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------

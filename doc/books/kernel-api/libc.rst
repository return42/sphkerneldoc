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
    :export:

.. kernel-doc:: include/linux/kernel.h
    :functions: kstrtol

.. kernel-doc:: include/linux/kernel.h
    :functions: kstrtoul

.. kernel-doc:: lib/kstrtox.c
    :export:

String Manipulation
===================


.. kernel-doc:: lib/string.c
    :export:

Bit Operations
==============


.. kernel-doc:: arch/x86/include/asm/bitops.h
    :internal:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

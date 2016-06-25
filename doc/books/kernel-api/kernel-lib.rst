.. -*- coding: utf-8; mode: rst -*-

.. _kernel-lib:

******************************
Basic Kernel Library Functions
******************************

The Linux kernel provides more basic utility functions.


Bitmap Operations
=================


.. kernel-doc:: lib/bitmap.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/bitmap.c
    :man-sect: 9
    :internal:


Command-line Parsing
====================


.. kernel-doc:: lib/cmdline.c
    :man-sect: 9
    :export:


.. _crc:

CRC Functions
=============


.. kernel-doc:: lib/crc7.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc16.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc-itu-t.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc32.c
    :man-sect: 9
    :export:


.. kernel-doc:: lib/crc-ccitt.c
    :man-sect: 9
    :export:


.. _idr:

idr/ida Functions
=================


.. kernel-doc:: include/linux/idr.h
    :man-sect: 9
    :doc: idr sync


.. kernel-doc:: lib/idr.c
    :man-sect: 9
    :doc: IDA description


.. kernel-doc:: lib/idr.c
    :man-sect: 9
    :export:




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

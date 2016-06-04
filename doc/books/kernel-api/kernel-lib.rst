.. -*- coding: utf-8; mode: rst -*-

.. _kernel-lib:

==============================
Basic Kernel Library Functions
==============================

The Linux kernel provides more basic utility functions.


Bitmap Operations
=================


.. kernel-doc:: lib/bitmap.c
    :export:

.. kernel-doc:: lib/bitmap.c
    :internal:

Command-line Parsing
====================


.. kernel-doc:: lib/cmdline.c
    :export:

.. _crc:

CRC Functions
=============


.. kernel-doc:: lib/crc7.c
    :export:

.. kernel-doc:: lib/crc16.c
    :export:

.. kernel-doc:: lib/crc-itu-t.c
    :export:

.. kernel-doc:: lib/crc32.c
    :export:

.. kernel-doc:: lib/crc-ccitt.c
    :export:

.. _idr:

idr/ida Functions
=================


.. kernel-doc:: include/linux/idr.h
    :doc: idr sync

.. kernel-doc:: lib/idr.c
    :doc: IDA description

.. kernel-doc:: lib/idr.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

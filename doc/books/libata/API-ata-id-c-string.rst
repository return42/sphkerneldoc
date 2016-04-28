.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-id-c-string:

===============
ata_id_c_string
===============

*man ata_id_c_string(9)*

*4.6.0-rc5*

Convert IDENTIFY DEVICE page into C string


Synopsis
========

.. c:function:: void ata_id_c_string( const u16 * id, unsigned char * s, unsigned int ofs, unsigned int len )

Arguments
=========

``id``
    IDENTIFY DEVICE results we will examine

``s``
    string into which data is output

``ofs``
    offset into identify device page

``len``
    length of string to return. must be an odd number.


Description
===========

This function is identical to ata_id_string except that it trims
trailing spaces and terminates the resulting string with null. ``len``
must be actual maximum length (even number) + 1.


LOCKING
=======

caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

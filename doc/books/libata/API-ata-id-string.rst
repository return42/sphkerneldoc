
.. _API-ata-id-string:

=============
ata_id_string
=============

*man ata_id_string(9)*

*4.6.0-rc1*

Convert IDENTIFY DEVICE page into string


Synopsis
========

.. c:function:: void ata_id_string( const u16 * id, unsigned char * s, unsigned int ofs, unsigned int len )

Arguments
=========

``id``
    IDENTIFY DEVICE results we will examine

``s``
    string into which data is output

``ofs``
    offset into identify device page

``len``
    length of string to return. must be an even number.


Description
===========

The strings in the IDENTIFY DEVICE page are broken up into 16-bit chunks. Run through the string, and output each 8-bit chunk linearly, regardless of platform.


LOCKING
=======

caller.

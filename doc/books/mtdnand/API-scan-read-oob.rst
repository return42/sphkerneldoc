
.. _API-scan-read-oob:

=============
scan_read_oob
=============

*man scan_read_oob(9)*

*4.6.0-rc1*

[GENERIC] Scan data+OOB region to buffer


Synopsis
========

.. c:function:: int scan_read_oob( struct mtd_info * mtd, uint8_t * buf, loff_t offs, size_t len )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``offs``
    offset at which to scan

``len``
    length of data region to read


Description
===========

Scan read data from data+OOB. May traverse multiple pages, interleaving page,OOB,page,OOB,... in buf. Completes transfer and returns the “strongest” ECC condition (error or
bitflip). May quit on the first (non-ECC) error.

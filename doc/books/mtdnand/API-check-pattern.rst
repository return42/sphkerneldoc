.. -*- coding: utf-8; mode: rst -*-

.. _API-check-pattern:

=============
check_pattern
=============

*man check_pattern(9)*

*4.6.0-rc5*

[GENERIC] check if a pattern is in the buffer


Synopsis
========

.. c:function:: int check_pattern( uint8_t * buf, int len, int paglen, struct nand_bbt_descr * td )

Arguments
=========

``buf``
    the buffer to search

``len``
    the length of buffer to search

``paglen``
    the pagelength

``td``
    search pattern descriptor


Description
===========

Check for a pattern at the given place. Used to search bad block tables
and good / bad block identifiers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

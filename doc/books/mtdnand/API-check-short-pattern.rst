
.. _API-check-short-pattern:

===================
check_short_pattern
===================

*man check_short_pattern(9)*

*4.6.0-rc1*

[GENERIC] check if a pattern is in the buffer


Synopsis
========

.. c:function:: int check_short_pattern( uint8_t * buf, struct nand_bbt_descr * td )

Arguments
=========

``buf``
    the buffer to search

``td``
    search pattern descriptor


Description
===========

Check for a pattern at the given place. Used to search bad block tables and good / bad block identifiers. Same as check_pattern, but no optional empty check.

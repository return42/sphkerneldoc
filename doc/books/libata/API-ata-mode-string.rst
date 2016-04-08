
.. _API-ata-mode-string:

===============
ata_mode_string
===============

*man ata_mode_string(9)*

*4.6.0-rc1*

convert xfer_mask to string


Synopsis
========

.. c:function:: const char ⋆ ata_mode_string( unsigned long xfer_mask )

Arguments
=========

``xfer_mask``
    mask of bits supported; only highest bit counts.


Description
===========

Determine string which represents the highest speed (highest bit in ``modemask``).


LOCKING
=======

None.


RETURNS
=======

Constant C string representing highest speed listed in ``mode_mask``, or the constant C string “<n/a>”.

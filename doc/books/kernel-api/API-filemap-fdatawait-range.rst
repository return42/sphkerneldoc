
.. _API-filemap-fdatawait-range:

=======================
filemap_fdatawait_range
=======================

*man filemap_fdatawait_range(9)*

*4.6.0-rc1*

wait for writeback to complete


Synopsis
========

.. c:function:: int filemap_fdatawait_range( struct address_space * mapping, loff_t start_byte, loff_t end_byte )

Arguments
=========

``mapping``
    address space structure to wait for

``start_byte``
    offset in bytes where the range starts

``end_byte``
    offset in bytes where the range ends (inclusive)


Description
===========

Walk the list of under-writeback pages of the given address space in the given range and wait for all of them. Check error status of the address space and return it.

Since the error status of the address space is cleared by this function, callers are responsible for checking the return value and handling and/or reporting the error.

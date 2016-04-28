.. -*- coding: utf-8; mode: rst -*-

.. _API-filemap-fdatawait:

=================
filemap_fdatawait
=================

*man filemap_fdatawait(9)*

*4.6.0-rc5*

wait for all under-writeback pages to complete


Synopsis
========

.. c:function:: int filemap_fdatawait( struct address_space * mapping )

Arguments
=========

``mapping``
    address space structure to wait for


Description
===========

Walk the list of under-writeback pages of the given address space and
wait for all of them. Check error status of the address space and return
it.

Since the error status of the address space is cleared by this function,
callers are responsible for checking the return value and handling
and/or reporting the error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

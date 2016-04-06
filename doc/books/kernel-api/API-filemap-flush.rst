
.. _API-filemap-flush:

=============
filemap_flush
=============

*man filemap_flush(9)*

*4.6.0-rc1*

mostly a non-blocking flush


Synopsis
========

.. c:function:: int filemap_flush( struct address_space * mapping )

Arguments
=========

``mapping``
    target address_space


Description
===========

This is a mostly non-blocking flush. Not suitable for data-integrity purposes - I/O may not be started against all dirty pages.

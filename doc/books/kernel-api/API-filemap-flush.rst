.. -*- coding: utf-8; mode: rst -*-

.. _API-filemap-flush:

=============
filemap_flush
=============

*man filemap_flush(9)*

*4.6.0-rc5*

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

This is a mostly non-blocking flush. Not suitable for data-integrity
purposes - I/O may not be started against all dirty pages.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

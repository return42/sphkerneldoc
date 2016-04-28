.. -*- coding: utf-8; mode: rst -*-

.. _API-write-one-page:

==============
write_one_page
==============

*man write_one_page(9)*

*4.6.0-rc5*

write out a single page and optionally wait on I/O


Synopsis
========

.. c:function:: int write_one_page( struct page * page, int wait )

Arguments
=========

``page``
    the page to write

``wait``
    if true, wait on writeout


Description
===========

The page must be locked by the caller and will be unlocked upon return.

``write_one_page`` returns a negative error code if I/O failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

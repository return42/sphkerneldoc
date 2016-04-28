.. -*- coding: utf-8; mode: rst -*-

.. _API-wbc-account-io:

==============
wbc_account_io
==============

*man wbc_account_io(9)*

*4.6.0-rc5*

account IO issued during writeback


Synopsis
========

.. c:function:: void wbc_account_io( struct writeback_control * wbc, struct page * page, size_t bytes )

Arguments
=========

``wbc``
    writeback_control of the writeback in progress

``page``
    page being written out

``bytes``
    number of bytes being written out


Description
===========

``bytes`` from ``page`` are about to written out during the writeback
controlled by ``wbc``. Keep the book for foreign inode detection. See
``wbc_detach_inode``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

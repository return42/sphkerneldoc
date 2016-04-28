.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-get-create-access:

==============================
jbd2_journal_get_create_access
==============================

*man jbd2_journal_get_create_access(9)*

*4.6.0-rc5*

notify intent to use newly created bh


Synopsis
========

.. c:function:: int jbd2_journal_get_create_access( handle_t * handle, struct buffer_head * bh )

Arguments
=========

``handle``
    transaction to new buffer to

``bh``
    new buffer.


Description
===========

Call this if you create a new bh.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

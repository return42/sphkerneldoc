.. -*- coding: utf-8; mode: rst -*-

.. _API-bh-uptodate-or-lock:

===================
bh_uptodate_or_lock
===================

*man bh_uptodate_or_lock(9)*

*4.6.0-rc5*

Test whether the buffer is uptodate


Synopsis
========

.. c:function:: int bh_uptodate_or_lock( struct buffer_head * bh )

Arguments
=========

``bh``
    struct buffer_head


Description
===========

Return true if the buffer is up-to-date and false, with the buffer
locked, if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

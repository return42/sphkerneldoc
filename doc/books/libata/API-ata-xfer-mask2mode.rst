.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-xfer-mask2mode:

==================
ata_xfer_mask2mode
==================

*man ata_xfer_mask2mode(9)*

*4.6.0-rc5*

Find matching XFER_* for the given xfer_mask


Synopsis
========

.. c:function:: u8 ata_xfer_mask2mode( unsigned long xfer_mask )

Arguments
=========

``xfer_mask``
    xfer_mask of interest


Description
===========

Return matching XFER_* value for ``xfer_mask``. Only the highest bit of
``xfer_mask`` is considered.


LOCKING
=======

None.


RETURNS
=======

Matching XFER_* value, 0xff if no match found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

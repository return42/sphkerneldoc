.. -*- coding: utf-8; mode: rst -*-

.. _API-bh-submit-read:

==============
bh_submit_read
==============

*man bh_submit_read(9)*

*4.6.0-rc5*

Submit a locked buffer for reading


Synopsis
========

.. c:function:: int bh_submit_read( struct buffer_head * bh )

Arguments
=========

``bh``
    struct buffer_head


Description
===========

Returns zero on success and -EIO on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

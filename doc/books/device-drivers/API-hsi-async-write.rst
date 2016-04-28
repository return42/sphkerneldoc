.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-async-write:

===============
hsi_async_write
===============

*man hsi_async_write(9)*

*4.6.0-rc5*

Submit a write transfer


Synopsis
========

.. c:function:: int hsi_async_write( struct hsi_client * cl, struct hsi_msg * msg )

Arguments
=========

``cl``
    Pointer to the HSI client

``msg``
    HSI message descriptor of the transfer


Description
===========

Return -errno on failure, 0 on success


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

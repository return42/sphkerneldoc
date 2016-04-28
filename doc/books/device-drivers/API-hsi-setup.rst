.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-setup:

=========
hsi_setup
=========

*man hsi_setup(9)*

*4.6.0-rc5*

Configure the client's port


Synopsis
========

.. c:function:: int hsi_setup( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to the HSI client


Description
===========

When sharing ports, clients should either relay on a single client setup
or have the same setup for all of them.

Return -errno on failure, 0 on success


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

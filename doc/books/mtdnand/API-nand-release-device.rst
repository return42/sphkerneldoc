.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-release-device:

===================
nand_release_device
===================

*man nand_release_device(9)*

*4.6.0-rc5*

[GENERIC] release chip


Synopsis
========

.. c:function:: void nand_release_device( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Release chip lock and wake up anyone waiting on the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

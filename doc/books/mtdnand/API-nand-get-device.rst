.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-get-device:

===============
nand_get_device
===============

*man nand_get_device(9)*

*4.6.0-rc5*

[GENERIC] Get chip for selected access


Synopsis
========

.. c:function:: int nand_get_device( struct mtd_info * mtd, int new_state )

Arguments
=========

``mtd``
    MTD device structure

``new_state``
    the state which is requested


Description
===========

Get the device and lock it for exclusive access


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

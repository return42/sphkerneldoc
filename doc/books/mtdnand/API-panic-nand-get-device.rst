.. -*- coding: utf-8; mode: rst -*-

.. _API-panic-nand-get-device:

=====================
panic_nand_get_device
=====================

*man panic_nand_get_device(9)*

*4.6.0-rc5*

[GENERIC] Get chip for selected access


Synopsis
========

.. c:function:: void panic_nand_get_device( struct nand_chip * chip, struct mtd_info * mtd, int new_state )

Arguments
=========

``chip``
    the nand chip descriptor

``mtd``
    MTD device structure

``new_state``
    the state which is requested


Description
===========

Used when in panic, no locks are taken.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

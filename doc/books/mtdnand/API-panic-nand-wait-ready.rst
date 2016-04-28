.. -*- coding: utf-8; mode: rst -*-

.. _API-panic-nand-wait-ready:

=====================
panic_nand_wait_ready
=====================

*man panic_nand_wait_ready(9)*

*4.6.0-rc5*

[GENERIC] Wait for the ready pin after commands.


Synopsis
========

.. c:function:: void panic_nand_wait_ready( struct mtd_info * mtd, unsigned long timeo )

Arguments
=========

``mtd``
    MTD device structure

``timeo``
    Timeout


Description
===========

Helper function for nand_wait_ready used when needing to wait in
interrupt context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

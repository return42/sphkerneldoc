
.. _API-panic-nand-wait-ready:

=====================
panic_nand_wait_ready
=====================

*man panic_nand_wait_ready(9)*

*4.6.0-rc1*

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

Helper function for nand_wait_ready used when needing to wait in interrupt context.

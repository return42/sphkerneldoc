
.. _API-panic-nand-wait:

===============
panic_nand_wait
===============

*man panic_nand_wait(9)*

*4.6.0-rc1*

[GENERIC] wait until the command is done


Synopsis
========

.. c:function:: void panic_nand_wait( struct mtd_info * mtd, struct nand_chip * chip, unsigned long timeo )

Arguments
=========

``mtd``
    MTD device structure

``chip``
    NAND chip structure

``timeo``
    timeout


Description
===========

Wait for command done. This is a helper function for nand_wait used when we are in interrupt context. May happen when in panic and trying to write an oops through mtdoops.

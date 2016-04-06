
.. _API-nand-wait-ready:

===============
nand_wait_ready
===============

*man nand_wait_ready(9)*

*4.6.0-rc1*

[GENERIC] Wait for the ready pin after commands.


Synopsis
========

.. c:function:: void nand_wait_ready( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Wait for the ready pin after a command, and warn if a timeout occurs.

.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-wait-ready:

===============
nand_wait_ready
===============

*man nand_wait_ready(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-wait-status-ready:

======================
nand_wait_status_ready
======================

*man nand_wait_status_ready(9)*

*4.6.0-rc5*

[GENERIC] Wait for the ready status after commands.


Synopsis
========

.. c:function:: void nand_wait_status_ready( struct mtd_info * mtd, unsigned long timeo )

Arguments
=========

``mtd``
    MTD device structure

``timeo``
    Timeout in ms


Description
===========

Wait for status ready (i.e. command done) or timeout.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

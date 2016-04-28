.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-check-wp:

=============
nand_check_wp
=============

*man nand_check_wp(9)*

*4.6.0-rc5*

[GENERIC] check if the chip is write protected


Synopsis
========

.. c:function:: int nand_check_wp( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Check, if the device is write protected. The function expects, that the
device is already selected.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

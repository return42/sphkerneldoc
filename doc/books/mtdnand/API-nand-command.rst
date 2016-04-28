.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-command:

============
nand_command
============

*man nand_command(9)*

*4.6.0-rc5*

[DEFAULT] Send command to NAND device


Synopsis
========

.. c:function:: void nand_command( struct mtd_info * mtd, unsigned int command, int column, int page_addr )

Arguments
=========

``mtd``
    MTD device structure

``command``
    the command to be sent

``column``
    the column address for this command, -1 if none

``page_addr``
    the page address for this command, -1 if none


Description
===========

Send command to NAND device. This function is used for small page
devices (512 Bytes per page).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

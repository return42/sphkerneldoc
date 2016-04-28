.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-wait:

=========
nand_wait
=========

*man nand_wait(9)*

*4.6.0-rc5*

[DEFAULT] wait until the command is done


Synopsis
========

.. c:function:: int nand_wait( struct mtd_info * mtd, struct nand_chip * chip )

Arguments
=========

``mtd``
    MTD device structure

``chip``
    NAND chip structure


Description
===========

Wait for command done. This applies to erase and program only.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

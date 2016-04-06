
.. _API-nand-wait:

=========
nand_wait
=========

*man nand_wait(9)*

*4.6.0-rc1*

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

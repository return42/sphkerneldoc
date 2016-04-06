
.. _API-nand-command-lp:

===============
nand_command_lp
===============

*man nand_command_lp(9)*

*4.6.0-rc1*

[DEFAULT] Send command to NAND large page device


Synopsis
========

.. c:function:: void nand_command_lp( struct mtd_info * mtd, unsigned int command, int column, int page_addr )

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

Send command to NAND device. This is the version for the new large page devices. We don't have the separate regions as we have in the small page devices. We must emulate
NAND_CMD_READOOB to keep the code compatible.

.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-transfer-oob:

=================
nand_transfer_oob
=================

*man nand_transfer_oob(9)*

*4.6.0-rc5*

[INTERN] Transfer oob to client buffer


Synopsis
========

.. c:function:: uint8_t * nand_transfer_oob( struct nand_chip * chip, uint8_t * oob, struct mtd_oob_ops * ops, size_t len )

Arguments
=========

``chip``
    nand chip structure

``oob``
    oob destination address

``ops``
    oob ops structure

``len``
    size of oob to transfer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

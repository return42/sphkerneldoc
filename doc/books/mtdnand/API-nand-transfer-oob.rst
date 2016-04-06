
.. _API-nand-transfer-oob:

=================
nand_transfer_oob
=================

*man nand_transfer_oob(9)*

*4.6.0-rc1*

[INTERN] Transfer oob to client buffer


Synopsis
========

.. c:function:: uint8_t ⋆ nand_transfer_oob( struct nand_chip * chip, uint8_t * oob, struct mtd_oob_ops * ops, size_t len )

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


.. _API-write-bbt:

=========
write_bbt
=========

*man write_bbt(9)*

*4.6.0-rc1*

[GENERIC] (Re)write the bad block table


Synopsis
========

.. c:function:: int write_bbt( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * td, struct nand_bbt_descr * md, int chipsel )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``td``
    descriptor for the bad block table

``md``
    descriptor for the bad block table mirror

``chipsel``
    selector for a specific chip, -1 for all


Description
===========

(Re)write the bad block table.

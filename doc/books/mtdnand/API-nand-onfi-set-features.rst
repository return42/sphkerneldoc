
.. _API-nand-onfi-set-features:

======================
nand_onfi_set_features
======================

*man nand_onfi_set_features(9)*

*4.6.0-rc1*

[REPLACEABLE] set features for ONFI nand


Synopsis
========

.. c:function:: int nand_onfi_set_features( struct mtd_info * mtd, struct nand_chip * chip, int addr, uint8_t * subfeature_param )

Arguments
=========

``mtd``
    MTD device structure

``chip``
    nand chip info structure

``addr``
    feature address.

``subfeature_param``
    the subfeature parameters, a four bytes array.

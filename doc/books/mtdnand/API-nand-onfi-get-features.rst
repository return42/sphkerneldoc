
.. _API-nand-onfi-get-features:

======================
nand_onfi_get_features
======================

*man nand_onfi_get_features(9)*

*4.6.0-rc1*

[REPLACEABLE] get features for ONFI nand


Synopsis
========

.. c:function:: int nand_onfi_get_features( struct mtd_info * mtd, struct nand_chip * chip, int addr, uint8_t * subfeature_param )

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

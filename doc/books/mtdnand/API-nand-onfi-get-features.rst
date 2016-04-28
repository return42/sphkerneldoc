.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-onfi-get-features:

======================
nand_onfi_get_features
======================

*man nand_onfi_get_features(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

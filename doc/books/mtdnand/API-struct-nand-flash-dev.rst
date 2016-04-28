.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-nand-flash-dev:

=====================
struct nand_flash_dev
=====================

*man struct nand_flash_dev(9)*

*4.6.0-rc5*

NAND Flash Device ID Structure


Synopsis
========

.. code-block:: c

    struct nand_flash_dev {
      char * name;
      union ecc;
      int onfi_timing_mode_default;
    };


Members
=======

name
    a human-readable name of the NAND chip

ecc
    ECC correctability and step information from the datasheet.
    ``ecc``.strength_ds: The ECC correctability from the datasheet,
    same as the ``ecc_strength_ds`` in nand_chip{}. ``ecc``.step_ds:
    The ECC step required by the ``ecc``.strength_ds, same as the
    ``ecc_step_ds`` in nand_chip{}, also from the datasheet. For
    example, the “4bit ECC for each 512Byte” can be set with
    NAND_ECC_INFO(4, 512).

onfi_timing_mode_default
    the default ONFI timing mode entered after a NAND reset. Should be
    deduced from timings described in the datasheet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

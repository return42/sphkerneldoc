.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-nand-ecc-ctrl:

====================
struct nand_ecc_ctrl
====================

*man struct nand_ecc_ctrl(9)*

*4.6.0-rc5*

Control structure for ECC


Synopsis
========

.. code-block:: c

    struct nand_ecc_ctrl {
      nand_ecc_modes_t mode;
      int steps;
      int size;
      int bytes;
      int total;
      int strength;
      int prepad;
      int postpad;
      unsigned int options;
      struct nand_ecclayout * layout;
      void * priv;
      void (* hwctl) (struct mtd_info *mtd, int mode);
      int (* calculate) (struct mtd_info *mtd, const uint8_t *dat,uint8_t *ecc_code);
      int (* correct) (struct mtd_info *mtd, uint8_t *dat, uint8_t *read_ecc,uint8_t *calc_ecc);
      int (* read_page_raw) (struct mtd_info *mtd, struct nand_chip *chip,uint8_t *buf, int oob_required, int page);
      int (* write_page_raw) (struct mtd_info *mtd, struct nand_chip *chip,const uint8_t *buf, int oob_required, int page);
      int (* read_page) (struct mtd_info *mtd, struct nand_chip *chip,uint8_t *buf, int oob_required, int page);
      int (* read_subpage) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offs, uint32_t len, uint8_t *buf, int page);
      int (* write_subpage) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offset, uint32_t data_len,const uint8_t *data_buf, int oob_required, int page);
      int (* write_page) (struct mtd_info *mtd, struct nand_chip *chip,const uint8_t *buf, int oob_required, int page);
      int (* write_oob_raw) (struct mtd_info *mtd, struct nand_chip *chip,int page);
      int (* read_oob_raw) (struct mtd_info *mtd, struct nand_chip *chip,int page);
      int (* read_oob) (struct mtd_info *mtd, struct nand_chip *chip, int page);
      int (* write_oob) (struct mtd_info *mtd, struct nand_chip *chip,int page);
    };


Members
=======

mode
    ECC mode

steps
    number of ECC steps per page

size
    data bytes per ECC step

bytes
    ECC bytes per step

total
    total number of ECC bytes per page

strength
    max number of correctible bits per ECC step

prepad
    padding information for syndrome based ECC generators

postpad
    padding information for syndrome based ECC generators

options
    ECC specific options (see NAND_ECC_XXX flags defined above)

layout
    ECC layout control struct pointer

priv
    pointer to private ECC control data

hwctl
    function to control hardware ECC generator. Must only be provided if
    an hardware ECC is available

calculate
    function for ECC calculation or readback from ECC hardware

correct
    function for ECC correction, matching to ECC generator (sw/hw).
    Should return a positive number representing the number of corrected
    bitflips, -EBADMSG if the number of bitflips exceed ECC strength, or
    any other error code if the error is not directly related to
    correction. If -EBADMSG is returned the input buffers should be left
    untouched.

read_page_raw
    function to read a raw page without ECC. This function should hide
    the specific layout used by the ECC controller and always return
    contiguous in-band and out-of-band data even if they're not stored
    contiguously on the NAND chip (e.g. NAND_ECC_HW_SYNDROME
    interleaves in-band and out-of-band data).

write_page_raw
    function to write a raw page without ECC. This function should hide
    the specific layout used by the ECC controller and consider the
    passed data as contiguous in-band and out-of-band data. ECC
    controller is responsible for doing the appropriate transformations
    to adapt to its specific layout (e.g. NAND_ECC_HW_SYNDROME
    interleaves in-band and out-of-band data).

read_page
    function to read a page according to the ECC generator requirements;
    returns maximum number of bitflips corrected in any single ECC step,
    0 if bitflips uncorrectable, -EIO hw error

read_subpage
    function to read parts of the page covered by ECC; returns same as
    ``read_page``

write_subpage
    function to write parts of the page covered by ECC.

write_page
    function to write a page according to the ECC generator
    requirements.

write_oob_raw
    function to write chip OOB data without ECC

read_oob_raw
    function to read chip OOB data without ECC

read_oob
    function to read chip OOB data

write_oob
    function to write chip OOB data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

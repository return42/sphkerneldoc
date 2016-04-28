.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-nand-chip:

================
struct nand_chip
================

*man struct nand_chip(9)*

*4.6.0-rc5*

NAND Private Flash Chip Data


Synopsis
========

.. code-block:: c

    struct nand_chip {
      struct mtd_info mtd;
      void __iomem * IO_ADDR_R;
      void __iomem * IO_ADDR_W;
      uint8_t (* read_byte) (struct mtd_info *mtd);
      u16 (* read_word) (struct mtd_info *mtd);
      void (* write_byte) (struct mtd_info *mtd, uint8_t byte);
      void (* write_buf) (struct mtd_info *mtd, const uint8_t *buf, int len);
      void (* read_buf) (struct mtd_info *mtd, uint8_t *buf, int len);
      void (* select_chip) (struct mtd_info *mtd, int chip);
      int (* block_bad) (struct mtd_info *mtd, loff_t ofs);
      int (* block_markbad) (struct mtd_info *mtd, loff_t ofs);
      void (* cmd_ctrl) (struct mtd_info *mtd, int dat, unsigned int ctrl);
      int (* dev_ready) (struct mtd_info *mtd);
      void (* cmdfunc) (struct mtd_info *mtd, unsigned command, int column,int page_addr);
      int(* waitfunc) (struct mtd_info *mtd, struct nand_chip *this);
      int (* erase) (struct mtd_info *mtd, int page);
      int (* scan_bbt) (struct mtd_info *mtd);
      int (* errstat) (struct mtd_info *mtd, struct nand_chip *this, int state,int status, int page);
      int (* write_page) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offset, int data_len, const uint8_t *buf,int oob_required, int page, int cached, int raw);
      int (* onfi_set_features) (struct mtd_info *mtd, struct nand_chip *chip,int feature_addr, uint8_t *subfeature_para);
      int (* onfi_get_features) (struct mtd_info *mtd, struct nand_chip *chip,int feature_addr, uint8_t *subfeature_para);
      int (* setup_read_retry) (struct mtd_info *mtd, int retry_mode);
      int chip_delay;
      unsigned int options;
      unsigned int bbt_options;
      int page_shift;
      int phys_erase_shift;
      int bbt_erase_shift;
      int chip_shift;
      int numchips;
      uint64_t chipsize;
      int pagemask;
      int pagebuf;
      unsigned int pagebuf_bitflips;
      int subpagesize;
      uint8_t bits_per_cell;
      uint16_t ecc_strength_ds;
      uint16_t ecc_step_ds;
      int onfi_timing_mode_default;
      int badblockpos;
      int badblockbits;
      int onfi_version;
      int jedec_version;
      union {unnamed_union};
      int read_retries;
      flstate_t state;
      uint8_t * oob_poi;
      struct nand_hw_control * controller;
      struct nand_ecc_ctrl ecc;
      struct nand_buffers * buffers;
      struct nand_hw_control hwcontrol;
      uint8_t * bbt;
      struct nand_bbt_descr * bbt_td;
      struct nand_bbt_descr * bbt_md;
      struct nand_bbt_descr * badblock_pattern;
      void * priv;
    };


Members
=======

mtd
    MTD device registered to the MTD framework

IO_ADDR_R
    [BOARDSPECIFIC] address to read the 8 I/O lines of the flash device

IO_ADDR_W
    [BOARDSPECIFIC] address to write the 8 I/O lines of the flash
    device.

read_byte
    [REPLACEABLE] read one byte from the chip

read_word
    [REPLACEABLE] read one word from the chip

write_byte
    [REPLACEABLE] write a single byte to the chip on the low 8 I/O lines

write_buf
    [REPLACEABLE] write data from the buffer to the chip

read_buf
    [REPLACEABLE] read data from the chip into the buffer

select_chip
    [REPLACEABLE] select chip nr

block_bad
    [REPLACEABLE] check if a block is bad, using OOB markers

block_markbad
    [REPLACEABLE] mark a block bad

cmd_ctrl
    [BOARDSPECIFIC] hardwarespecific function for controlling
    ALE/CLE/nCE. Also used to write command and address

dev_ready
    [BOARDSPECIFIC] hardwarespecific function for accessing device
    ready/busy line. If set to NULL no access to ready/busy is available
    and the ready/busy information is read from the chip status
    register.

cmdfunc
    [REPLACEABLE] hardwarespecific function for writing commands to the
    chip.

waitfunc
    [REPLACEABLE] hardwarespecific function for wait on ready.

erase
    [REPLACEABLE] erase function

scan_bbt
    [REPLACEABLE] function to scan bad block table

errstat
    [OPTIONAL] hardware specific function to perform additional error
    status checks (determine if errors are correctable).

write_page
    [REPLACEABLE] High-level page write function

onfi_set_features
    [REPLACEABLE] set the features for ONFI nand

onfi_get_features
    [REPLACEABLE] get the features for ONFI nand

setup_read_retry
    [FLASHSPECIFIC] flash (vendor) specific function for setting the
    read-retry mode. Mostly needed for MLC NAND.

chip_delay
    [BOARDSPECIFIC] chip dependent delay for transferring data from
    array to read regs (tR).

options
    [BOARDSPECIFIC] various chip options. They can partly be set to
    inform nand_scan about special functionality. See the defines for
    further explanation.

bbt_options
    [INTERN] bad block specific options. All options used here must come
    from bbm.h. By default, these options will be copied to the
    appropriate nand_bbt_descr's.

page_shift
    [INTERN] number of address bits in a page (column address bits).

phys_erase_shift
    [INTERN] number of address bits in a physical eraseblock

bbt_erase_shift
    [INTERN] number of address bits in a bbt entry

chip_shift
    [INTERN] number of address bits in one chip

numchips
    [INTERN] number of physical chips

chipsize
    [INTERN] the size of one chip for multichip arrays

pagemask
    [INTERN] page number mask = number of (pages / chip) - 1

pagebuf
    [INTERN] holds the pagenumber which is currently in data_buf.

pagebuf_bitflips
    [INTERN] holds the bitflip count for the page which is currently in
    data_buf.

subpagesize
    [INTERN] holds the subpagesize

bits_per_cell
    [INTERN] number of bits per cell. i.e., 1 means SLC.

ecc_strength_ds
    [INTERN] ECC correctability from the datasheet. Minimum amount of
    bit errors per ``ecc_step_ds`` guaranteed to be correctable. If
    unknown, set to zero.

ecc_step_ds
    [INTERN] ECC step required by the ``ecc_strength_ds``, also from the
    datasheet. It is the recommended ECC step size, if known; if
    unknown, set to zero.

onfi_timing_mode_default
    [INTERN] default ONFI timing mode. This field is either deduced from
    the datasheet if the NAND chip is not ONFI compliant or set to 0 if
    it is (an ONFI chip is always configured in mode 0 after a NAND
    reset)

badblockpos
    [INTERN] position of the bad block marker in the oob area.

badblockbits
    [INTERN] minimum number of set bits in a good block's bad block
    marker position; i.e., BBM == 11110111b is not bad when badblockbits
    == 7

onfi_version
    [INTERN] holds the chip ONFI version (BCD encoded), non 0 if ONFI
    supported.

jedec_version
    [INTERN] holds the chip JEDEC version (BCD encoded), non 0 if JEDEC
    supported.

{unnamed_union}
    anonymous

read_retries
    [INTERN] the number of read retry modes supported

state
    [INTERN] the current state of the NAND device

oob_poi
    "poison value buffer," used for laying out OOB data before writing

controller
    [REPLACEABLE] a pointer to a hardware controller structure which is
    shared among multiple independent devices.

ecc
    [BOARDSPECIFIC] ECC control structure

buffers
    buffer structure for read/write

hwcontrol
    platform-specific hardware control structure

bbt
    [INTERN] bad block table pointer

bbt_td
    [REPLACEABLE] bad block table descriptor for flash lookup.

bbt_md
    [REPLACEABLE] bad block table mirror descriptor

badblock_pattern
    [REPLACEABLE] bad block scan pattern used for initial bad block
    scan.

priv
    [OPTIONAL] pointer to private chip data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

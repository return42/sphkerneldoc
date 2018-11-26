.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/omap2.c

.. _`omap_prefetch_enable`:

omap_prefetch_enable
====================

.. c:function:: int omap_prefetch_enable(int cs, int fifo_th, int dma_mode, unsigned int u32_count, int is_write, struct omap_nand_info *info)

    configures and starts prefetch transfer

    :param cs:
        cs (chip select) number
    :type cs: int

    :param fifo_th:
        fifo threshold to be used for read/ write
    :type fifo_th: int

    :param dma_mode:
        dma mode enable (1) or disable (0)
    :type dma_mode: int

    :param u32_count:
        number of bytes to be transferred
    :type u32_count: unsigned int

    :param is_write:
        prefetch read(0) or write post(1) mode
    :type is_write: int

    :param info:
        *undescribed*
    :type info: struct omap_nand_info \*

.. _`omap_prefetch_reset`:

omap_prefetch_reset
===================

.. c:function:: int omap_prefetch_reset(int cs, struct omap_nand_info *info)

    disables and stops the prefetch engine

    :param cs:
        *undescribed*
    :type cs: int

    :param info:
        *undescribed*
    :type info: struct omap_nand_info \*

.. _`omap_hwcontrol`:

omap_hwcontrol
==============

.. c:function:: void omap_hwcontrol(struct nand_chip *chip, int cmd, unsigned int ctrl)

    hardware specific access to control-lines

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param cmd:
        command to device
    :type cmd: int

    :param ctrl:
        *undescribed*
    :type ctrl: unsigned int

.. _`omap_hwcontrol.nand_nce`:

NAND_NCE
--------

bit 0 -> don't care

.. _`omap_hwcontrol.nand_cle`:

NAND_CLE
--------

bit 1 -> Command Latch

.. _`omap_hwcontrol.nand_ale`:

NAND_ALE
--------

bit 2 -> Address Latch

.. _`omap_hwcontrol.note`:

NOTE
----

boards may use different bits for these!!

.. _`omap_read_buf8`:

omap_read_buf8
==============

.. c:function:: void omap_read_buf8(struct mtd_info *mtd, u_char *buf, int len)

    read data from NAND controller into buffer

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`omap_write_buf8`:

omap_write_buf8
===============

.. c:function:: void omap_write_buf8(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`omap_read_buf16`:

omap_read_buf16
===============

.. c:function:: void omap_read_buf16(struct mtd_info *mtd, u_char *buf, int len)

    read data from NAND controller into buffer

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`omap_write_buf16`:

omap_write_buf16
================

.. c:function:: void omap_write_buf16(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`omap_read_buf_pref`:

omap_read_buf_pref
==================

.. c:function:: void omap_read_buf_pref(struct nand_chip *chip, u_char *buf, int len)

    read data from NAND controller into buffer

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`omap_write_buf_pref`:

omap_write_buf_pref
===================

.. c:function:: void omap_write_buf_pref(struct nand_chip *chip, const u_char *buf, int len)

    write buffer to NAND controller

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`omap_read_buf_dma_pref`:

omap_read_buf_dma_pref
======================

.. c:function:: void omap_read_buf_dma_pref(struct nand_chip *chip, u_char *buf, int len)

    read data from NAND controller into buffer

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: u_char \*

    :param len:
        number of bytes to read
    :type len: int

.. _`omap_write_buf_dma_pref`:

omap_write_buf_dma_pref
=======================

.. c:function:: void omap_write_buf_dma_pref(struct nand_chip *chip, const u_char *buf, int len)

    write buffer to NAND controller

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const u_char \*

    :param len:
        number of bytes to write
    :type len: int

.. _`gen_true_ecc`:

gen_true_ecc
============

.. c:function:: void gen_true_ecc(u8 *ecc_buf)

    This function will generate true ECC value

    :param ecc_buf:
        buffer to store ecc code
    :type ecc_buf: u8 \*

.. _`gen_true_ecc.description`:

Description
-----------

This generated true ECC value can be used when correcting
data read from NAND flash memory core

.. _`omap_compare_ecc`:

omap_compare_ecc
================

.. c:function:: int omap_compare_ecc(u8 *ecc_data1, u8 *ecc_data2, u8 *page_data)

    Detect (2 bits) and correct (1 bit) error in data

    :param ecc_data1:
        ecc code from nand spare area
    :type ecc_data1: u8 \*

    :param ecc_data2:
        ecc code from hardware register obtained from hardware ecc
    :type ecc_data2: u8 \*

    :param page_data:
        page data
    :type page_data: u8 \*

.. _`omap_compare_ecc.description`:

Description
-----------

This function compares two ECC's and indicates if there is an error.
If the error can be corrected it will be corrected to the buffer.
If there is no error, \ ``0``\  is returned. If there is an error but it
was corrected, \ ``1``\  is returned. Otherwise, \ ``-1``\  is returned.

.. _`omap_correct_data`:

omap_correct_data
=================

.. c:function:: int omap_correct_data(struct nand_chip *chip, u_char *dat, u_char *read_ecc, u_char *calc_ecc)

    Compares the ECC read with HW generated ECC

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param dat:
        page data
    :type dat: u_char \*

    :param read_ecc:
        ecc read from nand flash
    :type read_ecc: u_char \*

    :param calc_ecc:
        ecc read from HW ECC registers
    :type calc_ecc: u_char \*

.. _`omap_correct_data.description`:

Description
-----------

Compares the ecc read from nand spare area with ECC registers values
and if ECC's mismatched, it will call 'omap_compare_ecc' for error
detection and correction. If there are no errors, \ ``0``\  is returned. If
there were errors and all of the errors were corrected, the number of
corrected errors is returned. If uncorrectable errors exist, \ ``-1``\  is
returned.

.. _`omap_calculate_ecc`:

omap_calculate_ecc
==================

.. c:function:: int omap_calculate_ecc(struct nand_chip *chip, const u_char *dat, u_char *ecc_code)

    Generate non-inverted ECC bytes.

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param dat:
        The pointer to data on which ecc is computed
    :type dat: const u_char \*

    :param ecc_code:
        The ecc_code buffer
    :type ecc_code: u_char \*

.. _`omap_calculate_ecc.description`:

Description
-----------

Using noninverted ECC can be considered ugly since writing a blank
page ie. padding will clear the ECC bytes. This is no problem as long
nobody is trying to write data on the seemingly unused page. Reading
an erased page will produce an ECC mismatch between generated and read
ECC bytes that has to be dealt with separately.

.. _`omap_enable_hwecc`:

omap_enable_hwecc
=================

.. c:function:: void omap_enable_hwecc(struct nand_chip *chip, int mode)

    This function enables the hardware ecc functionality

    :param chip:
        *undescribed*
    :type chip: struct nand_chip \*

    :param mode:
        Read/Write mode
    :type mode: int

.. _`omap_wait`:

omap_wait
=========

.. c:function:: int omap_wait(struct nand_chip *this)

    wait until the command is done

    :param this:
        NAND Chip structure
    :type this: struct nand_chip \*

.. _`omap_wait.description`:

Description
-----------

Wait function is called during Program and erase operations and
the way it is called from MTD layer, we should wait till the NAND
chip is ready after the programming/erase operation has completed.

Erase can take up to 400ms and program up to 20ms according to
general NAND and SmartMedia specs

.. _`omap_dev_ready`:

omap_dev_ready
==============

.. c:function:: int omap_dev_ready(struct nand_chip *chip)

    checks the NAND Ready GPIO line

    :param chip:
        *undescribed*
    :type chip: struct nand_chip \*

.. _`omap_dev_ready.description`:

Description
-----------

Returns true if ready and false if busy.

.. _`omap_enable_hwecc_bch`:

omap_enable_hwecc_bch
=====================

.. c:function:: void __maybe_unused omap_enable_hwecc_bch(struct nand_chip *chip, int mode)

    Program GPMC to perform BCH ECC calculation

    :param chip:
        *undescribed*
    :type chip: struct nand_chip \*

    :param mode:
        Read/Write mode
    :type mode: int

.. _`omap_enable_hwecc_bch.description`:

Description
-----------

When using BCH with SW correction (i.e. no ELM), sector size is set
to 512 bytes and we use BCH_WRAPMODE_6 wrapping mode

.. _`omap_enable_hwecc_bch.for-both-reading-and-writing-with`:

for both reading and writing with
---------------------------------

eccsize0 = 0  (no additional protected byte in spare area)
eccsize1 = 32 (skip 32 nibbles = 16 bytes per sector in spare area)

.. _`_omap_calculate_ecc_bch`:

\_omap_calculate_ecc_bch
========================

.. c:function:: int _omap_calculate_ecc_bch(struct mtd_info *mtd, const u_char *dat, u_char *ecc_calc, int i)

    Generate ECC bytes for one sector

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param dat:
        The pointer to data on which ecc is computed
    :type dat: const u_char \*

    :param ecc_calc:
        *undescribed*
    :type ecc_calc: u_char \*

    :param i:
        The sector number (for a multi sector page)
    :type i: int

.. _`_omap_calculate_ecc_bch.description`:

Description
-----------

Support calculating of BCH4/8/16 ECC vectors for one sector
within a page. Sector number is in \ ``i``\ .

.. _`omap_calculate_ecc_bch_sw`:

omap_calculate_ecc_bch_sw
=========================

.. c:function:: int omap_calculate_ecc_bch_sw(struct nand_chip *chip, const u_char *dat, u_char *ecc_calc)

    ECC generator for sector for SW based correction

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param dat:
        The pointer to data on which ecc is computed
    :type dat: const u_char \*

    :param ecc_calc:
        *undescribed*
    :type ecc_calc: u_char \*

.. _`omap_calculate_ecc_bch_sw.description`:

Description
-----------

Support calculating of BCH4/8/16 ECC vectors for one sector. This is used
when SW based correction is required as ECC is required for one sector
at a time.

.. _`omap_calculate_ecc_bch_multi`:

omap_calculate_ecc_bch_multi
============================

.. c:function:: int omap_calculate_ecc_bch_multi(struct mtd_info *mtd, const u_char *dat, u_char *ecc_calc)

    Generate ECC for multiple sectors

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param dat:
        The pointer to data on which ecc is computed
    :type dat: const u_char \*

    :param ecc_calc:
        *undescribed*
    :type ecc_calc: u_char \*

.. _`omap_calculate_ecc_bch_multi.description`:

Description
-----------

Support calculating of BCH4/8/16 ecc vectors for the entire page in one go.

.. _`erased_sector_bitflips`:

erased_sector_bitflips
======================

.. c:function:: int erased_sector_bitflips(u_char *data, u_char *oob, struct omap_nand_info *info)

    count bit flips

    :param data:
        data sector buffer
    :type data: u_char \*

    :param oob:
        oob buffer
    :type oob: u_char \*

    :param info:
        omap_nand_info
    :type info: struct omap_nand_info \*

.. _`erased_sector_bitflips.description`:

Description
-----------

Check the bit flips in erased page falls below correctable level.
If falls below, report the page as erased with correctable bit
flip, else report as uncorrectable page.

.. _`omap_elm_correct_data`:

omap_elm_correct_data
=====================

.. c:function:: int omap_elm_correct_data(struct nand_chip *chip, u_char *data, u_char *read_ecc, u_char *calc_ecc)

    corrects page data area in case error reported

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param data:
        page data
    :type data: u_char \*

    :param read_ecc:
        ecc read from nand flash
    :type read_ecc: u_char \*

    :param calc_ecc:
        ecc read from HW ECC registers
    :type calc_ecc: u_char \*

.. _`omap_elm_correct_data.description`:

Description
-----------

Calculated ecc vector reported as zero in case of non-error pages.
In case of non-zero ecc vector, first filter out erased-pages, and
then process data via ELM to detect bit-flips.

.. _`omap_write_page_bch`:

omap_write_page_bch
===================

.. c:function:: int omap_write_page_bch(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    BCH ecc based write page function for entire page

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page
    :type page: int

.. _`omap_write_page_bch.description`:

Description
-----------

Custom write page method evolved to support multi sector writing in one shot

.. _`omap_write_subpage_bch`:

omap_write_subpage_bch
======================

.. c:function:: int omap_write_subpage_bch(struct nand_chip *chip, u32 offset, u32 data_len, const u8 *buf, int oob_required, int page)

    BCH hardware ECC based subpage write

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param offset:
        column address of subpage within the page
    :type offset: u32

    :param data_len:
        data length
    :type data_len: u32

    :param buf:
        data buffer
    :type buf: const u8 \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`omap_write_subpage_bch.description`:

Description
-----------

OMAP optimized subpage write method.

.. _`omap_read_page_bch`:

omap_read_page_bch
==================

.. c:function:: int omap_read_page_bch(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    BCH ecc based page read function for entire page

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`omap_read_page_bch.description`:

Description
-----------

For BCH ecc scheme, GPMC used for syndrome calculation and ELM module
used for error correction.
Custom method evolved to support ELM error correction & multi sector
reading. On reading page data area is read along with OOB data with
ecc engine enabled. ecc vector updated after read of OOB data.
For non error pages ecc vector reported as zero.

.. _`is_elm_present`:

is_elm_present
==============

.. c:function:: bool is_elm_present(struct omap_nand_info *info, struct device_node *elm_node)

    checks for presence of ELM module by scanning DT nodes

    :param info:
        *undescribed*
    :type info: struct omap_nand_info \*

    :param elm_node:
        *undescribed*
    :type elm_node: struct device_node \*

.. This file was automatic generated / don't edit.


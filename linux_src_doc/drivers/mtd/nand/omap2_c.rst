.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/omap2.c

.. _`omap_prefetch_enable`:

omap_prefetch_enable
====================

.. c:function:: int omap_prefetch_enable(int cs, int fifo_th, int dma_mode, unsigned int u32_count, int is_write, struct omap_nand_info *info)

    configures and starts prefetch transfer

    :param int cs:
        cs (chip select) number

    :param int fifo_th:
        fifo threshold to be used for read/ write

    :param int dma_mode:
        dma mode enable (1) or disable (0)

    :param unsigned int u32_count:
        number of bytes to be transferred

    :param int is_write:
        prefetch read(0) or write post(1) mode

    :param struct omap_nand_info \*info:
        *undescribed*

.. _`omap_prefetch_reset`:

omap_prefetch_reset
===================

.. c:function:: int omap_prefetch_reset(int cs, struct omap_nand_info *info)

    disables and stops the prefetch engine

    :param int cs:
        *undescribed*

    :param struct omap_nand_info \*info:
        *undescribed*

.. _`omap_hwcontrol`:

omap_hwcontrol
==============

.. c:function:: void omap_hwcontrol(struct mtd_info *mtd, int cmd, unsigned int ctrl)

    hardware specific access to control-lines

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int cmd:
        command to device

    :param unsigned int ctrl:
        *undescribed*

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

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`omap_write_buf8`:

omap_write_buf8
===============

.. c:function:: void omap_write_buf8(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`omap_read_buf16`:

omap_read_buf16
===============

.. c:function:: void omap_read_buf16(struct mtd_info *mtd, u_char *buf, int len)

    read data from NAND controller into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`omap_write_buf16`:

omap_write_buf16
================

.. c:function:: void omap_write_buf16(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`omap_read_buf_pref`:

omap_read_buf_pref
==================

.. c:function:: void omap_read_buf_pref(struct mtd_info *mtd, u_char *buf, int len)

    read data from NAND controller into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`omap_write_buf_pref`:

omap_write_buf_pref
===================

.. c:function:: void omap_write_buf_pref(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`omap_read_buf_dma_pref`:

omap_read_buf_dma_pref
======================

.. c:function:: void omap_read_buf_dma_pref(struct mtd_info *mtd, u_char *buf, int len)

    read data from NAND controller into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*buf:
        buffer to store date

    :param int len:
        number of bytes to read

.. _`omap_write_buf_dma_pref`:

omap_write_buf_dma_pref
=======================

.. c:function:: void omap_write_buf_dma_pref(struct mtd_info *mtd, const u_char *buf, int len)

    write buffer to NAND controller

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*buf:
        data buffer

    :param int len:
        number of bytes to write

.. _`gen_true_ecc`:

gen_true_ecc
============

.. c:function:: void gen_true_ecc(u8 *ecc_buf)

    This function will generate true ECC value

    :param u8 \*ecc_buf:
        buffer to store ecc code

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

    :param u8 \*ecc_data1:
        ecc code from nand spare area

    :param u8 \*ecc_data2:
        ecc code from hardware register obtained from hardware ecc

    :param u8 \*page_data:
        page data

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

.. c:function:: int omap_correct_data(struct mtd_info *mtd, u_char *dat, u_char *read_ecc, u_char *calc_ecc)

    Compares the ECC read with HW generated ECC

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*dat:
        page data

    :param u_char \*read_ecc:
        ecc read from nand flash

    :param u_char \*calc_ecc:
        ecc read from HW ECC registers

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

.. c:function:: int omap_calculate_ecc(struct mtd_info *mtd, const u_char *dat, u_char *ecc_code)

    Generate non-inverted ECC bytes.

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*dat:
        The pointer to data on which ecc is computed

    :param u_char \*ecc_code:
        The ecc_code buffer

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

.. c:function:: void omap_enable_hwecc(struct mtd_info *mtd, int mode)

    This function enables the hardware ecc functionality

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int mode:
        Read/Write mode

.. _`omap_wait`:

omap_wait
=========

.. c:function:: int omap_wait(struct mtd_info *mtd, struct nand_chip *chip)

    wait until the command is done

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        NAND Chip structure

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

.. c:function:: int omap_dev_ready(struct mtd_info *mtd)

    checks the NAND Ready GPIO line

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`omap_dev_ready.description`:

Description
-----------

Returns true if ready and false if busy.

.. _`omap_enable_hwecc_bch`:

omap_enable_hwecc_bch
=====================

.. c:function:: void __maybe_unused omap_enable_hwecc_bch(struct mtd_info *mtd, int mode)

    Program GPMC to perform BCH ECC calculation

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int mode:
        Read/Write mode

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

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*dat:
        The pointer to data on which ecc is computed

    :param u_char \*ecc_calc:
        *undescribed*

    :param int i:
        The sector number (for a multi sector page)

.. _`_omap_calculate_ecc_bch.description`:

Description
-----------

Support calculating of BCH4/8/16 ECC vectors for one sector
within a page. Sector number is in \ ``i``\ .

.. _`omap_calculate_ecc_bch_sw`:

omap_calculate_ecc_bch_sw
=========================

.. c:function:: int omap_calculate_ecc_bch_sw(struct mtd_info *mtd, const u_char *dat, u_char *ecc_calc)

    ECC generator for sector for SW based correction

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*dat:
        The pointer to data on which ecc is computed

    :param u_char \*ecc_calc:
        *undescribed*

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

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const u_char \*dat:
        The pointer to data on which ecc is computed

    :param u_char \*ecc_calc:
        *undescribed*

.. _`omap_calculate_ecc_bch_multi.description`:

Description
-----------

Support calculating of BCH4/8/16 ecc vectors for the entire page in one go.

.. _`erased_sector_bitflips`:

erased_sector_bitflips
======================

.. c:function:: int erased_sector_bitflips(u_char *data, u_char *oob, struct omap_nand_info *info)

    count bit flips

    :param u_char \*data:
        data sector buffer

    :param u_char \*oob:
        oob buffer

    :param struct omap_nand_info \*info:
        omap_nand_info

.. _`erased_sector_bitflips.description`:

Description
-----------

Check the bit flips in erased page falls below correctable level.
If falls below, report the page as erased with correctable bit
flip, else report as uncorrectable page.

.. _`omap_elm_correct_data`:

omap_elm_correct_data
=====================

.. c:function:: int omap_elm_correct_data(struct mtd_info *mtd, u_char *data, u_char *read_ecc, u_char *calc_ecc)

    corrects page data area in case error reported

    :param struct mtd_info \*mtd:
        MTD device structure

    :param u_char \*data:
        page data

    :param u_char \*read_ecc:
        ecc read from nand flash

    :param u_char \*calc_ecc:
        ecc read from HW ECC registers

.. _`omap_elm_correct_data.description`:

Description
-----------

Calculated ecc vector reported as zero in case of non-error pages.
In case of non-zero ecc vector, first filter out erased-pages, and
then process data via ELM to detect bit-flips.

.. _`omap_write_page_bch`:

omap_write_page_bch
===================

.. c:function:: int omap_write_page_bch(struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    BCH ecc based write page function for entire page

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page

.. _`omap_write_page_bch.description`:

Description
-----------

Custom write page method evolved to support multi sector writing in one shot

.. _`omap_write_subpage_bch`:

omap_write_subpage_bch
======================

.. c:function:: int omap_write_subpage_bch(struct mtd_info *mtd, struct nand_chip *chip, u32 offset, u32 data_len, const u8 *buf, int oob_required, int page)

    BCH hardware ECC based subpage write

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param u32 offset:
        column address of subpage within the page

    :param u32 data_len:
        data length

    :param const u8 \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write

.. _`omap_write_subpage_bch.description`:

Description
-----------

OMAP optimized subpage write method.

.. _`omap_read_page_bch`:

omap_read_page_bch
==================

.. c:function:: int omap_read_page_bch(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    BCH ecc based page read function for entire page

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param uint8_t \*buf:
        buffer to store read data

    :param int oob_required:
        caller requires OOB data read to chip->oob_poi

    :param int page:
        page number to read

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

    :param struct omap_nand_info \*info:
        *undescribed*

    :param struct device_node \*elm_node:
        *undescribed*

.. This file was automatic generated / don't edit.


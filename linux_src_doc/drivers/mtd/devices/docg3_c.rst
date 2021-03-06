.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/devices/docg3.c

.. _`doc_delay`:

doc_delay
=========

.. c:function:: void doc_delay(struct docg3 *docg3, int nbNOPs)

    delay docg3 operations

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param nbNOPs:
        the number of NOPs to issue
    :type nbNOPs: int

.. _`doc_delay.description`:

Description
-----------

As no specification is available, the right timings between chip commands are
unknown. The only available piece of information are the observed nops on a
working docg3 chip.
Therefore, doc_delay relies on a busy loop of NOPs, instead of scheduler
friendlier \ :c:func:`msleep`\  functions or blocking \ :c:func:`mdelay`\ .

.. _`doc_read_data_area`:

doc_read_data_area
==================

.. c:function:: void doc_read_data_area(struct docg3 *docg3, void *buf, int len, int first)

    Read data from data area

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param buf:
        the buffer to fill in (might be NULL is dummy reads)
    :type buf: void \*

    :param len:
        the length to read
    :type len: int

    :param first:
        first time read, DOC_READADDRESS should be set
    :type first: int

.. _`doc_read_data_area.description`:

Description
-----------

Reads bytes from flash data. Handles the single byte / even bytes reads.

.. _`doc_write_data_area`:

doc_write_data_area
===================

.. c:function:: void doc_write_data_area(struct docg3 *docg3, const void *buf, int len)

    Write data into data area

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param buf:
        the buffer to get input bytes from
    :type buf: const void \*

    :param len:
        the length to write
    :type len: int

.. _`doc_write_data_area.description`:

Description
-----------

Writes bytes into flash data. Handles the single byte / even bytes writes.

.. _`doc_set_reliable_mode`:

doc_set_reliable_mode
=====================

.. c:function:: void doc_set_reliable_mode(struct docg3 *docg3)

    Sets the flash to normal or reliable data mode

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_set_reliable_mode.description`:

Description
-----------

The reliable data mode is a bit slower than the fast mode, but less errors
occur.  Entering the reliable mode cannot be done without entering the fast
mode first.

In reliable mode, pages 2\*n and 2\*n+1 are clones. Writing to page 0 of blocks
(4,5) make the hardware write also to page 1 of blocks blocks(4,5). Reading
from page 0 of blocks (4,5) or from page 1 of blocks (4,5) gives the same
result, which is a logical and between bytes from page 0 and page 1 (which is
consistent with the fact that writing to a page is \_clearing\_ bits of that
page).

.. _`doc_set_asic_mode`:

doc_set_asic_mode
=================

.. c:function:: void doc_set_asic_mode(struct docg3 *docg3, u8 mode)

    Set the ASIC mode

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param mode:
        the mode
    :type mode: u8

.. _`doc_set_asic_mode.description`:

Description
-----------

The ASIC can work in 3 modes :
- RESET: all registers are zeroed
- NORMAL: receives and handles commands
- POWERDOWN: minimal poweruse, flash parts shut off

.. _`doc_set_device_id`:

doc_set_device_id
=================

.. c:function:: void doc_set_device_id(struct docg3 *docg3, int id)

    Sets the devices id for cascaded G3 chips

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param id:
        the chip to select (amongst 0, 1, 2, 3)
    :type id: int

.. _`doc_set_device_id.description`:

Description
-----------

There can be 4 cascaded G3 chips. This function selects the one which will
should be the active one.

.. _`doc_set_extra_page_mode`:

doc_set_extra_page_mode
=======================

.. c:function:: int doc_set_extra_page_mode(struct docg3 *docg3)

    Change flash page layout

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_set_extra_page_mode.description`:

Description
-----------

Normally, the flash page is split into the data (512 bytes) and the out of
band data (16 bytes). For each, 4 more bytes can be accessed, where the wear
leveling counters are stored.  To access this last area of 4 bytes, a special
mode must be input to the flash ASIC.

Returns 0 if no error occurred, -EIO else.

.. _`doc_setup_addr_sector`:

doc_setup_addr_sector
=====================

.. c:function:: void doc_setup_addr_sector(struct docg3 *docg3, int sector)

    Setup blocks/page/ofs address for one plane

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param sector:
        the sector
    :type sector: int

.. _`doc_setup_writeaddr_sector`:

doc_setup_writeaddr_sector
==========================

.. c:function:: void doc_setup_writeaddr_sector(struct docg3 *docg3, int sector, int ofs)

    Setup blocks/page/ofs address for one plane

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param sector:
        the sector
    :type sector: int

    :param ofs:
        the offset in the page, between 0 and (512 + 16 + 512)
    :type ofs: int

.. _`doc_read_seek`:

doc_read_seek
=============

.. c:function:: int doc_read_seek(struct docg3 *docg3, int block0, int block1, int page, int wear, int ofs)

    Set both flash planes to the specified block, page for reading

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param block0:
        the first plane block index
    :type block0: int

    :param block1:
        the second plane block index
    :type block1: int

    :param page:
        the page index within the block
    :type page: int

    :param wear:
        if true, read will occur on the 4 extra bytes of the wear area
    :type wear: int

    :param ofs:
        offset in page to read
    :type ofs: int

.. _`doc_read_seek.description`:

Description
-----------

Programs the flash even and odd planes to the specific block and page.
Alternatively, programs the flash to the wear area of the specified page.

.. _`doc_write_seek`:

doc_write_seek
==============

.. c:function:: int doc_write_seek(struct docg3 *docg3, int block0, int block1, int page, int ofs)

    Set both flash planes to the specified block, page for writing

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param block0:
        the first plane block index
    :type block0: int

    :param block1:
        the second plane block index
    :type block1: int

    :param page:
        the page index within the block
    :type page: int

    :param ofs:
        offset in page to write
    :type ofs: int

.. _`doc_write_seek.description`:

Description
-----------

Programs the flash even and odd planes to the specific block and page.
Alternatively, programs the flash to the wear area of the specified page.

.. _`doc_read_page_ecc_init`:

doc_read_page_ecc_init
======================

.. c:function:: int doc_read_page_ecc_init(struct docg3 *docg3, int len)

    Initialize hardware ECC engine

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param len:
        the number of bytes covered by the ECC (BCH covered)
    :type len: int

.. _`doc_read_page_ecc_init.description`:

Description
-----------

The function does initialize the hardware ECC engine to compute the Hamming
ECC (on 1 byte) and the BCH hardware ECC (on 7 bytes).

Return 0 if succeeded, -EIO on error

.. _`doc_write_page_ecc_init`:

doc_write_page_ecc_init
=======================

.. c:function:: int doc_write_page_ecc_init(struct docg3 *docg3, int len)

    Initialize hardware BCH ECC engine

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param len:
        the number of bytes covered by the ECC (BCH covered)
    :type len: int

.. _`doc_write_page_ecc_init.description`:

Description
-----------

The function does initialize the hardware ECC engine to compute the Hamming
ECC (on 1 byte) and the BCH hardware ECC (on 7 bytes).

Return 0 if succeeded, -EIO on error

.. _`doc_ecc_disable`:

doc_ecc_disable
===============

.. c:function:: void doc_ecc_disable(struct docg3 *docg3)

    Disable Hamming and BCH ECC hardware calculator

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_ecc_disable.description`:

Description
-----------

Disables the hardware ECC generator and checker, for unchecked reads (as when
reading OOB only or write status byte).

.. _`doc_hamming_ecc_init`:

doc_hamming_ecc_init
====================

.. c:function:: void doc_hamming_ecc_init(struct docg3 *docg3, int nb_bytes)

    Initialize hardware Hamming ECC engine

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param nb_bytes:
        the number of bytes covered by the ECC (Hamming covered)
    :type nb_bytes: int

.. _`doc_hamming_ecc_init.description`:

Description
-----------

This function programs the ECC hardware to compute the hamming code on the
last provided N bytes to the hardware generator.

.. _`doc_ecc_bch_fix_data`:

doc_ecc_bch_fix_data
====================

.. c:function:: int doc_ecc_bch_fix_data(struct docg3 *docg3, void *buf, u8 *hwecc)

    Fix if need be read data from flash

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param buf:
        the buffer of read data (512 + 7 + 1 bytes)
    :type buf: void \*

    :param hwecc:
        the hardware calculated ECC.
        It's in fact recv_ecc ^ calc_ecc, where recv_ecc was read from OOB
        area data, and calc_ecc the ECC calculated by the hardware generator.
    :type hwecc: u8 \*

.. _`doc_ecc_bch_fix_data.description`:

Description
-----------

Checks if the received data matches the ECC, and if an error is detected,
tries to fix the bit flips (at most 4) in the buffer buf.  As the docg3
understands the (data, ecc, syndroms) in an inverted order in comparison to
the BCH library, the function reverses the order of bits (ie. bit7 and bit0,
bit6 and bit 1, ...) for all ECC data.

The hardware ecc unit produces oob_ecc ^ calc_ecc.  The kernel's bch
algorithm is used to decode this.  However the hw operates on page
data in a bit order that is the reverse of that of the bch alg,
requiring that the bits be reversed on the result.  Thanks to Ivan
Djelic for his analysis.

Returns number of fixed bits (0, 1, 2, 3, 4) or -EBADMSG if too many bit
errors were detected and cannot be fixed.

.. _`doc_read_page_prepare`:

doc_read_page_prepare
=====================

.. c:function:: int doc_read_page_prepare(struct docg3 *docg3, int block0, int block1, int page, int offset)

    Prepares reading data from a flash page

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param block0:
        the first plane block index on flash memory
    :type block0: int

    :param block1:
        the second plane block index on flash memory
    :type block1: int

    :param page:
        the page index in the block
    :type page: int

    :param offset:
        the offset in the page (must be a multiple of 4)
    :type offset: int

.. _`doc_read_page_prepare.description`:

Description
-----------

Prepares the page to be read in the flash memory :
- tell ASIC to map the flash pages
- tell ASIC to be in read mode

After a call to this method, a call to doc_read_page_finish is mandatory,
to end the read cycle of the flash.

Read data from a flash page. The length to be read must be between 0 and
(page_size + oob_size + wear_size), ie. 532, and a multiple of 4 (because
the extra bytes reading is not implemented).

As pages are grouped by 2 (in 2 planes), reading from a page must be done

.. _`doc_read_page_prepare.in-two-steps`:

in two steps
------------

- one read of 512 bytes at offset 0
- one read of 512 bytes at offset 512 + 16

Returns 0 if successful, -EIO if a read error occurred.

.. _`doc_read_page_getbytes`:

doc_read_page_getbytes
======================

.. c:function:: int doc_read_page_getbytes(struct docg3 *docg3, int len, u_char *buf, int first, int last_odd)

    Reads bytes from a prepared page

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param len:
        the number of bytes to be read (must be a multiple of 4)
    :type len: int

    :param buf:
        the buffer to be filled in (or NULL is forget bytes)
    :type buf: u_char \*

    :param first:
        1 if first time read, DOC_READADDRESS should be set
    :type first: int

    :param last_odd:
        1 if last read ended up on an odd byte
    :type last_odd: int

.. _`doc_read_page_getbytes.description`:

Description
-----------

Reads bytes from a prepared page. There is a trickery here : if the last read
ended up on an odd offset in the 1024 bytes double page, ie. between the 2
planes, the first byte must be read apart. If a word (16bit) read was used,
the read would return the byte of plane 2 as low \*and\* high endian, which
will mess the read.

.. _`doc_write_page_putbytes`:

doc_write_page_putbytes
=======================

.. c:function:: void doc_write_page_putbytes(struct docg3 *docg3, int len, const u_char *buf)

    Writes bytes into a prepared page

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param len:
        the number of bytes to be written
    :type len: int

    :param buf:
        the buffer of input bytes
    :type buf: const u_char \*

.. _`doc_get_bch_hw_ecc`:

doc_get_bch_hw_ecc
==================

.. c:function:: void doc_get_bch_hw_ecc(struct docg3 *docg3, u8 *hwecc)

    Get hardware calculated BCH ECC

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param hwecc:
        the array of 7 integers where the hardware ecc will be stored
    :type hwecc: u8 \*

.. _`doc_page_finish`:

doc_page_finish
===============

.. c:function:: void doc_page_finish(struct docg3 *docg3)

    Ends reading/writing of a flash page

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_read_page_finish`:

doc_read_page_finish
====================

.. c:function:: void doc_read_page_finish(struct docg3 *docg3)

    Ends reading of a flash page

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_read_page_finish.description`:

Description
-----------

As a side effect, resets the chip selector to 0. This ensures that after each
read operation, the floor 0 is selected. Therefore, if the systems halts, the
reboot will boot on floor 0, where the IPL is.

.. _`calc_block_sector`:

calc_block_sector
=================

.. c:function:: void calc_block_sector(loff_t from, int *block0, int *block1, int *page, int *ofs, int reliable)

    Calculate blocks, pages and ofs.

    :param from:
        offset in flash
    :type from: loff_t

    :param block0:
        first plane block index calculated
    :type block0: int \*

    :param block1:
        second plane block index calculated
    :type block1: int \*

    :param page:
        page calculated
    :type page: int \*

    :param ofs:
        offset in page
    :type ofs: int \*

    :param reliable:
        0 if docg3 in normal mode, 1 if docg3 in fast mode, 2 if docg3 in
        reliable mode.
    :type reliable: int

.. _`calc_block_sector.description`:

Description
-----------

The calculation is based on the reliable/normal mode. In normal mode, the 64
pages of a block are available. In reliable mode, as pages 2\*n and 2\*n+1 are
clones, only 32 pages per block are available.

.. _`doc_read_oob`:

doc_read_oob
============

.. c:function:: int doc_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    Read out of band bytes from flash

    :param mtd:
        the device
    :type mtd: struct mtd_info \*

    :param from:
        the offset from first block and first page, in bytes, aligned on page
        size
    :type from: loff_t

    :param ops:
        the mtd oob structure
    :type ops: struct mtd_oob_ops \*

.. _`doc_read_oob.description`:

Description
-----------

Reads flash memory OOB area of pages.

Returns 0 if read successful, of -EIO, -EINVAL if an error occurred

.. _`doc_block_isbad`:

doc_block_isbad
===============

.. c:function:: int doc_block_isbad(struct mtd_info *mtd, loff_t from)

    Checks whether a block is good or not

    :param mtd:
        the device
    :type mtd: struct mtd_info \*

    :param from:
        the offset to find the correct block
    :type from: loff_t

.. _`doc_block_isbad.description`:

Description
-----------

Returns 1 if block is bad, 0 if block is good

.. _`doc_get_erase_count`:

doc_get_erase_count
===================

.. c:function:: int doc_get_erase_count(struct docg3 *docg3, loff_t from)

    Get block erase count

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param from:
        the offset in which the block is.
    :type from: loff_t

.. _`doc_get_erase_count.description`:

Description
-----------

Get the number of times a block was erased. The number is the maximum of
erase times between first and second plane (which should be equal normally).

Returns The number of erases, or -EINVAL or -EIO on error.

.. _`doc_get_op_status`:

doc_get_op_status
=================

.. c:function:: int doc_get_op_status(struct docg3 *docg3)

    get erase/write operation status

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_get_op_status.description`:

Description
-----------

Queries the status from the chip, and returns it

Returns the status (bits DOC_PLANES_STATUS\_\*)

.. _`doc_write_erase_wait_status`:

doc_write_erase_wait_status
===========================

.. c:function:: int doc_write_erase_wait_status(struct docg3 *docg3)

    wait for write or erase completion

    :param docg3:
        the device
    :type docg3: struct docg3 \*

.. _`doc_write_erase_wait_status.description`:

Description
-----------

Wait for the chip to be ready again after erase or write operation, and check
erase/write status.

Returns 0 if erase successful, -EIO if erase/write issue, -ETIMEOUT if
timeout

.. _`doc_erase_block`:

doc_erase_block
===============

.. c:function:: int doc_erase_block(struct docg3 *docg3, int block0, int block1)

    Erase a couple of blocks

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param block0:
        the first block to erase (leftmost plane)
    :type block0: int

    :param block1:
        the second block to erase (rightmost plane)
    :type block1: int

.. _`doc_erase_block.description`:

Description
-----------

Erase both blocks, and return operation status

Returns 0 if erase successful, -EIO if erase issue, -ETIMEOUT if chip not
ready for too long

.. _`doc_erase`:

doc_erase
=========

.. c:function:: int doc_erase(struct mtd_info *mtd, struct erase_info *info)

    Erase a portion of the chip

    :param mtd:
        the device
    :type mtd: struct mtd_info \*

    :param info:
        the erase info
    :type info: struct erase_info \*

.. _`doc_erase.description`:

Description
-----------

Erase a bunch of contiguous blocks, by pairs, as a "mtd" page of 1024 is
split into 2 pages of 512 bytes on 2 contiguous blocks.

Returns 0 if erase successful, -EINVAL if addressing error, -EIO if erase
issue

.. _`doc_write_page`:

doc_write_page
==============

.. c:function:: int doc_write_page(struct docg3 *docg3, loff_t to, const u_char *buf, const u_char *oob, int autoecc)

    Write a single page to the chip

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param to:
        the offset from first block and first page, in bytes, aligned on page
        size
    :type to: loff_t

    :param buf:
        buffer to get bytes from
    :type buf: const u_char \*

    :param oob:
        buffer to get out of band bytes from (can be NULL if no OOB should be
        written)
    :type oob: const u_char \*

    :param autoecc:
        if 0, all 16 bytes from OOB are taken, regardless of HW Hamming or
        BCH computations. If 1, only bytes 0-7 and byte 15 are taken,
        remaining ones are filled with hardware Hamming and BCH
        computations. Its value is not meaningfull is oob == NULL.
    :type autoecc: int

.. _`doc_write_page.description`:

Description
-----------

Write one full page (ie. 1 page split on two planes), of 512 bytes, with the
OOB data. The OOB ECC is automatically computed by the hardware Hamming and
BCH generator if autoecc is not null.

Returns 0 if write successful, -EIO if write error, -EAGAIN if timeout

.. _`doc_guess_autoecc`:

doc_guess_autoecc
=================

.. c:function:: int doc_guess_autoecc(struct mtd_oob_ops *ops)

    Guess autoecc mode from mbd_oob_ops

    :param ops:
        the oob operations
    :type ops: struct mtd_oob_ops \*

.. _`doc_guess_autoecc.description`:

Description
-----------

Returns 0 or 1 if success, -EINVAL if invalid oob mode

.. _`doc_fill_autooob`:

doc_fill_autooob
================

.. c:function:: void doc_fill_autooob(u8 *dst, u8 *oobsrc)

    Fill a 16 bytes OOB from 8 non-ECC bytes

    :param dst:
        the target 16 bytes OOB buffer
    :type dst: u8 \*

    :param oobsrc:
        the source 8 bytes non-ECC OOB buffer
    :type oobsrc: u8 \*

.. _`doc_backup_oob`:

doc_backup_oob
==============

.. c:function:: int doc_backup_oob(struct docg3 *docg3, loff_t to, struct mtd_oob_ops *ops)

    Backup OOB into docg3 structure

    :param docg3:
        the device
    :type docg3: struct docg3 \*

    :param to:
        the page offset in the chip
    :type to: loff_t

    :param ops:
        the OOB size and buffer
    :type ops: struct mtd_oob_ops \*

.. _`doc_backup_oob.description`:

Description
-----------

As the docg3 should write a page with its OOB in one pass, and some userland
applications do \ :c:func:`write_oob`\  to setup the OOB and then \ :c:func:`write`\ , store the OOB
into a temporary storage. This is very dangerous, as 2 concurrent
applications could store an OOB, and then write their pages (which will
result into one having its OOB corrupted).

The only reliable way would be for userland to call \ :c:func:`doc_write_oob`\  with both
the page data \_and\_ the OOB area.

Returns 0 if success, -EINVAL if ops content invalid

.. _`doc_write_oob`:

doc_write_oob
=============

.. c:function:: int doc_write_oob(struct mtd_info *mtd, loff_t ofs, struct mtd_oob_ops *ops)

    Write out of band bytes to flash

    :param mtd:
        the device
    :type mtd: struct mtd_info \*

    :param ofs:
        the offset from first block and first page, in bytes, aligned on page
        size
    :type ofs: loff_t

    :param ops:
        the mtd oob structure
    :type ops: struct mtd_oob_ops \*

.. _`doc_write_oob.description`:

Description
-----------

Either write OOB data into a temporary buffer, for the subsequent write
page. The provided OOB should be 16 bytes long. If a data buffer is provided
as well, issue the page write.
Or provide data without OOB, and then a all zeroed OOB will be used (ECC will
still be filled in if asked for).

Returns 0 is successful, EINVAL if length is not 14 bytes

.. _`doc_set_driver_info`:

doc_set_driver_info
===================

.. c:function:: int doc_set_driver_info(int chip_id, struct mtd_info *mtd)

    Fill the mtd_info structure and docg3 structure

    :param chip_id:
        The chip ID of the supported chip
    :type chip_id: int

    :param mtd:
        The structure to fill
    :type mtd: struct mtd_info \*

.. _`doc_probe_device`:

doc_probe_device
================

.. c:function:: struct mtd_info *doc_probe_device(struct docg3_cascade *cascade, int floor, struct device *dev)

    Check if a device is available

    :param cascade:
        the cascade of chips this devices will belong to
    :type cascade: struct docg3_cascade \*

    :param floor:
        the floor of the probed device
    :type floor: int

    :param dev:
        the device
    :type dev: struct device \*

.. _`doc_probe_device.description`:

Description
-----------

Checks whether a device at the specified IO range, and floor is available.

Returns a mtd_info struct if there is a device, ENODEV if none found, ENOMEM
if a memory allocation failed. If floor 0 is checked, a reset of the ASIC is
launched.

.. _`doc_release_device`:

doc_release_device
==================

.. c:function:: void doc_release_device(struct mtd_info *mtd)

    Release a docg3 floor

    :param mtd:
        the device
    :type mtd: struct mtd_info \*

.. _`docg3_resume`:

docg3_resume
============

.. c:function:: int docg3_resume(struct platform_device *pdev)

    Awakens docg3 floor

    :param pdev:
        platfrom device
    :type pdev: struct platform_device \*

.. _`docg3_resume.description`:

Description
-----------

Returns 0 (always successful)

.. _`docg3_suspend`:

docg3_suspend
=============

.. c:function:: int docg3_suspend(struct platform_device *pdev, pm_message_t state)

    Put in low power mode the docg3 floor

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

    :param state:
        power state
    :type state: pm_message_t

.. _`docg3_suspend.description`:

Description
-----------

Shuts off most of docg3 circuitery to lower power consumption.

Returns 0 if suspend succeeded, -EIO if chip refused suspend

.. _`docg3_probe`:

docg3_probe
===========

.. c:function:: int docg3_probe(struct platform_device *pdev)

    Probe the IO space for a DiskOnChip G3 chip

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

.. _`docg3_probe.description`:

Description
-----------

Probes for a G3 chip at the specified IO space in the platform data
ressources. The floor 0 must be available.

Returns 0 on success, -ENOMEM, -ENXIO on error

.. _`docg3_release`:

docg3_release
=============

.. c:function:: int docg3_release(struct platform_device *pdev)

    Release the driver

    :param pdev:
        the platform device
    :type pdev: struct platform_device \*

.. _`docg3_release.description`:

Description
-----------

Returns 0

.. This file was automatic generated / don't edit.


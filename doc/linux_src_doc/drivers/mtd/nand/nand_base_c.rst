.. -*- coding: utf-8; mode: rst -*-

===========
nand_base.c
===========

.. _`nand_release_device`:

nand_release_device
===================

.. c:function:: void nand_release_device (struct mtd_info *mtd)

    [GENERIC] release chip

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_release_device.description`:

Description
-----------

Release chip lock and wake up anyone waiting on the device.


.. _`nand_read_byte`:

nand_read_byte
==============

.. c:function:: uint8_t nand_read_byte (struct mtd_info *mtd)

    [DEFAULT] read one byte from the chip

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_read_byte.description`:

Description
-----------

Default read function for 8bit buswidth


.. _`nand_read_byte16`:

nand_read_byte16
================

.. c:function:: uint8_t nand_read_byte16 (struct mtd_info *mtd)

    [DEFAULT] read one byte endianness aware from the chip

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_read_byte16.description`:

Description
-----------

Default read function for 16bit buswidth with endianness conversion.


.. _`nand_read_word`:

nand_read_word
==============

.. c:function:: u16 nand_read_word (struct mtd_info *mtd)

    [DEFAULT] read one word from the chip

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_read_word.description`:

Description
-----------

Default read function for 16bit buswidth without endianness conversion.


.. _`nand_select_chip`:

nand_select_chip
================

.. c:function:: void nand_select_chip (struct mtd_info *mtd, int chipnr)

    [DEFAULT] control CE line

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int chipnr:
        chipnumber to select, -1 for deselect


.. _`nand_select_chip.description`:

Description
-----------

Default select function for 1 chip devices.


.. _`nand_write_byte`:

nand_write_byte
===============

.. c:function:: void nand_write_byte (struct mtd_info *mtd, uint8_t byte)

    [DEFAULT] write single byte to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t byte:
        value to write


.. _`nand_write_byte.description`:

Description
-----------

Default function to write a byte to I/O[7:0]


.. _`nand_write_byte16`:

nand_write_byte16
=================

.. c:function:: void nand_write_byte16 (struct mtd_info *mtd, uint8_t byte)

    [DEFAULT] write single byte to a chip with width 16

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t byte:
        value to write


.. _`nand_write_byte16.description`:

Description
-----------

Default function to write a byte to I/O[7:0] on a 16-bit wide chip.


.. _`nand_write_buf`:

nand_write_buf
==============

.. c:function:: void nand_write_buf (struct mtd_info *mtd, const uint8_t *buf, int len)

    [DEFAULT] write buffer to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const uint8_t \*buf:
        data buffer

    :param int len:
        number of bytes to write


.. _`nand_write_buf.description`:

Description
-----------

Default write function for 8bit buswidth.


.. _`nand_read_buf`:

nand_read_buf
=============

.. c:function:: void nand_read_buf (struct mtd_info *mtd, uint8_t *buf, int len)

    [DEFAULT] read chip data into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        buffer to store date

    :param int len:
        number of bytes to read


.. _`nand_read_buf.description`:

Description
-----------

Default read function for 8bit buswidth.


.. _`nand_write_buf16`:

nand_write_buf16
================

.. c:function:: void nand_write_buf16 (struct mtd_info *mtd, const uint8_t *buf, int len)

    [DEFAULT] write buffer to chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param const uint8_t \*buf:
        data buffer

    :param int len:
        number of bytes to write


.. _`nand_write_buf16.description`:

Description
-----------

Default write function for 16bit buswidth.


.. _`nand_read_buf16`:

nand_read_buf16
===============

.. c:function:: void nand_read_buf16 (struct mtd_info *mtd, uint8_t *buf, int len)

    [DEFAULT] read chip data into buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        buffer to store date

    :param int len:
        number of bytes to read


.. _`nand_read_buf16.description`:

Description
-----------

Default read function for 16bit buswidth.


.. _`nand_block_bad`:

nand_block_bad
==============

.. c:function:: int nand_block_bad (struct mtd_info *mtd, loff_t ofs)

    [DEFAULT] Read bad block marker from the chip

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset from device start


.. _`nand_block_bad.description`:

Description
-----------

Check, if the block is bad.


.. _`nand_default_block_markbad`:

nand_default_block_markbad
==========================

.. c:function:: int nand_default_block_markbad (struct mtd_info *mtd, loff_t ofs)

    [DEFAULT] mark a block bad via bad block marker

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset from device start


.. _`nand_default_block_markbad.description`:

Description
-----------

This is the default implementation, which can be overridden by a hardware
specific driver. It provides the details for writing a bad block marker to a
block.


.. _`nand_block_markbad_lowlevel`:

nand_block_markbad_lowlevel
===========================

.. c:function:: int nand_block_markbad_lowlevel (struct mtd_info *mtd, loff_t ofs)

    mark a block bad

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset from device start


.. _`nand_block_markbad_lowlevel.description`:

Description
-----------

This function performs the generic NAND bad block marking steps (i.e., bad
block table(s) and/or marker(s)). We only allow the hardware driver to
specify how to write bad block markers to OOB (chip->block_markbad).

We try operations in the following order::

 (1) erase the affected block, to allow OOB marker to be written cleanly
 (2) write bad block marker to OOB area of affected block (unless flag
     NAND_BBT_NO_OOB_BBM is present)
 (3) update the BBT

Note that we retain the first error encountered in (2) or (3), finish the
procedures, and dump the error in the end.


.. _`nand_check_wp`:

nand_check_wp
=============

.. c:function:: int nand_check_wp (struct mtd_info *mtd)

    [GENERIC] check if the chip is write protected

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_check_wp.description`:

Description
-----------

Check, if the device is write protected. The function expects, that the
device is already selected.


.. _`nand_block_isreserved`:

nand_block_isreserved
=====================

.. c:function:: int nand_block_isreserved (struct mtd_info *mtd, loff_t ofs)

    [GENERIC] Check if a block is marked reserved.

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset from device start


.. _`nand_block_isreserved.description`:

Description
-----------

Check if the block is marked as reserved.


.. _`nand_block_checkbad`:

nand_block_checkbad
===================

.. c:function:: int nand_block_checkbad (struct mtd_info *mtd, loff_t ofs, int allowbbt)

    [GENERIC] Check if a block is marked bad

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset from device start

    :param int allowbbt:
        1, if its allowed to access the bbt area


.. _`nand_block_checkbad.description`:

Description
-----------

Check, if the block is bad. Either by reading the bad block table or
calling of the scan function.


.. _`panic_nand_wait_ready`:

panic_nand_wait_ready
=====================

.. c:function:: void panic_nand_wait_ready (struct mtd_info *mtd, unsigned long timeo)

    [GENERIC] Wait for the ready pin after commands.

    :param struct mtd_info \*mtd:
        MTD device structure

    :param unsigned long timeo:
        Timeout


.. _`panic_nand_wait_ready.description`:

Description
-----------

Helper function for nand_wait_ready used when needing to wait in interrupt
context.


.. _`nand_wait_ready`:

nand_wait_ready
===============

.. c:function:: void nand_wait_ready (struct mtd_info *mtd)

    [GENERIC] Wait for the ready pin after commands.

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_wait_ready.description`:

Description
-----------

Wait for the ready pin after a command, and warn if a timeout occurs.


.. _`nand_wait_status_ready`:

nand_wait_status_ready
======================

.. c:function:: void nand_wait_status_ready (struct mtd_info *mtd, unsigned long timeo)

    [GENERIC] Wait for the ready status after commands.

    :param struct mtd_info \*mtd:
        MTD device structure

    :param unsigned long timeo:
        Timeout in ms


.. _`nand_wait_status_ready.description`:

Description
-----------

Wait for status ready (i.e. command done) or timeout.


.. _`nand_command`:

nand_command
============

.. c:function:: void nand_command (struct mtd_info *mtd, unsigned int command, int column, int page_addr)

    [DEFAULT] Send command to NAND device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param unsigned int command:
        the command to be sent

    :param int column:
        the column address for this command, -1 if none

    :param int page_addr:
        the page address for this command, -1 if none


.. _`nand_command.description`:

Description
-----------

Send command to NAND device. This function is used for small page devices
(512 Bytes per page).


.. _`nand_command_lp`:

nand_command_lp
===============

.. c:function:: void nand_command_lp (struct mtd_info *mtd, unsigned int command, int column, int page_addr)

    [DEFAULT] Send command to NAND large page device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param unsigned int command:
        the command to be sent

    :param int column:
        the column address for this command, -1 if none

    :param int page_addr:
        the page address for this command, -1 if none


.. _`nand_command_lp.description`:

Description
-----------

Send command to NAND device. This is the version for the new large page
devices. We don't have the separate regions as we have in the small page
devices. We must emulate NAND_CMD_READOOB to keep the code compatible.


.. _`panic_nand_get_device`:

panic_nand_get_device
=====================

.. c:function:: void panic_nand_get_device (struct nand_chip *chip, struct mtd_info *mtd, int new_state)

    [GENERIC] Get chip for selected access

    :param struct nand_chip \*chip:
        the nand chip descriptor

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int new_state:
        the state which is requested


.. _`panic_nand_get_device.description`:

Description
-----------

Used when in panic, no locks are taken.


.. _`nand_get_device`:

nand_get_device
===============

.. c:function:: int nand_get_device (struct mtd_info *mtd, int new_state)

    [GENERIC] Get chip for selected access

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int new_state:
        the state which is requested


.. _`nand_get_device.description`:

Description
-----------

Get the device and lock it for exclusive access


.. _`panic_nand_wait`:

panic_nand_wait
===============

.. c:function:: void panic_nand_wait (struct mtd_info *mtd, struct nand_chip *chip, unsigned long timeo)

    [GENERIC] wait until the command is done

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        NAND chip structure

    :param unsigned long timeo:
        timeout


.. _`panic_nand_wait.description`:

Description
-----------

Wait for command done. This is a helper function for nand_wait used when
we are in interrupt context. May happen when in panic and trying to write
an oops through mtdoops.


.. _`nand_wait`:

nand_wait
=========

.. c:function:: int nand_wait (struct mtd_info *mtd, struct nand_chip *chip)

    [DEFAULT] wait until the command is done

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        NAND chip structure


.. _`nand_wait.description`:

Description
-----------

Wait for command done. This applies to erase and program only.


.. _`__nand_unlock`:

__nand_unlock
=============

.. c:function:: int __nand_unlock (struct mtd_info *mtd, loff_t ofs, uint64_t len, int invert)

    [REPLACEABLE] unlocks specified locked blocks

    :param struct mtd_info \*mtd:
        mtd info

    :param loff_t ofs:
        offset to start unlock from

    :param uint64_t len:
        length to unlock

    :param int invert:
        when = 0, unlock the range of blocks within the lower and
        upper boundary address
        when = 1, unlock the range of blocks outside the boundaries
        of the lower and upper boundary address


.. _`__nand_unlock.description`:

Description
-----------

Returs unlock status.


.. _`nand_unlock`:

nand_unlock
===========

.. c:function:: int nand_unlock (struct mtd_info *mtd, loff_t ofs, uint64_t len)

    [REPLACEABLE] unlocks specified locked blocks

    :param struct mtd_info \*mtd:
        mtd info

    :param loff_t ofs:
        offset to start unlock from

    :param uint64_t len:
        length to unlock


.. _`nand_unlock.description`:

Description
-----------

Returns unlock status.


.. _`nand_lock`:

nand_lock
=========

.. c:function:: int nand_lock (struct mtd_info *mtd, loff_t ofs, uint64_t len)

    [REPLACEABLE] locks all blocks present in the device

    :param struct mtd_info \*mtd:
        mtd info

    :param loff_t ofs:
        offset to start unlock from

    :param uint64_t len:
        length to unlock


.. _`nand_lock.description`:

Description
-----------

This feature is not supported in many NAND parts. 'Micron' NAND parts do
have this feature, but it allows only to lock all blocks, not for specified
range for block. Implementing 'lock' feature by making use of 'unlock', for
now.

Returns lock status.


.. _`nand_check_erased_buf`:

nand_check_erased_buf
=====================

.. c:function:: int nand_check_erased_buf (void *buf, int len, int bitflips_threshold)

    check if a buffer contains (almost) only 0xff data

    :param void \*buf:
        buffer to test

    :param int len:
        buffer length

    :param int bitflips_threshold:
        maximum number of bitflips


.. _`nand_check_erased_buf.description`:

Description
-----------

Check if a buffer contains only 0xff, which means the underlying region
has been erased and is ready to be programmed.
The bitflips_threshold specify the maximum number of bitflips before
considering the region is not erased.
Note: The logic of this function has been extracted from the memweight
implementation, except that nand_check_erased_buf function exit before
testing the whole buffer if the number of bitflips exceed the
bitflips_threshold value.

Returns a positive number of bitflips less than or equal to
bitflips_threshold, or -ERROR_CODE for bitflips in excess of the
threshold.


.. _`nand_check_erased_ecc_chunk`:

nand_check_erased_ecc_chunk
===========================

.. c:function:: int nand_check_erased_ecc_chunk (void *data, int datalen, void *ecc, int ecclen, void *extraoob, int extraooblen, int bitflips_threshold)

    check if an ECC chunk contains (almost) only 0xff data

    :param void \*data:
        data buffer to test

    :param int datalen:
        data length

    :param void \*ecc:
        ECC buffer

    :param int ecclen:
        ECC length

    :param void \*extraoob:
        extra OOB buffer

    :param int extraooblen:
        extra OOB length

    :param int bitflips_threshold:
        maximum number of bitflips


.. _`nand_check_erased_ecc_chunk.description`:

Description
-----------

Check if a data buffer and its associated ECC and OOB data contains only
0xff pattern, which means the underlying region has been erased and is
ready to be programmed.
The bitflips_threshold specify the maximum number of bitflips before
considering the region as not erased.

Note:
1/ ECC algorithms are working on pre-defined block sizes which are usually
different from the NAND page size. When fixing bitflips, ECC engines will
report the number of errors per chunk, and the NAND core infrastructure
expect you to return the maximum number of bitflips for the whole page.
This is why you should always use this function on a single chunk and
not on the whole page. After checking each chunk you should update your
max_bitflips value accordingly.

2/ When checking for bitflips in erased pages you should not only check
the payload data but also their associated ECC data, because a user might
have programmed almost all bits to 1 but a few. In this case, we
shouldn't consider the chunk as erased, and checking ECC bytes prevent
this case.

3/ The extraoob argument is optional, and should be used if some of your OOB
data are protected by the ECC engine.
It could also be used if you support subpages and want to attach some
extra OOB data to an ECC chunk.

Returns a positive number of bitflips less than or equal to
bitflips_threshold, or -ERROR_CODE for bitflips in excess of the
threshold. In case of success, the passed buffers are filled with 0xff.


.. _`nand_read_page_raw`:

nand_read_page_raw
==================

.. c:function:: int nand_read_page_raw (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [INTERN] read raw page data without ecc

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


.. _`nand_read_page_raw.description`:

Description
-----------

Not for syndrome calculating ECC controllers, which use a special oob layout.


.. _`nand_read_page_raw_syndrome`:

nand_read_page_raw_syndrome
===========================

.. c:function:: int nand_read_page_raw_syndrome (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [INTERN] read raw page data without ecc

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


.. _`nand_read_page_raw_syndrome.description`:

Description
-----------

We need a special oob layout and handling even when OOB isn't used.


.. _`nand_read_page_swecc`:

nand_read_page_swecc
====================

.. c:function:: int nand_read_page_swecc (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] software ECC based page read function

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


.. _`nand_read_subpage`:

nand_read_subpage
=================

.. c:function:: int nand_read_subpage (struct mtd_info *mtd, struct nand_chip *chip, uint32_t data_offs, uint32_t readlen, uint8_t *bufpoi, int page)

    [REPLACEABLE] ECC based sub-page read function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param uint32_t data_offs:
        offset of requested data within the page

    :param uint32_t readlen:
        data length

    :param uint8_t \*bufpoi:
        buffer to store read data

    :param int page:
        page number to read


.. _`nand_read_page_hwecc`:

nand_read_page_hwecc
====================

.. c:function:: int nand_read_page_hwecc (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based page read function

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


.. _`nand_read_page_hwecc.description`:

Description
-----------

Not for syndrome calculating ECC controllers which need a special oob layout.


.. _`nand_read_page_hwecc_oob_first`:

nand_read_page_hwecc_oob_first
==============================

.. c:function:: int nand_read_page_hwecc_oob_first (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hw ecc, read oob first

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


.. _`nand_read_page_hwecc_oob_first.description`:

Description
-----------

Hardware ECC for large page chips, require OOB to be read first. For this
ECC mode, the write_page method is re-used from ECC_HW. These methods
read/write ECC from the OOB area, unlike the ECC_HW_SYNDROME support with
multiple ECC steps, follows the "infix ECC" scheme and reads/writes ECC from
the data area, by overwriting the NAND manufacturer bad block markings.


.. _`nand_read_page_syndrome`:

nand_read_page_syndrome
=======================

.. c:function:: int nand_read_page_syndrome (struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC syndrome based page read

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


.. _`nand_read_page_syndrome.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore we
need a special oob layout and handling.


.. _`nand_transfer_oob`:

nand_transfer_oob
=================

.. c:function:: uint8_t *nand_transfer_oob (struct nand_chip *chip, uint8_t *oob, struct mtd_oob_ops *ops, size_t len)

    [INTERN] Transfer oob to client buffer

    :param struct nand_chip \*chip:
        nand chip structure

    :param uint8_t \*oob:
        oob destination address

    :param struct mtd_oob_ops \*ops:
        oob ops structure

    :param size_t len:
        size of oob to transfer


.. _`nand_setup_read_retry`:

nand_setup_read_retry
=====================

.. c:function:: int nand_setup_read_retry (struct mtd_info *mtd, int retry_mode)

    [INTERN] Set the READ RETRY mode

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int retry_mode:
        the retry mode to use


.. _`nand_setup_read_retry.description`:

Description
-----------

Some vendors supply a special command to shift the Vt threshold, to be used
when there are too many bitflips in a page (i.e., ECC error). After setting
a new threshold, the host should retry reading the page.


.. _`nand_do_read_ops`:

nand_do_read_ops
================

.. c:function:: int nand_do_read_ops (struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [INTERN] Read data with ECC

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t from:
        offset to read from

    :param struct mtd_oob_ops \*ops:
        oob ops structure


.. _`nand_do_read_ops.description`:

Description
-----------

Internal function. Called with chip held.


.. _`nand_read`:

nand_read
=========

.. c:function:: int nand_read (struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, uint8_t *buf)

    [MTD Interface] MTD compatibility function for nand_do_read_ecc

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t from:
        offset to read from

    :param size_t len:
        number of bytes to read

    :param size_t \*retlen:
        pointer to variable to store the number of read bytes

    :param uint8_t \*buf:
        the databuffer to put data


.. _`nand_read.description`:

Description
-----------

Get hold of the chip and call nand_do_read.


.. _`nand_read_oob_std`:

nand_read_oob_std
=================

.. c:function:: int nand_read_oob_std (struct mtd_info *mtd, struct nand_chip *chip, int page)

    [REPLACEABLE] the most common OOB data read function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int page:
        page number to read


.. _`nand_read_oob_syndrome`:

nand_read_oob_syndrome
======================

.. c:function:: int nand_read_oob_syndrome (struct mtd_info *mtd, struct nand_chip *chip, int page)

    [REPLACEABLE] OOB data read function for HW ECC with syndromes

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int page:
        page number to read


.. _`nand_write_oob_std`:

nand_write_oob_std
==================

.. c:function:: int nand_write_oob_std (struct mtd_info *mtd, struct nand_chip *chip, int page)

    [REPLACEABLE] the most common OOB data write function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int page:
        page number to write


.. _`nand_write_oob_syndrome`:

nand_write_oob_syndrome
=======================

.. c:function:: int nand_write_oob_syndrome (struct mtd_info *mtd, struct nand_chip *chip, int page)

    [REPLACEABLE] OOB data write function for HW ECC with syndrome - only for large page flash

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int page:
        page number to write


.. _`nand_do_read_oob`:

nand_do_read_oob
================

.. c:function:: int nand_do_read_oob (struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [INTERN] NAND read out-of-band

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t from:
        offset to read from

    :param struct mtd_oob_ops \*ops:
        oob operations description structure


.. _`nand_do_read_oob.description`:

Description
-----------

NAND read out-of-band data from the spare area.


.. _`nand_read_oob`:

nand_read_oob
=============

.. c:function:: int nand_read_oob (struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [MTD Interface] NAND read data and/or out-of-band

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t from:
        offset to read from

    :param struct mtd_oob_ops \*ops:
        oob operation description structure


.. _`nand_read_oob.description`:

Description
-----------

NAND read data and/or out-of-band data.


.. _`nand_write_page_raw`:

nand_write_page_raw
===================

.. c:function:: int nand_write_page_raw (struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [INTERN] raw page write function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_page_raw.description`:

Description
-----------

Not for syndrome calculating ECC controllers, which use a special oob layout.


.. _`nand_write_page_raw_syndrome`:

nand_write_page_raw_syndrome
============================

.. c:function:: int nand_write_page_raw_syndrome (struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [INTERN] raw page write function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_page_raw_syndrome.description`:

Description
-----------

We need a special oob layout and handling even when ECC isn't checked.


.. _`nand_write_page_swecc`:

nand_write_page_swecc
=====================

.. c:function:: int nand_write_page_swecc (struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] software ECC based page write function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_page_hwecc`:

nand_write_page_hwecc
=====================

.. c:function:: int nand_write_page_hwecc (struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based page write function

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_subpage_hwecc`:

nand_write_subpage_hwecc
========================

.. c:function:: int nand_write_subpage_hwecc (struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, uint32_t data_len, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based subpage write

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param uint32_t offset:
        column address of subpage within the page

    :param uint32_t data_len:
        data length

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_page_syndrome`:

nand_write_page_syndrome
========================

.. c:function:: int nand_write_page_syndrome (struct mtd_info *mtd, struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC syndrome based page write

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param const uint8_t \*buf:
        data buffer

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write


.. _`nand_write_page_syndrome.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore we
need a special oob layout and handling.


.. _`nand_write_page`:

nand_write_page
===============

.. c:function:: int nand_write_page (struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, int data_len, const uint8_t *buf, int oob_required, int page, int cached, int raw)

    [REPLACEABLE] write one page

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        NAND chip descriptor

    :param uint32_t offset:
        address offset within the page

    :param int data_len:
        length of actual data to be written

    :param const uint8_t \*buf:
        the data to write

    :param int oob_required:
        must write chip->oob_poi to OOB

    :param int page:
        page number to write

    :param int cached:
        cached programming

    :param int raw:
        use _raw version of write_page


.. _`nand_fill_oob`:

nand_fill_oob
=============

.. c:function:: uint8_t *nand_fill_oob (struct mtd_info *mtd, uint8_t *oob, size_t len, struct mtd_oob_ops *ops)

    [INTERN] Transfer client buffer to oob

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*oob:
        oob data buffer

    :param size_t len:
        oob data write length

    :param struct mtd_oob_ops \*ops:
        oob ops structure


.. _`nand_do_write_ops`:

nand_do_write_ops
=================

.. c:function:: int nand_do_write_ops (struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [INTERN] NAND write with ECC

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t to:
        offset to write to

    :param struct mtd_oob_ops \*ops:
        oob operations description structure


.. _`nand_do_write_ops.description`:

Description
-----------

NAND write with ECC.


.. _`panic_nand_write`:

panic_nand_write
================

.. c:function:: int panic_nand_write (struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const uint8_t *buf)

    [MTD Interface] NAND write with ECC

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t to:
        offset to write to

    :param size_t len:
        number of bytes to write

    :param size_t \*retlen:
        pointer to variable to store the number of written bytes

    :param const uint8_t \*buf:
        the data to write


.. _`panic_nand_write.description`:

Description
-----------

NAND write with ECC. Used when performing writes in interrupt context, this
may for example be called by mtdoops when writing an oops while in panic.


.. _`nand_write`:

nand_write
==========

.. c:function:: int nand_write (struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const uint8_t *buf)

    [MTD Interface] NAND write with ECC

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t to:
        offset to write to

    :param size_t len:
        number of bytes to write

    :param size_t \*retlen:
        pointer to variable to store the number of written bytes

    :param const uint8_t \*buf:
        the data to write


.. _`nand_write.description`:

Description
-----------

NAND write with ECC.


.. _`nand_do_write_oob`:

nand_do_write_oob
=================

.. c:function:: int nand_do_write_oob (struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [MTD Interface] NAND write out-of-band

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t to:
        offset to write to

    :param struct mtd_oob_ops \*ops:
        oob operation description structure


.. _`nand_do_write_oob.description`:

Description
-----------

NAND write out-of-band.


.. _`nand_write_oob`:

nand_write_oob
==============

.. c:function:: int nand_write_oob (struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [MTD Interface] NAND write data and/or out-of-band

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t to:
        offset to write to

    :param struct mtd_oob_ops \*ops:
        oob operation description structure


.. _`single_erase`:

single_erase
============

.. c:function:: int single_erase (struct mtd_info *mtd, int page)

    [GENERIC] NAND standard block erase command function

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int page:
        the page address of the block which will be erased


.. _`single_erase.description`:

Description
-----------

Standard erase command for NAND chips. Returns NAND status.


.. _`nand_erase`:

nand_erase
==========

.. c:function:: int nand_erase (struct mtd_info *mtd, struct erase_info *instr)

    [MTD Interface] erase block(s)

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct erase_info \*instr:
        erase instruction


.. _`nand_erase.description`:

Description
-----------

Erase one ore more blocks.


.. _`nand_erase_nand`:

nand_erase_nand
===============

.. c:function:: int nand_erase_nand (struct mtd_info *mtd, struct erase_info *instr, int allowbbt)

    [INTERN] erase block(s)

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct erase_info \*instr:
        erase instruction

    :param int allowbbt:
        allow erasing the bbt area


.. _`nand_erase_nand.description`:

Description
-----------

Erase one ore more blocks.


.. _`nand_sync`:

nand_sync
=========

.. c:function:: void nand_sync (struct mtd_info *mtd)

    [MTD Interface] sync

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_sync.description`:

Description
-----------

Sync is actually a wait for chip ready function.


.. _`nand_block_isbad`:

nand_block_isbad
================

.. c:function:: int nand_block_isbad (struct mtd_info *mtd, loff_t offs)

    [MTD Interface] Check if block at offset is bad

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t offs:
        offset relative to mtd start


.. _`nand_block_markbad`:

nand_block_markbad
==================

.. c:function:: int nand_block_markbad (struct mtd_info *mtd, loff_t ofs)

    [MTD Interface] Mark block at the given offset as bad

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t ofs:
        offset relative to mtd start


.. _`nand_onfi_set_features`:

nand_onfi_set_features
======================

.. c:function:: int nand_onfi_set_features (struct mtd_info *mtd, struct nand_chip *chip, int addr, uint8_t *subfeature_param)

    [REPLACEABLE] set features for ONFI nand

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int addr:
        feature address.

    :param uint8_t \*subfeature_param:
        the subfeature parameters, a four bytes array.


.. _`nand_onfi_get_features`:

nand_onfi_get_features
======================

.. c:function:: int nand_onfi_get_features (struct mtd_info *mtd, struct nand_chip *chip, int addr, uint8_t *subfeature_param)

    [REPLACEABLE] get features for ONFI nand

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param int addr:
        feature address.

    :param uint8_t \*subfeature_param:
        the subfeature parameters, a four bytes array.


.. _`nand_suspend`:

nand_suspend
============

.. c:function:: int nand_suspend (struct mtd_info *mtd)

    [MTD Interface] Suspend the NAND flash

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_resume`:

nand_resume
===========

.. c:function:: void nand_resume (struct mtd_info *mtd)

    [MTD Interface] Resume the NAND flash

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_shutdown`:

nand_shutdown
=============

.. c:function:: void nand_shutdown (struct mtd_info *mtd)

    [MTD Interface] Finish the current NAND operation and prevent further operations

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_scan_ident`:

nand_scan_ident
===============

.. c:function:: int nand_scan_ident (struct mtd_info *mtd, int maxchips, struct nand_flash_dev *table)

    [NAND Interface] Scan for the NAND device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int maxchips:
        number of chips to scan for

    :param struct nand_flash_dev \*table:
        alternative NAND ID table


.. _`nand_scan_ident.description`:

Description
-----------

This is the first phase of the normal :c:func:`nand_scan` function. It reads the
flash ID and sets up MTD fields accordingly.

The mtd->owner field must be set to the module of the caller.


.. _`nand_scan_tail`:

nand_scan_tail
==============

.. c:function:: int nand_scan_tail (struct mtd_info *mtd)

    [NAND Interface] Scan for the NAND device

    :param struct mtd_info \*mtd:
        MTD device structure


.. _`nand_scan_tail.description`:

Description
-----------

This is the second phase of the normal :c:func:`nand_scan` function. It fills out
all the uninitialized function pointers with the defaults and scans for a
bad block table if appropriate.


.. _`nand_scan`:

nand_scan
=========

.. c:function:: int nand_scan (struct mtd_info *mtd, int maxchips)

    [NAND Interface] Scan for the NAND device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param int maxchips:
        number of chips to scan for


.. _`nand_scan.description`:

Description
-----------

This fills out all the uninitialized function pointers with the defaults.
The flash ID is read and the mtd/chip structures are filled with the
appropriate values. The mtd->owner field must be set to the module of the
caller.


.. _`nand_release`:

nand_release
============

.. c:function:: void nand_release (struct mtd_info *mtd)

    [NAND Interface] Free resources held by the NAND device

    :param struct mtd_info \*mtd:
        MTD device structure


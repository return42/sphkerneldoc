.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/onenand/onenand_base.c

.. _`onenand_ooblayout_32_64_ecc`:

onenand_ooblayout_32_64_ecc
===========================

.. c:function:: int onenand_ooblayout_32_64_ecc(struct mtd_info *mtd, int section, struct mtd_oob_region *oobregion)

    oob info for large (2KB) page

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param section:
        *undescribed*
    :type section: int

    :param oobregion:
        *undescribed*
    :type oobregion: struct mtd_oob_region \*

.. _`onenand_readw`:

onenand_readw
=============

.. c:function:: unsigned short onenand_readw(void __iomem *addr)

    [OneNAND Interface] Read OneNAND register \ ``param``\  addr          address to read

    :param addr:
        *undescribed*
    :type addr: void __iomem \*

.. _`onenand_readw.description`:

Description
-----------

Read OneNAND register

.. _`onenand_writew`:

onenand_writew
==============

.. c:function:: void onenand_writew(unsigned short value, void __iomem *addr)

    [OneNAND Interface] Write OneNAND register with value \ ``param``\  value         value to write \ ``param``\  addr          address to write

    :param value:
        *undescribed*
    :type value: unsigned short

    :param addr:
        *undescribed*
    :type addr: void __iomem \*

.. _`onenand_writew.description`:

Description
-----------

Write OneNAND register with value

.. _`onenand_block_address`:

onenand_block_address
=====================

.. c:function:: int onenand_block_address(struct onenand_chip *this, int block)

    [DEFAULT] Get block address \ ``param``\  this          onenand chip data structure \ ``param``\  block         the block \ ``return``\               translated block address if DDP, otherwise same

    :param this:
        *undescribed*
    :type this: struct onenand_chip \*

    :param block:
        *undescribed*
    :type block: int

.. _`onenand_block_address.description`:

Description
-----------

Setup Start Address 1 Register (F100h)

.. _`onenand_bufferram_address`:

onenand_bufferram_address
=========================

.. c:function:: int onenand_bufferram_address(struct onenand_chip *this, int block)

    [DEFAULT] Get bufferram address \ ``param``\  this          onenand chip data structure \ ``param``\  block         the block \ ``return``\               set DBS value if DDP, otherwise 0

    :param this:
        *undescribed*
    :type this: struct onenand_chip \*

    :param block:
        *undescribed*
    :type block: int

.. _`onenand_bufferram_address.description`:

Description
-----------

Setup Start Address 2 Register (F101h) for DDP

.. _`onenand_page_address`:

onenand_page_address
====================

.. c:function:: int onenand_page_address(int page, int sector)

    [DEFAULT] Get page address \ ``param``\  page          the page address \ ``param``\  sector        the sector address \ ``return``\               combined page and sector address

    :param page:
        *undescribed*
    :type page: int

    :param sector:
        *undescribed*
    :type sector: int

.. _`onenand_page_address.description`:

Description
-----------

Setup Start Address 8 Register (F107h)

.. _`onenand_buffer_address`:

onenand_buffer_address
======================

.. c:function:: int onenand_buffer_address(int dataram1, int sectors, int count)

    [DEFAULT] Get buffer address \ ``param``\  dataram1      DataRAM index \ ``param``\  sectors       the sector address \ ``param``\  count         the number of sectors \ ``return``\               the start buffer value

    :param dataram1:
        *undescribed*
    :type dataram1: int

    :param sectors:
        *undescribed*
    :type sectors: int

    :param count:
        *undescribed*
    :type count: int

.. _`onenand_buffer_address.description`:

Description
-----------

Setup Start Buffer Register (F200h)

.. _`flexonenand_block`:

flexonenand_block
=================

.. c:function:: unsigned flexonenand_block(struct onenand_chip *this, loff_t addr)

    For given address return block number \ ``param``\  this         - OneNAND device structure \ ``param``\  addr          - Address for which block number is needed

    :param this:
        *undescribed*
    :type this: struct onenand_chip \*

    :param addr:
        *undescribed*
    :type addr: loff_t

.. _`flexonenand_addr`:

flexonenand_addr
================

.. c:function:: loff_t flexonenand_addr(struct onenand_chip *this, int block)

    Return address of the block

    :param this:
        OneNAND device structure
    :type this: struct onenand_chip \*

    :param block:
        Block number on Flex-OneNAND
    :type block: int

.. _`flexonenand_addr.description`:

Description
-----------

Return address of the block

.. _`onenand_get_density`:

onenand_get_density
===================

.. c:function:: int onenand_get_density(int dev_id)

    [DEFAULT] Get OneNAND density \ ``param``\  dev_id        OneNAND device ID

    :param dev_id:
        *undescribed*
    :type dev_id: int

.. _`onenand_get_density.description`:

Description
-----------

Get OneNAND density from device ID

.. _`flexonenand_region`:

flexonenand_region
==================

.. c:function:: int flexonenand_region(struct mtd_info *mtd, loff_t addr)

    [Flex-OneNAND] Return erase region of addr \ ``param``\  mtd           MTD device structure \ ``param``\  addr          address whose erase region needs to be identified

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

.. _`onenand_command`:

onenand_command
===============

.. c:function:: int onenand_command(struct mtd_info *mtd, int cmd, loff_t addr, size_t len)

    [DEFAULT] Send command to OneNAND device \ ``param``\  mtd           MTD device structure \ ``param``\  cmd           the command to be sent \ ``param``\  addr          offset to read from or write to \ ``param``\  len           number of bytes to read or write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param cmd:
        *undescribed*
    :type cmd: int

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param len:
        *undescribed*
    :type len: size_t

.. _`onenand_command.description`:

Description
-----------

Send command to OneNAND device. This function is used for middle/large page
devices (1KB/2KB Bytes per page)

.. _`onenand_read_ecc`:

onenand_read_ecc
================

.. c:function:: int onenand_read_ecc(struct onenand_chip *this)

    return ecc status \ ``param``\  this          onenand chip structure

    :param this:
        *undescribed*
    :type this: struct onenand_chip \*

.. _`onenand_wait`:

onenand_wait
============

.. c:function:: int onenand_wait(struct mtd_info *mtd, int state)

    [DEFAULT] wait until the command is done \ ``param``\  mtd           MTD device structure \ ``param``\  state         state to select the max. timeout value

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param state:
        *undescribed*
    :type state: int

.. _`onenand_wait.description`:

Description
-----------

Wait for command done. This applies to all OneNAND command
Read can take up to 30us, erase up to 2ms and program up to 350us
according to general OneNAND specs

.. _`onenand_bufferram_offset`:

onenand_bufferram_offset
========================

.. c:function:: int onenand_bufferram_offset(struct mtd_info *mtd, int area)

    [DEFAULT] BufferRAM offset \ ``param``\  mtd           MTD data structure \ ``param``\  area          BufferRAM area \ ``return``\               offset given area

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param area:
        *undescribed*
    :type area: int

.. _`onenand_bufferram_offset.description`:

Description
-----------

Return BufferRAM offset given area

.. _`onenand_read_bufferram`:

onenand_read_bufferram
======================

.. c:function:: int onenand_read_bufferram(struct mtd_info *mtd, int area, unsigned char *buffer, int offset, size_t count)

    [OneNAND Interface] Read the bufferram area \ ``param``\  mtd           MTD data structure \ ``param``\  area          BufferRAM area \ ``param``\  buffer        the databuffer to put/get data \ ``param``\  offset        offset to read from or write to \ ``param``\  count         number of bytes to read/write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param area:
        *undescribed*
    :type area: int

    :param buffer:
        *undescribed*
    :type buffer: unsigned char \*

    :param offset:
        *undescribed*
    :type offset: int

    :param count:
        *undescribed*
    :type count: size_t

.. _`onenand_read_bufferram.description`:

Description
-----------

Read the BufferRAM area

.. _`onenand_sync_read_bufferram`:

onenand_sync_read_bufferram
===========================

.. c:function:: int onenand_sync_read_bufferram(struct mtd_info *mtd, int area, unsigned char *buffer, int offset, size_t count)

    [OneNAND Interface] Read the bufferram area with Sync. Burst mode \ ``param``\  mtd           MTD data structure \ ``param``\  area          BufferRAM area \ ``param``\  buffer        the databuffer to put/get data \ ``param``\  offset        offset to read from or write to \ ``param``\  count         number of bytes to read/write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param area:
        *undescribed*
    :type area: int

    :param buffer:
        *undescribed*
    :type buffer: unsigned char \*

    :param offset:
        *undescribed*
    :type offset: int

    :param count:
        *undescribed*
    :type count: size_t

.. _`onenand_sync_read_bufferram.description`:

Description
-----------

Read the BufferRAM area with Sync. Burst Mode

.. _`onenand_write_bufferram`:

onenand_write_bufferram
=======================

.. c:function:: int onenand_write_bufferram(struct mtd_info *mtd, int area, const unsigned char *buffer, int offset, size_t count)

    [OneNAND Interface] Write the bufferram area \ ``param``\  mtd           MTD data structure \ ``param``\  area          BufferRAM area \ ``param``\  buffer        the databuffer to put/get data \ ``param``\  offset        offset to read from or write to \ ``param``\  count         number of bytes to read/write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param area:
        *undescribed*
    :type area: int

    :param buffer:
        *undescribed*
    :type buffer: const unsigned char \*

    :param offset:
        *undescribed*
    :type offset: int

    :param count:
        *undescribed*
    :type count: size_t

.. _`onenand_write_bufferram.description`:

Description
-----------

Write the BufferRAM area

.. _`onenand_get_2x_blockpage`:

onenand_get_2x_blockpage
========================

.. c:function:: int onenand_get_2x_blockpage(struct mtd_info *mtd, loff_t addr)

    [GENERIC] Get blockpage at 2x program mode \ ``param``\  mtd           MTD data structure \ ``param``\  addr          address to check \ ``return``\               blockpage address

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

.. _`onenand_get_2x_blockpage.description`:

Description
-----------

Get blockpage address at 2x program mode

.. _`onenand_check_bufferram`:

onenand_check_bufferram
=======================

.. c:function:: int onenand_check_bufferram(struct mtd_info *mtd, loff_t addr)

    [GENERIC] Check BufferRAM information \ ``param``\  mtd           MTD data structure \ ``param``\  addr          address to check \ ``return``\               1 if there are valid data, otherwise 0

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

.. _`onenand_check_bufferram.description`:

Description
-----------

Check bufferram if there is data we required

.. _`onenand_update_bufferram`:

onenand_update_bufferram
========================

.. c:function:: void onenand_update_bufferram(struct mtd_info *mtd, loff_t addr, int valid)

    [GENERIC] Update BufferRAM information \ ``param``\  mtd           MTD data structure \ ``param``\  addr          address to update \ ``param``\  valid         valid flag

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param valid:
        *undescribed*
    :type valid: int

.. _`onenand_update_bufferram.description`:

Description
-----------

Update BufferRAM information

.. _`onenand_invalidate_bufferram`:

onenand_invalidate_bufferram
============================

.. c:function:: void onenand_invalidate_bufferram(struct mtd_info *mtd, loff_t addr, unsigned int len)

    [GENERIC] Invalidate BufferRAM information \ ``param``\  mtd           MTD data structure \ ``param``\  addr          start address to invalidate \ ``param``\  len           length to invalidate

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param len:
        *undescribed*
    :type len: unsigned int

.. _`onenand_invalidate_bufferram.description`:

Description
-----------

Invalidate BufferRAM information

.. _`onenand_get_device`:

onenand_get_device
==================

.. c:function:: int onenand_get_device(struct mtd_info *mtd, int new_state)

    [GENERIC] Get chip for selected access \ ``param``\  mtd           MTD device structure \ ``param``\  new_state     the state which is requested

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param new_state:
        *undescribed*
    :type new_state: int

.. _`onenand_get_device.description`:

Description
-----------

Get the device and lock it for exclusive access

.. _`onenand_release_device`:

onenand_release_device
======================

.. c:function:: void onenand_release_device(struct mtd_info *mtd)

    [GENERIC] release chip \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_release_device.description`:

Description
-----------

Deselect, release chip lock and wake up anyone waiting on the device

.. _`onenand_transfer_auto_oob`:

onenand_transfer_auto_oob
=========================

.. c:function:: int onenand_transfer_auto_oob(struct mtd_info *mtd, uint8_t *buf, int column, int thislen)

    [INTERN] oob auto-placement transfer \ ``param``\  mtd           MTD device structure \ ``param``\  buf           destination address \ ``param``\  column        oob offset to read from \ ``param``\  thislen       oob length to read

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param buf:
        *undescribed*
    :type buf: uint8_t \*

    :param column:
        *undescribed*
    :type column: int

    :param thislen:
        *undescribed*
    :type thislen: int

.. _`onenand_recover_lsb`:

onenand_recover_lsb
===================

.. c:function:: int onenand_recover_lsb(struct mtd_info *mtd, loff_t addr, int status)

    [Flex-OneNAND] Recover LSB page data \ ``param``\  mtd           MTD device structure \ ``param``\  addr          address to recover \ ``param``\  status        return value from onenand_wait / onenand_bbt_wait

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param status:
        *undescribed*
    :type status: int

.. _`onenand_recover_lsb.description`:

Description
-----------

MLC NAND Flash cell has paired pages - LSB page and MSB page. LSB page has
lower page address and MSB page has higher page address in paired pages.
If power off occurs during MSB page program, the paired LSB page data can
become corrupt. LSB page recovery read is a way to read LSB page though page
data are corrupted. When uncorrectable error occurs as a result of LSB page
read after power up, issue LSB page recovery read.

.. _`onenand_mlc_read_ops_nolock`:

onenand_mlc_read_ops_nolock
===========================

.. c:function:: int onenand_mlc_read_ops_nolock(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    MLC OneNAND read main and/or out-of-band \ ``param``\  mtd           MTD device structure \ ``param``\  from          offset to read from

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_mlc_read_ops_nolock.description`:

Description
-----------

MLC OneNAND / Flex-OneNAND has 4KB page size and 4KB dataram.
So, read-while-load is not present.

.. _`onenand_read_ops_nolock`:

onenand_read_ops_nolock
=======================

.. c:function:: int onenand_read_ops_nolock(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [OneNAND Interface] OneNAND read main and/or out-of-band \ ``param``\  mtd           MTD device structure \ ``param``\  from          offset to read from

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_read_ops_nolock.description`:

Description
-----------

OneNAND read main and/or out-of-band data

.. _`onenand_read_oob_nolock`:

onenand_read_oob_nolock
=======================

.. c:function:: int onenand_read_oob_nolock(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [MTD Interface] OneNAND read out-of-band \ ``param``\  mtd           MTD device structure \ ``param``\  from          offset to read from

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_read_oob_nolock.description`:

Description
-----------

OneNAND read out-of-band data from the spare area

.. _`onenand_read_oob`:

onenand_read_oob
================

.. c:function:: int onenand_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [MTD Interface] Read main and/or out-of-band

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_bbt_wait`:

onenand_bbt_wait
================

.. c:function:: int onenand_bbt_wait(struct mtd_info *mtd, int state)

    [DEFAULT] wait until the command is done \ ``param``\  mtd           MTD device structure \ ``param``\  state         state to select the max. timeout value

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param state:
        *undescribed*
    :type state: int

.. _`onenand_bbt_wait.description`:

Description
-----------

Wait for command done.

.. _`onenand_bbt_read_oob`:

onenand_bbt_read_oob
====================

.. c:function:: int onenand_bbt_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [MTD Interface] OneNAND read out-of-band for bbt scan \ ``param``\  mtd           MTD device structure \ ``param``\  from          offset to read from \ ``param``\  ops           oob operation description structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_bbt_read_oob.description`:

Description
-----------

OneNAND read out-of-band data from the spare area for bbt scan

.. _`onenand_verify_oob`:

onenand_verify_oob
==================

.. c:function:: int onenand_verify_oob(struct mtd_info *mtd, const u_char *buf, loff_t to)

    [GENERIC] verify the oob contents after a write \ ``param``\  mtd           MTD device structure \ ``param``\  buf           the databuffer to verify \ ``param``\  to            offset to read from

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param buf:
        *undescribed*
    :type buf: const u_char \*

    :param to:
        *undescribed*
    :type to: loff_t

.. _`onenand_verify`:

onenand_verify
==============

.. c:function:: int onenand_verify(struct mtd_info *mtd, const u_char *buf, loff_t addr, size_t len)

    [GENERIC] verify the chip contents after a write \ ``param``\  mtd          MTD device structure \ ``param``\  buf          the databuffer to verify \ ``param``\  addr         offset to read from \ ``param``\  len          number of bytes to read and compare

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param buf:
        *undescribed*
    :type buf: const u_char \*

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param len:
        *undescribed*
    :type len: size_t

.. _`onenand_panic_write`:

onenand_panic_write
===================

.. c:function:: int onenand_panic_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const u_char *buf)

    [MTD Interface] write buffer to FLASH in a panic context \ ``param``\  mtd           MTD device structure \ ``param``\  to            offset to write to \ ``param``\  len           number of bytes to write \ ``param``\  retlen        pointer to variable to store the number of written bytes \ ``param``\  buf           the data to write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: const u_char \*

.. _`onenand_panic_write.description`:

Description
-----------

Write with ECC

.. _`onenand_fill_auto_oob`:

onenand_fill_auto_oob
=====================

.. c:function:: int onenand_fill_auto_oob(struct mtd_info *mtd, u_char *oob_buf, const u_char *buf, int column, int thislen)

    [INTERN] oob auto-placement transfer \ ``param``\  mtd           MTD device structure \ ``param``\  oob_buf       oob buffer \ ``param``\  buf           source address \ ``param``\  column        oob offset to write to \ ``param``\  thislen       oob length to write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param oob_buf:
        *undescribed*
    :type oob_buf: u_char \*

    :param buf:
        *undescribed*
    :type buf: const u_char \*

    :param column:
        *undescribed*
    :type column: int

    :param thislen:
        *undescribed*
    :type thislen: int

.. _`onenand_write_ops_nolock`:

onenand_write_ops_nolock
========================

.. c:function:: int onenand_write_ops_nolock(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [OneNAND Interface] write main and/or out-of-band \ ``param``\  mtd           MTD device structure \ ``param``\  to            offset to write to \ ``param``\  ops           oob operation description structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_write_ops_nolock.description`:

Description
-----------

Write main and/or oob with ECC

.. _`onenand_write_oob_nolock`:

onenand_write_oob_nolock
========================

.. c:function:: int onenand_write_oob_nolock(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [INTERN] OneNAND write out-of-band \ ``param``\  mtd           MTD device structure \ ``param``\  to            offset to write to \ ``param``\  len           number of bytes to write \ ``param``\  retlen        pointer to variable to store the number of written bytes \ ``param``\  buf           the data to write \ ``param``\  mode          operation mode

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_write_oob_nolock.description`:

Description
-----------

OneNAND write out-of-band

.. _`onenand_write_oob`:

onenand_write_oob
=================

.. c:function:: int onenand_write_oob(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [MTD Interface] NAND write data and/or out-of-band

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_block_isbad_nolock`:

onenand_block_isbad_nolock
==========================

.. c:function:: int onenand_block_isbad_nolock(struct mtd_info *mtd, loff_t ofs, int allowbbt)

    [GENERIC] Check if a block is marked bad \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset from device start \ ``param``\  allowbbt      1, if its allowed to access the bbt area

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

    :param allowbbt:
        *undescribed*
    :type allowbbt: int

.. _`onenand_block_isbad_nolock.description`:

Description
-----------

Check, if the block is bad. Either by reading the bad block table or
calling of the scan function.

.. _`onenand_multiblock_erase`:

onenand_multiblock_erase
========================

.. c:function:: int onenand_multiblock_erase(struct mtd_info *mtd, struct erase_info *instr, unsigned int block_size)

    [INTERN] erase block(s) using multiblock erase \ ``param``\  mtd           MTD device structure \ ``param``\  instr         erase instruction \ ``param``\  region        erase region

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param instr:
        *undescribed*
    :type instr: struct erase_info \*

    :param block_size:
        *undescribed*
    :type block_size: unsigned int

.. _`onenand_multiblock_erase.description`:

Description
-----------

Erase one or more blocks up to 64 block at a time

.. _`onenand_block_by_block_erase`:

onenand_block_by_block_erase
============================

.. c:function:: int onenand_block_by_block_erase(struct mtd_info *mtd, struct erase_info *instr, struct mtd_erase_region_info *region, unsigned int block_size)

    [INTERN] erase block(s) using regular erase \ ``param``\  mtd           MTD device structure \ ``param``\  instr         erase instruction \ ``param``\  region        erase region \ ``param``\  block_size    erase block size

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param instr:
        *undescribed*
    :type instr: struct erase_info \*

    :param region:
        *undescribed*
    :type region: struct mtd_erase_region_info \*

    :param block_size:
        *undescribed*
    :type block_size: unsigned int

.. _`onenand_block_by_block_erase.description`:

Description
-----------

Erase one or more blocks one block at a time

.. _`onenand_erase`:

onenand_erase
=============

.. c:function:: int onenand_erase(struct mtd_info *mtd, struct erase_info *instr)

    [MTD Interface] erase block(s) \ ``param``\  mtd           MTD device structure \ ``param``\  instr         erase instruction

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param instr:
        *undescribed*
    :type instr: struct erase_info \*

.. _`onenand_erase.description`:

Description
-----------

Erase one or more blocks

.. _`onenand_sync`:

onenand_sync
============

.. c:function:: void onenand_sync(struct mtd_info *mtd)

    [MTD Interface] sync \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_sync.description`:

Description
-----------

Sync is actually a wait for chip ready function

.. _`onenand_block_isbad`:

onenand_block_isbad
===================

.. c:function:: int onenand_block_isbad(struct mtd_info *mtd, loff_t ofs)

    [MTD Interface] Check whether the block at the given offset is bad \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset relative to mtd start

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

.. _`onenand_block_isbad.description`:

Description
-----------

Check whether the block is bad

.. _`onenand_default_block_markbad`:

onenand_default_block_markbad
=============================

.. c:function:: int onenand_default_block_markbad(struct mtd_info *mtd, loff_t ofs)

    [DEFAULT] mark a block bad \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset from device start

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

.. _`onenand_default_block_markbad.description`:

Description
-----------

This is the default implementation, which can be overridden by
a hardware specific driver.

.. _`onenand_block_markbad`:

onenand_block_markbad
=====================

.. c:function:: int onenand_block_markbad(struct mtd_info *mtd, loff_t ofs)

    [MTD Interface] Mark the block at the given offset as bad \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset relative to mtd start

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

.. _`onenand_block_markbad.description`:

Description
-----------

Mark the block as bad

.. _`onenand_do_lock_cmd`:

onenand_do_lock_cmd
===================

.. c:function:: int onenand_do_lock_cmd(struct mtd_info *mtd, loff_t ofs, size_t len, int cmd)

    [OneNAND Interface] Lock or unlock block(s) \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset relative to mtd start \ ``param``\  len           number of bytes to lock or unlock \ ``param``\  cmd           lock or unlock command

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`onenand_do_lock_cmd.description`:

Description
-----------

Lock or unlock one or more blocks

.. _`onenand_lock`:

onenand_lock
============

.. c:function:: int onenand_lock(struct mtd_info *mtd, loff_t ofs, uint64_t len)

    [MTD Interface] Lock block(s) \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset relative to mtd start \ ``param``\  len           number of bytes to unlock

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

    :param len:
        *undescribed*
    :type len: uint64_t

.. _`onenand_lock.description`:

Description
-----------

Lock one or more blocks

.. _`onenand_unlock`:

onenand_unlock
==============

.. c:function:: int onenand_unlock(struct mtd_info *mtd, loff_t ofs, uint64_t len)

    [MTD Interface] Unlock block(s) \ ``param``\  mtd           MTD device structure \ ``param``\  ofs           offset relative to mtd start \ ``param``\  len           number of bytes to unlock

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param ofs:
        *undescribed*
    :type ofs: loff_t

    :param len:
        *undescribed*
    :type len: uint64_t

.. _`onenand_unlock.description`:

Description
-----------

Unlock one or more blocks

.. _`onenand_check_lock_status`:

onenand_check_lock_status
=========================

.. c:function:: int onenand_check_lock_status(struct onenand_chip *this)

    [OneNAND Interface] Check lock status \ ``param``\  this          onenand chip data structure

    :param this:
        *undescribed*
    :type this: struct onenand_chip \*

.. _`onenand_check_lock_status.description`:

Description
-----------

Check lock status

.. _`onenand_unlock_all`:

onenand_unlock_all
==================

.. c:function:: void onenand_unlock_all(struct mtd_info *mtd)

    [OneNAND Interface] unlock all blocks \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_unlock_all.description`:

Description
-----------

Unlock all blocks

.. _`onenand_otp_command`:

onenand_otp_command
===================

.. c:function:: int onenand_otp_command(struct mtd_info *mtd, int cmd, loff_t addr, size_t len)

    Send OTP specific command to OneNAND device \ ``param``\  mtd    MTD device structure \ ``param``\  cmd    the command to be sent \ ``param``\  addr   offset to read from or write to \ ``param``\  len    number of bytes to read or write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param cmd:
        *undescribed*
    :type cmd: int

    :param addr:
        *undescribed*
    :type addr: loff_t

    :param len:
        *undescribed*
    :type len: size_t

.. _`onenand_otp_write_oob_nolock`:

onenand_otp_write_oob_nolock
============================

.. c:function:: int onenand_otp_write_oob_nolock(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [INTERN] OneNAND write out-of-band, specific to OTP \ ``param``\  mtd           MTD device structure \ ``param``\  to            offset to write to \ ``param``\  len           number of bytes to write \ ``param``\  retlen        pointer to variable to store the number of written bytes \ ``param``\  buf           the data to write

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param ops:
        *undescribed*
    :type ops: struct mtd_oob_ops \*

.. _`onenand_otp_write_oob_nolock.description`:

Description
-----------

OneNAND write out-of-band only for OTP

.. _`do_otp_read`:

do_otp_read
===========

.. c:function:: int do_otp_read(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf)

    [DEFAULT] Read OTP block area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to read \ ``param``\  len           number of bytes to read \ ``param``\  retlen        pointer to variable to store the number of readbytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`do_otp_read.description`:

Description
-----------

Read OTP block area.

.. _`do_otp_write`:

do_otp_write
============

.. c:function:: int do_otp_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, u_char *buf)

    [DEFAULT] Write OTP block area \ ``param``\  mtd           MTD device structure \ ``param``\  to            The offset to write \ ``param``\  len           number of bytes to write \ ``param``\  retlen        pointer to variable to store the number of write bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param to:
        *undescribed*
    :type to: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`do_otp_write.description`:

Description
-----------

Write OTP block area.

.. _`do_otp_lock`:

do_otp_lock
===========

.. c:function:: int do_otp_lock(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf)

    [DEFAULT] Lock OTP block area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to lock \ ``param``\  len           number of bytes to lock \ ``param``\  retlen        pointer to variable to store the number of lock bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`do_otp_lock.description`:

Description
-----------

Lock OTP block area.

.. _`onenand_otp_walk`:

onenand_otp_walk
================

.. c:function:: int onenand_otp_walk(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf, otp_op_t action, int mode)

    [DEFAULT] Handle OTP operation \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to read/write \ ``param``\  len           number of bytes to read/write \ ``param``\  retlen        pointer to variable to store the number of read bytes \ ``param``\  buf           the databuffer to put/get data \ ``param``\  action        do given action \ ``param``\  mode          specify user and factory

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

    :param action:
        *undescribed*
    :type action: otp_op_t

    :param mode:
        *undescribed*
    :type mode: int

.. _`onenand_otp_walk.description`:

Description
-----------

Handle OTP operation.

.. _`onenand_get_fact_prot_info`:

onenand_get_fact_prot_info
==========================

.. c:function:: int onenand_get_fact_prot_info(struct mtd_info *mtd, size_t len, size_t *retlen, struct otp_info *buf)

    [MTD Interface] Read factory OTP info \ ``param``\  mtd           MTD device structure \ ``param``\  len           number of bytes to read \ ``param``\  retlen        pointer to variable to store the number of read bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: struct otp_info \*

.. _`onenand_get_fact_prot_info.description`:

Description
-----------

Read factory OTP info.

.. _`onenand_read_fact_prot_reg`:

onenand_read_fact_prot_reg
==========================

.. c:function:: int onenand_read_fact_prot_reg(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf)

    [MTD Interface] Read factory OTP area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to read \ ``param``\  len           number of bytes to read \ ``param``\  retlen        pointer to variable to store the number of read bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`onenand_read_fact_prot_reg.description`:

Description
-----------

Read factory OTP area.

.. _`onenand_get_user_prot_info`:

onenand_get_user_prot_info
==========================

.. c:function:: int onenand_get_user_prot_info(struct mtd_info *mtd, size_t len, size_t *retlen, struct otp_info *buf)

    [MTD Interface] Read user OTP info \ ``param``\  mtd           MTD device structure \ ``param``\  retlen        pointer to variable to store the number of read bytes \ ``param``\  len           number of bytes to read \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: struct otp_info \*

.. _`onenand_get_user_prot_info.description`:

Description
-----------

Read user OTP info.

.. _`onenand_read_user_prot_reg`:

onenand_read_user_prot_reg
==========================

.. c:function:: int onenand_read_user_prot_reg(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf)

    [MTD Interface] Read user OTP area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to read \ ``param``\  len           number of bytes to read \ ``param``\  retlen        pointer to variable to store the number of read bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`onenand_read_user_prot_reg.description`:

Description
-----------

Read user OTP area.

.. _`onenand_write_user_prot_reg`:

onenand_write_user_prot_reg
===========================

.. c:function:: int onenand_write_user_prot_reg(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u_char *buf)

    [MTD Interface] Write user OTP area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to write \ ``param``\  len           number of bytes to write \ ``param``\  retlen        pointer to variable to store the number of write bytes \ ``param``\  buf           the databuffer to put/get data

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

    :param retlen:
        *undescribed*
    :type retlen: size_t \*

    :param buf:
        *undescribed*
    :type buf: u_char \*

.. _`onenand_write_user_prot_reg.description`:

Description
-----------

Write user OTP area.

.. _`onenand_lock_user_prot_reg`:

onenand_lock_user_prot_reg
==========================

.. c:function:: int onenand_lock_user_prot_reg(struct mtd_info *mtd, loff_t from, size_t len)

    [MTD Interface] Lock user OTP area \ ``param``\  mtd           MTD device structure \ ``param``\  from          The offset to lock \ ``param``\  len           number of bytes to unlock

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param from:
        *undescribed*
    :type from: loff_t

    :param len:
        *undescribed*
    :type len: size_t

.. _`onenand_lock_user_prot_reg.description`:

Description
-----------

Write lock mark on spare area in page 0 in OTP block

.. _`onenand_check_features`:

onenand_check_features
======================

.. c:function:: void onenand_check_features(struct mtd_info *mtd)

    Check and set OneNAND features \ ``param``\  mtd           MTD data structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_check_features.description`:

Description
-----------

Check and set OneNAND features
- lock scheme
- two plane

.. _`onenand_print_device_info`:

onenand_print_device_info
=========================

.. c:function:: void onenand_print_device_info(int device, int version)

    Print device & version ID \ ``param``\  device        device ID \ ``param``\  version       version ID

    :param device:
        *undescribed*
    :type device: int

    :param version:
        *undescribed*
    :type version: int

.. _`onenand_print_device_info.description`:

Description
-----------

Print device & version ID

.. _`onenand_check_maf`:

onenand_check_maf
=================

.. c:function:: int onenand_check_maf(int manuf)

    Check manufacturer ID \ ``param``\  manuf         manufacturer ID

    :param manuf:
        *undescribed*
    :type manuf: int

.. _`onenand_check_maf.description`:

Description
-----------

Check manufacturer ID

.. _`flexonenand_get_boundary`:

flexonenand_get_boundary
========================

.. c:function:: int flexonenand_get_boundary(struct mtd_info *mtd)

    Reads the SLC boundary \ ``param``\  onenand_info           - onenand info structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`flexonenand_get_size`:

flexonenand_get_size
====================

.. c:function:: void flexonenand_get_size(struct mtd_info *mtd)

    Fill up fields in onenand_chip and mtd_info boundary[], diesize[], mtd->size, mtd->erasesize \ ``param``\  mtd           - MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`flexonenand_check_blocks_erased`:

flexonenand_check_blocks_erased
===============================

.. c:function:: int flexonenand_check_blocks_erased(struct mtd_info *mtd, int start, int end)

    Check if blocks are erased \ ``param``\  mtd_info      - mtd info structure \ ``param``\  start         - first erase block to check \ ``param``\  end           - last erase block to check

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param start:
        *undescribed*
    :type start: int

    :param end:
        *undescribed*
    :type end: int

.. _`flexonenand_check_blocks_erased.description`:

Description
-----------

Converting an unerased block from MLC to SLC
causes byte values to change. Since both data and its ECC
have changed, reads on the block give uncorrectable error.
This might lead to the block being detected as bad.

Avoid this by ensuring that the block to be converted is
erased.

.. _`flexonenand_set_boundary`:

flexonenand_set_boundary
========================

.. c:function:: int flexonenand_set_boundary(struct mtd_info *mtd, int die, int boundary, int lock)

    Writes the SLC boundary \ ``param``\  mtd                   - mtd info structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param die:
        *undescribed*
    :type die: int

    :param boundary:
        *undescribed*
    :type boundary: int

    :param lock:
        *undescribed*
    :type lock: int

.. _`onenand_chip_probe`:

onenand_chip_probe
==================

.. c:function:: int onenand_chip_probe(struct mtd_info *mtd)

    [OneNAND Interface] The generic chip probe \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_chip_probe.onenand-detection-method`:

OneNAND detection method
------------------------

Compare the values from command with ones from register

.. _`onenand_probe`:

onenand_probe
=============

.. c:function:: int onenand_probe(struct mtd_info *mtd)

    [OneNAND Interface] Probe the OneNAND device \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_suspend`:

onenand_suspend
===============

.. c:function:: int onenand_suspend(struct mtd_info *mtd)

    [MTD Interface] Suspend the OneNAND flash \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_resume`:

onenand_resume
==============

.. c:function:: void onenand_resume(struct mtd_info *mtd)

    [MTD Interface] Resume the OneNAND flash \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_scan`:

onenand_scan
============

.. c:function:: int onenand_scan(struct mtd_info *mtd, int maxchips)

    [OneNAND Interface] Scan for the OneNAND device \ ``param``\  mtd           MTD device structure \ ``param``\  maxchips      Number of chips to scan for

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param maxchips:
        *undescribed*
    :type maxchips: int

.. _`onenand_scan.description`:

Description
-----------

This fills out all the not initialized function pointers
with the defaults.
The flash ID is read and the mtd/chip structures are
filled with the appropriate values.

.. _`onenand_release`:

onenand_release
===============

.. c:function:: void onenand_release(struct mtd_info *mtd)

    [OneNAND Interface] Free resources held by the OneNAND device \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. This file was automatic generated / don't edit.


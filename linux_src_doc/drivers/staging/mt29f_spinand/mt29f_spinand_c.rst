.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/mt29f_spinand/mt29f_spinand.c

.. _`spinand_cmd`:

spinand_cmd
===========

.. c:function:: int spinand_cmd(struct spi_device *spi, struct spinand_cmd *cmd)

    process a command to send to the SPI Nand

    :param spi:
        *undescribed*
    :type spi: struct spi_device \*

    :param cmd:
        *undescribed*
    :type cmd: struct spinand_cmd \*

.. _`spinand_cmd.description`:

Description
-----------

Set up the command buffer to send to the SPI controller.
The command buffer has to initialized to 0.

.. _`spinand_read_id`:

spinand_read_id
===============

.. c:function:: int spinand_read_id(struct spi_device *spi_nand, u8 *id)

    Read SPI Nand ID

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param id:
        *undescribed*
    :type id: u8 \*

.. _`spinand_read_id.description`:

Description
-----------

read two ID bytes from the SPI Nand device

.. _`spinand_read_status`:

spinand_read_status
===================

.. c:function:: int spinand_read_status(struct spi_device *spi_nand, u8 *status)

    send command 0xf to the SPI Nand status register

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param status:
        *undescribed*
    :type status: u8 \*

.. _`spinand_read_status.description`:

Description
-----------

After read, write, or erase, the Nand device is expected to set the
busy status.

.. _`spinand_read_status.this-function-is-to-allow-reading-the-status-of-the-command`:

This function is to allow reading the status of the command
-----------------------------------------------------------

read,
write, and erase.
Once the status turns to be ready, the other status bits also are
valid status bits.

.. _`spinand_get_otp`:

spinand_get_otp
===============

.. c:function:: int spinand_get_otp(struct spi_device *spi_nand, u8 *otp)

    send command 0xf to read the SPI Nand OTP register

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param otp:
        *undescribed*
    :type otp: u8 \*

.. _`spinand_get_otp.description`:

Description
-----------

There is one bit( bit 0x10 ) to set or to clear the internal ECC.
Enable chip internal ECC, set the bit to 1
Disable chip internal ECC, clear the bit to 0

.. _`spinand_set_otp`:

spinand_set_otp
===============

.. c:function:: int spinand_set_otp(struct spi_device *spi_nand, u8 *otp)

    send command 0x1f to write the SPI Nand OTP register

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param otp:
        *undescribed*
    :type otp: u8 \*

.. _`spinand_set_otp.description`:

Description
-----------

There is one bit( bit 0x10 ) to set or to clear the internal ECC.
Enable chip internal ECC, set the bit to 1
Disable chip internal ECC, clear the bit to 0

.. _`spinand_enable_ecc`:

spinand_enable_ecc
==================

.. c:function:: int spinand_enable_ecc(struct spi_device *spi_nand)

    send command 0x1f to write the SPI Nand OTP register

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

.. _`spinand_enable_ecc.description`:

Description
-----------

There is one bit( bit 0x10 ) to set or to clear the internal ECC.
Enable chip internal ECC, set the bit to 1
Disable chip internal ECC, clear the bit to 0

.. _`spinand_write_enable`:

spinand_write_enable
====================

.. c:function:: int spinand_write_enable(struct spi_device *spi_nand)

    send command 0x06 to enable write or erase the Nand cells

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

.. _`spinand_write_enable.description`:

Description
-----------

Before write and erase the Nand cells, the write enable has to be set.
After the write or erase, the write enable bit is automatically
cleared (status register bit 2)
Set the bit 2 of the status register has the same effect

.. _`spinand_read_from_cache`:

spinand_read_from_cache
=======================

.. c:function:: int spinand_read_from_cache(struct spi_device *spi_nand, u16 page_id, u16 byte_id, u16 len, u8 *rbuf)

    send command 0x03 to read out the data from the cache register (2112 bytes max)

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param page_id:
        *undescribed*
    :type page_id: u16

    :param byte_id:
        *undescribed*
    :type byte_id: u16

    :param len:
        *undescribed*
    :type len: u16

    :param rbuf:
        *undescribed*
    :type rbuf: u8 \*

.. _`spinand_read_from_cache.description`:

Description
-----------

The read can specify 1 to 2112 bytes of data read at the corresponding
locations.
No tRd delay.

.. _`spinand_read_page`:

spinand_read_page
=================

.. c:function:: int spinand_read_page(struct spi_device *spi_nand, u16 page_id, u16 offset, u16 len, u8 *rbuf)

    read a page

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param page_id:
        the physical page number
    :type page_id: u16

    :param offset:
        the location from 0 to 2111
    :type offset: u16

    :param len:
        number of bytes to read
    :type len: u16

    :param rbuf:
        read buffer to hold \ ``len``\  bytes
    :type rbuf: u8 \*

.. _`spinand_read_page.description`:

Description
-----------

The read includes two commands to the Nand - 0x13 and 0x03 commands
Poll to read status to wait for tRD time.

.. _`spinand_program_data_to_cache`:

spinand_program_data_to_cache
=============================

.. c:function:: int spinand_program_data_to_cache(struct spi_device *spi_nand, u16 page_id, u16 byte_id, u16 len, u8 *wbuf)

    write a page to cache

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param page_id:
        *undescribed*
    :type page_id: u16

    :param byte_id:
        the location to write to the cache
    :type byte_id: u16

    :param len:
        number of bytes to write
    :type len: u16

    :param wbuf:
        write buffer holding \ ``len``\  bytes
    :type wbuf: u8 \*

.. _`spinand_program_data_to_cache.description`:

Description
-----------

The write command used here is 0x84--indicating that the cache is
not cleared first.
Since it is writing the data to cache, there is no tPROG time.

.. _`spinand_program_execute`:

spinand_program_execute
=======================

.. c:function:: int spinand_program_execute(struct spi_device *spi_nand, u16 page_id)

    write a page from cache to the Nand array

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param page_id:
        the physical page location to write the page.
    :type page_id: u16

.. _`spinand_program_execute.description`:

Description
-----------

The write command used here is 0x10--indicating the cache is writing to
the Nand array.
Need to wait for tPROG time to finish the transaction.

.. _`spinand_program_page`:

spinand_program_page
====================

.. c:function:: int spinand_program_page(struct spi_device *spi_nand, u16 page_id, u16 offset, u16 len, u8 *buf)

    write a page

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param page_id:
        the physical page location to write the page.
    :type page_id: u16

    :param offset:
        the location from the cache starting from 0 to 2111
    :type offset: u16

    :param len:
        the number of bytes to write
    :type len: u16

    :param buf:
        the buffer holding \ ``len``\  bytes
    :type buf: u8 \*

.. _`spinand_program_page.description`:

Description
-----------

The commands used here are 0x06, 0x84, and 0x10--indicating that
the write enable is first sent, the write cache command, and the
write execute command.
Poll to wait for the tPROG time to finish the transaction.

.. _`spinand_erase_block_erase`:

spinand_erase_block_erase
=========================

.. c:function:: int spinand_erase_block_erase(struct spi_device *spi_nand, u16 block_id)

    erase a page

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param block_id:
        the physical block location to erase.
    :type block_id: u16

.. _`spinand_erase_block_erase.description`:

Description
-----------

The command used here is 0xd8--indicating an erase command to erase
one block--64 pages
Need to wait for tERS.

.. _`spinand_erase_block`:

spinand_erase_block
===================

.. c:function:: int spinand_erase_block(struct spi_device *spi_nand, u16 block_id)

    erase a page

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param block_id:
        the physical block location to erase.
    :type block_id: u16

.. _`spinand_erase_block.description`:

Description
-----------

The commands used here are 0x06 and 0xd8--indicating an erase
command to erase one block--64 pages
It will first to enable the write enable bit (0x06 command),
and then send the 0xd8 erase command
Poll to wait for the tERS time to complete the tranaction.

.. _`spinand_lock_block`:

spinand_lock_block
==================

.. c:function:: int spinand_lock_block(struct spi_device *spi_nand, u8 lock)

    send write register 0x1f command to the Nand device

    :param spi_nand:
        *undescribed*
    :type spi_nand: struct spi_device \*

    :param lock:
        *undescribed*
    :type lock: u8

.. _`spinand_lock_block.description`:

Description
-----------

After power up, all the Nand blocks are locked.  This function allows
one to unlock the blocks, and so it can be written or erased.

.. _`spinand_probe`:

spinand_probe
=============

.. c:function:: int spinand_probe(struct spi_device *spi_nand)

    [spinand Interface]

    :param spi_nand:
        registered device driver.
    :type spi_nand: struct spi_device \*

.. _`spinand_probe.description`:

Description
-----------

Set up the device driver parameters to make the device available.

.. _`spinand_remove`:

spinand_remove
==============

.. c:function:: int spinand_remove(struct spi_device *spi)

    remove the device driver

    :param spi:
        the spi device.
    :type spi: struct spi_device \*

.. _`spinand_remove.description`:

Description
-----------

Remove the device driver parameters and free up allocated memories.

.. This file was automatic generated / don't edit.


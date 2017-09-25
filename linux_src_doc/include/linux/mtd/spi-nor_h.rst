.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/spi-nor.h

.. _`spi_nor`:

struct spi_nor
==============

.. c:type:: struct spi_nor

    Structure for defining a the SPI NOR layer

.. _`spi_nor.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor {
        struct mtd_info mtd;
        struct mutex lock;
        struct device *dev;
        u32 page_size;
        u8 addr_width;
        u8 erase_opcode;
        u8 read_opcode;
        u8 read_dummy;
        u8 program_opcode;
        enum spi_nor_protocol read_proto;
        enum spi_nor_protocol write_proto;
        enum spi_nor_protocol reg_proto;
        bool sst_write_second;
        u32 flags;
        u8 cmd_buf[SPI_NOR_MAX_CMD_SIZE];
        int (*prepare)(struct spi_nor *nor, enum spi_nor_ops ops);
        void (*unprepare)(struct spi_nor *nor, enum spi_nor_ops ops);
        int (*read_reg)(struct spi_nor *nor, u8 opcode, u8 *buf, int len);
        int (*write_reg)(struct spi_nor *nor, u8 opcode, u8 *buf, int len);
        ssize_t (*read)(struct spi_nor *nor, loff_t from, size_t len, u_char *read_buf);
        ssize_t (*write)(struct spi_nor *nor, loff_t to, size_t len, const u_char *write_buf);
        int (*erase)(struct spi_nor *nor, loff_t offs);
        int (*flash_lock)(struct spi_nor *nor, loff_t ofs, uint64_t len);
        int (*flash_unlock)(struct spi_nor *nor, loff_t ofs, uint64_t len);
        int (*flash_is_locked)(struct spi_nor *nor, loff_t ofs, uint64_t len);
        void *priv;
    }

.. _`spi_nor.members`:

Members
-------

mtd
    point to a mtd_info structure

lock
    the lock for the read/write/erase/lock/unlock operations

dev
    point to a spi device, or a spi nor controller device.

page_size
    the page size of the SPI NOR

addr_width
    number of address bytes

erase_opcode
    the opcode for erasing a sector

read_opcode
    the read opcode

read_dummy
    the dummy needed by the read operation

program_opcode
    the program opcode

read_proto
    the SPI protocol for read operations

write_proto
    the SPI protocol for write operations
    \ ``reg_proto``\            the SPI protocol for read_reg/write_reg/erase operations

reg_proto
    *undescribed*

sst_write_second
    used by the SST write operation

flags
    flag options for the current SPI-NOR (SNOR_F\_\*)

cmd_buf
    used by the write_reg

prepare
    [OPTIONAL] do some preparations for the
    read/write/erase/lock/unlock operations

unprepare
    [OPTIONAL] do some post work after the
    read/write/erase/lock/unlock operations

read_reg
    [DRIVER-SPECIFIC] read out the register

write_reg
    [DRIVER-SPECIFIC] write data to the register

read
    [DRIVER-SPECIFIC] read data from the SPI NOR

write
    [DRIVER-SPECIFIC] write data to the SPI NOR

erase
    [DRIVER-SPECIFIC] erase a sector of the SPI NOR
    at the offset \ ``offs``\ ; if not provided by the driver,
    spi-nor will send the erase opcode via \ :c:func:`write_reg`\ 

flash_lock
    [FLASH-SPECIFIC] lock a region of the SPI NOR

flash_unlock
    [FLASH-SPECIFIC] unlock a region of the SPI NOR

flash_is_locked
    [FLASH-SPECIFIC] check if a region of the SPI NOR is
    completely locked

priv
    the private data

.. _`spi_nor_hwcaps`:

struct spi_nor_hwcaps
=====================

.. c:type:: struct spi_nor_hwcaps

    Structure for describing the hardware capabilies supported by the SPI controller (bus master).

.. _`spi_nor_hwcaps.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor_hwcaps {
        u32 mask;
    }

.. _`spi_nor_hwcaps.members`:

Members
-------

mask
    the bitmask listing all the supported hw capabilies

.. _`spi_nor_scan`:

spi_nor_scan
============

.. c:function:: int spi_nor_scan(struct spi_nor *nor, const char *name, const struct spi_nor_hwcaps *hwcaps)

    scan the SPI NOR

    :param struct spi_nor \*nor:
        the spi_nor structure

    :param const char \*name:
        the chip type name

    :param const struct spi_nor_hwcaps \*hwcaps:
        the hardware capabilities supported by the controller driver

.. _`spi_nor_scan.description`:

Description
-----------

The drivers can use this fuction to scan the SPI NOR.
In the scanning, it will try to get all the necessary information to
fill the mtd_info{} and the spi_nor{}.

The chip type name can be provided through the \ ``name``\  parameter.

.. _`spi_nor_scan.return`:

Return
------

0 for success, others for failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/spi-nor.h

.. _`spi_nor_erase_type`:

struct spi_nor_erase_type
=========================

.. c:type:: struct spi_nor_erase_type

    Structure to describe a SPI NOR erase type

.. _`spi_nor_erase_type.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor_erase_type {
        u32 size;
        u32 size_shift;
        u32 size_mask;
        u8 opcode;
        u8 idx;
    }

.. _`spi_nor_erase_type.members`:

Members
-------

size
    the size of the sector/block erased by the erase type.
    JEDEC JESD216B imposes erase sizes to be a power of 2.

size_shift
    \ ``size``\  is a power of 2, the shift is stored in
    \ ``size_shift``\ .

size_mask
    the size mask based on \ ``size_shift``\ .

opcode
    the SPI command op code to erase the sector/block.

idx
    Erase Type index as sorted in the Basic Flash Parameter
    Table. It will be used to synchronize the supported
    Erase Types with the ones identified in the SFDP
    optional tables.

.. _`spi_nor_erase_command`:

struct spi_nor_erase_command
============================

.. c:type:: struct spi_nor_erase_command

    Used for non-uniform erases The structure is used to describe a list of erase commands to be executed once we validate that the erase can be performed. The elements in the list are run-length encoded.

.. _`spi_nor_erase_command.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor_erase_command {
        struct list_head list;
        u32 count;
        u32 size;
        u8 opcode;
    }

.. _`spi_nor_erase_command.members`:

Members
-------

list
    for inclusion into the list of erase commands.

count
    how many times the same erase command should be
    consecutively used.

size
    the size of the sector/block erased by the command.

opcode
    the SPI command op code to erase the sector/block.

.. _`spi_nor_erase_region`:

struct spi_nor_erase_region
===========================

.. c:type:: struct spi_nor_erase_region

    Structure to describe a SPI NOR erase region

.. _`spi_nor_erase_region.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor_erase_region {
        u64 offset;
        u64 size;
    }

.. _`spi_nor_erase_region.members`:

Members
-------

offset
    the offset in the data array of erase region start.
    LSB bits are used as a bitmask encoding flags to
    determine if this region is overlaid, if this region is
    the last in the SPI NOR flash memory and to indicate
    all the supported erase commands inside this region.
    The erase types are sorted in ascending order with the
    smallest Erase Type size being at BIT(0).

size
    the size of the region in bytes.

.. _`spi_nor_erase_map`:

struct spi_nor_erase_map
========================

.. c:type:: struct spi_nor_erase_map

    Structure to describe the SPI NOR erase map

.. _`spi_nor_erase_map.definition`:

Definition
----------

.. code-block:: c

    struct spi_nor_erase_map {
        struct spi_nor_erase_region *regions;
        struct spi_nor_erase_region uniform_region;
        struct spi_nor_erase_type erase_type[SNOR_ERASE_TYPE_MAX];
        u8 uniform_erase_type;
    }

.. _`spi_nor_erase_map.members`:

Members
-------

regions
    array of erase regions. The regions are consecutive in
    address space. Walking through the regions is done
    incrementally.

uniform_region
    a pre-allocated erase region for SPI NOR with a uniform
    sector size (legacy implementation).

erase_type
    an array of erase types shared by all the regions.
    The erase types are sorted in ascending order, with the
    smallest Erase Type size being the first member in the
    erase_type array.

uniform_erase_type
    bitmask encoding erase types that can erase the
    entire memory. This member is completed at init by
    uniform and non-uniform SPI NOR flash memories if they
    support at least one erase type that can erase the
    entire memory.

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
        const struct flash_info *info;
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
        struct spi_nor_erase_map erase_map;
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
        int (*quad_enable)(struct spi_nor *nor);
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

info
    spi-nor part JDEC MFR id and other info

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

erase_map
    the erase map of the SPI NOR

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

quad_enable
    [FLASH-SPECIFIC] enables SPI NOR quad mode
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

    :param nor:
        the spi_nor structure
    :type nor: struct spi_nor \*

    :param name:
        the chip type name
    :type name: const char \*

    :param hwcaps:
        the hardware capabilities supported by the controller driver
    :type hwcaps: const struct spi_nor_hwcaps \*

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

.. _`spi_nor_restore`:

spi_nor_restore
===============

.. c:function:: void spi_nor_restore(struct spi_nor *nor)

    restore the status of SPI NOR

    :param nor:
        the spi_nor structure
    :type nor: struct spi_nor \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/onenand.h

.. _`onenand_bufferram`:

struct onenand_bufferram
========================

.. c:type:: struct onenand_bufferram

    OneNAND BufferRAM Data

.. _`onenand_bufferram.definition`:

Definition
----------

.. code-block:: c

    struct onenand_bufferram {
        int blockpage;
    }

.. _`onenand_bufferram.members`:

Members
-------

blockpage
    block & page address in BufferRAM

.. _`onenand_chip`:

struct onenand_chip
===================

.. c:type:: struct onenand_chip

    OneNAND Private Flash Chip Data

.. _`onenand_chip.definition`:

Definition
----------

.. code-block:: c

    struct onenand_chip {
        void __iomem *base;
        unsigned dies;
        unsigned boundary[MAX_DIES];
        loff_t diesize[MAX_DIES];
        unsigned int chipsize;
        unsigned int device_id;
        unsigned int version_id;
        unsigned int technology;
        unsigned int density_mask;
        unsigned int options;
        unsigned int erase_shift;
        unsigned int page_shift;
        unsigned int page_mask;
        unsigned int writesize;
        unsigned int bufferram_index;
        struct onenand_bufferram bufferram[MAX_BUFFERRAM];
        int (*command)(struct mtd_info *mtd, int cmd, loff_t address, size_t len);
        int (*wait)(struct mtd_info *mtd, int state);
        int (*bbt_wait)(struct mtd_info *mtd, int state);
        void (*unlock_all)(struct mtd_info *mtd);
        int (*read_bufferram)(struct mtd_info *mtd, int area, unsigned char *buffer, int offset, size_t count);
        int (*write_bufferram)(struct mtd_info *mtd, int area, const unsigned char *buffer, int offset, size_t count);
        unsigned short (*read_word)(void __iomem *addr);
        void (*write_word)(unsigned short value, void __iomem *addr);
        void (*mmcontrol)(struct mtd_info *mtd, int sync_read);
        int (*chip_probe)(struct mtd_info *mtd);
        int (*block_markbad)(struct mtd_info *mtd, loff_t ofs);
        int (*scan_bbt)(struct mtd_info *mtd);
        int (*enable)(struct mtd_info *mtd);
        int (*disable)(struct mtd_info *mtd);
        struct completion complete;
        int irq;
        spinlock_t chip_lock;
        wait_queue_head_t wq;
        flstate_t state;
        unsigned char *page_buf;
        unsigned char *oob_buf;
    #ifdef CONFIG_MTD_ONENAND_VERIFY_WRITE
        unsigned char *verify_buf;
    #endif
        int subpagesize;
        void *bbm;
        void *priv;
        unsigned int ongoing;
    }

.. _`onenand_chip.members`:

Members
-------

base
    [BOARDSPECIFIC] address to access OneNAND

dies
    [INTERN][FLEX-ONENAND] number of dies on chip

boundary
    [INTERN][FLEX-ONENAND] Boundary of the dies

diesize
    [INTERN][FLEX-ONENAND] Size of the dies

chipsize
    [INTERN] the size of one chip for multichip arrays
    FIXME For Flex-OneNAND, chipsize holds maximum possible
    device size ie when all blocks are considered MLC

device_id
    [INTERN] device ID

version_id
    *undescribed*

technology
    *undescribed*

density_mask
    chip density, used for DDP devices

options
    [BOARDSPECIFIC] various chip options. They can
    partly be set to inform onenand_scan about

erase_shift
    [INTERN] number of address bits in a block

page_shift
    [INTERN] number of address bits in a page

page_mask
    [INTERN] a page per block mask

writesize
    [INTERN] a real page size

bufferram_index
    [INTERN] BufferRAM index

bufferram
    [INTERN] BufferRAM info

command
    [REPLACEABLE] hardware specific function for writing
    commands to the chip

wait
    [REPLACEABLE] hardware specific function for wait on ready

bbt_wait
    [REPLACEABLE] hardware specific function for bbt wait on ready

unlock_all
    [REPLACEABLE] hardware specific function for unlock all

read_bufferram
    [REPLACEABLE] hardware specific function for BufferRAM Area

write_bufferram
    [REPLACEABLE] hardware specific function for BufferRAM Area

read_word
    [REPLACEABLE] hardware specific function for read
    register of OneNAND

write_word
    [REPLACEABLE] hardware specific function for write
    register of OneNAND

mmcontrol
    sync burst read function

chip_probe
    [REPLACEABLE] hardware specific function for chip probe

block_markbad
    function to mark a block as bad

scan_bbt
    [REPLACEALBE] hardware specific function for scanning
    Bad block Table

enable
    *undescribed*

disable
    *undescribed*

complete
    *undescribed*

irq
    *undescribed*

chip_lock
    [INTERN] spinlock used to protect access to this
    structure and the chip

wq
    [INTERN] wait queue to sleep on if a OneNAND
    operation is in progress

state
    [INTERN] the current state of the OneNAND device

page_buf
    [INTERN] page main data buffer

oob_buf
    [INTERN] page oob data buffer

verify_buf
    *undescribed*

subpagesize
    [INTERN] holds the subpagesize

bbm
    [REPLACEABLE] pointer to Bad Block Management

priv
    [OPTIONAL] pointer to private chip date

ongoing
    *undescribed*

.. _`onenand_manufacturers`:

struct onenand_manufacturers
============================

.. c:type:: struct onenand_manufacturers

    NAND Flash Manufacturer ID Structure

.. _`onenand_manufacturers.definition`:

Definition
----------

.. code-block:: c

    struct onenand_manufacturers {
        int id;
        char *name;
    }

.. _`onenand_manufacturers.members`:

Members
-------

id
    manufacturer ID code of device.

name
    Manufacturer name

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/devices/docg3.h

.. _`docg3_cascade`:

struct docg3_cascade
====================

.. c:type:: struct docg3_cascade

    Cascade of 1 to 4 docg3 chips

.. _`docg3_cascade.definition`:

Definition
----------

.. code-block:: c

    struct docg3_cascade {
        struct mtd_info  *floors[DOC_MAX_NBFLOORS];
        void __iomem *base;
        struct bch_control *bch;
        struct mutex lock;
    }

.. _`docg3_cascade.members`:

Members
-------

floors
    floors (ie. one physical docg3 chip is one floor)

base
    IO space to access all chips in the cascade

bch
    the BCH correcting control structure

lock
    lock to protect docg3 IO space from concurrent accesses

.. _`docg3`:

struct docg3
============

.. c:type:: struct docg3

    DiskOnChip driver private data

.. _`docg3.definition`:

Definition
----------

.. code-block:: c

    struct docg3 {
        struct device *dev;
        struct docg3_cascade *cascade;
        unsigned int device_id:4;
        unsigned int if_cfg:1;
        unsigned int reliable:2;
        int max_block;
        u8 *bbt;
        loff_t oob_write_ofs;
        int oob_autoecc;
        u8 oob_write_buf[DOC_LAYOUT_OOB_SIZE];
        struct dentry *debugfs_root;
    }

.. _`docg3.members`:

Members
-------

dev
    the device currently under control

cascade
    the cascade this device belongs to

device_id
    number of the cascaded DoCG3 device (0, 1, 2 or 3)

if_cfg
    if true, reads are on 16bits, else reads are on 8bits

reliable
    if 0, docg3 in normal mode, if 1 docg3 in fast mode, if 2 in
    reliable mode
    Fast mode implies more errors than normal mode.
    Reliable mode implies that page 2\*n and 2\*n+1 are clones.

max_block
    *undescribed*

bbt
    bad block table cache

oob_write_ofs
    offset of the MTD where this OOB should belong (ie. in next
    page_write)

oob_autoecc
    if 1, use only bytes 0-7, 15, and fill the others with HW ECC
    if 0, use all the 16 bytes.

oob_write_buf
    prepared OOB for next page_write

debugfs_root
    debugfs root node

.. This file was automatic generated / don't edit.


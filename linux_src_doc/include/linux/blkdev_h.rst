.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blkdev.h

.. _`blk_dax_ctl`:

struct blk_dax_ctl
==================

.. c:type:: struct blk_dax_ctl

    control and output parameters for ->direct_access

.. _`blk_dax_ctl.definition`:

Definition
----------

.. code-block:: c

    struct blk_dax_ctl {
        sector_t sector;
        void *addr;
        long size;
        pfn_t pfn;
    }

.. _`blk_dax_ctl.members`:

Members
-------

sector
    (input) offset relative to a block_device

addr
    (output) kernel virtual address for \ ``sector``\  populated by driver

size
    (input) number of bytes requested

pfn
    (output) page frame number for \ ``addr``\  populated by driver

.. This file was automatic generated / don't edit.


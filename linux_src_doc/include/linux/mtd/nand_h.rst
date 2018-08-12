.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/nand.h

.. _`nand_memory_organization`:

struct nand_memory_organization
===============================

.. c:type:: struct nand_memory_organization

    Memory organization structure

.. _`nand_memory_organization.definition`:

Definition
----------

.. code-block:: c

    struct nand_memory_organization {
        unsigned int bits_per_cell;
        unsigned int pagesize;
        unsigned int oobsize;
        unsigned int pages_per_eraseblock;
        unsigned int eraseblocks_per_lun;
        unsigned int planes_per_lun;
        unsigned int luns_per_target;
        unsigned int ntargets;
    }

.. _`nand_memory_organization.members`:

Members
-------

bits_per_cell
    number of bits per NAND cell

pagesize
    page size

oobsize
    OOB area size

pages_per_eraseblock
    number of pages per eraseblock

eraseblocks_per_lun
    number of eraseblocks per LUN (Logical Unit Number)

planes_per_lun
    number of planes per LUN

luns_per_target
    number of LUN per target (target is a synonym for die)

ntargets
    total number of targets exposed by the NAND device

.. _`nand_row_converter`:

struct nand_row_converter
=========================

.. c:type:: struct nand_row_converter

    Information needed to convert an absolute offset into a row address

.. _`nand_row_converter.definition`:

Definition
----------

.. code-block:: c

    struct nand_row_converter {
        unsigned int lun_addr_shift;
        unsigned int eraseblock_addr_shift;
    }

.. _`nand_row_converter.members`:

Members
-------

lun_addr_shift
    position of the LUN identifier in the row address

eraseblock_addr_shift
    position of the eraseblock identifier in the row
    address

.. _`nand_pos`:

struct nand_pos
===============

.. c:type:: struct nand_pos

    NAND position object

.. _`nand_pos.definition`:

Definition
----------

.. code-block:: c

    struct nand_pos {
        unsigned int target;
        unsigned int lun;
        unsigned int plane;
        unsigned int eraseblock;
        unsigned int page;
    }

.. _`nand_pos.members`:

Members
-------

target
    the NAND target/die

lun
    the LUN identifier

plane
    the plane within the LUN

eraseblock
    the eraseblock within the LUN

page
    the page within the LUN

.. _`nand_pos.description`:

Description
-----------

These information are usually used by specific sub-layers to select the
appropriate target/die and generate a row address to pass to the device.

.. _`nand_page_io_req`:

struct nand_page_io_req
=======================

.. c:type:: struct nand_page_io_req

    NAND I/O request object

.. _`nand_page_io_req.definition`:

Definition
----------

.. code-block:: c

    struct nand_page_io_req {
        struct nand_pos pos;
        unsigned int dataoffs;
        unsigned int datalen;
        union {
            const void *out;
            void *in;
        } databuf;
        unsigned int ooboffs;
        unsigned int ooblen;
        union {
            const void *out;
            void *in;
        } oobbuf;
        int mode;
    }

.. _`nand_page_io_req.members`:

Members
-------

pos
    the position this I/O request is targeting

dataoffs
    the offset within the page

datalen
    number of data bytes to read from/write to this page

databuf
    buffer to store data in or get data from

ooboffs
    the OOB offset within the page

ooblen
    the number of OOB bytes to read from/write to this page

oobbuf
    buffer to store OOB data in or get OOB data from

mode
    one of the \ ``MTD_OPS_XXX``\  mode

.. _`nand_page_io_req.description`:

Description
-----------

This object is used to pass per-page I/O requests to NAND sub-layers. This
way all useful information are already formatted in a useful way and
specific NAND layers can focus on translating these information into
specific commands/operations.

.. _`nand_ecc_req`:

struct nand_ecc_req
===================

.. c:type:: struct nand_ecc_req

    NAND ECC requirements

.. _`nand_ecc_req.definition`:

Definition
----------

.. code-block:: c

    struct nand_ecc_req {
        unsigned int strength;
        unsigned int step_size;
    }

.. _`nand_ecc_req.members`:

Members
-------

strength
    ECC strength

step_size
    ECC step/block size

.. _`nand_bbt`:

struct nand_bbt
===============

.. c:type:: struct nand_bbt

    bad block table object

.. _`nand_bbt.definition`:

Definition
----------

.. code-block:: c

    struct nand_bbt {
        unsigned long *cache;
    }

.. _`nand_bbt.members`:

Members
-------

cache
    in memory BBT cache

.. _`nand_ops`:

struct nand_ops
===============

.. c:type:: struct nand_ops

    NAND operations

.. _`nand_ops.definition`:

Definition
----------

.. code-block:: c

    struct nand_ops {
        int (*erase)(struct nand_device *nand, const struct nand_pos *pos);
        int (*markbad)(struct nand_device *nand, const struct nand_pos *pos);
        bool (*isbad)(struct nand_device *nand, const struct nand_pos *pos);
    }

.. _`nand_ops.members`:

Members
-------

erase
    erase a specific block. No need to check if the block is bad before
    erasing, this has been taken care of by the generic NAND layer

markbad
    mark a specific block bad. No need to check if the block is
    already marked bad, this has been taken care of by the generic
    NAND layer. This method should just write the BBM (Bad Block
    Marker) so that future call to struct_nand_ops->isbad() return
    true

isbad
    check whether a block is bad or not. This method should just read
    the BBM and return whether the block is bad or not based on what it
    reads

.. _`nand_ops.description`:

Description
-----------

These are all low level operations that should be implemented by specialized
NAND layers (SPI NAND, raw NAND, ...).

.. _`nand_device`:

struct nand_device
==================

.. c:type:: struct nand_device

    NAND device

.. _`nand_device.definition`:

Definition
----------

.. code-block:: c

    struct nand_device {
        struct mtd_info mtd;
        struct nand_memory_organization memorg;
        struct nand_ecc_req eccreq;
        struct nand_row_converter rowconv;
        struct nand_bbt bbt;
        const struct nand_ops *ops;
    }

.. _`nand_device.members`:

Members
-------

mtd
    MTD instance attached to the NAND device

memorg
    memory layout

eccreq
    ECC requirements

rowconv
    position to row address converter

bbt
    bad block table info

ops
    NAND operations attached to the NAND device

.. _`nand_device.description`:

Description
-----------

Generic NAND object. Specialized NAND layers (raw NAND, SPI NAND, OneNAND)
should declare their own NAND object embedding a nand_device struct (that's
how inheritance is done).
struct_nand_device->memorg and struct_nand_device->eccreq should be filled
at device detection time to reflect the NAND device
capabilities/requirements. Once this is done \ :c:func:`nanddev_init`\  can be called.
It will take care of converting NAND information into MTD ones, which means
the specialized NAND layers should never manually tweak
struct_nand_device->mtd except for the ->_read/write() hooks.

.. _`nand_io_iter`:

struct nand_io_iter
===================

.. c:type:: struct nand_io_iter

    NAND I/O iterator

.. _`nand_io_iter.definition`:

Definition
----------

.. code-block:: c

    struct nand_io_iter {
        struct nand_page_io_req req;
        unsigned int oobbytes_per_page;
        unsigned int dataleft;
        unsigned int oobleft;
    }

.. _`nand_io_iter.members`:

Members
-------

req
    current I/O request

oobbytes_per_page
    maximum number of OOB bytes per page

dataleft
    remaining number of data bytes to read/write

oobleft
    remaining number of OOB bytes to read/write

.. _`nand_io_iter.description`:

Description
-----------

Can be used by specialized NAND layers to iterate over all pages covered
by an MTD I/O request, which should greatly simplifies the boiler-plate
code needed to read/write data from/to a NAND device.

.. _`mtd_to_nanddev`:

mtd_to_nanddev
==============

.. c:function:: struct nand_device *mtd_to_nanddev(struct mtd_info *mtd)

    Get the NAND device attached to the MTD instance

    :param struct mtd_info \*mtd:
        MTD instance

.. _`mtd_to_nanddev.return`:

Return
------

the NAND device embedding \ ``mtd``\ .

.. _`nanddev_to_mtd`:

nanddev_to_mtd
==============

.. c:function:: struct mtd_info *nanddev_to_mtd(struct nand_device *nand)

    Get the MTD device attached to a NAND device

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_to_mtd.return`:

Return
------

the MTD device embedded in \ ``nand``\ .

.. _`nanddev_page_size`:

nanddev_page_size
=================

.. c:function:: size_t nanddev_page_size(const struct nand_device *nand)

    Get NAND page size

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_page_size.return`:

Return
------

the page size.

.. _`nanddev_per_page_oobsize`:

nanddev_per_page_oobsize
========================

.. c:function:: unsigned int nanddev_per_page_oobsize(const struct nand_device *nand)

    Get NAND OOB size

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_per_page_oobsize.return`:

Return
------

the OOB size.

.. _`nanddev_pages_per_eraseblock`:

nanddev_pages_per_eraseblock
============================

.. c:function:: unsigned int nanddev_pages_per_eraseblock(const struct nand_device *nand)

    Get the number of pages per eraseblock

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_pages_per_eraseblock.return`:

Return
------

the number of pages per eraseblock.

.. _`nanddev_eraseblock_size`:

nanddev_eraseblock_size
=======================

.. c:function:: size_t nanddev_eraseblock_size(const struct nand_device *nand)

    Get NAND erase block size

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_eraseblock_size.return`:

Return
------

the eraseblock size.

.. _`nanddev_eraseblocks_per_lun`:

nanddev_eraseblocks_per_lun
===========================

.. c:function:: unsigned int nanddev_eraseblocks_per_lun(const struct nand_device *nand)

    Get the number of eraseblocks per LUN

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_eraseblocks_per_lun.return`:

Return
------

the number of eraseblocks per LUN.

.. _`nanddev_target_size`:

nanddev_target_size
===================

.. c:function:: u64 nanddev_target_size(const struct nand_device *nand)

    Get the total size provided by a single target/die

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_target_size.return`:

Return
------

the total size exposed by a single target/die in bytes.

.. _`nanddev_ntargets`:

nanddev_ntargets
================

.. c:function:: unsigned int nanddev_ntargets(const struct nand_device *nand)

    Get the total of targets

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_ntargets.return`:

Return
------

the number of targets/dies exposed by \ ``nand``\ .

.. _`nanddev_neraseblocks`:

nanddev_neraseblocks
====================

.. c:function:: unsigned int nanddev_neraseblocks(const struct nand_device *nand)

    Get the total number of erasablocks

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_neraseblocks.return`:

Return
------

the total number of eraseblocks exposed by \ ``nand``\ .

.. _`nanddev_size`:

nanddev_size
============

.. c:function:: u64 nanddev_size(const struct nand_device *nand)

    Get NAND size

    :param const struct nand_device \*nand:
        NAND device

.. _`nanddev_size.return`:

Return
------

the total size (in bytes) exposed by \ ``nand``\ .

.. _`nanddev_get_memorg`:

nanddev_get_memorg
==================

.. c:function:: struct nand_memory_organization *nanddev_get_memorg(struct nand_device *nand)

    Extract memory organization info from a NAND device

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_get_memorg.description`:

Description
-----------

This can be used by the upper layer to fill the memorg info before calling
\ :c:func:`nanddev_init`\ .

.. _`nanddev_get_memorg.return`:

Return
------

the memorg object embedded in the NAND device.

.. _`nanddev_register`:

nanddev_register
================

.. c:function:: int nanddev_register(struct nand_device *nand)

    Register a NAND device

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_register.description`:

Description
-----------

Register a NAND device.
This function is just a wrapper around \ :c:func:`mtd_device_register`\ 
registering the MTD device embedded in \ ``nand``\ .

.. _`nanddev_register.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_unregister`:

nanddev_unregister
==================

.. c:function:: int nanddev_unregister(struct nand_device *nand)

    Unregister a NAND device

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_unregister.description`:

Description
-----------

Unregister a NAND device.
This function is just a wrapper around \ :c:func:`mtd_device_unregister`\ 
unregistering the MTD device embedded in \ ``nand``\ .

.. _`nanddev_unregister.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_set_of_node`:

nanddev_set_of_node
===================

.. c:function:: void nanddev_set_of_node(struct nand_device *nand, struct device_node *np)

    Attach a DT node to a NAND device

    :param struct nand_device \*nand:
        NAND device

    :param struct device_node \*np:
        DT node

.. _`nanddev_set_of_node.description`:

Description
-----------

Attach a DT node to a NAND device.

.. _`nanddev_get_of_node`:

nanddev_get_of_node
===================

.. c:function:: struct device_node *nanddev_get_of_node(struct nand_device *nand)

    Retrieve the DT node attached to a NAND device

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_get_of_node.return`:

Return
------

the DT node attached to \ ``nand``\ .

.. _`nanddev_offs_to_pos`:

nanddev_offs_to_pos
===================

.. c:function:: unsigned int nanddev_offs_to_pos(struct nand_device *nand, loff_t offs, struct nand_pos *pos)

    Convert an absolute NAND offset into a NAND position

    :param struct nand_device \*nand:
        NAND device

    :param loff_t offs:
        absolute NAND offset (usually passed by the MTD layer)

    :param struct nand_pos \*pos:
        a NAND position object to fill in

.. _`nanddev_offs_to_pos.description`:

Description
-----------

Converts \ ``offs``\  into a nand_pos representation.

.. _`nanddev_offs_to_pos.return`:

Return
------

the offset within the NAND page pointed by \ ``pos``\ .

.. _`nanddev_pos_cmp`:

nanddev_pos_cmp
===============

.. c:function:: int nanddev_pos_cmp(const struct nand_pos *a, const struct nand_pos *b)

    Compare two NAND positions

    :param const struct nand_pos \*a:
        First NAND position

    :param const struct nand_pos \*b:
        Second NAND position

.. _`nanddev_pos_cmp.description`:

Description
-----------

Compares two NAND positions.

.. _`nanddev_pos_cmp.return`:

Return
------

-1 if \ ``a``\  < \ ``b``\ , 0 if \ ``a``\  == \ ``b``\  and 1 if \ ``a``\  > \ ``b``\ .

.. _`nanddev_pos_to_offs`:

nanddev_pos_to_offs
===================

.. c:function:: loff_t nanddev_pos_to_offs(struct nand_device *nand, const struct nand_pos *pos)

    Convert a NAND position into an absolute offset

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        the NAND position to convert

.. _`nanddev_pos_to_offs.description`:

Description
-----------

Converts \ ``pos``\  NAND position into an absolute offset.

.. _`nanddev_pos_to_offs.return`:

Return
------

the absolute offset. Note that \ ``pos``\  points to the beginning of a
page, if one wants to point to a specific offset within this page
the returned offset has to be adjusted manually.

.. _`nanddev_pos_to_row`:

nanddev_pos_to_row
==================

.. c:function:: unsigned int nanddev_pos_to_row(struct nand_device *nand, const struct nand_pos *pos)

    Extract a row address from a NAND position

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        the position to convert

.. _`nanddev_pos_to_row.description`:

Description
-----------

Converts a NAND position into a row address that can then be passed to the
device.

.. _`nanddev_pos_to_row.return`:

Return
------

the row address extracted from \ ``pos``\ .

.. _`nanddev_pos_next_target`:

nanddev_pos_next_target
=======================

.. c:function:: void nanddev_pos_next_target(struct nand_device *nand, struct nand_pos *pos)

    Move a position to the next target/die

    :param struct nand_device \*nand:
        NAND device

    :param struct nand_pos \*pos:
        the position to update

.. _`nanddev_pos_next_target.description`:

Description
-----------

Updates \ ``pos``\  to point to the start of the next target/die. Useful when you
want to iterate over all targets/dies of a NAND device.

.. _`nanddev_pos_next_lun`:

nanddev_pos_next_lun
====================

.. c:function:: void nanddev_pos_next_lun(struct nand_device *nand, struct nand_pos *pos)

    Move a position to the next LUN

    :param struct nand_device \*nand:
        NAND device

    :param struct nand_pos \*pos:
        the position to update

.. _`nanddev_pos_next_lun.description`:

Description
-----------

Updates \ ``pos``\  to point to the start of the next LUN. Useful when you want to
iterate over all LUNs of a NAND device.

.. _`nanddev_pos_next_eraseblock`:

nanddev_pos_next_eraseblock
===========================

.. c:function:: void nanddev_pos_next_eraseblock(struct nand_device *nand, struct nand_pos *pos)

    Move a position to the next eraseblock

    :param struct nand_device \*nand:
        NAND device

    :param struct nand_pos \*pos:
        the position to update

.. _`nanddev_pos_next_eraseblock.description`:

Description
-----------

Updates \ ``pos``\  to point to the start of the next eraseblock. Useful when you
want to iterate over all eraseblocks of a NAND device.

.. _`nanddev_pos_next_page`:

nanddev_pos_next_page
=====================

.. c:function:: void nanddev_pos_next_page(struct nand_device *nand, struct nand_pos *pos)

    Move a position to the next page

    :param struct nand_device \*nand:
        NAND device

    :param struct nand_pos \*pos:
        the position to update

.. _`nanddev_pos_next_page.description`:

Description
-----------

Updates \ ``pos``\  to point to the start of the next page. Useful when you want to
iterate over all pages of a NAND device.

.. _`nanddev_io_iter_init`:

nanddev_io_iter_init
====================

.. c:function:: void nanddev_io_iter_init(struct nand_device *nand, loff_t offs, struct mtd_oob_ops *req, struct nand_io_iter *iter)

    Initialize a NAND I/O iterator

    :param struct nand_device \*nand:
        NAND device

    :param loff_t offs:
        absolute offset

    :param struct mtd_oob_ops \*req:
        MTD request

    :param struct nand_io_iter \*iter:
        NAND I/O iterator

.. _`nanddev_io_iter_init.description`:

Description
-----------

Initializes a NAND iterator based on the information passed by the MTD
layer.

.. _`nanddev_io_iter_next_page`:

nanddev_io_iter_next_page
=========================

.. c:function:: void nanddev_io_iter_next_page(struct nand_device *nand, struct nand_io_iter *iter)

    Move to the next page

    :param struct nand_device \*nand:
        NAND device

    :param struct nand_io_iter \*iter:
        NAND I/O iterator

.. _`nanddev_io_iter_next_page.description`:

Description
-----------

Updates the \ ``iter``\  to point to the next page.

.. _`nanddev_io_iter_end`:

nanddev_io_iter_end
===================

.. c:function:: bool nanddev_io_iter_end(struct nand_device *nand, const struct nand_io_iter *iter)

    Should end iteration or not

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_io_iter \*iter:
        NAND I/O iterator

.. _`nanddev_io_iter_end.description`:

Description
-----------

Check whether \ ``iter``\  has reached the end of the NAND portion it was asked to
iterate on or not.

.. _`nanddev_io_iter_end.return`:

Return
------

true if \ ``iter``\  has reached the end of the iteration request, false
otherwise.

.. _`nanddev_io_for_each_page`:

nanddev_io_for_each_page
========================

.. c:function::  nanddev_io_for_each_page( nand,  start,  req,  iter)

    Iterate over all NAND pages contained in an MTD I/O request

    :param  nand:
        NAND device

    :param  start:
        start address to read/write from

    :param  req:
        MTD I/O request

    :param  iter:
        NAND I/O iterator

.. _`nanddev_io_for_each_page.description`:

Description
-----------

Should be used for iterate over pages that are contained in an MTD request.

.. _`nanddev_bbt_pos_to_entry`:

nanddev_bbt_pos_to_entry
========================

.. c:function:: unsigned int nanddev_bbt_pos_to_entry(struct nand_device *nand, const struct nand_pos *pos)

    Convert a NAND position into a BBT entry

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        the NAND position we want to get BBT entry for

.. _`nanddev_bbt_pos_to_entry.description`:

Description
-----------

Return the BBT entry used to store information about the eraseblock pointed
by \ ``pos``\ .

.. _`nanddev_bbt_pos_to_entry.return`:

Return
------

the BBT entry storing information about eraseblock pointed by \ ``pos``\ .

.. _`nanddev_bbt_is_initialized`:

nanddev_bbt_is_initialized
==========================

.. c:function:: bool nanddev_bbt_is_initialized(struct nand_device *nand)

    Check if the BBT has been initialized

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_bbt_is_initialized.return`:

Return
------

true if the BBT has been initialized, false otherwise.

.. This file was automatic generated / don't edit.


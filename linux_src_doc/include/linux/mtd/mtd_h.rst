.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/mtd.h

.. _`mtd_oob_ops`:

struct mtd_oob_ops
==================

.. c:type:: struct mtd_oob_ops

    oob operation operands

.. _`mtd_oob_ops.definition`:

Definition
----------

.. code-block:: c

    struct mtd_oob_ops {
        unsigned int mode;
        size_t len;
        size_t retlen;
        size_t ooblen;
        size_t oobretlen;
        uint32_t ooboffs;
        uint8_t *datbuf;
        uint8_t *oobbuf;
    }

.. _`mtd_oob_ops.members`:

Members
-------

mode
    operation mode

len
    number of data bytes to write/read

retlen
    number of data bytes written/read

ooblen
    number of oob bytes to write/read

oobretlen
    number of oob bytes written/read

ooboffs
    offset of oob data in the oob area (only relevant when
    mode = MTD_OPS_PLACE_OOB or MTD_OPS_RAW)

datbuf
    data buffer - if NULL only oob data are read/written

oobbuf
    oob data buffer

.. _`mtd_oob_ops.description`:

Description
-----------

Note, it is allowed to read more than one OOB area at one go, but not write.
The interface assumes that the OOB write requests program only one page's
OOB area.

.. _`mtd_oob_region`:

struct mtd_oob_region
=====================

.. c:type:: struct mtd_oob_region

    oob region definition

.. _`mtd_oob_region.definition`:

Definition
----------

.. code-block:: c

    struct mtd_oob_region {
        u32 offset;
        u32 length;
    }

.. _`mtd_oob_region.members`:

Members
-------

offset
    region offset

length
    region length

.. _`mtd_oob_region.description`:

Description
-----------

This structure describes a region of the OOB area, and is used
to retrieve ECC or free bytes sections.
Each section is defined by an offset within the OOB area and a
length.

.. _`mtd_pairing_info`:

struct mtd_pairing_info
=======================

.. c:type:: struct mtd_pairing_info

    page pairing information

.. _`mtd_pairing_info.definition`:

Definition
----------

.. code-block:: c

    struct mtd_pairing_info {
        int pair;
        int group;
    }

.. _`mtd_pairing_info.members`:

Members
-------

pair
    pair id

group
    group id

.. _`mtd_pairing_info.description`:

Description
-----------

The term "pair" is used here, even though TLC NANDs might group pages by 3
(3 bits in a single cell). A pair should regroup all pages that are sharing
the same cell. Pairs are then indexed in ascending order.

\ ``group``\  is defining the position of a page in a given pair. It can also be

.. _`mtd_pairing_info.seen-as-the-bit-position-in-the-cell`:

seen as the bit position in the cell
------------------------------------

page attached to bit 0 belongs to
group 0, page attached to bit 1 belongs to group 1, etc.

.. _`mtd_pairing_info.example`:

Example
-------

.. code-block:: c

    The H27UCG8T2BTR-BC datasheet describes the following pairing scheme:

                 group-0         group-1

     pair-0      page-0          page-4
     pair-1      page-1          page-5
     pair-2      page-2          page-8
     ...
     pair-127    page-251        page-255


    Note that the "group" and "pair" terms were extracted from Samsung and
    Hynix datasheets, and might be referenced under other names in other
    datasheets (Micron is describing this concept as "shared pages").


.. _`mtd_pairing_scheme`:

struct mtd_pairing_scheme
=========================

.. c:type:: struct mtd_pairing_scheme

    page pairing scheme description

.. _`mtd_pairing_scheme.definition`:

Definition
----------

.. code-block:: c

    struct mtd_pairing_scheme {
        int ngroups;
        int (*get_info)(struct mtd_info *mtd, int wunit, struct mtd_pairing_info *info);
        int (*get_wunit)(struct mtd_info *mtd, const struct mtd_pairing_info *info);
    }

.. _`mtd_pairing_scheme.members`:

Members
-------

ngroups
    number of groups. Should be related to the number of bits
    per cell.

get_info
    converts a write-unit (page number within an erase block) into
    mtd_pairing information (pair + group). This function should
    fill the info parameter based on the wunit index or return
    -EINVAL if the wunit parameter is invalid.

get_wunit
    converts pairing information into a write-unit (page) number.
    This function should return the wunit index pointed by the
    pairing information described in the info argument. It should
    return -EINVAL, if there's no wunit corresponding to the
    passed pairing information.

.. _`mtd_pairing_scheme.description`:

Description
-----------

See mtd_pairing_info documentation for a detailed explanation of the
pair and group concepts.

The mtd_pairing_scheme structure provides a generic solution to represent
NAND page pairing scheme. Instead of exposing two big tables to do the
write-unit <-> (pair + group) conversions, we ask the MTD drivers to
implement the ->get_info() and ->get_wunit() functions.

MTD users will then be able to query these information by using the
\ :c:func:`mtd_pairing_info_to_wunit`\  and \ :c:func:`mtd_wunit_to_pairing_info`\  helpers.

\ ``ngroups``\  is here to help MTD users iterating over all the pages in a
given pair. This value can be retrieved by MTD users using the
\ :c:func:`mtd_pairing_groups`\  helper.

Examples are given in the \ :c:func:`mtd_pairing_info_to_wunit`\  and
\ :c:func:`mtd_wunit_to_pairing_info`\  documentation.

.. _`mtd_debug_info`:

struct mtd_debug_info
=====================

.. c:type:: struct mtd_debug_info

    debugging information for an MTD device.

.. _`mtd_debug_info.definition`:

Definition
----------

.. code-block:: c

    struct mtd_debug_info {
        struct dentry *dfs_dir;
    }

.. _`mtd_debug_info.members`:

Members
-------

dfs_dir
    direntry object of the MTD device debugfs directory

.. _`mtd_align_erase_req`:

mtd_align_erase_req
===================

.. c:function:: void mtd_align_erase_req(struct mtd_info *mtd, struct erase_info *req)

    Adjust an erase request to align things on eraseblock boundaries.

    :param struct mtd_info \*mtd:
        the MTD device this erase request applies on

    :param struct erase_info \*req:
        the erase request to adjust

.. _`mtd_align_erase_req.description`:

Description
-----------

This function will adjust \ ``req``\ ->addr and \ ``req``\ ->len to align them on
\ ``mtd``\ ->erasesize. Of course we expect \ ``mtd``\ ->erasesize to be != 0.

.. This file was automatic generated / don't edit.


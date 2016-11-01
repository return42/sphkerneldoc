.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/nand_bbt.c

.. _`check_pattern`:

check_pattern
=============

.. c:function:: int check_pattern(uint8_t *buf, int len, int paglen, struct nand_bbt_descr *td)

    [GENERIC] check if a pattern is in the buffer

    :param uint8_t \*buf:
        the buffer to search

    :param int len:
        the length of buffer to search

    :param int paglen:
        the pagelength

    :param struct nand_bbt_descr \*td:
        search pattern descriptor

.. _`check_pattern.description`:

Description
-----------

Check for a pattern at the given place. Used to search bad block tables and
good / bad block identifiers.

.. _`check_short_pattern`:

check_short_pattern
===================

.. c:function:: int check_short_pattern(uint8_t *buf, struct nand_bbt_descr *td)

    [GENERIC] check if a pattern is in the buffer

    :param uint8_t \*buf:
        the buffer to search

    :param struct nand_bbt_descr \*td:
        search pattern descriptor

.. _`check_short_pattern.description`:

Description
-----------

Check for a pattern at the given place. Used to search bad block tables and
good / bad block identifiers. Same as check_pattern, but no optional empty
check.

.. _`add_marker_len`:

add_marker_len
==============

.. c:function:: u32 add_marker_len(struct nand_bbt_descr *td)

    compute the length of the marker in data area

    :param struct nand_bbt_descr \*td:
        BBT descriptor used for computation

.. _`add_marker_len.description`:

Description
-----------

The length will be 0 if the marker is located in OOB area.

.. _`read_bbt`:

read_bbt
========

.. c:function:: int read_bbt(struct mtd_info *mtd, uint8_t *buf, int page, int num, struct nand_bbt_descr *td, int offs)

    [GENERIC] Read the bad block table starting from page

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param int page:
        the starting page

    :param int num:
        the number of bbt descriptors to read

    :param struct nand_bbt_descr \*td:
        the bbt describtion table

    :param int offs:
        block number offset in the table

.. _`read_bbt.description`:

Description
-----------

Read the bad block table starting from page.

.. _`read_abs_bbt`:

read_abs_bbt
============

.. c:function:: int read_abs_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, int chip)

    [GENERIC] Read the bad block table starting at a given page

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*td:
        descriptor for the bad block table

    :param int chip:
        read the table for a specific chip, -1 read all chips; applies only if
        NAND_BBT_PERCHIP option is set

.. _`read_abs_bbt.description`:

Description
-----------

Read the bad block table for all chips starting at a given page. We assume
that the bbt bits are in consecutive order.

.. _`scan_read_oob`:

scan_read_oob
=============

.. c:function:: int scan_read_oob(struct mtd_info *mtd, uint8_t *buf, loff_t offs, size_t len)

    [GENERIC] Scan data+OOB region to buffer

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param loff_t offs:
        offset at which to scan

    :param size_t len:
        length of data region to read

.. _`scan_read_oob.description`:

Description
-----------

Scan read data from data+OOB. May traverse multiple pages, interleaving
page,OOB,page,OOB,... in buf. Completes transfer and returns the "strongest"
ECC condition (error or bitflip). May quit on the first (non-ECC) error.

.. _`read_abs_bbts`:

read_abs_bbts
=============

.. c:function:: void read_abs_bbts(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md)

    [GENERIC] Read the bad block table(s) for all chips starting at a given page

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*td:
        descriptor for the bad block table

    :param struct nand_bbt_descr \*md:
        descriptor for the bad block table mirror

.. _`read_abs_bbts.description`:

Description
-----------

Read the bad block table(s) for all chips starting at a given page. We
assume that the bbt bits are in consecutive order.

.. _`create_bbt`:

create_bbt
==========

.. c:function:: int create_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *bd, int chip)

    [GENERIC] Create a bad block table by scanning the device

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*bd:
        descriptor for the good/bad block search pattern

    :param int chip:
        create the table for a specific chip, -1 read all chips; applies only
        if NAND_BBT_PERCHIP option is set

.. _`create_bbt.description`:

Description
-----------

Create a bad block table by scanning the device for the given good/bad block
identify pattern.

.. _`search_bbt`:

search_bbt
==========

.. c:function:: int search_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td)

    [GENERIC] scan the device for a specific bad block table

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*td:
        descriptor for the bad block table

.. _`search_bbt.description`:

Description
-----------

Read the bad block table by searching for a given ident pattern. Search is
preformed either from the beginning up or from the end of the device
downwards. The search starts always at the start of a block. If the option
NAND_BBT_PERCHIP is given, each chip is searched for a bbt, which contains
the bad block information of this chip. This is necessary to provide support
for certain DOC devices.

The bbt ident pattern resides in the oob area of the first page in a block.

.. _`search_read_bbts`:

search_read_bbts
================

.. c:function:: void search_read_bbts(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md)

    [GENERIC] scan the device for bad block table(s)

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*td:
        descriptor for the bad block table

    :param struct nand_bbt_descr \*md:
        descriptor for the bad block table mirror

.. _`search_read_bbts.description`:

Description
-----------

Search and read the bad block table(s).

.. _`get_bbt_block`:

get_bbt_block
=============

.. c:function:: int get_bbt_block(struct nand_chip *this, struct nand_bbt_descr *td, struct nand_bbt_descr *md, int chip)

    Get the first valid eraseblock suitable to store a BBT

    :param struct nand_chip \*this:
        the NAND device

    :param struct nand_bbt_descr \*td:
        the BBT description

    :param struct nand_bbt_descr \*md:
        the mirror BBT descriptor

    :param int chip:
        the CHIP selector

.. _`get_bbt_block.description`:

Description
-----------

This functions returns a positive block number pointing a valid eraseblock
suitable to store a BBT (i.e. in the range reserved for BBT), or -ENOSPC if
all blocks are already used of marked bad. If td->pages[chip] was already
pointing to a valid block we re-use it, otherwise we search for the next
valid one.

.. _`mark_bbt_block_bad`:

mark_bbt_block_bad
==================

.. c:function:: void mark_bbt_block_bad(struct nand_chip *this, struct nand_bbt_descr *td, int chip, int block)

    Mark one of the block reserved for BBT bad

    :param struct nand_chip \*this:
        the NAND device

    :param struct nand_bbt_descr \*td:
        the BBT description

    :param int chip:
        the CHIP selector

    :param int block:
        the BBT block to mark

.. _`mark_bbt_block_bad.description`:

Description
-----------

Blocks reserved for BBT can become bad. This functions is an helper to mark
such blocks as bad. It takes care of updating the in-memory BBT, marking the
block as bad using a bad block marker and invalidating the associated
td->pages[] entry.

.. _`write_bbt`:

write_bbt
=========

.. c:function:: int write_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md, int chipsel)

    [GENERIC] (Re)write the bad block table

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*td:
        descriptor for the bad block table

    :param struct nand_bbt_descr \*md:
        descriptor for the bad block table mirror

    :param int chipsel:
        selector for a specific chip, -1 for all

.. _`write_bbt.description`:

Description
-----------

(Re)write the bad block table.

.. _`nand_memory_bbt`:

nand_memory_bbt
===============

.. c:function:: int nand_memory_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd)

    [GENERIC] create a memory based bad block table

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_bbt_descr \*bd:
        descriptor for the good/bad block search pattern

.. _`nand_memory_bbt.description`:

Description
-----------

The function creates a memory based bbt by scanning the device for
manufacturer / software marked good / bad blocks.

.. _`check_create`:

check_create
============

.. c:function:: int check_create(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *bd)

    [GENERIC] create and write bbt(s) if necessary

    :param struct mtd_info \*mtd:
        MTD device structure

    :param uint8_t \*buf:
        temporary buffer

    :param struct nand_bbt_descr \*bd:
        descriptor for the good/bad block search pattern

.. _`check_create.description`:

Description
-----------

The function checks the results of the previous call to read_bbt and creates
/ updates the bbt(s) if necessary. Creation is necessary if no bbt was found
for the chip/device. Update is necessary if one of the tables is missing or
the version nr. of one table is less than the other.

.. _`mark_bbt_region`:

mark_bbt_region
===============

.. c:function:: void mark_bbt_region(struct mtd_info *mtd, struct nand_bbt_descr *td)

    [GENERIC] mark the bad block table regions

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_bbt_descr \*td:
        bad block table descriptor

.. _`mark_bbt_region.description`:

Description
-----------

The bad block table regions are marked as "bad" to prevent accidental
erasures / writes. The regions are identified by the mark 0x02.

.. _`verify_bbt_descr`:

verify_bbt_descr
================

.. c:function:: void verify_bbt_descr(struct mtd_info *mtd, struct nand_bbt_descr *bd)

    verify the bad block description

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_bbt_descr \*bd:
        the table to verify

.. _`verify_bbt_descr.description`:

Description
-----------

This functions performs a few sanity checks on the bad block description
table.

.. _`nand_scan_bbt`:

nand_scan_bbt
=============

.. c:function:: int nand_scan_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd)

    [NAND Interface] scan, find, read and maybe create bad block table(s)

    :param struct mtd_info \*mtd:
        MTD device structure

    :param struct nand_bbt_descr \*bd:
        descriptor for the good/bad block search pattern

.. _`nand_scan_bbt.description`:

Description
-----------

The function checks, if a bad block table(s) is/are already available. If
not it scans the device for manufacturer marked good / bad blocks and writes
the bad block table(s) to the selected place.

The bad block table memory is allocated here. It must be freed by calling
the nand_free_bbt function.

.. _`nand_update_bbt`:

nand_update_bbt
===============

.. c:function:: int nand_update_bbt(struct mtd_info *mtd, loff_t offs)

    update bad block table(s)

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t offs:
        the offset of the newly marked block

.. _`nand_update_bbt.description`:

Description
-----------

The function updates the bad block table(s).

.. _`nand_create_badblock_pattern`:

nand_create_badblock_pattern
============================

.. c:function:: int nand_create_badblock_pattern(struct nand_chip *this)

    [INTERN] Creates a BBT descriptor structure

    :param struct nand_chip \*this:
        NAND chip to create descriptor for

.. _`nand_create_badblock_pattern.description`:

Description
-----------

This function allocates and initializes a nand_bbt_descr for BBM detection
based on the properties of \ ``this``\ . The new descriptor is stored in
this->badblock_pattern. Thus, this->badblock_pattern should be NULL when
passed to this function.

.. _`nand_default_bbt`:

nand_default_bbt
================

.. c:function:: int nand_default_bbt(struct mtd_info *mtd)

    [NAND Interface] Select a default bad block table for the device

    :param struct mtd_info \*mtd:
        MTD device structure

.. _`nand_default_bbt.description`:

Description
-----------

This function selects the default bad block table support for the device and
calls the nand_scan_bbt function.

.. _`nand_isreserved_bbt`:

nand_isreserved_bbt
===================

.. c:function:: int nand_isreserved_bbt(struct mtd_info *mtd, loff_t offs)

    [NAND Interface] Check if a block is reserved

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t offs:
        offset in the device

.. _`nand_isbad_bbt`:

nand_isbad_bbt
==============

.. c:function:: int nand_isbad_bbt(struct mtd_info *mtd, loff_t offs, int allowbbt)

    [NAND Interface] Check if a block is bad

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t offs:
        offset in the device

    :param int allowbbt:
        allow access to bad block table region

.. _`nand_markbad_bbt`:

nand_markbad_bbt
================

.. c:function:: int nand_markbad_bbt(struct mtd_info *mtd, loff_t offs)

    [NAND Interface] Mark a block bad in the BBT

    :param struct mtd_info \*mtd:
        MTD device structure

    :param loff_t offs:
        offset of the bad block

.. This file was automatic generated / don't edit.


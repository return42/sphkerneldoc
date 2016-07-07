.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/bbm.h

.. _`nand_bbt_descr`:

struct nand_bbt_descr
=====================

.. c:type:: struct nand_bbt_descr

    bad block table descriptor

.. _`nand_bbt_descr.definition`:

Definition
----------

.. code-block:: c

    struct nand_bbt_descr {
        int options;
        int pages[NAND_MAX_CHIPS];
        int offs;
        int veroffs;
        uint8_t version[NAND_MAX_CHIPS];
        int len;
        int maxblocks;
        int reserved_block_code;
        uint8_t *pattern;
    }

.. _`nand_bbt_descr.members`:

Members
-------

options
    options for this descriptor

pages
    the page(s) where we find the bbt, used with option BBT_ABSPAGE
    when bbt is searched, then we store the found bbts pages here.
    Its an array and supports up to 8 chips now

offs
    offset of the pattern in the oob area of the page

veroffs
    offset of the bbt version counter in the oob are of the page

version
    version read from the bbt page during scan

len
    length of the pattern, if 0 no pattern check is performed

maxblocks
    maximum number of blocks to search for a bbt. This number of
    blocks is reserved at the end of the device where the tables are
    written.

reserved_block_code
    if non-0, this pattern denotes a reserved (rather than
    bad) block in the stored bbt

pattern
    pattern to identify bad block table or factory marked good /
    bad blocks, can be NULL, if len = 0

.. _`nand_bbt_descr.description`:

Description
-----------

Descriptor for the bad block table marker and the descriptor for the
pattern which identifies good and bad blocks. The assumption is made
that the pattern and the version count are always located in the oob area
of the first block.

.. _`bbm_info`:

struct bbm_info
===============

.. c:type:: struct bbm_info

    [GENERIC] Bad Block Table data structure

.. _`bbm_info.definition`:

Definition
----------

.. code-block:: c

    struct bbm_info {
        int bbt_erase_shift;
        int badblockpos;
        int options;
        uint8_t *bbt;
        int (* isbad_bbt) (struct mtd_info *mtd, loff_t ofs, int allowbbt);
        struct nand_bbt_descr *badblock_pattern;
        void *priv;
    }

.. _`bbm_info.members`:

Members
-------

bbt_erase_shift
    [INTERN] number of address bits in a bbt entry

badblockpos
    [INTERN] position of the bad block marker in the oob area

options
    options for this descriptor

bbt
    [INTERN] bad block table pointer

isbad_bbt
    function to determine if a block is bad

badblock_pattern
    [REPLACEABLE] bad block scan pattern used for
    initial bad block scan

priv
    [OPTIONAL] pointer to private bbm date

.. This file was automatic generated / don't edit.


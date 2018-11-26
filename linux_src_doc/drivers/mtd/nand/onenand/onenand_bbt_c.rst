.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/onenand/onenand_bbt.c

.. _`check_short_pattern`:

check_short_pattern
===================

.. c:function:: int check_short_pattern(uint8_t *buf, int len, int paglen, struct nand_bbt_descr *td)

    [GENERIC] check if a pattern is in the buffer \ ``param``\  buf           the buffer to search \ ``param``\  len           the length of buffer to search \ ``param``\  paglen        the pagelength \ ``param``\  td            search pattern descriptor

    :param buf:
        *undescribed*
    :type buf: uint8_t \*

    :param len:
        *undescribed*
    :type len: int

    :param paglen:
        *undescribed*
    :type paglen: int

    :param td:
        *undescribed*
    :type td: struct nand_bbt_descr \*

.. _`check_short_pattern.description`:

Description
-----------

Check for a pattern at the given place. Used to search bad block
tables and good / bad block identifiers. Same as check_pattern, but
no optional empty check and the pattern is expected to start
at offset 0.

.. _`create_bbt`:

create_bbt
==========

.. c:function:: int create_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *bd, int chip)

    [GENERIC] Create a bad block table by scanning the device \ ``param``\  mtd           MTD device structure \ ``param``\  buf           temporary buffer \ ``param``\  bd            descriptor for the good/bad block search pattern \ ``param``\  chip          create the table for a specific chip, -1 read all chips. Applies only if NAND_BBT_PERCHIP option is set

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param buf:
        *undescribed*
    :type buf: uint8_t \*

    :param bd:
        *undescribed*
    :type bd: struct nand_bbt_descr \*

    :param chip:
        *undescribed*
    :type chip: int

.. _`create_bbt.description`:

Description
-----------

Create a bad block table by scanning the device
for the given good/bad block identify pattern

.. _`onenand_memory_bbt`:

onenand_memory_bbt
==================

.. c:function:: int onenand_memory_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd)

    [GENERIC] create a memory based bad block table \ ``param``\  mtd           MTD device structure \ ``param``\  bd            descriptor for the good/bad block search pattern

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param bd:
        *undescribed*
    :type bd: struct nand_bbt_descr \*

.. _`onenand_memory_bbt.description`:

Description
-----------

The function creates a memory based bbt by scanning the device
for manufacturer / software marked good / bad blocks

.. _`onenand_isbad_bbt`:

onenand_isbad_bbt
=================

.. c:function:: int onenand_isbad_bbt(struct mtd_info *mtd, loff_t offs, int allowbbt)

    [OneNAND Interface] Check if a block is bad \ ``param``\  mtd           MTD device structure \ ``param``\  offs          offset in the device \ ``param``\  allowbbt      allow access to bad block table region

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param offs:
        *undescribed*
    :type offs: loff_t

    :param allowbbt:
        *undescribed*
    :type allowbbt: int

.. _`onenand_scan_bbt`:

onenand_scan_bbt
================

.. c:function:: int onenand_scan_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd)

    [OneNAND Interface] scan, find, read and maybe create bad block table(s) \ ``param``\  mtd           MTD device structure \ ``param``\  bd            descriptor for the good/bad block search pattern

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

    :param bd:
        *undescribed*
    :type bd: struct nand_bbt_descr \*

.. _`onenand_scan_bbt.description`:

Description
-----------

The function checks, if a bad block table(s) is/are already
available. If not it scans the device for manufacturer
marked good / bad blocks and writes the bad block table(s) to
the selected place.

The bad block table memory is allocated here. It is freed
by the onenand_release function.

.. _`onenand_default_bbt`:

onenand_default_bbt
===================

.. c:function:: int onenand_default_bbt(struct mtd_info *mtd)

    [OneNAND Interface] Select a default bad block table for the device \ ``param``\  mtd           MTD device structure

    :param mtd:
        *undescribed*
    :type mtd: struct mtd_info \*

.. _`onenand_default_bbt.description`:

Description
-----------

This function selects the default bad block table
support for the device and calls the onenand_scan_bbt function

.. This file was automatic generated / don't edit.


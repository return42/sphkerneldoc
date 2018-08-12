.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/cafe_nand.c

.. _`cafe_nand_read_page`:

cafe_nand_read_page
===================

.. c:function:: int cafe_nand_read_page(struct mtd_info *mtd, struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ecc syndrome based page read

    :param struct mtd_info \*mtd:
        mtd info structure

    :param struct nand_chip \*chip:
        nand chip info structure

    :param uint8_t \*buf:
        buffer to store read data

    :param int oob_required:
        caller expects OOB data read to chip->oob_poi

    :param int page:
        *undescribed*

.. _`cafe_nand_read_page.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore
we need a special oob layout and handling.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/cafe_nand.c

.. _`cafe_nand_read_page`:

cafe_nand_read_page
===================

.. c:function:: int cafe_nand_read_page(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ecc syndrome based page read

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller expects OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        *undescribed*
    :type page: int

.. _`cafe_nand_read_page.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore
we need a special oob layout and handling.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_ids.c

.. _`nand_get_manufacturer`:

nand_get_manufacturer
=====================

.. c:function:: const struct nand_manufacturer *nand_get_manufacturer(u8 id)

    Get manufacturer information from the manufacturer ID

    :param u8 id:
        manufacturer ID

.. _`nand_get_manufacturer.description`:

Description
-----------

Returns a pointer a nand_manufacturer object if the manufacturer is defined
in the NAND manufacturers database, NULL otherwise.

.. This file was automatic generated / don't edit.


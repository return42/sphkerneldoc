.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/bbt.c

.. _`nanddev_bbt_init`:

nanddev_bbt_init
================

.. c:function:: int nanddev_bbt_init(struct nand_device *nand)

    Initialize the BBT (Bad Block Table)

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_bbt_init.description`:

Description
-----------

Initialize the in-memory BBT.

.. _`nanddev_bbt_init.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_bbt_cleanup`:

nanddev_bbt_cleanup
===================

.. c:function:: void nanddev_bbt_cleanup(struct nand_device *nand)

    Cleanup the BBT (Bad Block Table)

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_bbt_cleanup.description`:

Description
-----------

Undoes what has been done in \ :c:func:`nanddev_bbt_init`\ 

.. _`nanddev_bbt_update`:

nanddev_bbt_update
==================

.. c:function:: int nanddev_bbt_update(struct nand_device *nand)

    Update a BBT

    :param struct nand_device \*nand:
        nand device

.. _`nanddev_bbt_update.description`:

Description
-----------

Update the BBT. Currently a NOP function since on-flash bbt is not yet
supported.

.. _`nanddev_bbt_update.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_bbt_get_block_status`:

nanddev_bbt_get_block_status
============================

.. c:function:: int nanddev_bbt_get_block_status(const struct nand_device *nand, unsigned int entry)

    Return the status of an eraseblock

    :param const struct nand_device \*nand:
        nand device

    :param unsigned int entry:
        the BBT entry

.. _`nanddev_bbt_get_block_status.return`:

Return
------

a positive number nand_bbt_block_status status or -%ERANGE if \ ``entry``\ 
is bigger than the BBT size.

.. _`nanddev_bbt_set_block_status`:

nanddev_bbt_set_block_status
============================

.. c:function:: int nanddev_bbt_set_block_status(struct nand_device *nand, unsigned int entry, enum nand_bbt_block_status status)

    Update the status of an eraseblock in the in-memory BBT

    :param struct nand_device \*nand:
        nand device

    :param unsigned int entry:
        the BBT entry to update

    :param enum nand_bbt_block_status status:
        the new status

.. _`nanddev_bbt_set_block_status.description`:

Description
-----------

Update an entry of the in-memory BBT. If you want to push the updated BBT
the NAND you should call \ :c:func:`nanddev_bbt_update`\ .

.. _`nanddev_bbt_set_block_status.return`:

Return
------

0 in case of success or -%ERANGE if \ ``entry``\  is bigger than the BBT
size.

.. This file was automatic generated / don't edit.


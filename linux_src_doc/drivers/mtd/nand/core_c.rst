.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/core.c

.. _`nanddev_isbad`:

nanddev_isbad
=============

.. c:function:: bool nanddev_isbad(struct nand_device *nand, const struct nand_pos *pos)

    Check if a block is bad

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        position pointing to the block we want to check

.. _`nanddev_isbad.return`:

Return
------

true if the block is bad, false otherwise.

.. _`nanddev_markbad`:

nanddev_markbad
===============

.. c:function:: int nanddev_markbad(struct nand_device *nand, const struct nand_pos *pos)

    Mark a block as bad

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        position of the block to mark bad

.. _`nanddev_markbad.description`:

Description
-----------

Mark a block bad. This function is updating the BBT if available and
calls the low-level markbad hook (nand->ops->markbad()).

.. _`nanddev_markbad.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_isreserved`:

nanddev_isreserved
==================

.. c:function:: bool nanddev_isreserved(struct nand_device *nand, const struct nand_pos *pos)

    Check whether an eraseblock is reserved or not

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        NAND position to test

.. _`nanddev_isreserved.description`:

Description
-----------

Checks whether the eraseblock pointed by \ ``pos``\  is reserved or not.

.. _`nanddev_isreserved.return`:

Return
------

true if the eraseblock is reserved, false otherwise.

.. _`nanddev_erase`:

nanddev_erase
=============

.. c:function:: int nanddev_erase(struct nand_device *nand, const struct nand_pos *pos)

    Erase a NAND portion

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_pos \*pos:
        position of the block to erase

.. _`nanddev_erase.description`:

Description
-----------

Erases the block if it's not bad.

.. _`nanddev_erase.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_mtd_erase`:

nanddev_mtd_erase
=================

.. c:function:: int nanddev_mtd_erase(struct mtd_info *mtd, struct erase_info *einfo)

    Generic mtd->_erase() implementation for NAND devices

    :param struct mtd_info \*mtd:
        MTD device

    :param struct erase_info \*einfo:
        erase request

.. _`nanddev_mtd_erase.description`:

Description
-----------

This is a simple mtd->_erase() implementation iterating over all blocks
concerned by \ ``einfo``\  and calling nand->ops->erase() on each of them.

Note that mtd->_erase should not be directly assigned to this helper,
because there's no locking here. NAND specialized layers should instead
implement there own wrapper around \ :c:func:`nanddev_mtd_erase`\  taking the
appropriate lock before calling \ :c:func:`nanddev_mtd_erase`\ .

.. _`nanddev_mtd_erase.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_init`:

nanddev_init
============

.. c:function:: int nanddev_init(struct nand_device *nand, const struct nand_ops *ops, struct module *owner)

    Initialize a NAND device

    :param struct nand_device \*nand:
        NAND device

    :param const struct nand_ops \*ops:
        NAND device operations

    :param struct module \*owner:
        NAND device owner

.. _`nanddev_init.description`:

Description
-----------

Initializes a NAND device object. Consistency checks are done on \ ``ops``\  and
\ ``nand``\ ->memorg. Also takes care of initializing the BBT.

.. _`nanddev_init.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`nanddev_cleanup`:

nanddev_cleanup
===============

.. c:function:: void nanddev_cleanup(struct nand_device *nand)

    Release resources allocated in \ :c:func:`nanddev_init`\ 

    :param struct nand_device \*nand:
        NAND device

.. _`nanddev_cleanup.description`:

Description
-----------

Basically undoes what has been done in \ :c:func:`nanddev_init`\ .

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ufs/super.c

.. _`ufs_put_super_internal`:

ufs_put_super_internal
======================

.. c:function:: void ufs_put_super_internal(struct super_block *sb)

    put on-disk intrenal structures

    :param sb:
        pointer to super_block structure
        Put on-disk structures associated with cylinder groups
        and write them back to disk, also update cs_total on disk
    :type sb: struct super_block \*

.. This file was automatic generated / don't edit.


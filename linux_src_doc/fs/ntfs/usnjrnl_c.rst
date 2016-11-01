.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/usnjrnl.c

.. _`ntfs_stamp_usnjrnl`:

ntfs_stamp_usnjrnl
==================

.. c:function:: bool ntfs_stamp_usnjrnl(ntfs_volume *vol)

    stamp the transaction log ($UsnJrnl) on an ntfs volume

    :param ntfs_volume \*vol:
        ntfs volume on which to stamp the transaction log

.. _`ntfs_stamp_usnjrnl.description`:

Description
-----------

Stamp the transaction log ($UsnJrnl) on the ntfs volume \ ``vol``\  and return
'true' on success and 'false' on error.

This function assumes that the transaction log has already been loaded and
consistency checked by a call to fs/ntfs/super.c::load_and_init_usnjrnl().

.. This file was automatic generated / don't edit.


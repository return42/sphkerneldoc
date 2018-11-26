.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/dir.c

.. _`is_dx_dir`:

is_dx_dir
=========

.. c:function:: int is_dx_dir(struct inode *inode)

    inode refers to an htree-indexed directory (or a directory which could potentially get converted to use htree indexing).

    :param inode:
        *undescribed*
    :type inode: struct inode \*

.. _`is_dx_dir.description`:

Description
-----------

Return 1 if it is a dx dir, 0 if not

.. This file was automatic generated / don't edit.


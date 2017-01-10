.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/file_table.c

.. _`alloc_file`:

alloc_file
==========

.. c:function:: struct file *alloc_file(const struct path *path, fmode_t mode, const struct file_operations *fop)

    allocate and initialize a 'struct file'

    :param const struct path \*path:
        the (dentry, vfsmount) pair for the new file

    :param fmode_t mode:
        the mode with which the new file will be opened

    :param const struct file_operations \*fop:
        the 'struct file_operations' for the new file

.. This file was automatic generated / don't edit.


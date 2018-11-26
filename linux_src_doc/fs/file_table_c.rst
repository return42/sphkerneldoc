.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/file_table.c

.. _`alloc_file`:

alloc_file
==========

.. c:function:: struct file *alloc_file(const struct path *path, int flags, const struct file_operations *fop)

    allocate and initialize a 'struct file'

    :param path:
        the (dentry, vfsmount) pair for the new file
    :type path: const struct path \*

    :param flags:
        O_... flags with which the new file will be opened
    :type flags: int

    :param fop:
        the 'struct file_operations' for the new file
    :type fop: const struct file_operations \*

.. This file was automatic generated / don't edit.


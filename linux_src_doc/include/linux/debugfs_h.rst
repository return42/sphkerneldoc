.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/debugfs.h

.. _`debugfs_real_fops`:

debugfs_real_fops
=================

.. c:function:: const struct file_operations *debugfs_real_fops(const struct file *filp)

    getter for the real file operation

    :param const struct file \*filp:
        a pointer to a struct file

.. _`debugfs_real_fops.description`:

Description
-----------

Must only be called under the protection established by
\ :c:func:`debugfs_use_file_start`\ .

.. This file was automatic generated / don't edit.


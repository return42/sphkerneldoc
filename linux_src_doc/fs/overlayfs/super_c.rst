.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/overlayfs/super.c

.. _`ovl_statfs`:

ovl_statfs
==========

.. c:function:: int ovl_statfs(struct dentry *dentry, struct kstatfs *buf)

    :param dentry:
        *undescribed*
    :type dentry: struct dentry \*

    :param buf:
        The struct kstatfs to fill in with stats
    :type buf: struct kstatfs \*

.. _`ovl_statfs.description`:

Description
-----------

Get the filesystem statistics.  As writes always target the upper layer
filesystem pass the statfs to the upper filesystem (if it exists)

.. _`ovl_show_options`:

ovl_show_options
================

.. c:function:: int ovl_show_options(struct seq_file *m, struct dentry *dentry)

    :param m:
        *undescribed*
    :type m: struct seq_file \*

    :param dentry:
        *undescribed*
    :type dentry: struct dentry \*

.. _`ovl_show_options.description`:

Description
-----------

Prints the mount options for a given superblock.
Returns zero; does not fail.

.. This file was automatic generated / don't edit.


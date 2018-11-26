.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fat/nfs.c

.. _`fat_dget`:

fat_dget
========

.. c:function:: struct inode *fat_dget(struct super_block *sb, int i_logstart)

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param i_logstart:
        *undescribed*
    :type i_logstart: int

.. _`fat_fh_to_dentry`:

fat_fh_to_dentry
================

.. c:function:: struct dentry *fat_fh_to_dentry(struct super_block *sb, struct fid *fid, int fh_len, int fh_type)

    The dentry may or may not be connected to the filesystem root.

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param fid:
        *undescribed*
    :type fid: struct fid \*

    :param fh_len:
        *undescribed*
    :type fh_len: int

    :param fh_type:
        *undescribed*
    :type fh_type: int

.. This file was automatic generated / don't edit.


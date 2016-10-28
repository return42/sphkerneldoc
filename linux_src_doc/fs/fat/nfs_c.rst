.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fat/nfs.c

.. _`fat_dget`:

fat_dget
========

.. c:function:: struct inode *fat_dget(struct super_block *sb, int i_logstart)

    :param struct super_block \*sb:
        *undescribed*

    :param int i_logstart:
        *undescribed*

.. _`fat_fh_to_dentry`:

fat_fh_to_dentry
================

.. c:function:: struct dentry *fat_fh_to_dentry(struct super_block *sb, struct fid *fid, int fh_len, int fh_type)

    The dentry may or may not be connected to the filesystem root.

    :param struct super_block \*sb:
        *undescribed*

    :param struct fid \*fid:
        *undescribed*

    :param int fh_len:
        *undescribed*

    :param int fh_type:
        *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/namei.c

.. _`ocfs2_prepare_orphan_dir`:

ocfs2_prepare_orphan_dir
========================

.. c:function:: int ocfs2_prepare_orphan_dir(struct ocfs2_super *osb, struct inode **ret_orphan_dir, u64 blkno, char *name, struct ocfs2_dir_lookup_result *lookup, bool dio)

    Prepare an orphan directory for insertion of an orphan.

    :param struct ocfs2_super \*osb:
        ocfs2 file system

    :param struct inode \*\*ret_orphan_dir:
        Orphan dir inode - returned locked!

    :param u64 blkno:
        Actual block number of the inode to be inserted into orphan dir.

    :param char \*name:
        *undescribed*

    :param struct ocfs2_dir_lookup_result \*lookup:
        dir lookup result, to be passed back into functions like
        ocfs2_orphan_add

    :param bool dio:
        *undescribed*

.. _`ocfs2_prepare_orphan_dir.description`:

Description
-----------

Returns zero on success and the ret_orphan_dir, name and lookup
fields will be populated.

Returns non-zero on failure.

.. _`ocfs2_prep_new_orphaned_file`:

ocfs2_prep_new_orphaned_file
============================

.. c:function:: int ocfs2_prep_new_orphaned_file(struct inode *dir, struct buffer_head *dir_bh, char *orphan_name, struct inode **ret_orphan_dir, u64 *ret_di_blkno, struct ocfs2_dir_lookup_result *orphan_insert, struct ocfs2_alloc_context **ret_inode_ac)

    Prepare the orphan dir to receive a newly allocated file. This is different from the typical 'add to orphan dir' operation in that the inode does not yet exist. This is a problem because the orphan dir stringifies the inode block number to come up with it's dirent. Obviously if the inode does not yet exist we have a chicken and egg problem. This function works around it by calling deeper into the orphan and suballoc code than other callers. Use this only by necessity.

    :param struct inode \*dir:
        The directory which this inode will ultimately wind up under - not the
        orphan dir!

    :param struct buffer_head \*dir_bh:
        buffer_head the \ ``dir``\  inode block

    :param char \*orphan_name:
        string of length (CFS2_ORPHAN_NAMELEN + 1). Will be filled
        with the string to be used for orphan dirent. Pass back to the orphan dir
        code.

    :param struct inode \*\*ret_orphan_dir:
        orphan dir inode returned to be passed back into orphan
        dir code.

    :param u64 \*ret_di_blkno:
        block number where the new inode will be allocated.

    :param struct ocfs2_dir_lookup_result \*orphan_insert:
        Dir insert context to be passed back into orphan dir code.

    :param struct ocfs2_alloc_context \*\*ret_inode_ac:
        Inode alloc context to be passed back to the allocator.

.. _`ocfs2_prep_new_orphaned_file.description`:

Description
-----------

Returns zero on success and the ret_orphan_dir, name and lookup
fields will be populated.

Returns non-zero on failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/namei.c

.. _`ocfs2_prepare_orphan_dir`:

ocfs2_prepare_orphan_dir
========================

.. c:function:: int ocfs2_prepare_orphan_dir(struct ocfs2_super *osb, struct inode **ret_orphan_dir, u64 blkno, char *name, struct ocfs2_dir_lookup_result *lookup, bool dio)

    Prepare an orphan directory for insertion of an orphan.

    :param osb:
        ocfs2 file system
    :type osb: struct ocfs2_super \*

    :param ret_orphan_dir:
        Orphan dir inode - returned locked!
    :type ret_orphan_dir: struct inode \*\*

    :param blkno:
        Actual block number of the inode to be inserted into orphan dir.
    :type blkno: u64

    :param name:
        *undescribed*
    :type name: char \*

    :param lookup:
        dir lookup result, to be passed back into functions like
        ocfs2_orphan_add
    :type lookup: struct ocfs2_dir_lookup_result \*

    :param dio:
        *undescribed*
    :type dio: bool

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

    :param dir:
        The directory which this inode will ultimately wind up under - not the
        orphan dir!
    :type dir: struct inode \*

    :param dir_bh:
        buffer_head the \ ``dir``\  inode block
    :type dir_bh: struct buffer_head \*

    :param orphan_name:
        string of length (CFS2_ORPHAN_NAMELEN + 1). Will be filled
        with the string to be used for orphan dirent. Pass back to the orphan dir
        code.
    :type orphan_name: char \*

    :param ret_orphan_dir:
        orphan dir inode returned to be passed back into orphan
        dir code.
    :type ret_orphan_dir: struct inode \*\*

    :param ret_di_blkno:
        block number where the new inode will be allocated.
    :type ret_di_blkno: u64 \*

    :param orphan_insert:
        Dir insert context to be passed back into orphan dir code.
    :type orphan_insert: struct ocfs2_dir_lookup_result \*

    :param ret_inode_ac:
        Inode alloc context to be passed back to the allocator.
    :type ret_inode_ac: struct ocfs2_alloc_context \*\*

.. _`ocfs2_prep_new_orphaned_file.description`:

Description
-----------

Returns zero on success and the ret_orphan_dir, name and lookup
fields will be populated.

Returns non-zero on failure.

.. This file was automatic generated / don't edit.


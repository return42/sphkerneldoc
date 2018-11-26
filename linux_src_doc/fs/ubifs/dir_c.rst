.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/dir.c

.. _`inherit_flags`:

inherit_flags
=============

.. c:function:: int inherit_flags(const struct inode *dir, umode_t mode)

    inherit flags of the parent inode.

    :param dir:
        parent inode
    :type dir: const struct inode \*

    :param mode:
        new inode mode flags
    :type mode: umode_t

.. _`inherit_flags.description`:

Description
-----------

This is a helper function for 'ubifs_new_inode()' which inherits flag of the
parent directory inode \ ``dir``\ . UBIFS inodes inherit the following flags:
o \ ``UBIFS_COMPR_FL``\ , which is useful to switch compression on/of on
sub-directory basis;
o \ ``UBIFS_SYNC_FL``\  - useful for the same reasons;
o \ ``UBIFS_DIRSYNC_FL``\  - similar, but relevant only to directories.

This function returns the inherited flags.

.. _`ubifs_new_inode`:

ubifs_new_inode
===============

.. c:function:: struct inode *ubifs_new_inode(struct ubifs_info *c, struct inode *dir, umode_t mode)

    allocate new UBIFS inode object.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param dir:
        parent directory inode
    :type dir: struct inode \*

    :param mode:
        inode mode flags
    :type mode: umode_t

.. _`ubifs_new_inode.description`:

Description
-----------

This function finds an unused inode number, allocates new inode and
initializes it. Returns new inode in case of success and an error code in
case of failure.

.. _`vfs_dent_type`:

vfs_dent_type
=============

.. c:function:: unsigned int vfs_dent_type(uint8_t type)

    get VFS directory entry type.

    :param type:
        UBIFS directory entry type
    :type type: uint8_t

.. _`vfs_dent_type.description`:

Description
-----------

This function converts UBIFS directory entry type into VFS directory entry
type.

.. _`lock_2_inodes`:

lock_2_inodes
=============

.. c:function:: void lock_2_inodes(struct inode *inode1, struct inode *inode2)

    a wrapper for locking two UBIFS inodes.

    :param inode1:
        first inode
    :type inode1: struct inode \*

    :param inode2:
        second inode
    :type inode2: struct inode \*

.. _`lock_2_inodes.description`:

Description
-----------

We do not implement any tricks to guarantee strict lock ordering, because
VFS has already done it for us on the \ ``i_mutex``\ . So this is just a simple
wrapper function.

.. _`unlock_2_inodes`:

unlock_2_inodes
===============

.. c:function:: void unlock_2_inodes(struct inode *inode1, struct inode *inode2)

    a wrapper for unlocking two UBIFS inodes.

    :param inode1:
        first inode
    :type inode1: struct inode \*

    :param inode2:
        second inode
    :type inode2: struct inode \*

.. _`ubifs_check_dir_empty`:

ubifs_check_dir_empty
=====================

.. c:function:: int ubifs_check_dir_empty(struct inode *dir)

    check if a directory is empty or not.

    :param dir:
        VFS inode object of the directory to check
    :type dir: struct inode \*

.. _`ubifs_check_dir_empty.description`:

Description
-----------

This function checks if directory \ ``dir``\  is empty. Returns zero if the
directory is empty, \ ``-ENOTEMPTY``\  if it is not, and other negative error codes
in case of of errors.

.. _`lock_4_inodes`:

lock_4_inodes
=============

.. c:function:: void lock_4_inodes(struct inode *inode1, struct inode *inode2, struct inode *inode3, struct inode *inode4)

    a wrapper for locking three UBIFS inodes.

    :param inode1:
        first inode
    :type inode1: struct inode \*

    :param inode2:
        second inode
    :type inode2: struct inode \*

    :param inode3:
        third inode
    :type inode3: struct inode \*

    :param inode4:
        fouth inode
    :type inode4: struct inode \*

.. _`lock_4_inodes.description`:

Description
-----------

This function is used for 'ubifs_rename()' and \ ``inode1``\  may be the same as
\ ``inode2``\  whereas \ ``inode3``\  and \ ``inode4``\  may be \ ``NULL``\ .

We do not implement any tricks to guarantee strict lock ordering, because
VFS has already done it for us on the \ ``i_mutex``\ . So this is just a simple
wrapper function.

.. _`unlock_4_inodes`:

unlock_4_inodes
===============

.. c:function:: void unlock_4_inodes(struct inode *inode1, struct inode *inode2, struct inode *inode3, struct inode *inode4)

    a wrapper for unlocking three UBIFS inodes for rename.

    :param inode1:
        first inode
    :type inode1: struct inode \*

    :param inode2:
        second inode
    :type inode2: struct inode \*

    :param inode3:
        third inode
    :type inode3: struct inode \*

    :param inode4:
        fouth inode
    :type inode4: struct inode \*

.. This file was automatic generated / don't edit.


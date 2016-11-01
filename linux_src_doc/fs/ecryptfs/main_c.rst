.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/main.c

.. _`ecryptfs_init_lower_file`:

ecryptfs_init_lower_file
========================

.. c:function:: int ecryptfs_init_lower_file(struct dentry *dentry, struct file **lower_file)

    :param struct dentry \*dentry:
        *undescribed*

    :param struct file \*\*lower_file:
        *undescribed*

.. _`ecryptfs_init_lower_file.description`:

Description
-----------

eCryptfs only ever keeps a single open file for every lower
inode. All I/O operations to the lower inode occur through that
file. When the first eCryptfs dentry that interposes with the first
lower dentry for that inode is created, this function creates the
lower file struct and associates it with the eCryptfs
inode. When all eCryptfs files associated with the inode are released, the
file is closed.

The lower file will be opened with read/write permissions, if
possible. Otherwise, it is opened read-only.

This function does nothing if a lower file is already
associated with the eCryptfs inode.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_parse_options`:

ecryptfs_parse_options
======================

.. c:function:: int ecryptfs_parse_options(struct ecryptfs_sb_info *sbi, char *options, uid_t *check_ruid)

    :param struct ecryptfs_sb_info \*sbi:
        *undescribed*

    :param char \*options:
        The options passed to the kernel

    :param uid_t \*check_ruid:
        set to 1 if device uid should be checked against the ruid

.. _`ecryptfs_parse_options.parse-mount-options`:

Parse mount options
-------------------

debug=N         - ecryptfs_verbosity level for debug output
sig=XXX         - description(signature) of the key to use

Returns the dentry object of the lower-level (lower/interposed)
directory; We want to mount our stackable file system on top of
that lower directory.

The signature of the key to use must be the description of a key
already in the keyring. Mounting will fail if the key can not be
found.

Returns zero on success; non-zero on error

.. _`ecryptfs_mount`:

ecryptfs_mount
==============

.. c:function:: struct dentry *ecryptfs_mount(struct file_system_type *fs_type, int flags, const char *dev_name, void *raw_data)

    @fs_type \ ``flags``\ 

    :param struct file_system_type \*fs_type:
        *undescribed*

    :param int flags:
        *undescribed*

    :param const char \*dev_name:
        The path to mount over

    :param void \*raw_data:
        The options passed into the kernel

.. _`ecryptfs_kill_block_super`:

ecryptfs_kill_block_super
=========================

.. c:function:: void ecryptfs_kill_block_super(struct super_block *sb)

    :param struct super_block \*sb:
        The ecryptfs super block

.. _`ecryptfs_kill_block_super.description`:

Description
-----------

Used to bring the superblock down and free the private data.

.. _`inode_info_init_once`:

inode_info_init_once
====================

.. c:function:: void inode_info_init_once(void *vptr)

    :param void \*vptr:
        *undescribed*

.. _`inode_info_init_once.description`:

Description
-----------

Initializes the ecryptfs_inode_info_cache when it is created

.. _`ecryptfs_init_kmem_caches`:

ecryptfs_init_kmem_caches
=========================

.. c:function:: int ecryptfs_init_kmem_caches( void)

    :param  void:
        no arguments

.. _`ecryptfs_init_kmem_caches.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. This file was automatic generated / don't edit.


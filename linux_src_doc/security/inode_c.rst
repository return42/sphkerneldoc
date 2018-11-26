.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/inode.c

.. _`securityfs_create_dentry`:

securityfs_create_dentry
========================

.. c:function:: struct dentry *securityfs_create_dentry(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops, const struct inode_operations *iops)

    create a dentry in the securityfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the securityfs filesystem.
    :type parent: struct dentry \*

    :param data:
        a pointer to something that the caller will want to get to later
        on.  The inode.i_private pointer will point to this value on
        the \ :c:func:`open`\  call.
    :type data: void \*

    :param fops:
        a pointer to a struct file_operations that should be used for
        this file.
    :type fops: const struct file_operations \*

    :param iops:
        a point to a struct of inode_operations that should be used for
        this file/dir
    :type iops: const struct inode_operations \*

.. _`securityfs_create_dentry.description`:

Description
-----------

This is the basic "create a file/dir/symlink" function for
securityfs.  It allows for a wide range of flexibility in creating
a file, or a directory (if you want to create a directory, the
\ :c:func:`securityfs_create_dir`\  function is recommended to be used
instead).

This function returns a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`securityfs_remove`\  function when the
file is to be removed (no automatic cleanup happens if your module
is unloaded, you are responsible here).  If an error occurs, the
function will return the error value (via ERR_PTR).

If securityfs is not enabled in the kernel, the value \ ``-ENODEV``\  is
returned.

.. _`securityfs_create_file`:

securityfs_create_file
======================

.. c:function:: struct dentry *securityfs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the securityfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the securityfs filesystem.
    :type parent: struct dentry \*

    :param data:
        a pointer to something that the caller will want to get to later
        on.  The inode.i_private pointer will point to this value on
        the \ :c:func:`open`\  call.
    :type data: void \*

    :param fops:
        a pointer to a struct file_operations that should be used for
        this file.
    :type fops: const struct file_operations \*

.. _`securityfs_create_file.description`:

Description
-----------

This function creates a file in securityfs with the given \ ``name``\ .

This function returns a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`securityfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here).  If an error occurs, the function will return
the error value (via ERR_PTR).

If securityfs is not enabled in the kernel, the value \ ``-ENODEV``\  is
returned.

.. _`securityfs_create_dir`:

securityfs_create_dir
=====================

.. c:function:: struct dentry *securityfs_create_dir(const char *name, struct dentry *parent)

    create a directory in the securityfs filesystem

    :param name:
        a pointer to a string containing the name of the directory to
        create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        directory will be created in the root of the securityfs filesystem.
    :type parent: struct dentry \*

.. _`securityfs_create_dir.description`:

Description
-----------

This function creates a directory in securityfs with the given \ ``name``\ .

This function returns a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`securityfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here).  If an error occurs, the function will return
the error value (via ERR_PTR).

If securityfs is not enabled in the kernel, the value \ ``-ENODEV``\  is
returned.

.. _`securityfs_create_symlink`:

securityfs_create_symlink
=========================

.. c:function:: struct dentry *securityfs_create_symlink(const char *name, struct dentry *parent, const char *target, const struct inode_operations *iops)

    create a symlink in the securityfs filesystem

    :param name:
        a pointer to a string containing the name of the symlink to
        create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for the symlink.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        directory will be created in the root of the securityfs filesystem.
    :type parent: struct dentry \*

    :param target:
        a pointer to a string containing the name of the symlink's target.
        If this parameter is \ ``NULL``\ , then the \ ``iops``\  parameter needs to be
        setup to handle .readlink and .get_link inode_operations.
    :type target: const char \*

    :param iops:
        a pointer to the struct inode_operations to use for the symlink. If
        this parameter is \ ``NULL``\ , then the default simple_symlink_inode
        operations will be used.
    :type iops: const struct inode_operations \*

.. _`securityfs_create_symlink.description`:

Description
-----------

This function creates a symlink in securityfs with the given \ ``name``\ .

This function returns a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`securityfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here).  If an error occurs, the function will return
the error value (via ERR_PTR).

If securityfs is not enabled in the kernel, the value \ ``-ENODEV``\  is
returned.

.. _`securityfs_remove`:

securityfs_remove
=================

.. c:function:: void securityfs_remove(struct dentry *dentry)

    removes a file or directory from the securityfs filesystem

    :param dentry:
        a pointer to a the dentry of the file or directory to be removed.
    :type dentry: struct dentry \*

.. _`securityfs_remove.description`:

Description
-----------

This function removes a file or directory in securityfs that was previously
created with a call to another securityfs function (like
\ :c:func:`securityfs_create_file`\  or variants thereof.)

This function is required to be called in order for the file to be
removed. No automatic cleanup of files will happen when a module is
removed; you are responsible here.

.. This file was automatic generated / don't edit.


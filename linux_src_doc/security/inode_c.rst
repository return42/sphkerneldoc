.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/inode.c

.. _`securityfs_create_file`:

securityfs_create_file
======================

.. c:function:: struct dentry *securityfs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the securityfs filesystem

    :param const char \*name:
        a pointer to a string containing the name of the file to create.

    :param umode_t mode:
        the permission that the file should have

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        file will be created in the root of the securityfs filesystem.

    :param void \*data:
        a pointer to something that the caller will want to get to later
        on.  The inode.i_private pointer will point to this value on
        the \ :c:func:`open`\  call.

    :param const struct file_operations \*fops:
        a pointer to a struct file_operations that should be used for
        this file.

.. _`securityfs_create_file.description`:

Description
-----------

This is the basic "create a file" function for securityfs.  It allows for a
wide range of flexibility in creating a file, or a directory (if you
want to create a directory, the \ :c:func:`securityfs_create_dir`\  function is
recommended to be used instead).

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

    :param const char \*name:
        a pointer to a string containing the name of the directory to
        create.

    :param struct dentry \*parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is \ ``NULL``\ , then the
        directory will be created in the root of the securityfs filesystem.

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

.. _`securityfs_remove`:

securityfs_remove
=================

.. c:function:: void securityfs_remove(struct dentry *dentry)

    removes a file or directory from the securityfs filesystem

    :param struct dentry \*dentry:
        a pointer to a the dentry of the file or directory to be removed.

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


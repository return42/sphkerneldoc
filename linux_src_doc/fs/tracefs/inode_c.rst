.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/tracefs/inode.c

.. _`tracefs_create_file`:

tracefs_create_file
===================

.. c:function:: struct dentry *tracefs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the tracefs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have.
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        file will be created in the root of the tracefs filesystem.
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

.. _`tracefs_create_file.description`:

Description
-----------

This is the basic "create a file" function for tracefs.  It allows for a
wide range of flexibility in creating a file, or a directory (if you want
to create a directory, the \ :c:func:`tracefs_create_dir`\  function is
recommended to be used instead.)

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`tracefs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If tracefs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`tracefs_create_dir`:

tracefs_create_dir
==================

.. c:function:: struct dentry *tracefs_create_dir(const char *name, struct dentry *parent)

    create a directory in the tracefs filesystem

    :param name:
        a pointer to a string containing the name of the directory to
        create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        directory will be created in the root of the tracefs filesystem.
    :type parent: struct dentry \*

.. _`tracefs_create_dir.description`:

Description
-----------

This function creates a directory in tracefs with the given name.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`tracefs_remove`\  function when the file is
to be removed. If an error occurs, \ ``NULL``\  will be returned.

If tracing is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`tracefs_create_instance_dir`:

tracefs_create_instance_dir
===========================

.. c:function:: struct dentry *tracefs_create_instance_dir(const char *name, struct dentry *parent, int (*mkdir)(const char *name), int (*rmdir)(const char *name))

    create the tracing instances directory

    :param name:
        The name of the instances directory to create
    :type name: const char \*

    :param parent:
        The parent directory that the instances directory will exist
    :type parent: struct dentry \*

    :param int (\*mkdir)(const char \*name):
        The function to call when a mkdir is performed.

    :param int (\*rmdir)(const char \*name):
        The function to call when a rmdir is performed.

.. _`tracefs_create_instance_dir.description`:

Description
-----------

Only one instances directory is allowed.

The instances directory is special as it allows for mkdir and rmdir to
to be done by userspace. When a mkdir or rmdir is performed, the inode
locks are released and the methhods passed in (@mkdir and \ ``rmdir``\ ) are
called without locks and with the name of the directory being created
within the instances directory.

Returns the dentry of the instances directory.

.. _`tracefs_remove`:

tracefs_remove
==============

.. c:function:: void tracefs_remove(struct dentry *dentry)

    removes a file or directory from the tracefs filesystem

    :param dentry:
        a pointer to a the dentry of the file or directory to be
        removed.
    :type dentry: struct dentry \*

.. _`tracefs_remove.description`:

Description
-----------

This function removes a file or directory in tracefs that was previously
created with a call to another tracefs function (like
\ :c:func:`tracefs_create_file`\  or variants thereof.)

.. _`tracefs_remove_recursive`:

tracefs_remove_recursive
========================

.. c:function:: void tracefs_remove_recursive(struct dentry *dentry)

    recursively removes a directory

    :param dentry:
        a pointer to a the dentry of the directory to be removed.
    :type dentry: struct dentry \*

.. _`tracefs_remove_recursive.description`:

Description
-----------

This function recursively removes a directory tree in tracefs that
was previously created with a call to another tracefs function
(like \ :c:func:`tracefs_create_file`\  or variants thereof.)

.. _`tracefs_initialized`:

tracefs_initialized
===================

.. c:function:: bool tracefs_initialized( void)

    Tells whether tracefs has been registered

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/debugfs/inode.c

.. _`debugfs_lookup`:

debugfs_lookup
==============

.. c:function:: struct dentry *debugfs_lookup(const char *name, struct dentry *parent)

    look up an existing debugfs file

    :param name:
        a pointer to a string containing the name of the file to look up.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry of the file.
    :type parent: struct dentry \*

.. _`debugfs_lookup.description`:

Description
-----------

This function will return a pointer to a dentry if it succeeds.  If the file
doesn't exist or an error occurs, \ ``NULL``\  will be returned.  The returned
dentry must be passed to \ :c:func:`dput`\  when it is no longer needed.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_create_file`:

debugfs_create_file
===================

.. c:function:: struct dentry *debugfs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have.
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        file will be created in the root of the debugfs filesystem.
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

.. _`debugfs_create_file.description`:

Description
-----------

This is the basic "create a file" function for debugfs.  It allows for a
wide range of flexibility in creating a file, or a directory (if you want
to create a directory, the \ :c:func:`debugfs_create_dir`\  function is
recommended to be used instead.)

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_create_file_unsafe`:

debugfs_create_file_unsafe
==========================

.. c:function:: struct dentry *debugfs_create_file_unsafe(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops)

    create a file in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have.
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        file will be created in the root of the debugfs filesystem.
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

.. _`debugfs_create_file_unsafe.description`:

Description
-----------

\ :c:func:`debugfs_create_file_unsafe`\  is completely analogous to
\ :c:func:`debugfs_create_file`\ , the only difference being that the fops
handed it will not get protected against file removals by the
debugfs core.

It is your responsibility to protect your struct file_operation
methods against file removals by means of \ :c:func:`debugfs_use_file_start`\ 
and \ :c:func:`debugfs_use_file_finish`\ . ->open() is still protected by
debugfs though.

Any struct file_operations defined by means of
\ :c:func:`DEFINE_DEBUGFS_ATTRIBUTE`\  is protected against file removals and
thus, may be used here.

.. _`debugfs_create_file_size`:

debugfs_create_file_size
========================

.. c:function:: struct dentry *debugfs_create_file_size(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops, loff_t file_size)

    create a file in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param mode:
        the permission that the file should have.
    :type mode: umode_t

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        file will be created in the root of the debugfs filesystem.
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

    :param file_size:
        initial file size
    :type file_size: loff_t

.. _`debugfs_create_file_size.description`:

Description
-----------

This is the basic "create a file" function for debugfs.  It allows for a
wide range of flexibility in creating a file, or a directory (if you want
to create a directory, the \ :c:func:`debugfs_create_dir`\  function is
recommended to be used instead.)

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_create_dir`:

debugfs_create_dir
==================

.. c:function:: struct dentry *debugfs_create_dir(const char *name, struct dentry *parent)

    create a directory in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the directory to
        create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        directory will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

.. _`debugfs_create_dir.description`:

Description
-----------

This function creates a directory in debugfs with the given name.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the file is
to be removed (no automatic cleanup happens if your module is unloaded,
you are responsible here.)  If an error occurs, \ ``NULL``\  will be returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_create_automount`:

debugfs_create_automount
========================

.. c:function:: struct dentry *debugfs_create_automount(const char *name, struct dentry *parent, debugfs_automount_t f, void *data)

    create automount point in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the file to create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this file.  This should be a
        directory dentry if set.  If this parameter is NULL, then the
        file will be created in the root of the debugfs filesystem.
    :type parent: struct dentry \*

    :param f:
        function to be called when pathname resolution steps on that one.
    :type f: debugfs_automount_t

    :param data:
        opaque argument to pass to \ :c:func:`f`\ .
    :type data: void \*

.. _`debugfs_create_automount.description`:

Description
-----------

\ ``f``\  should return what ->d_automount() would.

.. _`debugfs_create_symlink`:

debugfs_create_symlink
======================

.. c:function:: struct dentry *debugfs_create_symlink(const char *name, struct dentry *parent, const char *target)

    create a symbolic link in the debugfs filesystem

    :param name:
        a pointer to a string containing the name of the symbolic link to
        create.
    :type name: const char \*

    :param parent:
        a pointer to the parent dentry for this symbolic link.  This
        should be a directory dentry if set.  If this parameter is NULL,
        then the symbolic link will be created in the root of the debugfs
        filesystem.
    :type parent: struct dentry \*

    :param target:
        a pointer to a string containing the path to the target of the
        symbolic link.
    :type target: const char \*

.. _`debugfs_create_symlink.description`:

Description
-----------

This function creates a symbolic link with the given name in debugfs that
links to the given target path.

This function will return a pointer to a dentry if it succeeds.  This
pointer must be passed to the \ :c:func:`debugfs_remove`\  function when the symbolic
link is to be removed (no automatic cleanup happens if your module is
unloaded, you are responsible here.)  If an error occurs, \ ``NULL``\  will be
returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_remove`:

debugfs_remove
==============

.. c:function:: void debugfs_remove(struct dentry *dentry)

    removes a file or directory from the debugfs filesystem

    :param dentry:
        a pointer to a the dentry of the file or directory to be
        removed.  If this parameter is NULL or an error value, nothing
        will be done.
    :type dentry: struct dentry \*

.. _`debugfs_remove.description`:

Description
-----------

This function removes a file or directory in debugfs that was previously
created with a call to another debugfs function (like
\ :c:func:`debugfs_create_file`\  or variants thereof.)

This function is required to be called in order for the file to be
removed, no automatic cleanup of files will happen when a module is
removed, you are responsible here.

.. _`debugfs_remove_recursive`:

debugfs_remove_recursive
========================

.. c:function:: void debugfs_remove_recursive(struct dentry *dentry)

    recursively removes a directory

    :param dentry:
        a pointer to a the dentry of the directory to be removed.  If this
        parameter is NULL or an error value, nothing will be done.
    :type dentry: struct dentry \*

.. _`debugfs_remove_recursive.description`:

Description
-----------

This function recursively removes a directory tree in debugfs that
was previously created with a call to another debugfs function
(like \ :c:func:`debugfs_create_file`\  or variants thereof.)

This function is required to be called in order for the file to be
removed, no automatic cleanup of files will happen when a module is
removed, you are responsible here.

.. _`debugfs_rename`:

debugfs_rename
==============

.. c:function:: struct dentry *debugfs_rename(struct dentry *old_dir, struct dentry *old_dentry, struct dentry *new_dir, const char *new_name)

    rename a file/directory in the debugfs filesystem

    :param old_dir:
        a pointer to the parent dentry for the renamed object. This
        should be a directory dentry.
    :type old_dir: struct dentry \*

    :param old_dentry:
        dentry of an object to be renamed.
    :type old_dentry: struct dentry \*

    :param new_dir:
        a pointer to the parent dentry where the object should be
        moved. This should be a directory dentry.
    :type new_dir: struct dentry \*

    :param new_name:
        a pointer to a string containing the target name.
    :type new_name: const char \*

.. _`debugfs_rename.description`:

Description
-----------

This function renames a file/directory in debugfs.  The target must not
exist for rename to succeed.

This function will return a pointer to old_dentry (which is updated to
reflect renaming) if it succeeds. If an error occurs, \ ``NULL``\  will be
returned.

If debugfs is not enabled in the kernel, the value -%ENODEV will be
returned.

.. _`debugfs_initialized`:

debugfs_initialized
===================

.. c:function:: bool debugfs_initialized( void)

    Tells whether debugfs has been registered

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


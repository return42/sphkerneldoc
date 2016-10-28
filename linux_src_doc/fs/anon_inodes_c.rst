.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/anon_inodes.c

.. _`anon_inode_getfile`:

anon_inode_getfile
==================

.. c:function:: struct file *anon_inode_getfile(const char *name, const struct file_operations *fops, void *priv, int flags)

    creates a new file instance by hooking it up to an anonymous inode, and a dentry that describe the "class" of the file

    :param const char \*name:
        [in]    name of the "class" of the new file

    :param const struct file_operations \*fops:
        [in]    file operations for the new file

    :param void \*priv:
        [in]    private data for the new file (will be file's private_data)

    :param int flags:
        [in]    flags

.. _`anon_inode_getfile.description`:

Description
-----------

Creates a new file by hooking it on a single inode. This is useful for files
that do not need to have a full-fledged inode in order to operate correctly.
All the files created with \ :c:func:`anon_inode_getfile`\  will share a single inode,
hence saving memory and avoiding code duplication for the file/inode/dentry
setup.  Returns the newly created file\* or an error pointer.

.. _`anon_inode_getfd`:

anon_inode_getfd
================

.. c:function:: int anon_inode_getfd(const char *name, const struct file_operations *fops, void *priv, int flags)

    creates a new file instance by hooking it up to an anonymous inode, and a dentry that describe the "class" of the file

    :param const char \*name:
        [in]    name of the "class" of the new file

    :param const struct file_operations \*fops:
        [in]    file operations for the new file

    :param void \*priv:
        [in]    private data for the new file (will be file's private_data)

    :param int flags:
        [in]    flags

.. _`anon_inode_getfd.description`:

Description
-----------

Creates a new file by hooking it on a single inode. This is useful for files
that do not need to have a full-fledged inode in order to operate correctly.
All the files created with \ :c:func:`anon_inode_getfd`\  will share a single inode,
hence saving memory and avoiding code duplication for the file/inode/dentry
setup.  Returns new descriptor or an error code.

.. This file was automatic generated / don't edit.


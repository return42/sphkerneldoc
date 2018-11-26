.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/open.c

.. _`finish_open`:

finish_open
===========

.. c:function:: int finish_open(struct file *file, struct dentry *dentry, int (*open)(struct inode *, struct file *))

    finish opening a file

    :param file:
        file pointer
    :type file: struct file \*

    :param dentry:
        pointer to dentry
    :type dentry: struct dentry \*

    :param int (\*open)(struct inode \*, struct file \*):
        open callback

.. _`finish_open.description`:

Description
-----------

This can be used to finish opening a file passed to i_op->atomic_open().

If the open callback is set to NULL, then the standard f_op->open()
filesystem callback is substituted.

NB: the dentry reference is \_not\_ consumed.  If, for example, the dentry is
the return value of \ :c:func:`d_splice_alias`\ , then the caller needs to perform \ :c:func:`dput`\ 
on it after \ :c:func:`finish_open`\ .

On successful return \ ``file``\  is a fully instantiated open file.  After this, if
an error occurs in ->atomic_open(), it needs to clean up with \ :c:func:`fput`\ .

Returns zero on success or -errno if the open failed.

.. _`finish_no_open`:

finish_no_open
==============

.. c:function:: int finish_no_open(struct file *file, struct dentry *dentry)

    finish ->atomic_open() without opening the file

    :param file:
        file pointer
    :type file: struct file \*

    :param dentry:
        dentry or NULL (as returned from ->lookup())
    :type dentry: struct dentry \*

.. _`finish_no_open.description`:

Description
-----------

This can be used to set the result of a successful lookup in ->atomic_open().

NB: unlike \ :c:func:`finish_open`\  this function does consume the dentry reference and
the caller need not \ :c:func:`dput`\  it.

Returns "0" which must be the return value of ->atomic_open() after having
called this function.

.. _`vfs_open`:

vfs_open
========

.. c:function:: int vfs_open(const struct path *path, struct file *file)

    open the file at the given path

    :param path:
        path to open
    :type path: const struct path \*

    :param file:
        newly allocated file with f_flag initialized
    :type file: struct file \*

.. _`file_open_name`:

file_open_name
==============

.. c:function:: struct file *file_open_name(struct filename *name, int flags, umode_t mode)

    open file and return file pointer

    :param name:
        struct filename containing path to open
    :type name: struct filename \*

    :param flags:
        open flags as per the open(2) second argument
    :type flags: int

    :param mode:
        mode for the new file if O_CREAT is set, else ignored
    :type mode: umode_t

.. _`file_open_name.description`:

Description
-----------

This is the helper to open a file from kernelspace if you really
have to.  But in generally you should not do this, so please move
along, nothing to see here..

.. _`filp_open`:

filp_open
=========

.. c:function:: struct file *filp_open(const char *filename, int flags, umode_t mode)

    open file and return file pointer

    :param filename:
        path to open
    :type filename: const char \*

    :param flags:
        open flags as per the open(2) second argument
    :type flags: int

    :param mode:
        mode for the new file if O_CREAT is set, else ignored
    :type mode: umode_t

.. _`filp_open.description`:

Description
-----------

This is the helper to open a file from kernelspace if you really
have to.  But in generally you should not do this, so please move
along, nothing to see here..

.. This file was automatic generated / don't edit.


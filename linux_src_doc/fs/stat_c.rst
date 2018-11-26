.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/stat.c

.. _`generic_fillattr`:

generic_fillattr
================

.. c:function:: void generic_fillattr(struct inode *inode, struct kstat *stat)

    Fill in the basic attributes from the inode struct

    :param inode:
        Inode to use as the source
    :type inode: struct inode \*

    :param stat:
        Where to fill in the attributes
    :type stat: struct kstat \*

.. _`generic_fillattr.description`:

Description
-----------

Fill in the basic attributes in the kstat structure from data that's to be
found on the VFS inode structure.  This is the default if no getattr inode
operation is supplied.

.. _`vfs_getattr_nosec`:

vfs_getattr_nosec
=================

.. c:function:: int vfs_getattr_nosec(const struct path *path, struct kstat *stat, u32 request_mask, unsigned int query_flags)

    getattr without security checks

    :param path:
        file to get attributes from
    :type path: const struct path \*

    :param stat:
        structure to return attributes in
    :type stat: struct kstat \*

    :param request_mask:
        STATX_xxx flags indicating what the caller wants
    :type request_mask: u32

    :param query_flags:
        Query mode (KSTAT_QUERY_FLAGS)
    :type query_flags: unsigned int

.. _`vfs_getattr_nosec.description`:

Description
-----------

Get attributes without calling security_inode_getattr.

Currently the only caller other than vfs_getattr is internal to the
filehandle lookup code, which uses only the inode number and returns no
attributes to any user.  Any other code probably wants vfs_getattr.

.. _`vfs_statx_fd`:

vfs_statx_fd
============

.. c:function:: int vfs_statx_fd(unsigned int fd, struct kstat *stat, u32 request_mask, unsigned int query_flags)

    Get the enhanced basic attributes by file descriptor

    :param fd:
        The file descriptor referring to the file of interest
    :type fd: unsigned int

    :param stat:
        The result structure to fill in.
    :type stat: struct kstat \*

    :param request_mask:
        STATX_xxx flags indicating what the caller wants
    :type request_mask: u32

    :param query_flags:
        Query mode (KSTAT_QUERY_FLAGS)
    :type query_flags: unsigned int

.. _`vfs_statx_fd.description`:

Description
-----------

This function is a wrapper around \ :c:func:`vfs_getattr`\ .  The main difference is
that it uses a file descriptor to determine the file location.

0 will be returned on success, and a -ve error code if unsuccessful.

.. _`vfs_statx`:

vfs_statx
=========

.. c:function:: int vfs_statx(int dfd, const char __user *filename, int flags, struct kstat *stat, u32 request_mask)

    Get basic and extra attributes by filename

    :param dfd:
        A file descriptor representing the base dir for a relative filename
    :type dfd: int

    :param filename:
        The name of the file of interest
    :type filename: const char __user \*

    :param flags:
        Flags to control the query
    :type flags: int

    :param stat:
        The result structure to fill in.
    :type stat: struct kstat \*

    :param request_mask:
        STATX_xxx flags indicating what the caller wants
    :type request_mask: u32

.. _`vfs_statx.description`:

Description
-----------

This function is a wrapper around \ :c:func:`vfs_getattr`\ .  The main difference is
that it uses a filename and base directory to determine the file location.
Additionally, the use of AT_SYMLINK_NOFOLLOW in flags will prevent a symlink
at the given name from being referenced.

0 will be returned on success, and a -ve error code if unsuccessful.

.. _`sys_statx`:

sys_statx
=========

.. c:function:: long sys_statx(int dfd, const char __user *filename, unsigned flags, unsigned int mask, struct statx __user *buffer)

    System call to get enhanced stats

    :param dfd:
        Base directory to pathwalk from *or* fd to stat.
    :type dfd: int

    :param filename:
        File to stat or "" with AT_EMPTY_PATH
    :type filename: const char __user \*

    :param flags:
        AT_* flags to control pathwalk.
    :type flags: unsigned

    :param mask:
        Parts of statx struct actually required.
    :type mask: unsigned int

    :param buffer:
        Result buffer.
    :type buffer: struct statx __user \*

.. _`sys_statx.description`:

Description
-----------

Note that \ :c:func:`fstat`\  can be emulated by setting dfd to the fd of interest,
supplying "" as the filename and setting AT_EMPTY_PATH in the flags.

.. This file was automatic generated / don't edit.


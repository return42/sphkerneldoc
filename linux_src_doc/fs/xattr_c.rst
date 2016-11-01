.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/xattr.c

.. _`__vfs_setxattr_noperm`:

__vfs_setxattr_noperm
=====================

.. c:function:: int __vfs_setxattr_noperm(struct dentry *dentry, const char *name, const void *value, size_t size, int flags)

    perform setxattr operation without performing permission checks.

    :param struct dentry \*dentry:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param const void \*value:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param int flags:
        *undescribed*

.. _`__vfs_setxattr_noperm.description`:

Description
-----------

@dentry - object to perform setxattr on
\ ``name``\  - xattr name to set
\ ``value``\  - value to set \ ``name``\  to
\ ``size``\  - size of \ ``value``\ 
\ ``flags``\  - flags to pass into filesystem operations

returns the result of the internal setxattr or setsecurity operations.

This function requires the caller to lock the inode's i_mutex before it
is executed. It also assumes that the caller will make the appropriate
permission checks.

.. _`xattr_full_name`:

xattr_full_name
===============

.. c:function:: const char *xattr_full_name(const struct xattr_handler *handler, const char *name)

    Compute full attribute name from suffix

    :param const struct xattr_handler \*handler:
        handler of the xattr_handler operation

    :param const char \*name:
        name passed to the xattr_handler operation

.. _`xattr_full_name.description`:

Description
-----------

The get and set xattr handler operations are called with the remainder of
the attribute name after skipping the handler's prefix: for example, "foo"
is passed to the get operation of a handler with prefix "user." to get
attribute "user.foo".  The full name is still "there" in the name though.

.. _`xattr_full_name.note`:

Note
----

the list xattr handler operation when called from the vfs is passed a
NULL name; some file systems use this operation internally, with varying
semantics.

.. _`simple_xattr_set`:

simple_xattr_set
================

.. c:function:: int simple_xattr_set(struct simple_xattrs *xattrs, const char *name, const void *value, size_t size, int flags)

    xattr SET operation for in-memory/pseudo filesystems

    :param struct simple_xattrs \*xattrs:
        target simple_xattr list

    :param const char \*name:
        name of the extended attribute

    :param const void \*value:
        value of the xattr. If \ ``NULL``\ , will remove the attribute.

    :param size_t size:
        size of the new xattr

    :param int flags:
        %XATTR_{CREATE\|REPLACE}

.. _`simple_xattr_set.description`:

Description
-----------

%XATTR_CREATE is set, the xattr shouldn't exist already; otherwise fails
with -EEXIST.  If \ ``XATTR_REPLACE``\  is set, the xattr should exist;
otherwise, fails with -ENODATA.

Returns 0 on success, -errno on failure.

.. This file was automatic generated / don't edit.


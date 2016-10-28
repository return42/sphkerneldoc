.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/stat.c

.. _`vfs_getattr_nosec`:

vfs_getattr_nosec
=================

.. c:function:: int vfs_getattr_nosec(struct path *path, struct kstat *stat)

    getattr without security checks

    :param struct path \*path:
        file to get attributes from

    :param struct kstat \*stat:
        structure to return attributes in

.. _`vfs_getattr_nosec.description`:

Description
-----------

Get attributes without calling security_inode_getattr.

Currently the only caller other than vfs_getattr is internal to the
filehandle lookup code, which uses only the inode number and returns
no attributes to any user.  Any other code probably wants
vfs_getattr.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/vfs.c

.. _`nfsd4_is_junction`:

nfsd4_is_junction
=================

.. c:function:: int nfsd4_is_junction(struct dentry *dentry)

    Test if an object could be an NFS junction

    :param dentry:
        object to test
    :type dentry: struct dentry \*

.. _`nfsd4_is_junction.description`:

Description
-----------

Returns 1 if "dentry" appears to contain NFS junction information.
Otherwise 0 is returned.

.. This file was automatic generated / don't edit.


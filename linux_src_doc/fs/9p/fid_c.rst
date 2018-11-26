.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/fid.c

.. _`__add_fid`:

\__add_fid
==========

.. c:function:: void __add_fid(struct dentry *dentry, struct p9_fid *fid)

    add a fid to a dentry

    :param dentry:
        dentry that the fid is being added to
    :type dentry: struct dentry \*

    :param fid:
        fid to add
    :type fid: struct p9_fid \*

.. _`v9fs_fid_find`:

v9fs_fid_find
=============

.. c:function:: struct p9_fid *v9fs_fid_find(struct dentry *dentry, kuid_t uid, int any)

    retrieve a fid that belongs to the specified uid

    :param dentry:
        dentry to look for fid in
    :type dentry: struct dentry \*

    :param uid:
        return fid that belongs to the specified user
    :type uid: kuid_t

    :param any:
        if non-zero, return any fid associated with the dentry
    :type any: int

.. _`v9fs_fid_lookup`:

v9fs_fid_lookup
===============

.. c:function:: struct p9_fid *v9fs_fid_lookup(struct dentry *dentry)

    lookup for a fid, try to walk if not found

    :param dentry:
        dentry to look for fid in
    :type dentry: struct dentry \*

.. _`v9fs_fid_lookup.description`:

Description
-----------

Look for a fid in the specified dentry for the current user.
If no fid is found, try to create one walking from a fid from the parent
dentry (if it has one), or the root dentry. If the user haven't accessed
the fs yet, attach now and walk from the root.

.. This file was automatic generated / don't edit.


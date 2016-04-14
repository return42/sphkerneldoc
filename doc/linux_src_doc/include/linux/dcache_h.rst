.. -*- coding: utf-8; mode: rst -*-

========
dcache.h
========

.. _`dget_dlock`:

dget_dlock
==========

.. c:function:: struct dentry *dget_dlock (struct dentry *dentry)

    get a reference to a dentry

    :param struct dentry \*dentry:
        dentry to get a reference to


.. _`dget_dlock.description`:

Description
-----------

Given a dentry or ``NULL`` pointer increment the reference count
if appropriate and return the dentry. A dentry will not be 
destroyed when it has references.


.. _`d_unhashed`:

d_unhashed
==========

.. c:function:: int d_unhashed (const struct dentry *dentry)

    is dentry hashed

    :param const struct dentry \*dentry:
        entry to check


.. _`d_unhashed.description`:

Description
-----------

Returns true if the dentry passed is not currently hashed.


.. _`d_really_is_negative`:

d_really_is_negative
====================

.. c:function:: bool d_really_is_negative (const struct dentry *dentry)

    Determine if a dentry is really negative (ignoring fallthroughs)

    :param const struct dentry \*dentry:
        The dentry in question


.. _`d_really_is_negative.description`:

Description
-----------

Returns true if the dentry represents either an absent name or a name that
doesn't map to an inode (ie. ->d_inode is NULL).  The dentry could represent
a true miss, a whiteout that isn't represented by a 0,0 chardev or a
fallthrough marker in an opaque directory.

Note!  (1) This should be used \*only\* by a filesystem to examine its own
dentries.  It should not be used to look at some other filesystem's
dentries.  (2) It should also be used in combination with :c:func:`d_inode` to get
the inode.  (3) The dentry may have something attached to ->d_lower and the
type field of the flags may be set to something other than miss or whiteout.


.. _`d_really_is_positive`:

d_really_is_positive
====================

.. c:function:: bool d_really_is_positive (const struct dentry *dentry)

    Determine if a dentry is really positive (ignoring fallthroughs)

    :param const struct dentry \*dentry:
        The dentry in question


.. _`d_really_is_positive.description`:

Description
-----------

Returns true if the dentry represents a name that maps to an inode
(ie. ->d_inode is not NULL).  The dentry might still represent a whiteout if
that is represented on medium as a 0,0 chardev.

Note!  (1) This should be used \*only\* by a filesystem to examine its own
dentries.  It should not be used to look at some other filesystem's
dentries.  (2) It should also be used in combination with :c:func:`d_inode` to get
the inode.


.. _`d_inode`:

d_inode
=======

.. c:function:: struct inode *d_inode (const struct dentry *dentry)

    Get the actual inode of this dentry

    :param const struct dentry \*dentry:
        The dentry to query


.. _`d_inode.description`:

Description
-----------

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.


.. _`d_inode_rcu`:

d_inode_rcu
===========

.. c:function:: struct inode *d_inode_rcu (const struct dentry *dentry)

    Get the actual inode of this dentry with ACCESS_ONCE()

    :param const struct dentry \*dentry:
        The dentry to query


.. _`d_inode_rcu.description`:

Description
-----------

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.


.. _`d_backing_inode`:

d_backing_inode
===============

.. c:function:: struct inode *d_backing_inode (const struct dentry *upper)

    Get upper or lower inode we should be using

    :param const struct dentry \*upper:
        The upper layer


.. _`d_backing_inode.description`:

Description
-----------

This is the helper that should be used to get at the inode that will be used
if this dentry were to be opened as a file.  The inode may be on the upper
dentry or it may be on a lower dentry pinned by the upper.

Normal filesystems should not use this to access their own inodes.


.. _`d_backing_dentry`:

d_backing_dentry
================

.. c:function:: struct dentry *d_backing_dentry (struct dentry *upper)

    Get upper or lower dentry we should be using

    :param struct dentry \*upper:
        The upper layer


.. _`d_backing_dentry.description`:

Description
-----------

This is the helper that should be used to get the dentry of the inode that
will be used if this dentry were opened as a file.  It may be the upper
dentry or it may be a lower dentry pinned by the upper.

Normal filesystems should not use this to access their own dentries.


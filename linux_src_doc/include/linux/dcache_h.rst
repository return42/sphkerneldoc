.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dcache.h

.. _`dget_dlock`:

dget_dlock
==========

.. c:function:: struct dentry *dget_dlock(struct dentry *dentry)

    get a reference to a dentry

    :param dentry:
        dentry to get a reference to
    :type dentry: struct dentry \*

.. _`dget_dlock.description`:

Description
-----------

     Given a dentry or \ ``NULL``\  pointer increment the reference count
     if appropriate and return the dentry. A dentry will not be
     destroyed when it has references.

.. _`d_unhashed`:

d_unhashed
==========

.. c:function:: int d_unhashed(const struct dentry *dentry)

    is dentry hashed

    :param dentry:
        entry to check
    :type dentry: const struct dentry \*

.. _`d_unhashed.description`:

Description
-----------

     Returns true if the dentry passed is not currently hashed.

.. _`d_really_is_negative`:

d_really_is_negative
====================

.. c:function:: bool d_really_is_negative(const struct dentry *dentry)

    Determine if a dentry is really negative (ignoring fallthroughs)

    :param dentry:
        The dentry in question
    :type dentry: const struct dentry \*

.. _`d_really_is_negative.description`:

Description
-----------

Returns true if the dentry represents either an absent name or a name that
doesn't map to an inode (ie. ->d_inode is NULL).  The dentry could represent
a true miss, a whiteout that isn't represented by a 0,0 chardev or a
fallthrough marker in an opaque directory.

Note!  (1) This should be used *only* by a filesystem to examine its own
dentries.  It should not be used to look at some other filesystem's
dentries.  (2) It should also be used in combination with \ :c:func:`d_inode`\  to get
the inode.  (3) The dentry may have something attached to ->d_lower and the
type field of the flags may be set to something other than miss or whiteout.

.. _`d_really_is_positive`:

d_really_is_positive
====================

.. c:function:: bool d_really_is_positive(const struct dentry *dentry)

    Determine if a dentry is really positive (ignoring fallthroughs)

    :param dentry:
        The dentry in question
    :type dentry: const struct dentry \*

.. _`d_really_is_positive.description`:

Description
-----------

Returns true if the dentry represents a name that maps to an inode
(ie. ->d_inode is not NULL).  The dentry might still represent a whiteout if
that is represented on medium as a 0,0 chardev.

Note!  (1) This should be used *only* by a filesystem to examine its own
dentries.  It should not be used to look at some other filesystem's
dentries.  (2) It should also be used in combination with \ :c:func:`d_inode`\  to get
the inode.

.. _`d_inode`:

d_inode
=======

.. c:function:: struct inode *d_inode(const struct dentry *dentry)

    Get the actual inode of this dentry

    :param dentry:
        The dentry to query
    :type dentry: const struct dentry \*

.. _`d_inode.description`:

Description
-----------

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.

.. _`d_inode_rcu`:

d_inode_rcu
===========

.. c:function:: struct inode *d_inode_rcu(const struct dentry *dentry)

    Get the actual inode of this dentry with \ :c:func:`READ_ONCE`\ 

    :param dentry:
        The dentry to query
    :type dentry: const struct dentry \*

.. _`d_inode_rcu.description`:

Description
-----------

This is the helper normal filesystems should use to get at their own inodes
in their own dentries and ignore the layering superimposed upon them.

.. _`d_backing_inode`:

d_backing_inode
===============

.. c:function:: struct inode *d_backing_inode(const struct dentry *upper)

    Get upper or lower inode we should be using

    :param upper:
        The upper layer
    :type upper: const struct dentry \*

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

.. c:function:: struct dentry *d_backing_dentry(struct dentry *upper)

    Get upper or lower dentry we should be using

    :param upper:
        The upper layer
    :type upper: struct dentry \*

.. _`d_backing_dentry.description`:

Description
-----------

This is the helper that should be used to get the dentry of the inode that
will be used if this dentry were opened as a file.  It may be the upper
dentry or it may be a lower dentry pinned by the upper.

Normal filesystems should not use this to access their own dentries.

.. _`d_real`:

d_real
======

.. c:function:: struct dentry *d_real(struct dentry *dentry, const struct inode *inode)

    Return the real dentry

    :param dentry:
        the dentry to query
    :type dentry: struct dentry \*

    :param inode:
        inode to select the dentry from multiple layers (can be NULL)
    :type inode: const struct inode \*

.. _`d_real.description`:

Description
-----------

If dentry is on a union/overlay, then return the underlying, real dentry.
Otherwise return the dentry itself.

See also: Documentation/filesystems/vfs.txt

.. _`d_real_inode`:

d_real_inode
============

.. c:function:: struct inode *d_real_inode(const struct dentry *dentry)

    Return the real inode

    :param dentry:
        The dentry to query
    :type dentry: const struct dentry \*

.. _`d_real_inode.description`:

Description
-----------

If dentry is on a union/overlay, then return the underlying, real inode.
Otherwise return \ :c:func:`d_inode`\ .

.. This file was automatic generated / don't edit.


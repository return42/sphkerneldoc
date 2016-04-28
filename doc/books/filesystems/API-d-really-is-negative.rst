.. -*- coding: utf-8; mode: rst -*-

.. _API-d-really-is-negative:

====================
d_really_is_negative
====================

*man d_really_is_negative(9)*

*4.6.0-rc5*

Determine if a dentry is really negative (ignoring fallthroughs)


Synopsis
========

.. c:function:: bool d_really_is_negative( const struct dentry * dentry )

Arguments
=========

``dentry``
    The dentry in question


Description
===========

Returns true if the dentry represents either an absent name or a name
that doesn't map to an inode (ie. ->d_inode is NULL). The dentry could
represent a true miss, a whiteout that isn't represented by a 0,0
chardev or a fallthrough marker in an opaque directory.

Note! (1) This should be used *only* by a filesystem to examine its own
dentries. It should not be used to look at some other filesystem's
dentries. (2) It should also be used in combination with ``d_inode`` to
get the inode. (3) The dentry may have something attached to ->d_lower
and the type field of the flags may be set to something other than miss
or whiteout.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

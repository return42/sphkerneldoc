
.. _API-d-really-is-positive:

====================
d_really_is_positive
====================

*man d_really_is_positive(9)*

*4.6.0-rc1*

Determine if a dentry is really positive (ignoring fallthroughs)


Synopsis
========

.. c:function:: bool d_really_is_positive( const struct dentry * dentry )

Arguments
=========

``dentry``
    The dentry in question


Description
===========

Returns true if the dentry represents a name that maps to an inode (ie. ->d_inode is not NULL). The dentry might still represent a whiteout if that is represented on medium as a
0,0 chardev.

Note! (1) This should be used ⋆only⋆ by a filesystem to examine its own dentries. It should not be used to look at some other filesystem's dentries. (2) It should also be used in
combination with ``d_inode`` to get the inode.

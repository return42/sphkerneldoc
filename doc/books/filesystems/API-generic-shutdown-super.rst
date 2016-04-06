
.. _API-generic-shutdown-super:

======================
generic_shutdown_super
======================

*man generic_shutdown_super(9)*

*4.6.0-rc1*

common helper for ->``kill_sb``


Synopsis
========

.. c:function:: void generic_shutdown_super( struct super_block * sb )

Arguments
=========

``sb``
    superblock to kill


Description
===========

``generic_shutdown_super`` does all fs-independent work on superblock shutdown. Typical ->``kill_sb`` should pick all fs-specific objects that need destruction out of superblock,
call ``generic_shutdown_super`` and release aforementioned objects. Note: dentries and inodes _are_ taken care of and do not need specific handling.

Upon calling this function, the filesystem may no longer alter or rearrange the set of dentries belonging to this super_block, nor may it change the attachments of dentries to
inodes.


.. _API-deactivate-super:

================
deactivate_super
================

*man deactivate_super(9)*

*4.6.0-rc1*

drop an active reference to superblock


Synopsis
========

.. c:function:: void deactivate_super( struct super_block * s )

Arguments
=========

``s``
    superblock to deactivate


Description
===========

Variant of ``deactivate_locked_super``, except that superblock is ⋆not⋆ locked by caller. If we are going to drop the final active reference, lock will be acquired prior to that.

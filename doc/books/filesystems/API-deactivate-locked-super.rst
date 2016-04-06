
.. _API-deactivate-locked-super:

=======================
deactivate_locked_super
=======================

*man deactivate_locked_super(9)*

*4.6.0-rc1*

drop an active reference to superblock


Synopsis
========

.. c:function:: void deactivate_locked_super( struct super_block * s )

Arguments
=========

``s``
    superblock to deactivate


Description
===========

Drops an active reference to superblock, converting it into a temprory one if there is no other active references left. In that case we tell fs driver to shut it down and drop the
temporary reference we had just acquired.

Caller holds exclusive lock on superblock; that lock is released.

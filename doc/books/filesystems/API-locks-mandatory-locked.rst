
.. _API-locks-mandatory-locked:

======================
locks_mandatory_locked
======================

*man locks_mandatory_locked(9)*

*4.6.0-rc1*

Check for an active lock


Synopsis
========

.. c:function:: int locks_mandatory_locked( struct file * file )

Arguments
=========

``file``
    the file to check


Description
===========

Searches the inode's list of locks to find any POSIX locks which conflict. This function is called from ``locks_verify_locked`` only.

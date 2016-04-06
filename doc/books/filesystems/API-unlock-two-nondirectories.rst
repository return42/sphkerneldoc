
.. _API-unlock-two-nondirectories:

=========================
unlock_two_nondirectories
=========================

*man unlock_two_nondirectories(9)*

*4.6.0-rc1*

release locks from ``lock_two_nondirectories``


Synopsis
========

.. c:function:: void unlock_two_nondirectories( struct inode * inode1, struct inode * inode2 )

Arguments
=========

``inode1``
    first inode to unlock

``inode2``
    second inode to unlock

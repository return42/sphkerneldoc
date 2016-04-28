.. -*- coding: utf-8; mode: rst -*-

.. _API-locks-mandatory-locked:

======================
locks_mandatory_locked
======================

*man locks_mandatory_locked(9)*

*4.6.0-rc5*

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

Searches the inode's list of locks to find any POSIX locks which
conflict. This function is called from ``locks_verify_locked`` only.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

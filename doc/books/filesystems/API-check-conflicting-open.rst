.. -*- coding: utf-8; mode: rst -*-

.. _API-check-conflicting-open:

======================
check_conflicting_open
======================

*man check_conflicting_open(9)*

*4.6.0-rc5*

see if the given dentry points to a file that has an existing open that
would conflict with the desired lease.


Synopsis
========

.. c:function:: int check_conflicting_open( const struct dentry * dentry, const long arg, int flags )

Arguments
=========

``dentry``
    dentry to check

``arg``
    type of lease that we're trying to acquire

``flags``
    current lock flags


Description
===========

Check to see if there's an existing open fd on this file that would
conflict with the lease we're trying to set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

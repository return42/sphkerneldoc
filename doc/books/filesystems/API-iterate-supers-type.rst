.. -*- coding: utf-8; mode: rst -*-

.. _API-iterate-supers-type:

===================
iterate_supers_type
===================

*man iterate_supers_type(9)*

*4.6.0-rc5*

call function for superblocks of given type


Synopsis
========

.. c:function:: void iterate_supers_type( struct file_system_type * type, void (*f) struct super_block *, void *, void * arg )

Arguments
=========

``type``
    fs type

``f``
    function to call

``arg``
    argument to pass to it


Description
===========

Scans the superblock list and calls given function, passing it locked
superblock and given argument.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

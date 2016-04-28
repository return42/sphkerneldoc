.. -*- coding: utf-8; mode: rst -*-

.. _API-cdev-alloc:

==========
cdev_alloc
==========

*man cdev_alloc(9)*

*4.6.0-rc5*

allocate a cdev structure


Synopsis
========

.. c:function:: struct cdev * cdev_alloc( void )

Arguments
=========

``void``
    no arguments


Description
===========

Allocates and returns a cdev structure, or NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

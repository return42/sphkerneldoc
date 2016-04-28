.. -*- coding: utf-8; mode: rst -*-

.. _API-kgdb-arch-exit:

==============
kgdb_arch_exit
==============

*man kgdb_arch_exit(9)*

*4.6.0-rc5*

Perform any architecture specific uninitalization.


Synopsis
========

.. c:function:: void kgdb_arch_exit( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function will handle the uninitalization of any architecture
specific callbacks, for dynamic registration and unregistration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

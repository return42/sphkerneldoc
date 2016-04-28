.. -*- coding: utf-8; mode: rst -*-

.. _API-kgdb-arch-late:

==============
kgdb_arch_late
==============

*man kgdb_arch_late(9)*

*4.6.0-rc5*

Perform any architecture specific initalization.


Synopsis
========

.. c:function:: void kgdb_arch_late( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function will handle the late initalization of any architecture
specific callbacks. This is an optional function for handling things
like late initialization of hw breakpoints. The default implementation
does nothing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

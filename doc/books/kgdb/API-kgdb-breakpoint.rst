.. -*- coding: utf-8; mode: rst -*-

.. _API-kgdb-breakpoint:

===============
kgdb_breakpoint
===============

*man kgdb_breakpoint(9)*

*4.6.0-rc5*

compiled in breakpoint


Synopsis
========

.. c:function:: void kgdb_breakpoint( void )

Arguments
=========

``void``
    no arguments


Description
===========

This will be implemented as a static inline per architecture. This
function is called by the kgdb core to execute an architecture specific
trap to cause kgdb to enter the exception processing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

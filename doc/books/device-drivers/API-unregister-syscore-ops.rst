.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-syscore-ops:

======================
unregister_syscore_ops
======================

*man unregister_syscore_ops(9)*

*4.6.0-rc5*

Unregister a set of system core operations.


Synopsis
========

.. c:function:: void unregister_syscore_ops( struct syscore_ops * ops )

Arguments
=========

``ops``
    System core operations to unregister.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

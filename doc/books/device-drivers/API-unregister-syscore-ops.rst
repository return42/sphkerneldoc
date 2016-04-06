
.. _API-unregister-syscore-ops:

======================
unregister_syscore_ops
======================

*man unregister_syscore_ops(9)*

*4.6.0-rc1*

Unregister a set of system core operations.


Synopsis
========

.. c:function:: void unregister_syscore_ops( struct syscore_ops * ops )

Arguments
=========

``ops``
    System core operations to unregister.

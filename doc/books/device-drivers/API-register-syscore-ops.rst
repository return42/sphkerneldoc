
.. _API-register-syscore-ops:

====================
register_syscore_ops
====================

*man register_syscore_ops(9)*

*4.6.0-rc1*

Register a set of system core operations.


Synopsis
========

.. c:function:: void register_syscore_ops( struct syscore_ops * ops )

Arguments
=========

``ops``
    System core operations to register.

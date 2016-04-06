
.. _API-srcu-barrier:

============
srcu_barrier
============

*man srcu_barrier(9)*

*4.6.0-rc1*

Wait until all in-flight ``call_srcu`` callbacks complete.


Synopsis
========

.. c:function:: void srcu_barrier( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct on which to wait for in-flight callbacks.

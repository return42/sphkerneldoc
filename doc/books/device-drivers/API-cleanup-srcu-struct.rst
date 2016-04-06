
.. _API-cleanup-srcu-struct:

===================
cleanup_srcu_struct
===================

*man cleanup_srcu_struct(9)*

*4.6.0-rc1*

deconstruct a sleep-RCU structure


Synopsis
========

.. c:function:: void cleanup_srcu_struct( struct srcu_struct * sp )

Arguments
=========

``sp``
    structure to clean up.


Description
===========

Must invoke this after you are finished using a given srcu_struct that was initialized via ``init_srcu_struct``, else you leak memory.

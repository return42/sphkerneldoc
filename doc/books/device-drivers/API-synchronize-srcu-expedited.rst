
.. _API-synchronize-srcu-expedited:

==========================
synchronize_srcu_expedited
==========================

*man synchronize_srcu_expedited(9)*

*4.6.0-rc1*

Brute-force SRCU grace period


Synopsis
========

.. c:function:: void synchronize_srcu_expedited( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct with which to synchronize.


Description
===========

Wait for an SRCU grace period to elapse, but be more aggressive about spinning rather than blocking when waiting.

Note that ``synchronize_srcu_expedited`` has the same deadlock and memory-ordering properties as does ``synchronize_srcu``.

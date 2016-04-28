.. -*- coding: utf-8; mode: rst -*-

.. _API-cond-synchronize-rcu:

====================
cond_synchronize_rcu
====================

*man cond_synchronize_rcu(9)*

*4.6.0-rc5*

Conditionally wait for an RCU grace period


Synopsis
========

.. c:function:: void cond_synchronize_rcu( unsigned long oldstate )

Arguments
=========

``oldstate``
    return value from earlier call to ``get_state_synchronize_rcu``


Description
===========

If a full RCU grace period has elapsed since the earlier call to
``get_state_synchronize_rcu``, just return. Otherwise, invoke
``synchronize_rcu`` to wait for a full grace period.

Yes, this function does not take counter wrap into account. But counter
wrap is harmless. If the counter wraps, we have waited for more than 2
billion grace periods (and way more on a 64-bit system!), so waiting for
one additional grace period should be just fine.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

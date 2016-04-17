.. -*- coding: utf-8; mode: rst -*-

=========
rcutree.h
=========


.. _`synchronize_rcu_bh_expedited`:

synchronize_rcu_bh_expedited
============================

.. c:function:: void synchronize_rcu_bh_expedited ( void)

    Brute-force RCU-bh grace period

    :param void:
        no arguments



.. _`synchronize_rcu_bh_expedited.description`:

Description
-----------


Wait for an RCU-bh grace period to elapse, but use a "big hammer"
approach to force the grace period to end quickly.  This consumes
significant time on all CPUs and is unfriendly to real-time workloads,
so is thus not recommended for any sort of common-case code.  In fact,
if you are using :c:func:`synchronize_rcu_bh_expedited` in a loop, please
restructure your code to batch your updates, and then use a single
:c:func:`synchronize_rcu_bh` instead.

Note that it is illegal to call this function while holding any lock
that is acquired by a CPU-hotplug notifier.  And yes, it is also illegal
to call this function from a CPU-hotplug notifier.  Failing to observe
these restriction will result in deadlock.


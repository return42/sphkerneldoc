.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rcupdate_wait.h

.. _`synchronize_rcu_mult`:

synchronize_rcu_mult
====================

.. c:function::  synchronize_rcu_mult( ...)

    Wait concurrently for multiple grace periods

    :param ... :
        List of \ :c:func:`call_rcu`\  functions for the flavors to wait on.

.. _`synchronize_rcu_mult.description`:

Description
-----------

This macro waits concurrently for multiple flavors of RCU grace periods.
For example, synchronize_rcu_mult(call_rcu, call_rcu_bh) would wait
on concurrent RCU and RCU-bh grace periods.  Waiting on a give SRCU
domain requires you to write a wrapper function for that SRCU domain's
\ :c:func:`call_srcu`\  function, supplying the corresponding srcu_struct.

If Tiny RCU, tell \_wait_rcu_gp() not to bother waiting for RCU
or RCU-bh, given that anywhere \ :c:func:`synchronize_rcu_mult`\  can be called
is automatically a grace period.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/sync.c

.. _`rcu_sync_init`:

rcu_sync_init
=============

.. c:function:: void rcu_sync_init(struct rcu_sync *rsp, enum rcu_sync_type type)

    Initialize an rcu_sync structure

    :param struct rcu_sync \*rsp:
        Pointer to rcu_sync structure to be initialized

    :param enum rcu_sync_type type:
        Flavor of RCU with which to synchronize rcu_sync structure

.. _`rcu_sync_enter_start`:

rcu_sync_enter_start
====================

.. c:function:: void rcu_sync_enter_start(struct rcu_sync *rsp)

    :param struct rcu_sync \*rsp:
        *undescribed*

.. _`rcu_sync_enter_start.description`:

Description
-----------

Ensures \ :c:func:`rcu_sync_is_idle`\  returns false and rcu_sync_{enter,exit}()
pairs turn into NO-OPs.

.. _`rcu_sync_enter`:

rcu_sync_enter
==============

.. c:function:: void rcu_sync_enter(struct rcu_sync *rsp)

    Force readers onto slowpath

    :param struct rcu_sync \*rsp:
        Pointer to rcu_sync structure to use for synchronization

.. _`rcu_sync_enter.description`:

Description
-----------

This function is used by updaters who need readers to make use of
a slowpath during the update.  After this function returns, all
subsequent calls to \ :c:func:`rcu_sync_is_idle`\  will return false, which
tells readers to stay off their fastpaths.  A later call to
\ :c:func:`rcu_sync_exit`\  re-enables reader slowpaths.

When called in isolation, \ :c:func:`rcu_sync_enter`\  must wait for a grace
period, however, closely spaced calls to \ :c:func:`rcu_sync_enter`\  can
optimize away the grace-period wait via a state machine implemented
by \ :c:func:`rcu_sync_enter`\ , \ :c:func:`rcu_sync_exit`\ , and \ :c:func:`rcu_sync_func`\ .

.. _`rcu_sync_func`:

rcu_sync_func
=============

.. c:function:: void rcu_sync_func(struct rcu_head *rcu)

    Callback function managing reader access to fastpath

    :param struct rcu_head \*rcu:
        *undescribed*

.. _`rcu_sync_func.description`:

Description
-----------

This function is passed to one of the \ :c:func:`call_rcu`\  functions by
\ :c:func:`rcu_sync_exit`\ , so that it is invoked after a grace period following the
that invocation of \ :c:func:`rcu_sync_exit`\ .  It takes action based on events that
have taken place in the meantime, so that closely spaced \ :c:func:`rcu_sync_enter`\ 
and \ :c:func:`rcu_sync_exit`\  pairs need not wait for a grace period.

If another \ :c:func:`rcu_sync_enter`\  is invoked before the grace period
ended, reset state to allow the next \ :c:func:`rcu_sync_exit`\  to let the
readers back onto their fastpaths (after a grace period).  If both
another \ :c:func:`rcu_sync_enter`\  and its matching \ :c:func:`rcu_sync_exit`\  are invoked
before the grace period ended, re-invoke \ :c:func:`call_rcu`\  on behalf of that
\ :c:func:`rcu_sync_exit`\ .  Otherwise, set all state back to idle so that readers
can again use their fastpaths.

.. _`rcu_sync_exit`:

rcu_sync_exit
=============

.. c:function:: void rcu_sync_exit(struct rcu_sync *rsp)

    Allow readers back onto fast patch after grace period

    :param struct rcu_sync \*rsp:
        Pointer to rcu_sync structure to use for synchronization

.. _`rcu_sync_exit.description`:

Description
-----------

This function is used by updaters who have completed, and can therefore
now allow readers to make use of their fastpaths after a grace period
has elapsed.  After this grace period has completed, all subsequent
calls to \ :c:func:`rcu_sync_is_idle`\  will return true, which tells readers that
they can once again use their fastpaths.

.. _`rcu_sync_dtor`:

rcu_sync_dtor
=============

.. c:function:: void rcu_sync_dtor(struct rcu_sync *rsp)

    Clean up an rcu_sync structure

    :param struct rcu_sync \*rsp:
        Pointer to rcu_sync structure to be cleaned up

.. This file was automatic generated / don't edit.


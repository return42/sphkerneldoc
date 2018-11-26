.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/cell/spufs/sched.c

.. _`spu_bind_context`:

spu_bind_context
================

.. c:function:: void spu_bind_context(struct spu *spu, struct spu_context *ctx)

    bind spu context to physical spu

    :param spu:
        physical spu to bind to
    :type spu: struct spu \*

    :param ctx:
        context to bind
    :type ctx: struct spu_context \*

.. _`spu_unbind_context`:

spu_unbind_context
==================

.. c:function:: void spu_unbind_context(struct spu *spu, struct spu_context *ctx)

    unbind spu context from physical spu

    :param spu:
        physical spu to unbind from
    :type spu: struct spu \*

    :param ctx:
        context to unbind
    :type ctx: struct spu_context \*

.. _`__spu_add_to_rq`:

\__spu_add_to_rq
================

.. c:function:: void __spu_add_to_rq(struct spu_context *ctx)

    add a context to the runqueue

    :param ctx:
        context to add
    :type ctx: struct spu_context \*

.. _`find_victim`:

find_victim
===========

.. c:function:: struct spu *find_victim(struct spu_context *ctx)

    find a lower priority context to preempt

    :param ctx:
        candidate context for running
    :type ctx: struct spu_context \*

.. _`find_victim.description`:

Description
-----------

Returns the freed physical spu to run the new context on.

.. _`spu_unschedule`:

spu_unschedule
==============

.. c:function:: void spu_unschedule(struct spu *spu, struct spu_context *ctx, int free_spu)

    remove a context from a spu, and possibly release it.

    :param spu:
        The SPU to unschedule from
    :type spu: struct spu \*

    :param ctx:
        The context currently scheduled on the SPU
        \ ``free_spu``\     Whether to free the SPU for other contexts
    :type ctx: struct spu_context \*

    :param free_spu:
        *undescribed*
    :type free_spu: int

.. _`spu_unschedule.description`:

Description
-----------

Unbinds the context \ ``ctx``\  from the SPU \ ``spu``\ . If \ ``free_spu``\  is non-zero, the
SPU is made available for other contexts (ie, may be returned by
spu_get_idle). If this is zero, the caller is expected to schedule another
context to this spu.

Should be called with ctx->state_mutex held.

.. _`spu_activate`:

spu_activate
============

.. c:function:: int spu_activate(struct spu_context *ctx, unsigned long flags)

    find a free spu for a context and execute it

    :param ctx:
        spu context to schedule
    :type ctx: struct spu_context \*

    :param flags:
        flags (currently ignored)
    :type flags: unsigned long

.. _`spu_activate.description`:

Description
-----------

Tries to find a free spu to run \ ``ctx``\ .  If no free spu is available
add the context to the runqueue so it gets woken up once an spu
is available.

.. _`grab_runnable_context`:

grab_runnable_context
=====================

.. c:function:: struct spu_context *grab_runnable_context(int prio, int node)

    try to find a runnable context

    :param prio:
        *undescribed*
    :type prio: int

    :param node:
        *undescribed*
    :type node: int

.. _`grab_runnable_context.description`:

Description
-----------

Remove the highest priority context on the runqueue and return it
to the caller.  Returns \ ``NULL``\  if no runnable context was found.

.. _`spu_deactivate`:

spu_deactivate
==============

.. c:function:: void spu_deactivate(struct spu_context *ctx)

    unbind a context from it's physical spu

    :param ctx:
        spu context to unbind
    :type ctx: struct spu_context \*

.. _`spu_deactivate.description`:

Description
-----------

Unbind \ ``ctx``\  from the physical spu it is running on and schedule
the highest priority context to run on the freed physical spu.

.. _`spu_yield`:

spu_yield
=========

.. c:function:: void spu_yield(struct spu_context *ctx)

    yield a physical spu if others are waiting

    :param ctx:
        spu context to yield
    :type ctx: struct spu_context \*

.. _`spu_yield.description`:

Description
-----------

Check if there is a higher priority context waiting and if yes
unbind \ ``ctx``\  from the physical spu and schedule the highest
priority context to run on the freed physical spu instead.

.. _`count_active_contexts`:

count_active_contexts
=====================

.. c:function:: unsigned long count_active_contexts( void)

    count nr of active tasks

    :param void:
        no arguments
    :type void: 

.. _`count_active_contexts.description`:

Description
-----------

Return the number of tasks currently running or waiting to run.

Note that we don't take runq_lock / list_mutex here.  Reading
a single 32bit value is atomic on powerpc, and we don't care
about memory ordering issues here.

.. _`spu_calc_load`:

spu_calc_load
=============

.. c:function:: void spu_calc_load( void)

    update the avenrun load estimates.

    :param void:
        no arguments
    :type void: 

.. _`spu_calc_load.description`:

Description
-----------

No locking against reading these values from userspace, as for
the CPU loadavg code.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/percpu_counter.c

.. _`percpu_counter_add_batch`:

percpu_counter_add_batch
========================

.. c:function:: void percpu_counter_add_batch(struct percpu_counter *fbc, s64 amount, s32 batch)

    preemption disable. The latter is guaranteed by the fact that the slow path is explicitly protected by an irq-safe spinlock whereas the fast patch uses this_cpu_add which is irq-safe by definition. Hence there is no need muck with irq state before calling this one

    :param struct percpu_counter \*fbc:
        *undescribed*

    :param s64 amount:
        *undescribed*

    :param s32 batch:
        *undescribed*

.. This file was automatic generated / don't edit.


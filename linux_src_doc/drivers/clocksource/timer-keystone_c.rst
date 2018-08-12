.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/timer-keystone.c

.. _`keystone_timer_barrier`:

keystone_timer_barrier
======================

.. c:function:: void keystone_timer_barrier( void)

    write memory barrier use explicit barrier to avoid using readl/writel non relaxed function variants, because in our case non relaxed variants hide the true places where barrier is needed.

    :param  void:
        no arguments

.. _`keystone_timer_config`:

keystone_timer_config
=====================

.. c:function:: int keystone_timer_config(u64 period, int mask)

    configures timer to work in oneshot/periodic modes. \ ````\  mask: mask of the mode to configure \ ````\  period: cycles number to configure for

    :param u64 period:
        *undescribed*

    :param int mask:
        *undescribed*

.. This file was automatic generated / don't edit.


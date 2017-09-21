.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/swait.h

.. _`swait_event_idle`:

swait_event_idle
================

.. c:function::  swait_event_idle( wq,  condition)

    wait without system load contribution

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

.. _`swait_event_idle.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the \ ``condition``\  evaluates to
true. The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

This function is mostly used when a kthread or workqueue waits for some
condition and doesn't want to contribute to system load. Signals are
ignored.

.. _`swait_event_idle_timeout`:

swait_event_idle_timeout
========================

.. c:function::  swait_event_idle_timeout( wq,  condition,  timeout)

    wait up to timeout without load contribution

    :param  wq:
        the waitqueue to wait on

    :param  condition:
        a C expression for the event to wait for

    :param  timeout:
        timeout at which we'll give up in jiffies

.. _`swait_event_idle_timeout.description`:

Description
-----------

The process is put to sleep (TASK_IDLE) until the \ ``condition``\  evaluates to
true. The \ ``condition``\  is checked each time the waitqueue \ ``wq``\  is woken up.

This function is mostly used when a kthread or workqueue waits for some
condition and doesn't want to contribute to system load. Signals are
ignored.

.. _`swait_event_idle_timeout.return`:

Return
------

0 if the \ ``condition``\  evaluated to \ ``false``\  after the \ ``timeout``\  elapsed,
1 if the \ ``condition``\  evaluated to \ ``true``\  after the \ ``timeout``\  elapsed,
or the remaining jiffies (at least 1) if the \ ``condition``\  evaluated
to \ ``true``\  before the \ ``timeout``\  elapsed.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

============
mpic_timer.c
============


.. _`mpic_start_timer`:

mpic_start_timer
================

.. c:function:: void mpic_start_timer (struct mpic_timer *handle)

    start hardware timer

    :param struct mpic_timer \*handle:
        the timer to be started.



.. _`mpic_start_timer.description`:

Description
-----------

It will do ->fn(->dev) callback from the hardware interrupt at
the ->timeval point in the future.



.. _`mpic_stop_timer`:

mpic_stop_timer
===============

.. c:function:: void mpic_stop_timer (struct mpic_timer *handle)

    stop hardware timer

    :param struct mpic_timer \*handle:
        the timer to be stoped



.. _`mpic_stop_timer.description`:

Description
-----------

The timer periodically generates an interrupt. Unless user stops the timer.



.. _`mpic_get_remain_time`:

mpic_get_remain_time
====================

.. c:function:: void mpic_get_remain_time (struct mpic_timer *handle, struct timeval *time)

    get timer time

    :param struct mpic_timer \*handle:
        the timer to be selected.

    :param struct timeval \*time:
        time for timer



.. _`mpic_get_remain_time.description`:

Description
-----------

Query timer remaining time.



.. _`mpic_free_timer`:

mpic_free_timer
===============

.. c:function:: void mpic_free_timer (struct mpic_timer *handle)

    free hardware timer

    :param struct mpic_timer \*handle:
        the timer to be removed.



.. _`mpic_free_timer.description`:

Description
-----------

Free the timer.



.. _`mpic_free_timer.note`:

Note
----

can not be used in interrupt context.



.. _`mpic_request_timer`:

mpic_request_timer
==================

.. c:function:: struct mpic_timer *mpic_request_timer (irq_handler_t fn, void *dev, const struct timeval *time)

    get a hardware timer

    :param irq_handler_t fn:
        interrupt handler function

    :param void \*dev:
        callback function of the data

    :param const struct timeval \*time:
        time for timer



.. _`mpic_request_timer.description`:

Description
-----------

This executes the "request_irq", returning NULL
else "handle" on success.


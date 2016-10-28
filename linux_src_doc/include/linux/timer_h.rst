.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/timer.h

.. _`timer_pending`:

timer_pending
=============

.. c:function:: int timer_pending(const struct timer_list *timer)

    is a timer pending?

    :param const struct timer_list \*timer:
        the timer in question

.. _`timer_pending.description`:

Description
-----------

timer_pending will tell whether a given timer is currently pending,
or not. Callers must ensure serialization wrt. other operations done
to this timer, eg. interrupt contexts, or other CPUs on SMP.

.. _`timer_pending.return-value`:

return value
------------

1 if the timer is pending, 0 if not.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/timer.h

.. _`timer_setup`:

timer_setup
===========

.. c:function::  timer_setup( timer,  callback,  flags)

    prepare a timer for first use

    :param  timer:
        the timer in question

    :param  callback:
        the function to call when timer expires

    :param  flags:
        any TIMER\_\* flags

.. _`timer_setup.description`:

Description
-----------

Regular timer initialization should use either \ :c:func:`DEFINE_TIMER`\  above,
or \ :c:func:`timer_setup`\ . For timers on the stack, \ :c:func:`timer_setup_on_stack`\  must
be used and must be balanced with a call to \ :c:func:`destroy_timer_on_stack`\ .

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


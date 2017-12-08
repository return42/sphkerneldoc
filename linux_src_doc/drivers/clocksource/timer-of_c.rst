.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/timer-of.c

.. _`timer_of_cleanup`:

timer_of_cleanup
================

.. c:function:: void timer_of_cleanup(struct timer_of *to)

    release timer_of ressources

    :param struct timer_of \*to:
        timer_of structure

.. _`timer_of_cleanup.description`:

Description
-----------

Release the ressources that has been used in \ :c:func:`timer_of_init`\ .
This function should be called in init error cases

.. This file was automatic generated / don't edit.


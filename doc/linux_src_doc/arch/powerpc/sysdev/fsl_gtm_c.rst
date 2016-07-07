.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/fsl_gtm.c

.. _`gtm_get_timer16`:

gtm_get_timer16
===============

.. c:function:: struct gtm_timer *gtm_get_timer16( void)

    request GTM timer to use it with the rest of GTM API

    :param  void:
        no arguments

.. _`gtm_get_timer16.context`:

Context
-------

non-IRQ

.. _`gtm_get_timer16.description`:

Description
-----------

This function reserves GTM timer for later use. It returns gtm_timer
structure to use with the rest of GTM API, you should use timer->irq
to manage timer interrupt.

.. _`gtm_get_specific_timer16`:

gtm_get_specific_timer16
========================

.. c:function:: struct gtm_timer *gtm_get_specific_timer16(struct gtm *gtm, unsigned int timer)

    request specific GTM timer

    :param struct gtm \*gtm:
        specific GTM, pass here GTM's device_node->data

    :param unsigned int timer:
        specific timer number, Timer1 is 0.

.. _`gtm_get_specific_timer16.context`:

Context
-------

non-IRQ

.. _`gtm_get_specific_timer16.description`:

Description
-----------

This function reserves GTM timer for later use. It returns gtm_timer
structure to use with the rest of GTM API, you should use timer->irq
to manage timer interrupt.

.. _`gtm_put_timer16`:

gtm_put_timer16
===============

.. c:function:: void gtm_put_timer16(struct gtm_timer *tmr)

    release 16 bits GTM timer

    :param struct gtm_timer \*tmr:
        pointer to the gtm_timer structure obtained from gtm_get_timer

.. _`gtm_put_timer16.context`:

Context
-------

any

.. _`gtm_put_timer16.description`:

Description
-----------

This function releases GTM timer so others may request it.

.. _`gtm_set_timer16`:

gtm_set_timer16
===============

.. c:function:: int gtm_set_timer16(struct gtm_timer *tmr, unsigned long usec, bool reload)

    (re)set 16 bit timer with arbitrary precision

    :param struct gtm_timer \*tmr:
        pointer to the gtm_timer structure obtained from gtm_get_timer

    :param unsigned long usec:
        timer interval in microseconds

    :param bool reload:
        if set, the timer will reset upon expiry rather than
        continue running free.

.. _`gtm_set_timer16.context`:

Context
-------

any

.. _`gtm_set_timer16.description`:

Description
-----------

This function (re)sets the GTM timer so that it counts up to the requested
interval value, and fires the interrupt when the value is reached. This
function will reduce the precision of the timer as needed in order for the
requested timeout to fit in a 16-bit register.

.. _`gtm_set_exact_timer16`:

gtm_set_exact_timer16
=====================

.. c:function:: int gtm_set_exact_timer16(struct gtm_timer *tmr, u16 usec, bool reload)

    (re)set 16 bits timer

    :param struct gtm_timer \*tmr:
        pointer to the gtm_timer structure obtained from gtm_get_timer

    :param u16 usec:
        timer interval in microseconds

    :param bool reload:
        if set, the timer will reset upon expiry rather than
        continue running free.

.. _`gtm_set_exact_timer16.context`:

Context
-------

any

.. _`gtm_set_exact_timer16.description`:

Description
-----------

This function (re)sets GTM timer so that it counts up to the requested
interval value, and fires the interrupt when the value is reached. If reload
flag was set, timer will also reset itself upon reference value, otherwise
it continues to increment.

The \_exact\_ bit in the function name states that this function will not
crop precision of the "usec" argument, thus usec is limited to 16 bits
(single timer width).

.. _`gtm_stop_timer16`:

gtm_stop_timer16
================

.. c:function:: void gtm_stop_timer16(struct gtm_timer *tmr)

    stop single timer

    :param struct gtm_timer \*tmr:
        pointer to the gtm_timer structure obtained from gtm_get_timer

.. _`gtm_stop_timer16.context`:

Context
-------

any

.. _`gtm_stop_timer16.description`:

Description
-----------

This function simply stops the GTM timer.

.. _`gtm_ack_timer16`:

gtm_ack_timer16
===============

.. c:function:: void gtm_ack_timer16(struct gtm_timer *tmr, u16 events)

    acknowledge timer event (free-run timers only)

    :param struct gtm_timer \*tmr:
        pointer to the gtm_timer structure obtained from gtm_get_timer

    :param u16 events:
        events mask to ack

.. _`gtm_ack_timer16.context`:

Context
-------

any

.. _`gtm_ack_timer16.description`:

Description
-----------

Thus function used to acknowledge timer interrupt event, use it inside the
interrupt handler.

.. This file was automatic generated / don't edit.


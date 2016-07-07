.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/clock.h

.. _`meta_clock_desc`:

struct meta_clock_desc
======================

.. c:type:: struct meta_clock_desc

    Meta Core clock callbacks.

.. _`meta_clock_desc.definition`:

Definition
----------

.. code-block:: c

    struct meta_clock_desc {
        unsigned long (* get_core_freq) (void);
    }

.. _`meta_clock_desc.members`:

Members
-------

get_core_freq
    Get the frequency of the Meta core. If this is NULL, the
    core frequency will be determined like this:
    Meta 1: based on loops_per_jiffy.
    Meta 2: (EXPAND_TIMER_DIV + 1) MHz.
    If a "core" clock is provided by the device tree, it
    will override this function.

.. _`get_coreclock`:

get_coreclock
=============

.. c:function:: unsigned long get_coreclock( void)

    Get the frequency of the Meta core clock.

    :param  void:
        no arguments

.. _`get_coreclock.return`:

Return
------

The Meta core clock frequency in Hz.

.. This file was automatic generated / don't edit.


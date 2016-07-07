.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/clocksource.h

.. _`arch_clocksource_data`:

struct arch_clocksource_data
============================

.. c:type:: struct arch_clocksource_data

    Architecture-specific clocksource information.

.. _`arch_clocksource_data.definition`:

Definition
----------

.. code-block:: c

    struct arch_clocksource_data {
        u8 vdso_clock_mode;
    }

.. _`arch_clocksource_data.members`:

Members
-------

vdso_clock_mode
    Method the VDSO should use to access the clocksource.

.. This file was automatic generated / don't edit.


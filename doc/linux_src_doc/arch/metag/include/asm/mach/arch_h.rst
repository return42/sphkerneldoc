.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/mach/arch.h

.. _`machine_desc`:

struct machine_desc
===================

.. c:type:: struct machine_desc

    Describes a board controlled by a Meta.

.. _`machine_desc.definition`:

Definition
----------

.. code-block:: c

    struct machine_desc {
        const char *name;
        const char **dt_compat;
        struct meta_clock_desc *clocks;
        unsigned int nr_irqs;
        void (* init_early) (void);
        void (* init_irq) (void);
        void (* init_machine) (void);
        void (* init_late) (void);
    }

.. _`machine_desc.members`:

Members
-------

name
    Board/SoC name.

dt_compat
    Array of device tree 'compatible' strings.

clocks
    Clock callbacks.

nr_irqs
    Maximum number of IRQs.
    If 0, defaults to NR_IRQS in asm-generic/irq.h.

init_early
    Early init callback.

init_irq
    IRQ init callback for setting up IRQ controllers.

init_machine
    Arch init callback for setting up devices.

init_late
    Late init callback.

.. _`machine_desc.description`:

Description
-----------

This structure is provided by each board which can be controlled by a Meta.
It is chosen by matching the compatible strings in the device tree provided
by the bootloader with the strings in \ ``dt_compat``\ , and sets up any aspects of
the machine that aren't configured with device tree (yet).

.. This file was automatic generated / don't edit.


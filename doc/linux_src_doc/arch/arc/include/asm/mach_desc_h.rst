.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arc/include/asm/mach_desc.h

.. _`machine_desc`:

struct machine_desc
===================

.. c:type:: struct machine_desc

    Board specific callbacks, called from ARC common code Provided by each ARC board using \ :c:func:`MACHINE_START`\ /\ :c:func:`MACHINE_END`\ , so a multi-platform kernel builds with array of such descriptors. We extend the early DT scan to also match the DT's "compatible" string against the \ ``dt_compat``\  of all such descriptors, and one with highest "DT score" is selected as global \ ``machine_desc``\ .

.. _`machine_desc.definition`:

Definition
----------

.. code-block:: c

    struct machine_desc {
        const char *name;
        const char **dt_compat;
        void (* init_early) (void);
        #ifdef CONFIG_SMP
        void (* init_per_cpu) (unsigned int);
        #endif
        void (* init_machine) (void);
        void (* init_late) (void);
    }

.. _`machine_desc.members`:

Members
-------

name
    Board/SoC name

dt_compat
    Array of device tree 'compatible' strings
    (XXX: although only 1st entry is looked at)

init_early
    Very early callback [called from \ :c:func:`setup_arch`\ ]

init_per_cpu
    for each CPU as it is coming up (SMP as well as UP)
    [(M):\ :c:func:`init_IRQ`\ , (o):\ :c:func:`start_kernel_secondary`\ ]

init_machine
    arch initcall level callback (e.g. populate static
    platform devices or parse Devicetree)

init_late
    Late initcall level callback

.. This file was automatic generated / don't edit.


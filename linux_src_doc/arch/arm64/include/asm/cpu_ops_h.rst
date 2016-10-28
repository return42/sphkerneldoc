.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/include/asm/cpu_ops.h

.. _`cpu_operations`:

struct cpu_operations
=====================

.. c:type:: struct cpu_operations

    Callback operations for hotplugging CPUs.

.. _`cpu_operations.definition`:

Definition
----------

.. code-block:: c

    struct cpu_operations {
        const char *name;
        int (*cpu_init)(unsigned int);
        int (*cpu_prepare)(unsigned int);
        int (*cpu_boot)(unsigned int);
        void (*cpu_postboot)(void);
    #ifdef CONFIG_HOTPLUG_CPU
        int (*cpu_disable)(unsigned int cpu);
        void (*cpu_die)(unsigned int cpu);
        int (*cpu_kill)(unsigned int cpu);
    #endif
    #ifdef CONFIG_CPU_IDLE
        int (*cpu_init_idle)(unsigned int);
        int (*cpu_suspend)(unsigned long);
    #endif
    }

.. _`cpu_operations.members`:

Members
-------

name
    Name of the property as appears in a devicetree cpu node's
    enable-method property. On systems booting with ACPI, \ ``name``\ 
    identifies the struct cpu_operations entry corresponding to
    the boot protocol specified in the ACPI MADT table.

cpu_init
    Reads any data necessary for a specific enable-method for a
    proposed logical id.

cpu_prepare
    Early one-time preparation step for a cpu. If there is a
    mechanism for doing so, tests whether it is possible to boot
    the given CPU.

cpu_boot
    Boots a cpu into the kernel.

cpu_postboot
    Optionally, perform any post-boot cleanup or necesary
    synchronisation. Called from the cpu being booted.

cpu_disable
    Prepares a cpu to die. May fail for some mechanism-specific
    reason, which will cause the hot unplug to be aborted. Called
    from the cpu to be killed.

cpu_die
    Makes a cpu leave the kernel. Must not fail. Called from the
    cpu being killed.

cpu_kill
    Ensures a cpu has left the kernel. Called from another cpu.

cpu_init_idle
    Reads any data necessary to initialize CPU idle states for
    a proposed logical id.

cpu_suspend
    Suspends a cpu and saves the required context. May fail owing
    to wrong parameters or error conditions. Called from the
    CPU being suspended. Must be called with IRQs disabled.

.. This file was automatic generated / don't edit.


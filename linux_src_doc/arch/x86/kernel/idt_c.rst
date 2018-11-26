.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/idt.c

.. _`idt_setup_early_traps`:

idt_setup_early_traps
=====================

.. c:function:: void idt_setup_early_traps( void)

    Initialize the idt table with early traps

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_early_traps.description`:

Description
-----------

On X8664 these traps do not use interrupt stacks as they can't work
before \ :c:func:`cpu_init`\  is invoked and sets up TSS. The IST variants are
installed after that.

.. _`idt_setup_traps`:

idt_setup_traps
===============

.. c:function:: void idt_setup_traps( void)

    Initialize the idt table with default traps

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_early_pf`:

idt_setup_early_pf
==================

.. c:function:: void idt_setup_early_pf( void)

    Initialize the idt table with early pagefault handler

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_early_pf.description`:

Description
-----------

On X8664 this does not use interrupt stacks as they can't work before
\ :c:func:`cpu_init`\  is invoked and sets up TSS. The IST variant is installed
after that.

.. _`idt_setup_early_pf.fixme`:

FIXME
-----

Why is 32bit and 64bit installing the PF handler at different
places in the early setup code?

.. _`idt_setup_ist_traps`:

idt_setup_ist_traps
===================

.. c:function:: void idt_setup_ist_traps( void)

    Initialize the idt table with traps using IST

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_debugidt_traps`:

idt_setup_debugidt_traps
========================

.. c:function:: void idt_setup_debugidt_traps( void)

    Initialize the debug idt table with debug traps

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_apic_and_irq_gates`:

idt_setup_apic_and_irq_gates
============================

.. c:function:: void idt_setup_apic_and_irq_gates( void)

    Setup APIC/SMP and normal interrupt gates

    :param void:
        no arguments
    :type void: 

.. _`idt_setup_early_handler`:

idt_setup_early_handler
=======================

.. c:function:: void idt_setup_early_handler( void)

    Initializes the idt table with early handlers

    :param void:
        no arguments
    :type void: 

.. _`idt_invalidate`:

idt_invalidate
==============

.. c:function:: void idt_invalidate(void *addr)

    Invalidate interrupt descriptor table

    :param addr:
        The virtual address of the 'invalid' IDT
    :type addr: void \*

.. This file was automatic generated / don't edit.


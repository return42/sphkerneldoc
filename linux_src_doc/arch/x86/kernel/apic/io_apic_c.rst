.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/apic/io_apic.c

.. _`disable_ioapic_support`:

disable_ioapic_support
======================

.. c:function:: void disable_ioapic_support( void)

    disables ioapic support at runtime

    :param void:
        no arguments
    :type void: 

.. _`mp_register_ioapic`:

mp_register_ioapic
==================

.. c:function:: int mp_register_ioapic(int id, u32 address, u32 gsi_base, struct ioapic_domain_cfg *cfg)

    Register an IOAPIC device

    :param id:
        hardware IOAPIC ID
    :type id: int

    :param address:
        physical address of IOAPIC register area
    :type address: u32

    :param gsi_base:
        base of GSI associated with the IOAPIC
    :type gsi_base: u32

    :param cfg:
        configuration information for the IOAPIC
    :type cfg: struct ioapic_domain_cfg \*

.. This file was automatic generated / don't edit.


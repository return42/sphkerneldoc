.. -*- coding: utf-8; mode: rst -*-

=========
io_apic.c
=========


.. _`disable_ioapic_support`:

disable_ioapic_support
======================

.. c:function:: void disable_ioapic_support ( void)

    disables ioapic support at runtime

    :param void:
        no arguments



.. _`mp_register_ioapic`:

mp_register_ioapic
==================

.. c:function:: int mp_register_ioapic (int id, u32 address, u32 gsi_base, struct ioapic_domain_cfg *cfg)

    Register an IOAPIC device

    :param int id:
        hardware IOAPIC ID

    :param u32 address:
        physical address of IOAPIC register area

    :param u32 gsi_base:
        base of GSI associated with the IOAPIC

    :param struct ioapic_domain_cfg \*cfg:
        configuration information for the IOAPIC


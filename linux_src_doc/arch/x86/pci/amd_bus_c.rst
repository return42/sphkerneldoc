.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/pci/amd_bus.c

.. _`early_root_info_init`:

early_root_info_init
====================

.. c:function:: int early_root_info_init( void)

    called before pcibios_scan_root and pci_scan_bus fills the mp_bus_to_cpumask array based according to the LDT Bus Number Registers found in the northbridge.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


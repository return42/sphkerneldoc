.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/mips-cpc.c

.. _`mips_cpc_phys_base`:

mips_cpc_phys_base
==================

.. c:function:: phys_addr_t mips_cpc_phys_base( void)

    retrieve the physical base address of the CPC

    :param  void:
        no arguments

.. _`mips_cpc_phys_base.description`:

Description
-----------

This function returns the physical base address of the Cluster Power
Controller memory mapped registers, or 0 if no Cluster Power Controller
is present.

.. This file was automatic generated / don't edit.


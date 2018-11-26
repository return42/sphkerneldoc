.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kernel/devtree.c

.. _`setup_machine_fdt`:

setup_machine_fdt
=================

.. c:function:: const struct machine_desc *setup_machine_fdt(unsigned int dt_phys)

    Machine setup when an dtb was passed to the kernel

    :param dt_phys:
        physical address of dt blob
    :type dt_phys: unsigned int

.. _`setup_machine_fdt.description`:

Description
-----------

If a dtb was passed to the kernel in r2, then use it to choose the
correct machine_desc and to setup the system.

.. This file was automatic generated / don't edit.


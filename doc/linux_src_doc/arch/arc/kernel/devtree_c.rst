.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arc/kernel/devtree.c

.. _`setup_machine_fdt`:

setup_machine_fdt
=================

.. c:function:: const struct machine_desc *setup_machine_fdt(void *dt)

    Machine setup when an dtb was passed to the kernel

    :param void \*dt:
        virtual address pointer to dt blob

.. _`setup_machine_fdt.description`:

Description
-----------

If a dtb was passed to the kernel, then use it to choose the correct
machine_desc and to setup the system.

.. This file was automatic generated / don't edit.


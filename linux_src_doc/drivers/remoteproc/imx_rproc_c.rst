.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/imx_rproc.c

.. _`imx_rproc_mem`:

struct imx_rproc_mem
====================

.. c:type:: struct imx_rproc_mem

    slim internal memory structure

.. _`imx_rproc_mem.definition`:

Definition
----------

.. code-block:: c

    struct imx_rproc_mem {
        void __iomem *cpu_addr;
        phys_addr_t sys_addr;
        size_t size;
    }

.. _`imx_rproc_mem.members`:

Members
-------

cpu_addr
    MPU virtual address of the memory region

sys_addr
    Bus address used to access the memory region

size
    Size of the memory region

.. This file was automatic generated / don't edit.


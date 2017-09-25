.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/wkup_m3_rproc.c

.. _`wkup_m3_mem`:

struct wkup_m3_mem
==================

.. c:type:: struct wkup_m3_mem

    WkupM3 internal memory structure

.. _`wkup_m3_mem.definition`:

Definition
----------

.. code-block:: c

    struct wkup_m3_mem {
        void __iomem *cpu_addr;
        phys_addr_t bus_addr;
        u32 dev_addr;
        size_t size;
    }

.. _`wkup_m3_mem.members`:

Members
-------

cpu_addr
    MPU virtual address of the memory region

bus_addr
    Bus address used to access the memory region

dev_addr
    Device address from Wakeup M3 view

size
    Size of the memory region

.. _`wkup_m3_rproc`:

struct wkup_m3_rproc
====================

.. c:type:: struct wkup_m3_rproc

    WkupM3 remote processor state

.. _`wkup_m3_rproc.definition`:

Definition
----------

.. code-block:: c

    struct wkup_m3_rproc {
        struct rproc *rproc;
        struct platform_device *pdev;
        struct wkup_m3_mem mem[WKUPM3_MEM_MAX];
    }

.. _`wkup_m3_rproc.members`:

Members
-------

rproc
    rproc handle

pdev
    pointer to platform device

mem
    WkupM3 memory information

.. This file was automatic generated / don't edit.


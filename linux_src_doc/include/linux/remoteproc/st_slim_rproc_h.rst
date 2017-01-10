.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/remoteproc/st_slim_rproc.h

.. _`st_slim_mem`:

struct st_slim_mem
==================

.. c:type:: struct st_slim_mem

    slim internal memory structure

.. _`st_slim_mem.definition`:

Definition
----------

.. code-block:: c

    struct st_slim_mem {
        void __iomem *cpu_addr;
        phys_addr_t bus_addr;
        size_t size;
    }

.. _`st_slim_mem.members`:

Members
-------

cpu_addr
    MPU virtual address of the memory region

bus_addr
    Bus address used to access the memory region

size
    Size of the memory region

.. _`st_slim_rproc`:

struct st_slim_rproc
====================

.. c:type:: struct st_slim_rproc

    SLIM slim core

.. _`st_slim_rproc.definition`:

Definition
----------

.. code-block:: c

    struct st_slim_rproc {
        struct rproc *rproc;
        struct st_slim_mem mem[ST_SLIM_MEM_MAX];
        void __iomem *slimcore;
        void __iomem *peri;
        struct clk  *clks[ST_SLIM_MAX_CLK];
    }

.. _`st_slim_rproc.members`:

Members
-------

rproc
    rproc handle

mem
    slim memory information

slimcore
    slim slimcore regs

peri
    slim peripheral regs

clks
    slim clocks

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/keystone_remoteproc.c

.. _`keystone_rproc_mem`:

struct keystone_rproc_mem
=========================

.. c:type:: struct keystone_rproc_mem

    internal memory structure

.. _`keystone_rproc_mem.definition`:

Definition
----------

.. code-block:: c

    struct keystone_rproc_mem {
        void __iomem *cpu_addr;
        phys_addr_t bus_addr;
        u32 dev_addr;
        size_t size;
    }

.. _`keystone_rproc_mem.members`:

Members
-------

cpu_addr
    MPU virtual address of the memory region

bus_addr
    Bus address used to access the memory region

dev_addr
    Device address of the memory region from DSP view

size
    Size of the memory region

.. _`keystone_rproc`:

struct keystone_rproc
=====================

.. c:type:: struct keystone_rproc

    keystone remote processor driver structure

.. _`keystone_rproc.definition`:

Definition
----------

.. code-block:: c

    struct keystone_rproc {
        struct device *dev;
        struct rproc *rproc;
        struct keystone_rproc_mem *mem;
        int num_mems;
        struct regmap *dev_ctrl;
        struct reset_control *reset;
        u32 boot_offset;
        int irq_ring;
        int irq_fault;
        int kick_gpio;
        struct work_struct workqueue;
    }

.. _`keystone_rproc.members`:

Members
-------

dev
    cached device pointer

rproc
    remoteproc device handle

mem
    internal memory regions data

num_mems
    number of internal memory regions

dev_ctrl
    device control regmap handle

reset
    reset control handle

boot_offset
    boot register offset in \ ``dev_ctrl``\  regmap

irq_ring
    irq entry for vring

irq_fault
    irq entry for exception

kick_gpio
    gpio used for virtio kicks

workqueue
    workqueue for processing virtio interrupts

.. This file was automatic generated / don't edit.


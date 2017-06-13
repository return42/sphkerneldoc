.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-vpu/mtk_vpu.c

.. _`init_timeout_ms`:

INIT_TIMEOUT_MS
===============

.. c:function::  INIT_TIMEOUT_MS()

    related to video codec, scaling and color format converting. VPU interfaces with other blocks by share memory and interrupt.

.. _`vpu_fw_type`:

enum vpu_fw_type
================

.. c:type:: enum vpu_fw_type

    VPU firmware type

.. _`vpu_fw_type.definition`:

Definition
----------

.. code-block:: c

    enum vpu_fw_type {
        P_FW,
        D_FW
    };

.. _`vpu_fw_type.constants`:

Constants
---------

P_FW
    program firmware

D_FW
    data firmware

.. _`vpu_mem`:

struct vpu_mem
==============

.. c:type:: struct vpu_mem

    VPU extended program/data memory information

.. _`vpu_mem.definition`:

Definition
----------

.. code-block:: c

    struct vpu_mem {
        void *va;
        dma_addr_t pa;
    }

.. _`vpu_mem.members`:

Members
-------

va
    the kernel virtual memory address of VPU extended memory

pa
    the physical memory address of VPU extended memory

.. _`vpu_regs`:

struct vpu_regs
===============

.. c:type:: struct vpu_regs

    VPU TCM and configuration registers

.. _`vpu_regs.definition`:

Definition
----------

.. code-block:: c

    struct vpu_regs {
        void __iomem *tcm;
        void __iomem *cfg;
        int irq;
    }

.. _`vpu_regs.members`:

Members
-------

tcm
    the register for VPU Tightly-Coupled Memory

cfg
    the register for VPU configuration

irq
    the irq number for VPU interrupt

.. _`vpu_wdt_handler`:

struct vpu_wdt_handler
======================

.. c:type:: struct vpu_wdt_handler

    VPU watchdog reset handler

.. _`vpu_wdt_handler.definition`:

Definition
----------

.. code-block:: c

    struct vpu_wdt_handler {
        void (*reset_func)(void *);
        void *priv;
    }

.. _`vpu_wdt_handler.members`:

Members
-------

reset_func
    reset handler

priv
    private data

.. _`vpu_wdt`:

struct vpu_wdt
==============

.. c:type:: struct vpu_wdt

    VPU watchdog workqueue

.. _`vpu_wdt.definition`:

Definition
----------

.. code-block:: c

    struct vpu_wdt {
        struct vpu_wdt_handler handler;
        struct work_struct ws;
        struct workqueue_struct *wq;
    }

.. _`vpu_wdt.members`:

Members
-------

handler
    VPU watchdog reset handler

ws
    workstruct for VPU watchdog

wq
    workqueue for VPU watchdog

.. _`vpu_run`:

struct vpu_run
==============

.. c:type:: struct vpu_run

    VPU initialization status

.. _`vpu_run.definition`:

Definition
----------

.. code-block:: c

    struct vpu_run {
        u32 signaled;
        char fw_ver;
        unsigned int dec_capability;
        unsigned int enc_capability;
        wait_queue_head_t wq;
    }

.. _`vpu_run.members`:

Members
-------

signaled
    the signal of vpu initialization completed

fw_ver
    VPU firmware version

dec_capability
    decoder capability which is not used for now and
    the value is reserved for future use

enc_capability
    encoder capability which is not used for now and
    the value is reserved for future use

wq
    wait queue for VPU initialization status

.. _`vpu_ipi_desc`:

struct vpu_ipi_desc
===================

.. c:type:: struct vpu_ipi_desc

    VPU IPI descriptor

.. _`vpu_ipi_desc.definition`:

Definition
----------

.. code-block:: c

    struct vpu_ipi_desc {
        ipi_handler_t handler;
        const char *name;
        void *priv;
    }

.. _`vpu_ipi_desc.members`:

Members
-------

handler
    IPI handler

name
    the name of IPI handler

priv
    the private data of IPI handler

.. _`share_obj`:

struct share_obj
================

.. c:type:: struct share_obj

    DTCM (Data Tightly-Coupled Memory) buffer shared with AP and VPU

.. _`share_obj.definition`:

Definition
----------

.. code-block:: c

    struct share_obj {
        s32 id;
        u32 len;
        unsigned char share_buf;
    }

.. _`share_obj.members`:

Members
-------

id
    IPI id

len
    share buffer length

share_buf
    share buffer data

.. _`mtk_vpu`:

struct mtk_vpu
==============

.. c:type:: struct mtk_vpu

    vpu driver data

.. _`mtk_vpu.definition`:

Definition
----------

.. code-block:: c

    struct mtk_vpu {
        struct vpu_mem extmem;
        struct vpu_regs reg;
        struct vpu_run run;
        struct vpu_wdt wdt;
        struct vpu_ipi_desc ipi_desc;
        struct share_obj *recv_buf;
        struct share_obj *send_buf;
        struct device *dev;
        struct clk *clk;
        bool fw_loaded;
        bool enable_4GB;
        struct mutex vpu_mutex;
        u32 wdt_refcnt;
        wait_queue_head_t ack_wq;
        bool ipi_id_ack;
    }

.. _`mtk_vpu.members`:

Members
-------

extmem
    VPU extended memory information

reg
    VPU TCM and configuration registers

run
    VPU initialization status

wdt
    *undescribed*

ipi_desc
    VPU IPI descriptor

recv_buf
    VPU DTCM share buffer for receiving. The
    receive buffer is only accessed in interrupt context.

send_buf
    VPU DTCM share buffer for sending

dev
    VPU struct device

clk
    VPU clock on/off

fw_loaded
    indicate VPU firmware loaded

enable_4GB
    VPU 4GB mode on/off

vpu_mutex
    protect mtk_vpu (except recv_buf) and ensure only
    one client to use VPU service at a time. For example,
    suppose a client is using VPU to decode VP8.
    If the other client wants to encode VP8,
    it has to wait until VP8 decode completes.
    \ ``wdt_refcnt``\           WDT reference count to make sure the watchdog can be
    disabled if no other client is using VPU service

wdt_refcnt
    *undescribed*

ack_wq
    The wait queue for each codec and mdp. When sleeping
    processes wake up, they will check the condition
    "ipi_id_ack" to run the corresponding action or
    go back to sleep.

ipi_id_ack
    The ACKs for registered IPI function sending
    interrupt to VPU

.. This file was automatic generated / don't edit.


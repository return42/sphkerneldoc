.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hsi/controllers/omap_ssi.h

.. _`omap_ssm_ctx`:

struct omap_ssm_ctx
===================

.. c:type:: struct omap_ssm_ctx

    OMAP synchronous serial module (TX/RX) context

.. _`omap_ssm_ctx.definition`:

Definition
----------

.. code-block:: c

    struct omap_ssm_ctx {
        u32 mode;
        u32 channels;
        u32 frame_size;
        union {unnamed_union};
    }

.. _`omap_ssm_ctx.members`:

Members
-------

mode
    Bit transmission mode

channels
    Number of channels

frame_size
    *undescribed*

{unnamed_union}
    anonymous


.. _`omap_ssi_port`:

struct omap_ssi_port
====================

.. c:type:: struct omap_ssi_port

    OMAP SSI port data

.. _`omap_ssi_port.definition`:

Definition
----------

.. code-block:: c

    struct omap_ssi_port {
        struct device *dev;
        struct device *pdev;
        dma_addr_t sst_dma;
        dma_addr_t ssr_dma;
        void __iomem *sst_base;
        void __iomem *ssr_base;
        spinlock_t wk_lock;
        spinlock_t lock;
        unsigned int channels;
        struct list_head txqueue[SSI_MAX_CHANNELS];
        struct list_head rxqueue[SSI_MAX_CHANNELS];
        struct list_head brkqueue;
        unsigned int irq;
        int wake_irq;
        struct gpio_desc *wake_gpio;
        struct tasklet_struct pio_tasklet;
        struct tasklet_struct wake_tasklet;
        bool wktest:1;
        bool wkin_cken:1;
        unsigned int wk_refcount;
        u32 sys_mpu_enable;
        struct omap_ssm_ctx sst;
        struct omap_ssm_ctx ssr;
        u32 loss_count;
        u32 port_id;
        #ifdef CONFIG_DEBUG_FS
        struct dentry *dir;
        #endif
    }

.. _`omap_ssi_port.members`:

Members
-------

dev
    device associated to the port (HSI port)

pdev
    platform device associated to the port

sst_dma
    SSI transmitter physical base address

ssr_dma
    SSI receiver physical base address

sst_base
    SSI transmitter base address

ssr_base
    SSI receiver base address

wk_lock
    spin lock to serialize access to the wake lines

lock
    Spin lock to serialize access to the SSI port

channels
    Current number of channels configured (1,2,4 or 8)

txqueue
    TX message queues

rxqueue
    RX message queues

brkqueue
    Queue of incoming HWBREAK requests (FRAME mode)

irq
    IRQ number

wake_irq
    IRQ number for incoming wake line (-1 if none)

wake_gpio
    GPIO number for incoming wake line (-1 if none)

pio_tasklet
    Bottom half for PIO transfers and events

wake_tasklet
    Bottom half for incoming wake events

wktest
    *undescribed*

wkin_cken
    Keep track of clock references due to the incoming wake line

wk_refcount
    Reference count for output wake line

sys_mpu_enable
    Context for the interrupt enable register for irq 0

sst
    Context for the synchronous serial transmitter

ssr
    Context for the synchronous serial receiver

loss_count
    *undescribed*

port_id
    *undescribed*

dir
    *undescribed*

.. _`gdd_trn`:

struct gdd_trn
==============

.. c:type:: struct gdd_trn

    GDD transaction data

.. _`gdd_trn.definition`:

Definition
----------

.. code-block:: c

    struct gdd_trn {
        struct hsi_msg *msg;
        struct scatterlist *sg;
    }

.. _`gdd_trn.members`:

Members
-------

msg
    Pointer to the HSI message being served

sg
    Pointer to the current sg entry being served

.. _`omap_ssi_controller`:

struct omap_ssi_controller
==========================

.. c:type:: struct omap_ssi_controller

    OMAP SSI controller data

.. _`omap_ssi_controller.definition`:

Definition
----------

.. code-block:: c

    struct omap_ssi_controller {
        struct device *dev;
        void __iomem *sys;
        void __iomem *gdd;
        struct clk *fck;
        unsigned int gdd_irq;
        struct tasklet_struct gdd_tasklet;
        struct gdd_trn gdd_trn[SSI_MAX_GDD_LCH];
        spinlock_t lock;
        struct notifier_block fck_nb;
        unsigned long fck_rate;
        u32 loss_count;
        u32 max_speed;
        u32 sysconfig;
        u32 gdd_gcr;
        int (*get_loss)(struct device *dev);
        struct omap_ssi_port **port;
        #ifdef CONFIG_DEBUG_FS
        struct dentry *dir;
        #endif
    }

.. _`omap_ssi_controller.members`:

Members
-------

dev
    device associated to the controller (HSI controller)

sys
    SSI I/O base address

gdd
    GDD I/O base address

fck
    SSI functional clock

gdd_irq
    IRQ line for GDD

gdd_tasklet
    bottom half for DMA transfers

gdd_trn
    Array of GDD transaction data for ongoing GDD transfers

lock
    lock to serialize access to GDD

fck_nb
    DVFS notfifier block

fck_rate
    clock rate

loss_count
    To follow if we need to restore context or not

max_speed
    Maximum TX speed (Kb/s) set by the clients.

sysconfig
    SSI controller saved context

gdd_gcr
    SSI GDD saved context

get_loss
    Pointer to omap_pm_get_dev_context_loss_count, if any

port
    Array of pointers of the ports of the controller

dir
    Debugfs SSI root directory

.. This file was automatic generated / don't edit.


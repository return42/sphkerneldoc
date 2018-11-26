.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fsl/bestcomm/bestcomm_priv.h

.. _`bcom_tdt`:

struct bcom_tdt
===============

.. c:type:: struct bcom_tdt

    Task Descriptor Table Entry

.. _`bcom_tdt.definition`:

Definition
----------

.. code-block:: c

    struct bcom_tdt {
        u32 start;
        u32 stop;
        u32 var;
        u32 fdt;
        u32 exec_status;
        u32 mvtp;
        u32 context;
        u32 litbase;
    }

.. _`bcom_tdt.members`:

Members
-------

start
    *undescribed*

stop
    *undescribed*

var
    *undescribed*

fdt
    *undescribed*

exec_status
    *undescribed*

mvtp
    *undescribed*

context
    *undescribed*

litbase
    *undescribed*

.. _`bcom_engine`:

struct bcom_engine
==================

.. c:type:: struct bcom_engine


.. _`bcom_engine.definition`:

Definition
----------

.. code-block:: c

    struct bcom_engine {
        struct device_node *ofnode;
        struct mpc52xx_sdma __iomem *regs;
        phys_addr_t regs_base;
        struct bcom_tdt *tdt;
        u32 *ctx;
        u32 *var;
        u32 *fdt;
        spinlock_t lock;
    }

.. _`bcom_engine.members`:

Members
-------

ofnode
    *undescribed*

regs
    *undescribed*

regs_base
    *undescribed*

tdt
    *undescribed*

ctx
    *undescribed*

var
    *undescribed*

fdt
    *undescribed*

lock
    *undescribed*

.. _`bcom_engine.description`:

Description
-----------

This holds all info needed globaly to handle the engine

.. _`bcom_disable_prefetch`:

bcom_disable_prefetch
=====================

.. c:function:: void bcom_disable_prefetch( void)

    Hook to disable bus prefetching

    :param void:
        no arguments
    :type void: 

.. _`bcom_disable_prefetch.description`:

Description
-----------

ATA DMA and the original MPC5200 need this due to silicon bugs.  At the
moment disabling prefetch is a one-way street.  There is no mechanism
in place to turn prefetch back on after it has been disabled.  There is
no reason it couldn't be done, it would just be more complex to implement.

.. This file was automatic generated / don't edit.


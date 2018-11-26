.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_interrupts.h

.. _`dpu_hw_intr`:

struct dpu_hw_intr
==================

.. c:type:: struct dpu_hw_intr

    hw interrupts handling data structure

.. _`dpu_hw_intr.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_intr {
        struct dpu_hw_blk_reg_map hw;
        struct dpu_hw_intr_ops ops;
        u32 *cache_irq_mask;
        u32 *save_irq_status;
        u32 irq_idx_tbl_size;
        spinlock_t irq_lock;
    }

.. _`dpu_hw_intr.members`:

Members
-------

hw
    virtual address mapping

ops
    function pointer mapping for IRQ handling

cache_irq_mask
    array of IRQ enable masks reg storage created during init

save_irq_status
    array of IRQ status reg storage created during init

irq_idx_tbl_size
    total number of irq_idx mapped in the hw_interrupts

irq_lock
    spinlock for accessing IRQ resources

.. _`dpu_hw_intr_init`:

dpu_hw_intr_init
================

.. c:function:: struct dpu_hw_intr *dpu_hw_intr_init(void __iomem *addr, struct dpu_mdss_cfg *m)

    Initializes the interrupts hw object

    :param addr:
        mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        pointer to mdss catalog data
    :type m: struct dpu_mdss_cfg \*

.. _`dpu_hw_intr_destroy`:

dpu_hw_intr_destroy
===================

.. c:function:: void dpu_hw_intr_destroy(struct dpu_hw_intr *intr)

    Cleanup interrutps hw object

    :param intr:
        pointer to interrupts hw object
    :type intr: struct dpu_hw_intr \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_core_irq.h

.. _`dpu_core_irq_preinstall`:

dpu_core_irq_preinstall
=======================

.. c:function:: void dpu_core_irq_preinstall(struct dpu_kms *dpu_kms)

    perform pre-installation of core IRQ handler

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_core_irq_postinstall`:

dpu_core_irq_postinstall
========================

.. c:function:: int dpu_core_irq_postinstall(struct dpu_kms *dpu_kms)

    perform post-installation of core IRQ handler

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_core_irq_uninstall`:

dpu_core_irq_uninstall
======================

.. c:function:: void dpu_core_irq_uninstall(struct dpu_kms *dpu_kms)

    uninstall core IRQ handler

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_core_irq`:

dpu_core_irq
============

.. c:function:: irqreturn_t dpu_core_irq(struct dpu_kms *dpu_kms)

    core IRQ handler

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_core_irq_idx_lookup`:

dpu_core_irq_idx_lookup
=======================

.. c:function:: int dpu_core_irq_idx_lookup(struct dpu_kms *dpu_kms, enum dpu_intr_type intr_type, uint32_t instance_idx)

    IRQ helper function for lookup irq_idx from HW interrupt mapping table.

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param intr_type:
        DPU HW interrupt type for lookup
    :type intr_type: enum dpu_intr_type

    :param instance_idx:
        DPU HW block instance defined in dpu_hw_mdss.h
    :type instance_idx: uint32_t

.. _`dpu_core_irq_enable`:

dpu_core_irq_enable
===================

.. c:function:: int dpu_core_irq_enable(struct dpu_kms *dpu_kms, int *irq_idxs, uint32_t irq_count)

    IRQ helper function for enabling one or more IRQs

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param irq_idxs:
        Array of irq index
    :type irq_idxs: int \*

    :param irq_count:
        Number of irq_idx provided in the array
    :type irq_count: uint32_t

.. _`dpu_core_irq_enable.description`:

Description
-----------

This function increments count on each enable and decrements on each
disable.  Interrupts is enabled if count is 0 before increment.

.. _`dpu_core_irq_disable`:

dpu_core_irq_disable
====================

.. c:function:: int dpu_core_irq_disable(struct dpu_kms *dpu_kms, int *irq_idxs, uint32_t irq_count)

    IRQ helper function for disabling one of more IRQs

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param irq_idxs:
        Array of irq index
    :type irq_idxs: int \*

    :param irq_count:
        Number of irq_idx provided in the array
    :type irq_count: uint32_t

.. _`dpu_core_irq_disable.description`:

Description
-----------

This function increments count on each enable and decrements on each
disable.  Interrupts is disabled if count is 0 after decrement.

.. _`dpu_core_irq_read`:

dpu_core_irq_read
=================

.. c:function:: u32 dpu_core_irq_read(struct dpu_kms *dpu_kms, int irq_idx, bool clear)

    IRQ helper function for reading IRQ status

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param irq_idx:
        irq index
    :type irq_idx: int

    :param clear:
        True to clear the irq after read
    :type clear: bool

.. _`dpu_core_irq_register_callback`:

dpu_core_irq_register_callback
==============================

.. c:function:: int dpu_core_irq_register_callback(struct dpu_kms *dpu_kms, int irq_idx, struct dpu_irq_callback *irq_cb)

    For registering callback function on IRQ interrupt

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param irq_idx:
        irq index
    :type irq_idx: int

    :param irq_cb:
        IRQ callback structure, containing callback function
        and argument. Passing NULL for irq_cb will unregister
        the callback for the given irq_idx
        This must exist until un-registration.
    :type irq_cb: struct dpu_irq_callback \*

.. _`dpu_core_irq_register_callback.description`:

Description
-----------

This function supports registration of multiple callbacks for each interrupt.

.. _`dpu_core_irq_unregister_callback`:

dpu_core_irq_unregister_callback
================================

.. c:function:: int dpu_core_irq_unregister_callback(struct dpu_kms *dpu_kms, int irq_idx, struct dpu_irq_callback *irq_cb)

    For unregistering callback function on IRQ interrupt

    :param dpu_kms:
        DPU handle
    :type dpu_kms: struct dpu_kms \*

    :param irq_idx:
        irq index
    :type irq_idx: int

    :param irq_cb:
        IRQ callback structure, containing callback function
        and argument. Passing NULL for irq_cb will unregister
        the callback for the given irq_idx
        This must match with registration.
    :type irq_cb: struct dpu_irq_callback \*

.. _`dpu_core_irq_unregister_callback.description`:

Description
-----------

This function supports registration of multiple callbacks for each interrupt.

.. _`dpu_debugfs_core_irq_init`:

dpu_debugfs_core_irq_init
=========================

.. c:function:: int dpu_debugfs_core_irq_init(struct dpu_kms *dpu_kms, struct dentry *parent)

    register core irq debugfs

    :param dpu_kms:
        pointer to kms
    :type dpu_kms: struct dpu_kms \*

    :param parent:
        debugfs directory root
    :type parent: struct dentry \*

.. _`dpu_debugfs_core_irq_destroy`:

dpu_debugfs_core_irq_destroy
============================

.. c:function:: void dpu_debugfs_core_irq_destroy(struct dpu_kms *dpu_kms)

    deregister core irq debugfs

    :param dpu_kms:
        pointer to kms
    :type dpu_kms: struct dpu_kms \*

.. This file was automatic generated / don't edit.


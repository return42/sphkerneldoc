.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c

.. _`interrupt-handling`:

Interrupt Handling
==================

Interrupts generated within GPU hardware raise interrupt requests that are
passed to amdgpu IRQ handler which is responsible for detecting source and
type of the interrupt and dispatching matching handlers. If handling an
interrupt requires calling kernel functions that may sleep processing is
dispatched to work handlers.

If MSI functionality is not disabled by module parameter then MSI
support will be enabled.

For GPU interrupt sources that may be driven by another driver, IRQ domain
support is used (with mapping between virtual and hardware IRQs).

.. _`amdgpu_hotplug_work_func`:

amdgpu_hotplug_work_func
========================

.. c:function:: void amdgpu_hotplug_work_func(struct work_struct *work)

    work handler for display hotplug event

    :param work:
        work struct pointer
    :type work: struct work_struct \*

.. _`amdgpu_hotplug_work_func.description`:

Description
-----------

This is the hotplug event work handler (all ASICs).
The work gets scheduled from the IRQ handler if there
was a hotplug interrupt.  It walks through the connector table
and calls hotplug handler for each connector. After this, it sends
a DRM hotplug event to alert userspace.

This design approach is required in order to defer hotplug event handling
from the IRQ handler to a work handler because hotplug handler has to use
mutexes which cannot be locked in an IRQ handler (since \ :c:type:`struct mutex_lock <mutex_lock>`\  may
sleep).

.. _`amdgpu_irq_reset_work_func`:

amdgpu_irq_reset_work_func
==========================

.. c:function:: void amdgpu_irq_reset_work_func(struct work_struct *work)

    execute GPU reset

    :param work:
        work struct pointer
    :type work: struct work_struct \*

.. _`amdgpu_irq_reset_work_func.description`:

Description
-----------

Execute scheduled GPU reset (Cayman+).
This function is called when the IRQ handler thinks we need a GPU reset.

.. _`amdgpu_irq_disable_all`:

amdgpu_irq_disable_all
======================

.. c:function:: void amdgpu_irq_disable_all(struct amdgpu_device *adev)

    disable *all* interrupts

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_disable_all.description`:

Description
-----------

Disable all types of interrupts from all sources.

.. _`amdgpu_irq_callback`:

amdgpu_irq_callback
===================

.. c:function:: void amdgpu_irq_callback(struct amdgpu_device *adev, struct amdgpu_ih_ring *ih)

    callback from the IH ring

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param ih:
        amdgpu ih ring
    :type ih: struct amdgpu_ih_ring \*

.. _`amdgpu_irq_callback.description`:

Description
-----------

Callback from IH ring processing to handle the entry at the current position
and advance the read pointer.

.. _`amdgpu_irq_handler`:

amdgpu_irq_handler
==================

.. c:function:: irqreturn_t amdgpu_irq_handler(int irq, void *arg)

    IRQ handler

    :param irq:
        IRQ number (unused)
    :type irq: int

    :param arg:
        pointer to DRM device
    :type arg: void \*

.. _`amdgpu_irq_handler.description`:

Description
-----------

IRQ handler for amdgpu driver (all ASICs).

.. _`amdgpu_irq_handler.return`:

Return
------

result of handling the IRQ, as defined by \ :c:type:`struct irqreturn_t <irqreturn_t>`\ 

.. _`amdgpu_msi_ok`:

amdgpu_msi_ok
=============

.. c:function:: bool amdgpu_msi_ok(struct amdgpu_device *adev)

    check whether MSI functionality is enabled

    :param adev:
        amdgpu device pointer (unused)
    :type adev: struct amdgpu_device \*

.. _`amdgpu_msi_ok.description`:

Description
-----------

Checks whether MSI functionality has been disabled via module parameter
(all ASICs).

.. _`amdgpu_msi_ok.return`:

Return
------

*true* if MSIs are allowed to be enabled or *false* otherwise

.. _`amdgpu_irq_init`:

amdgpu_irq_init
===============

.. c:function:: int amdgpu_irq_init(struct amdgpu_device *adev)

    initialize interrupt handling

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_init.description`:

Description
-----------

Sets up work functions for hotplug and reset interrupts, enables MSI
functionality, initializes vblank, hotplug and reset interrupt handling.

.. _`amdgpu_irq_init.return`:

Return
------

0 on success or error code on failure

.. _`amdgpu_irq_fini`:

amdgpu_irq_fini
===============

.. c:function:: void amdgpu_irq_fini(struct amdgpu_device *adev)

    shut down interrupt handling

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_fini.description`:

Description
-----------

Tears down work functions for hotplug and reset interrupts, disables MSI
functionality, shuts down vblank, hotplug and reset interrupt handling,
turns off interrupts from all sources (all ASICs).

.. _`amdgpu_irq_add_id`:

amdgpu_irq_add_id
=================

.. c:function:: int amdgpu_irq_add_id(struct amdgpu_device *adev, unsigned client_id, unsigned src_id, struct amdgpu_irq_src *source)

    register IRQ source

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param client_id:
        client id
    :type client_id: unsigned

    :param src_id:
        source id
    :type src_id: unsigned

    :param source:
        IRQ source pointer
    :type source: struct amdgpu_irq_src \*

.. _`amdgpu_irq_add_id.description`:

Description
-----------

Registers IRQ source on a client.

.. _`amdgpu_irq_add_id.return`:

Return
------

0 on success or error code otherwise

.. _`amdgpu_irq_dispatch`:

amdgpu_irq_dispatch
===================

.. c:function:: void amdgpu_irq_dispatch(struct amdgpu_device *adev, struct amdgpu_iv_entry *entry)

    dispatch IRQ to IP blocks

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param entry:
        interrupt vector pointer
    :type entry: struct amdgpu_iv_entry \*

.. _`amdgpu_irq_dispatch.description`:

Description
-----------

Dispatches IRQ to IP blocks.

.. _`amdgpu_irq_update`:

amdgpu_irq_update
=================

.. c:function:: int amdgpu_irq_update(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    update hardware interrupt state

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param src:
        interrupt source pointer
    :type src: struct amdgpu_irq_src \*

    :param type:
        type of interrupt
    :type type: unsigned

.. _`amdgpu_irq_update.description`:

Description
-----------

Updates interrupt state for the specific source (all ASICs).

.. _`amdgpu_irq_gpu_reset_resume_helper`:

amdgpu_irq_gpu_reset_resume_helper
==================================

.. c:function:: void amdgpu_irq_gpu_reset_resume_helper(struct amdgpu_device *adev)

    update interrupt states on all sources

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_gpu_reset_resume_helper.description`:

Description
-----------

Updates state of all types of interrupts on all sources on resume after
reset.

.. _`amdgpu_irq_get`:

amdgpu_irq_get
==============

.. c:function:: int amdgpu_irq_get(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    enable interrupt

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param src:
        interrupt source pointer
    :type src: struct amdgpu_irq_src \*

    :param type:
        type of interrupt
    :type type: unsigned

.. _`amdgpu_irq_get.description`:

Description
-----------

Enables specified type of interrupt on the specified source (all ASICs).

.. _`amdgpu_irq_get.return`:

Return
------

0 on success or error code otherwise

.. _`amdgpu_irq_put`:

amdgpu_irq_put
==============

.. c:function:: int amdgpu_irq_put(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    disable interrupt

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param src:
        interrupt source pointer
    :type src: struct amdgpu_irq_src \*

    :param type:
        type of interrupt
    :type type: unsigned

.. _`amdgpu_irq_put.description`:

Description
-----------

Enables specified type of interrupt on the specified source (all ASICs).

.. _`amdgpu_irq_put.return`:

Return
------

0 on success or error code otherwise

.. _`amdgpu_irq_enabled`:

amdgpu_irq_enabled
==================

.. c:function:: bool amdgpu_irq_enabled(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    check whether interrupt is enabled or not

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param src:
        interrupt source pointer
    :type src: struct amdgpu_irq_src \*

    :param type:
        type of interrupt
    :type type: unsigned

.. _`amdgpu_irq_enabled.description`:

Description
-----------

Checks whether the given type of interrupt is enabled on the given source.

.. _`amdgpu_irq_enabled.return`:

Return
------

*true* if interrupt is enabled, *false* if interrupt is disabled or on
invalid parameters

.. _`amdgpu_irqdomain_map`:

amdgpu_irqdomain_map
====================

.. c:function:: int amdgpu_irqdomain_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hwirq)

    create mapping between virtual and hardware IRQ numbers

    :param d:
        amdgpu IRQ domain pointer (unused)
    :type d: struct irq_domain \*

    :param irq:
        virtual IRQ number
    :type irq: unsigned int

    :param hwirq:
        hardware irq number
    :type hwirq: irq_hw_number_t

.. _`amdgpu_irqdomain_map.description`:

Description
-----------

Current implementation assigns simple interrupt handler to the given virtual
IRQ.

.. _`amdgpu_irqdomain_map.return`:

Return
------

0 on success or error code otherwise

.. _`amdgpu_irq_add_domain`:

amdgpu_irq_add_domain
=====================

.. c:function:: int amdgpu_irq_add_domain(struct amdgpu_device *adev)

    create a linear IRQ domain

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_add_domain.description`:

Description
-----------

Creates an IRQ domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

.. _`amdgpu_irq_add_domain.return`:

Return
------

0 on success or error code otherwise

.. _`amdgpu_irq_remove_domain`:

amdgpu_irq_remove_domain
========================

.. c:function:: void amdgpu_irq_remove_domain(struct amdgpu_device *adev)

    remove the IRQ domain

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_irq_remove_domain.description`:

Description
-----------

Removes the IRQ domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

.. _`amdgpu_irq_create_mapping`:

amdgpu_irq_create_mapping
=========================

.. c:function:: unsigned amdgpu_irq_create_mapping(struct amdgpu_device *adev, unsigned src_id)

    create mapping between domain Linux IRQs

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param src_id:
        IH source id
    :type src_id: unsigned

.. _`amdgpu_irq_create_mapping.description`:

Description
-----------

Creates mapping between a domain IRQ (GPU IH src id) and a Linux IRQ
Use this for components that generate a GPU interrupt, but are driven
by a different driver (e.g., ACP).

.. _`amdgpu_irq_create_mapping.return`:

Return
------

Linux IRQ

.. This file was automatic generated / don't edit.


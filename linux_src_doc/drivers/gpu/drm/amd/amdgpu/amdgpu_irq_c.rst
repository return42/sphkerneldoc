.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_irq.c

.. _`amdgpu_hotplug_work_func`:

amdgpu_hotplug_work_func
========================

.. c:function:: void amdgpu_hotplug_work_func(struct work_struct *work)

    display hotplug work handler

    :param struct work_struct \*work:
        work struct

.. _`amdgpu_hotplug_work_func.description`:

Description
-----------

This is the hot plug event work handler (all asics).
The work gets scheduled from the irq handler if there
was a hot plug interrupt.  It walks the connector table
and calls the hotplug handler for each one, then sends
a drm hotplug event to alert userspace.

.. _`amdgpu_irq_reset_work_func`:

amdgpu_irq_reset_work_func
==========================

.. c:function:: void amdgpu_irq_reset_work_func(struct work_struct *work)

    execute gpu reset

    :param struct work_struct \*work:
        work struct

.. _`amdgpu_irq_reset_work_func.description`:

Description
-----------

Execute scheduled gpu reset (cayman+).
This function is called when the irq handler
thinks we need a gpu reset.

.. _`amdgpu_irq_preinstall`:

amdgpu_irq_preinstall
=====================

.. c:function:: void amdgpu_irq_preinstall(struct drm_device *dev)

    drm irq preinstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`amdgpu_irq_preinstall.description`:

Description
-----------

Gets the hw ready to enable irqs (all asics).
This function disables all interrupt sources on the GPU.

.. _`amdgpu_irq_postinstall`:

amdgpu_irq_postinstall
======================

.. c:function:: int amdgpu_irq_postinstall(struct drm_device *dev)

    drm irq preinstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`amdgpu_irq_postinstall.description`:

Description
-----------

Handles stuff to be done after enabling irqs (all asics).
Returns 0 on success.

.. _`amdgpu_irq_uninstall`:

amdgpu_irq_uninstall
====================

.. c:function:: void amdgpu_irq_uninstall(struct drm_device *dev)

    drm irq uninstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`amdgpu_irq_uninstall.description`:

Description
-----------

This function disables all interrupt sources on the GPU (all asics).

.. _`amdgpu_irq_handler`:

amdgpu_irq_handler
==================

.. c:function:: irqreturn_t amdgpu_irq_handler(int irq, void *arg)

    irq handler

    :param int irq:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`amdgpu_irq_handler.description`:

Description
-----------

This is the irq handler for the amdgpu driver (all asics).

.. _`amdgpu_msi_ok`:

amdgpu_msi_ok
=============

.. c:function:: bool amdgpu_msi_ok(struct amdgpu_device *adev)

    asic specific msi checks

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_msi_ok.description`:

Description
-----------

Handles asic specific MSI checks to determine if
MSIs should be enabled on a particular chip (all asics).
Returns true if MSIs should be enabled, false if MSIs
should not be enabled.

.. _`amdgpu_irq_init`:

amdgpu_irq_init
===============

.. c:function:: int amdgpu_irq_init(struct amdgpu_device *adev)

    init driver interrupt info

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_irq_init.description`:

Description
-----------

Sets up the work irq handlers, vblank init, MSIs, etc. (all asics).
Returns 0 for success, error for failure.

.. _`amdgpu_irq_fini`:

amdgpu_irq_fini
===============

.. c:function:: void amdgpu_irq_fini(struct amdgpu_device *adev)

    tear down driver interrupt info

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_irq_fini.description`:

Description
-----------

Tears down the work irq handlers, vblank handlers, MSIs, etc. (all asics).

.. _`amdgpu_irq_add_id`:

amdgpu_irq_add_id
=================

.. c:function:: int amdgpu_irq_add_id(struct amdgpu_device *adev, unsigned src_id, struct amdgpu_irq_src *source)

    register irq source

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param unsigned src_id:
        source id for this source

    :param struct amdgpu_irq_src \*source:
        irq source

.. _`amdgpu_irq_dispatch`:

amdgpu_irq_dispatch
===================

.. c:function:: void amdgpu_irq_dispatch(struct amdgpu_device *adev, struct amdgpu_iv_entry *entry)

    dispatch irq to IP blocks

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_iv_entry \*entry:
        interrupt vector

.. _`amdgpu_irq_dispatch.description`:

Description
-----------

Dispatches the irq to the different IP blocks

.. _`amdgpu_irq_update`:

amdgpu_irq_update
=================

.. c:function:: int amdgpu_irq_update(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    update hw interrupt state

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_irq_src \*src:
        interrupt src you want to enable

    :param unsigned type:
        type of interrupt you want to update

.. _`amdgpu_irq_update.description`:

Description
-----------

Updates the interrupt state for a specific src (all asics).

.. _`amdgpu_irq_get`:

amdgpu_irq_get
==============

.. c:function:: int amdgpu_irq_get(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    enable interrupt

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_irq_src \*src:
        interrupt src you want to enable

    :param unsigned type:
        type of interrupt you want to enable

.. _`amdgpu_irq_get.description`:

Description
-----------

Enables the interrupt type for a specific src (all asics).

.. _`amdgpu_irq_put`:

amdgpu_irq_put
==============

.. c:function:: int amdgpu_irq_put(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    disable interrupt

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_irq_src \*src:
        interrupt src you want to disable

    :param unsigned type:
        type of interrupt you want to disable

.. _`amdgpu_irq_put.description`:

Description
-----------

Disables the interrupt type for a specific src (all asics).

.. _`amdgpu_irq_enabled`:

amdgpu_irq_enabled
==================

.. c:function:: bool amdgpu_irq_enabled(struct amdgpu_device *adev, struct amdgpu_irq_src *src, unsigned type)

    test if irq is enabled or not

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_irq_src \*src:
        *undescribed*

    :param unsigned type:
        *undescribed*

.. _`amdgpu_irq_enabled.description`:

Description
-----------

Tests if the given interrupt source is enabled or not

.. _`amdgpu_irq_add_domain`:

amdgpu_irq_add_domain
=====================

.. c:function:: int amdgpu_irq_add_domain(struct amdgpu_device *adev)

    create a linear irq domain

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_irq_add_domain.description`:

Description
-----------

Create an irq domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

.. _`amdgpu_irq_remove_domain`:

amdgpu_irq_remove_domain
========================

.. c:function:: void amdgpu_irq_remove_domain(struct amdgpu_device *adev)

    remove the irq domain

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_irq_remove_domain.description`:

Description
-----------

Remove the irq domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

.. _`amdgpu_irq_create_mapping`:

amdgpu_irq_create_mapping
=========================

.. c:function:: unsigned amdgpu_irq_create_mapping(struct amdgpu_device *adev, unsigned src_id)

    create a mapping between a domain irq and a Linux irq

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param unsigned src_id:
        IH source id

.. _`amdgpu_irq_create_mapping.description`:

Description
-----------

Create a mapping between a domain irq (GPU IH src id) and a Linux irq
Use this for components that generate a GPU interrupt, but are driven
by a different driver (e.g., ACP).
Returns the Linux irq.

.. This file was automatic generated / don't edit.


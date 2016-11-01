.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/fsl-mc-allocator.c

.. _`fsl_mc_resource_pool_add_device`:

fsl_mc_resource_pool_add_device
===============================

.. c:function:: int fsl_mc_resource_pool_add_device(struct fsl_mc_bus *mc_bus, enum fsl_mc_pool_type pool_type, struct fsl_mc_device *mc_dev)

    add allocatable device to a resource pool of a given MC bus

    :param struct fsl_mc_bus \*mc_bus:
        pointer to the MC bus

    :param enum fsl_mc_pool_type pool_type:
        MC bus pool type

    :param struct fsl_mc_device \*mc_dev:
        Pointer to allocatable MC object device

.. _`fsl_mc_resource_pool_add_device.description`:

Description
-----------

It adds an allocatable MC object device to a container's resource pool of
the given resource type

.. _`fsl_mc_resource_pool_remove_device`:

fsl_mc_resource_pool_remove_device
==================================

.. c:function:: int fsl_mc_resource_pool_remove_device(struct fsl_mc_device *mc_dev)

    remove an allocatable device from a resource pool

    :param struct fsl_mc_device \*mc_dev:
        Pointer to allocatable MC object device

.. _`fsl_mc_resource_pool_remove_device.description`:

Description
-----------

It permanently removes an allocatable MC object device from the resource
pool, the device is currently in, as long as it is in the pool's free list.

.. _`fsl_mc_object_allocate`:

fsl_mc_object_allocate
======================

.. c:function:: int fsl_mc_object_allocate(struct fsl_mc_device *mc_dev, enum fsl_mc_pool_type pool_type, struct fsl_mc_device **new_mc_adev)

    Allocates a MC object device of the given pool type from a given MC bus

    :param struct fsl_mc_device \*mc_dev:
        MC device for which the MC object device is to be allocated

    :param enum fsl_mc_pool_type pool_type:
        MC bus resource pool type

    :param struct fsl_mc_device \*\*new_mc_adev:
        *undescribed*

.. _`fsl_mc_object_allocate.description`:

Description
-----------

This function allocates a MC object device from the device's parent DPRC,
from the corresponding MC bus' pool of allocatable MC object devices of
the given resource type. mc_dev cannot be a DPRC itself.

.. _`fsl_mc_object_allocate.note`:

NOTE
----

pool_type must be different from FSL_MC_POOL_MCP, since MC
portals are allocated using \ :c:func:`fsl_mc_portal_allocate`\ , instead of
this function.

.. _`fsl_mc_object_free`:

fsl_mc_object_free
==================

.. c:function:: void fsl_mc_object_free(struct fsl_mc_device *mc_adev)

    Returns an allocatable MC object device to the corresponding resource pool of a given MC bus.

    :param struct fsl_mc_device \*mc_adev:
        Pointer to the MC object device

.. _`fsl_mc_cleanup_irq_pool`:

fsl_mc_cleanup_irq_pool
=======================

.. c:function:: void fsl_mc_cleanup_irq_pool(struct fsl_mc_bus *mc_bus)

    It frees the IRQs that were allocated to the pool, back to the GIC-ITS.

    :param struct fsl_mc_bus \*mc_bus:
        *undescribed*

.. _`fsl_mc_allocate_irqs`:

fsl_mc_allocate_irqs
====================

.. c:function:: int fsl_mc_allocate_irqs(struct fsl_mc_device *mc_dev)

    IRQs are allocated from the interrupt pool associated with the MC bus that contains the device, if the device is not a DPRC device. Otherwise, the IRQs are allocated from the interrupt pool associated with the MC bus that represents the DPRC device itself.

    :param struct fsl_mc_device \*mc_dev:
        *undescribed*

.. _`fsl_mc_allocator_probe`:

fsl_mc_allocator_probe
======================

.. c:function:: int fsl_mc_allocator_probe(struct fsl_mc_device *mc_dev)

    callback invoked when an allocatable device is being added to the system

    :param struct fsl_mc_device \*mc_dev:
        *undescribed*

.. _`fsl_mc_allocator_remove`:

fsl_mc_allocator_remove
=======================

.. c:function:: int fsl_mc_allocator_remove(struct fsl_mc_device *mc_dev)

    callback invoked when an allocatable device is being removed from the system

    :param struct fsl_mc_device \*mc_dev:
        *undescribed*

.. This file was automatic generated / don't edit.


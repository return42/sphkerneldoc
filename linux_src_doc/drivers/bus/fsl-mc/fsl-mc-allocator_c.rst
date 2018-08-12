.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/fsl-mc/fsl-mc-allocator.c

.. _`fsl_mc_resource_pool_add_device`:

fsl_mc_resource_pool_add_device
===============================

.. c:function:: int fsl_mc_resource_pool_add_device(struct fsl_mc_bus *mc_bus, enum fsl_mc_pool_type pool_type, struct fsl_mc_device *mc_dev)

    add allocatable object to a resource pool of a given fsl-mc bus

    :param struct fsl_mc_bus \*mc_bus:
        pointer to the fsl-mc bus

    :param enum fsl_mc_pool_type pool_type:
        pool type

    :param struct fsl_mc_device \*mc_dev:
        pointer to allocatable fsl-mc device

.. _`fsl_mc_resource_pool_remove_device`:

fsl_mc_resource_pool_remove_device
==================================

.. c:function:: int fsl_mc_resource_pool_remove_device(struct fsl_mc_device *mc_dev)

    remove an allocatable device from a resource pool

    :param struct fsl_mc_device \*mc_dev:
        pointer to allocatable fsl-mc device

.. _`fsl_mc_resource_pool_remove_device.description`:

Description
-----------

It permanently removes an allocatable fsl-mc device from the resource
pool. It's an error if the device is in use.

.. _`fsl_mc_object_allocate`:

fsl_mc_object_allocate
======================

.. c:function:: int fsl_mc_object_allocate(struct fsl_mc_device *mc_dev, enum fsl_mc_pool_type pool_type, struct fsl_mc_device **new_mc_adev)

    Allocates an fsl-mc object of the given pool type from a given fsl-mc bus instance

    :param struct fsl_mc_device \*mc_dev:
        fsl-mc device which is used in conjunction with the
        allocated object

    :param enum fsl_mc_pool_type pool_type:
        pool type

    :param struct fsl_mc_device \*\*new_mc_adev:
        *undescribed*

.. _`fsl_mc_object_allocate.description`:

Description
-----------

Allocatable objects are always used in conjunction with some functional
device.  This function allocates an object of the specified type from
the DPRC containing the functional device.

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

    Returns an fsl-mc object to the resource pool where it came from.

    :param struct fsl_mc_device \*mc_adev:
        Pointer to the fsl-mc device

.. _`fsl_mc_cleanup_irq_pool`:

fsl_mc_cleanup_irq_pool
=======================

.. c:function:: void fsl_mc_cleanup_irq_pool(struct fsl_mc_bus *mc_bus)

    mc bus. It frees the IRQs that were allocated to the pool, back to the GIC-ITS.

    :param struct fsl_mc_bus \*mc_bus:
        *undescribed*

.. _`fsl_mc_allocate_irqs`:

fsl_mc_allocate_irqs
====================

.. c:function:: int fsl_mc_allocate_irqs(struct fsl_mc_device *mc_dev)

    mc device.

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


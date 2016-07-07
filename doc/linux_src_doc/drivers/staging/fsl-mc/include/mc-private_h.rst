.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/mc-private.h

.. _`fsl_mc_irq_pool_max_total_irqs`:

FSL_MC_IRQ_POOL_MAX_TOTAL_IRQS
==============================

.. c:function::  FSL_MC_IRQ_POOL_MAX_TOTAL_IRQS()

    allocated for an MC bus' IRQ pool

.. _`fsl_mc`:

struct fsl_mc
=============

.. c:type:: struct fsl_mc

    Private data of a "fsl,qoriq-mc" platform device

.. _`fsl_mc.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc {
        struct fsl_mc_device *root_mc_bus_dev;
        u8 num_translation_ranges;
        struct fsl_mc_addr_translation_range *translation_ranges;
    }

.. _`fsl_mc.members`:

Members
-------

root_mc_bus_dev
    MC object device representing the root DPRC

num_translation_ranges
    number of entries in addr_translation_ranges

translation_ranges
    array of bus to system address translation ranges

.. _`fsl_mc_addr_translation_range`:

struct fsl_mc_addr_translation_range
====================================

.. c:type:: struct fsl_mc_addr_translation_range

    bus to system address translation range

.. _`fsl_mc_addr_translation_range.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_addr_translation_range {
        enum dprc_region_type mc_region_type;
        u64 start_mc_offset;
        u64 end_mc_offset;
        phys_addr_t start_phys_addr;
    }

.. _`fsl_mc_addr_translation_range.members`:

Members
-------

mc_region_type
    Type of MC region for the range being translated

start_mc_offset
    Start MC offset of the range being translated

end_mc_offset
    MC offset of the first byte after the range (last MC
    offset of the range is end_mc_offset - 1)

start_phys_addr
    system physical address corresponding to start_mc_addr

.. _`fsl_mc_resource_pool`:

struct fsl_mc_resource_pool
===========================

.. c:type:: struct fsl_mc_resource_pool

    Pool of MC resources of a given type

.. _`fsl_mc_resource_pool.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_resource_pool {
        enum fsl_mc_pool_type type;
        int16_t max_count;
        int16_t free_count;
        struct mutex mutex;
        struct list_head free_list;
        struct fsl_mc_bus *mc_bus;
    }

.. _`fsl_mc_resource_pool.members`:

Members
-------

type
    type of resources in the pool

max_count
    maximum number of resources in the pool

free_count
    number of free resources in the pool

mutex
    mutex to serialize access to the pool's free list

free_list
    anchor node of list of free resources in the pool

mc_bus
    pointer to the MC bus that owns this resource pool

.. _`fsl_mc_bus`:

struct fsl_mc_bus
=================

.. c:type:: struct fsl_mc_bus

    logical bus that corresponds to a physical DPRC

.. _`fsl_mc_bus.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_bus {
        struct fsl_mc_device mc_dev;
        struct fsl_mc_resource_pool resource_pools[FSL_MC_NUM_POOL_TYPES];
        struct fsl_mc_device_irq *irq_resources;
        struct mutex scan_mutex;
        struct dprc_attributes dprc_attr;
    }

.. _`fsl_mc_bus.members`:

Members
-------

mc_dev
    fsl-mc device for the bus device itself.

resource_pools
    array of resource pools (one pool per resource type)
    for this MC bus. These resources represent allocatable entities
    from the physical DPRC.

irq_resources
    Pointer to array of IRQ objects for the IRQ pool

scan_mutex
    Serializes bus scanning

dprc_attr
    DPRC attributes

.. This file was automatic generated / don't edit.


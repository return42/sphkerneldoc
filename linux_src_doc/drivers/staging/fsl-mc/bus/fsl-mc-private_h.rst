.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/fsl-mc-private.h

.. _`dprc_irq_cfg`:

struct dprc_irq_cfg
===================

.. c:type:: struct dprc_irq_cfg

    IRQ configuration

.. _`dprc_irq_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dprc_irq_cfg {
        phys_addr_t paddr;
        u32 val;
        int irq_num;
    }

.. _`dprc_irq_cfg.members`:

Members
-------

paddr
    Address that must be written to signal a message-based interrupt

val
    Value to write into irq_addr address

irq_num
    A user defined number associated with this IRQ

.. _`dprc_attributes`:

struct dprc_attributes
======================

.. c:type:: struct dprc_attributes

    Container attributes

.. _`dprc_attributes.definition`:

Definition
----------

.. code-block:: c

    struct dprc_attributes {
        int container_id;
        u16 icid;
        int portal_id;
        u64 options;
    }

.. _`dprc_attributes.members`:

Members
-------

container_id
    Container's ID

icid
    Container's ICID

portal_id
    Container's portal ID

options
    Container's options as set at container's creation

.. _`dprc_region_type`:

enum dprc_region_type
=====================

.. c:type:: enum dprc_region_type

    Region type

.. _`dprc_region_type.definition`:

Definition
----------

.. code-block:: c

    enum dprc_region_type {
        DPRC_REGION_TYPE_MC_PORTAL,
        DPRC_REGION_TYPE_QBMAN_PORTAL
    };

.. _`dprc_region_type.constants`:

Constants
---------

DPRC_REGION_TYPE_MC_PORTAL
    MC portal region

DPRC_REGION_TYPE_QBMAN_PORTAL
    Qbman portal region

.. _`dprc_region_desc`:

struct dprc_region_desc
=======================

.. c:type:: struct dprc_region_desc

    Mappable region descriptor

.. _`dprc_region_desc.definition`:

Definition
----------

.. code-block:: c

    struct dprc_region_desc {
        u32 base_offset;
        u32 size;
        u32 flags;
        enum dprc_region_type type;
    }

.. _`dprc_region_desc.members`:

Members
-------

base_offset
    Region offset from region's base address.
    For DPMCP and DPRC objects, region base is offset from SoC MC portals
    base address; For DPIO, region base is offset from SoC QMan portals
    base address

size
    Region size (in bytes)

flags
    Region attributes

type
    Portal region type

.. _`fsl_mc_irq_pool_max_total_irqs`:

FSL_MC_IRQ_POOL_MAX_TOTAL_IRQS
==============================

.. c:function::  FSL_MC_IRQ_POOL_MAX_TOTAL_IRQS()

    allocated for an MC bus' IRQ pool

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
        int max_count;
        int free_count;
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


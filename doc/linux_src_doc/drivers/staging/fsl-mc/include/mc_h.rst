.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/mc.h

.. _`fsl_mc_driver`:

struct fsl_mc_driver
====================

.. c:type:: struct fsl_mc_driver

    MC object device driver object

.. _`fsl_mc_driver.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_driver {
        struct device_driver driver;
        const struct fsl_mc_device_match_id *match_id_table;
        int (* probe) (struct fsl_mc_device *dev);
        int (* remove) (struct fsl_mc_device *dev);
        void (* shutdown) (struct fsl_mc_device *dev);
        int (* suspend) (struct fsl_mc_device *dev, pm_message_t state);
        int (* resume) (struct fsl_mc_device *dev);
    }

.. _`fsl_mc_driver.members`:

Members
-------

driver
    Generic device driver

match_id_table
    table of supported device matching Ids

probe
    Function called when a device is added

remove
    Function called when a device is removed

shutdown
    Function called at shutdown time to quiesce the device

suspend
    Function called when a device is stopped

resume
    Function called when a device is resumed

.. _`fsl_mc_driver.description`:

Description
-----------

Generic DPAA device driver object for device drivers that are registered
with a DPRC bus. This structure is to be embedded in each device-specific
driver structure.

.. _`fsl_mc_device_match_id`:

struct fsl_mc_device_match_id
=============================

.. c:type:: struct fsl_mc_device_match_id

    MC object device Id entry for driver matching

.. _`fsl_mc_device_match_id.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_device_match_id {
        u16 vendor;
        const char obj_type[16];
        u32 ver_major;
        u32 ver_minor;
    }

.. _`fsl_mc_device_match_id.members`:

Members
-------

vendor
    vendor ID

obj_type
    MC object type

ver_major
    MC object version major number

ver_minor
    MC object version minor number

.. _`fsl_mc_device_match_id.description`:

Description
-----------

Type of entries in the "device Id" table for MC object devices supported by
a MC object device driver. The last entry of the table has vendor set to 0x0

.. _`fsl_mc_pool_type`:

enum fsl_mc_pool_type
=====================

.. c:type:: enum fsl_mc_pool_type

    Types of allocatable MC bus resources

.. _`fsl_mc_pool_type.definition`:

Definition
----------

.. code-block:: c

    enum fsl_mc_pool_type {
        FSL_MC_POOL_DPMCP,
        FSL_MC_POOL_DPBP,
        FSL_MC_POOL_DPCON,
        FSL_MC_POOL_IRQ,
        FSL_MC_NUM_POOL_TYPES
    };

.. _`fsl_mc_pool_type.constants`:

Constants
---------

FSL_MC_POOL_DPMCP
    *undescribed*

FSL_MC_POOL_DPBP
    *undescribed*

FSL_MC_POOL_DPCON
    *undescribed*

FSL_MC_POOL_IRQ
    *undescribed*

FSL_MC_NUM_POOL_TYPES
    *undescribed*

.. _`fsl_mc_pool_type.description`:

Description
-----------

Entries in these enum are used as indices in the array of resource
pools of an fsl_mc_bus object.

.. _`fsl_mc_resource`:

struct fsl_mc_resource
======================

.. c:type:: struct fsl_mc_resource

    MC generic resource

.. _`fsl_mc_resource.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_resource {
        enum fsl_mc_pool_type type;
        int32_t id;
        void *data;
        struct fsl_mc_resource_pool *parent_pool;
        struct list_head node;
    }

.. _`fsl_mc_resource.members`:

Members
-------

type
    type of resource

id
    unique MC resource Id within the resources of the same type

data
    pointer to resource-specific data if the resource is currently
    allocated, or NULL if the resource is not currently allocated.

parent_pool
    pointer to the parent resource pool from which this
    resource is allocated from.

node
    Node in the free list of the corresponding resource pool

.. _`fsl_mc_resource.note`:

NOTE
----

This structure is to be embedded as a field of specific
MC resource structures.

.. _`fsl_mc_device_irq`:

struct fsl_mc_device_irq
========================

.. c:type:: struct fsl_mc_device_irq

    MC object device message-based interrupt

.. _`fsl_mc_device_irq.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_device_irq {
        struct msi_desc *msi_desc;
        struct fsl_mc_device *mc_dev;
        u8 dev_irq_index;
        struct fsl_mc_resource resource;
    }

.. _`fsl_mc_device_irq.members`:

Members
-------

msi_desc
    pointer to MSI descriptor allocated by \ :c:func:`fsl_mc_msi_alloc_descs`\ 

mc_dev
    MC object device that owns this interrupt

dev_irq_index
    device-relative IRQ index

resource
    MC generic resource associated with the interrupt

.. _`fsl_mc_is_dprc`:

FSL_MC_IS_DPRC
==============

.. c:function::  FSL_MC_IS_DPRC()

.. _`fsl_mc_default_dma_mask`:

FSL_MC_DEFAULT_DMA_MASK
=======================

.. c:function::  FSL_MC_DEFAULT_DMA_MASK()

    mc bus

.. _`fsl_mc_device`:

struct fsl_mc_device
====================

.. c:type:: struct fsl_mc_device

    MC object device object

.. _`fsl_mc_device.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_device {
        struct device dev;
        u64 dma_mask;
        u16 flags;
        u16 icid;
        u16 mc_handle;
        struct fsl_mc_io *mc_io;
        struct dprc_obj_desc obj_desc;
        struct resource *regions;
        struct fsl_mc_device_irq **irqs;
        struct fsl_mc_resource *resource;
    }

.. _`fsl_mc_device.members`:

Members
-------

dev
    Linux driver model device object

dma_mask
    Default DMA mask

flags
    MC object device flags

icid
    Isolation context ID for the device

mc_handle
    MC handle for the corresponding MC object opened

mc_io
    Pointer to MC IO object assigned to this device or
    NULL if none.

obj_desc
    MC description of the DPAA device

regions
    pointer to array of MMIO region entries

irqs
    pointer to array of pointers to interrupts allocated to this device

resource
    generic resource associated with this MC object device, if any.

.. _`fsl_mc_device.description`:

Description
-----------

Generic device object for MC object devices that are "attached" to a
MC bus.

.. _`fsl_mc_device.notes`:

NOTES
-----

- For a non-DPRC object its icid is the same as its parent DPRC's icid.
- The SMMU notifier callback gets invoked after \ :c:func:`device_add`\  has been
called for an MC object device, but before the device-specific probe
callback gets called.
- DP_OBJ_DPRC objects are the only MC objects that have built-in MC
portals. For all other MC objects, their device drivers are responsible for
allocating MC portals for them by calling \ :c:func:`fsl_mc_portal_allocate`\ .
- Some types of MC objects (e.g., DP_OBJ_DPBP, DP_OBJ_DPCON) are
treated as resources that can be allocated/deallocated from the
corresponding resource pool in the object's parent DPRC, using the
\ :c:func:`fsl_mc_object_allocate`\ /\ :c:func:`fsl_mc_object_free`\  functions. These MC objects
are known as "allocatable" objects. For them, the corresponding
fsl_mc_device's 'resource' points to the associated resource object.
For MC objects that are not allocatable (e.g., DP_OBJ_DPRC, DP_OBJ_DPNI),
'resource' is NULL.

.. This file was automatic generated / don't edit.


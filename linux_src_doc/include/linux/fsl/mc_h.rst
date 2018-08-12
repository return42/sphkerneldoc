.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fsl/mc.h

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
        const struct fsl_mc_device_id *match_id_table;
        int (*probe)(struct fsl_mc_device *dev);
        int (*remove)(struct fsl_mc_device *dev);
        void (*shutdown)(struct fsl_mc_device *dev);
        int (*suspend)(struct fsl_mc_device *dev, pm_message_t state);
        int (*resume)(struct fsl_mc_device *dev);
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
        s32 id;
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

.. _`fsl_mc_obj_flag_no_mem_shareability`:

FSL_MC_OBJ_FLAG_NO_MEM_SHAREABILITY
===================================

.. c:function::  FSL_MC_OBJ_FLAG_NO_MEM_SHAREABILITY()

    Object flag indicating no memory shareability. the object generates memory accesses that are non coherent with other masters; user is responsible for proper memory handling through IOMMU configuration.

.. _`fsl_mc_obj_desc`:

struct fsl_mc_obj_desc
======================

.. c:type:: struct fsl_mc_obj_desc

    Object descriptor

.. _`fsl_mc_obj_desc.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_obj_desc {
        char type[16];
        int id;
        u16 vendor;
        u16 ver_major;
        u16 ver_minor;
        u8 irq_count;
        u8 region_count;
        u32 state;
        char label[16];
        u16 flags;
    }

.. _`fsl_mc_obj_desc.members`:

Members
-------

type
    Type of object: NULL terminated string

id
    ID of logical object resource

vendor
    Object vendor identifier

ver_major
    Major version number

ver_minor
    Minor version number

irq_count
    Number of interrupts supported by the object

region_count
    Number of mappable regions supported by the object

state
    Object state: combination of FSL_MC_OBJ_STATE\_ states

label
    Object label: NULL terminated string

flags
    Object's flags

.. _`fsl_mc_is_dprc`:

FSL_MC_IS_DPRC
==============

.. c:function::  FSL_MC_IS_DPRC()

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
        struct fsl_mc_obj_desc obj_desc;
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
\ :c:func:`fsl_mc_object_allocate`\ /fsl_mc_object_free() functions. These MC objects
are known as "allocatable" objects. For them, the corresponding
fsl_mc_device's 'resource' points to the associated resource object.
For MC objects that are not allocatable (e.g., DP_OBJ_DPRC, DP_OBJ_DPNI),
'resource' is NULL.

.. _`fsl_mc_io_atomic_context_portal`:

FSL_MC_IO_ATOMIC_CONTEXT_PORTAL
===============================

.. c:function::  FSL_MC_IO_ATOMIC_CONTEXT_PORTAL()

.. _`fsl_mc_io`:

struct fsl_mc_io
================

.. c:type:: struct fsl_mc_io

    MC I/O object to be passed-in to \ :c:func:`mc_send_command`\ 

.. _`fsl_mc_io.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_io {
        struct device *dev;
        u16 flags;
        u32 portal_size;
        phys_addr_t portal_phys_addr;
        void __iomem *portal_virt_addr;
        struct fsl_mc_device *dpmcp_dev;
        union {
            struct mutex mutex;
            spinlock_t spinlock;
        } ;
    }

.. _`fsl_mc_io.members`:

Members
-------

dev
    device associated with this Mc I/O object

flags
    flags for \ :c:func:`mc_send_command`\ 

portal_size
    MC command portal size in bytes

portal_phys_addr
    MC command portal physical address

portal_virt_addr
    MC command portal virtual address

dpmcp_dev
    pointer to the DPMCP device associated with the MC portal.

{unnamed_union}
    anonymous

mutex
    Mutex to serialize \ :c:func:`mc_send_command`\  calls that use the same MC
    portal, if the fsl_mc_io object was created with the
    FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag off. \ :c:func:`mc_send_command`\  calls for this
    fsl_mc_io object must be made only from non-atomic context.

spinlock
    Spinlock to serialize \ :c:func:`mc_send_command`\  calls that use the same MC
    portal, if the fsl_mc_io object was created with the
    FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag on. \ :c:func:`mc_send_command`\  calls for this
    fsl_mc_io object can be made from atomic or non-atomic context.

.. _`fsl_mc_io.description`:

Description
-----------

Fields are only meaningful if the FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag is not

Fields are only meaningful if the FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag is

.. _`dpbp_attr`:

struct dpbp_attr
================

.. c:type:: struct dpbp_attr

    Structure representing DPBP attributes

.. _`dpbp_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpbp_attr {
        int id;
        u16 bpid;
    }

.. _`dpbp_attr.members`:

Members
-------

id
    DPBP object ID

bpid
    Hardware buffer pool ID; should be used as an argument in
    acquire/release operations on buffers

.. _`dpcon_invalid_dpio_id`:

DPCON_INVALID_DPIO_ID
=====================

.. c:function::  DPCON_INVALID_DPIO_ID()

.. _`dpcon_attr`:

struct dpcon_attr
=================

.. c:type:: struct dpcon_attr

    Structure representing DPCON attributes

.. _`dpcon_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpcon_attr {
        int id;
        u16 qbman_ch_id;
        u8 num_priorities;
    }

.. _`dpcon_attr.members`:

Members
-------

id
    DPCON object ID

qbman_ch_id
    Channel ID to be used by dequeue operation

num_priorities
    Number of priorities for the DPCON channel (1-8)

.. _`dpcon_notification_cfg`:

struct dpcon_notification_cfg
=============================

.. c:type:: struct dpcon_notification_cfg

    Structure representing notification params

.. _`dpcon_notification_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpcon_notification_cfg {
        int dpio_id;
        u8 priority;
        u64 user_ctx;
    }

.. _`dpcon_notification_cfg.members`:

Members
-------

dpio_id
    DPIO object ID; must be configured with a notification channel;
    to disable notifications set it to 'DPCON_INVALID_DPIO_ID';

priority
    Priority selection within the DPIO channel; valid values
    are 0-7, depending on the number of priorities in that channel

user_ctx
    User context value provided with each CDAN message

.. This file was automatic generated / don't edit.


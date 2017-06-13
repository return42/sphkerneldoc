.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dprc.h

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

.. _`dprc_obj_flag_no_mem_shareability`:

DPRC_OBJ_FLAG_NO_MEM_SHAREABILITY
=================================

.. c:function::  DPRC_OBJ_FLAG_NO_MEM_SHAREABILITY()

    Object flag indicating no memory shareability. the object generates memory accesses that are non coherent with other masters; user is responsible for proper memory handling through IOMMU configuration.

.. _`dprc_obj_desc`:

struct dprc_obj_desc
====================

.. c:type:: struct dprc_obj_desc

    Object descriptor, returned from \ :c:func:`dprc_get_obj`\ 

.. _`dprc_obj_desc.definition`:

Definition
----------

.. code-block:: c

    struct dprc_obj_desc {
        char type;
        int id;
        u16 vendor;
        u16 ver_major;
        u16 ver_minor;
        u8 irq_count;
        u8 region_count;
        u32 state;
        char label;
        u16 flags;
    }

.. _`dprc_obj_desc.members`:

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
    Object state: combination of DPRC_OBJ_STATE\_ states

label
    Object label

flags
    Object's flags

.. _`dprc_iter_status`:

enum dprc_iter_status
=====================

.. c:type:: enum dprc_iter_status

    Iteration status

.. _`dprc_iter_status.definition`:

Definition
----------

.. code-block:: c

    enum dprc_iter_status {
        DPRC_ITER_STATUS_FIRST,
        DPRC_ITER_STATUS_MORE,
        DPRC_ITER_STATUS_LAST
    };

.. _`dprc_iter_status.constants`:

Constants
---------

DPRC_ITER_STATUS_FIRST
    Perform first iteration

DPRC_ITER_STATUS_MORE
    Indicates more/next iteration is needed

DPRC_ITER_STATUS_LAST
    Indicates last iteration

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

.. This file was automatic generated / don't edit.


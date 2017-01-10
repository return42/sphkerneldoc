.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dprc.h

.. _`dprc_get_icid_from_pool`:

DPRC_GET_ICID_FROM_POOL
=======================

.. c:function::  DPRC_GET_ICID_FROM_POOL()

    container, in case the ICID is not selected by the user and should be allocated by the DPRC from the pool of ICIDs.

.. _`dprc_get_portal_id_from_pool`:

DPRC_GET_PORTAL_ID_FROM_POOL
============================

.. c:function::  DPRC_GET_PORTAL_ID_FROM_POOL()

    container, in case the portal ID is not specifically selected by the user and should be allocated by the DPRC from the pool of portal ids.

.. _`dprc_cfg_opt_spawn_allowed`:

DPRC_CFG_OPT_SPAWN_ALLOWED
==========================

.. c:function::  DPRC_CFG_OPT_SPAWN_ALLOWED()

.. _`dprc_cfg_opt_spawn_allowed.description`:

Description
-----------

These options may be selected at container creation by the container creator
and can be retrieved using \ :c:func:`dprc_get_attributes`\ 

.. _`dprc_cfg`:

struct dprc_cfg
===============

.. c:type:: struct dprc_cfg

    Container configuration options

.. _`dprc_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dprc_cfg {
        u16 icid;
        int portal_id;
        u64 options;
        char label[16];
    }

.. _`dprc_cfg.members`:

Members
-------

icid
    Container's ICID; if set to 'DPRC_GET_ICID_FROM_POOL', a free
    ICID value is allocated by the DPRC

portal_id
    Portal ID; if set to 'DPRC_GET_PORTAL_ID_FROM_POOL', a free
    portal ID is allocated by the DPRC

options
    Combination of 'DPRC_CFG_OPT_<X>' options

label
    Object's label

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

.. _`dprc_res_req`:

struct dprc_res_req
===================

.. c:type:: struct dprc_res_req

    Resource request descriptor, to be used in assignment or un-assignment of resources and objects.

.. _`dprc_res_req.definition`:

Definition
----------

.. code-block:: c

    struct dprc_res_req {
        char type[16];
        u32 num;
        u32 options;
        int id_base_align;
    }

.. _`dprc_res_req.members`:

Members
-------

type
    Resource/object type: Represent as a NULL terminated string.
    This string may received by using \ :c:func:`dprc_get_pool`\  to get resource
    type and \ :c:func:`dprc_get_obj`\  to get object type;

num
    Number of resources

options
    Request options: combination of DPRC_RES_REQ_OPT\_ options

id_base_align
    In case of explicit assignment (DPRC_RES_REQ_OPT_EXPLICIT
    is set at option), this field represents the required base ID
    for resource allocation; In case of aligned assignment
    (DPRC_RES_REQ_OPT_ALIGNED is set at option), this field
    indicates the required alignment for the resource ID(s) -
    use 0 if there is no alignment or explicit ID requirements

.. _`dprc_res_req.note`:

Note
----

it is not possible to assign/un-assign DPRC objects

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

.. _`dprc_res_ids_range_desc`:

struct dprc_res_ids_range_desc
==============================

.. c:type:: struct dprc_res_ids_range_desc

    Resource ID range descriptor

.. _`dprc_res_ids_range_desc.definition`:

Definition
----------

.. code-block:: c

    struct dprc_res_ids_range_desc {
        int base_id;
        int last_id;
        enum dprc_iter_status iter_status;
    }

.. _`dprc_res_ids_range_desc.members`:

Members
-------

base_id
    Base resource ID of this range

last_id
    Last resource ID of this range

iter_status
    Iteration status - should be set to DPRC_ITER_STATUS_FIRST at
    first iteration; while the returned marker is DPRC_ITER_STATUS_MORE,
    additional iterations are needed, until the returned marker is
    DPRC_ITER_STATUS_LAST

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

.. _`dprc_endpoint`:

struct dprc_endpoint
====================

.. c:type:: struct dprc_endpoint

    Endpoint description for link connect/disconnect operations

.. _`dprc_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct dprc_endpoint {
        char type[16];
        int id;
        int if_id;
    }

.. _`dprc_endpoint.members`:

Members
-------

type
    Endpoint object type: NULL terminated string

id
    Endpoint object ID

if_id
    Interface ID; should be set for endpoints with multiple
    interfaces ("dpsw", "dpdmux"); for others, always set to 0

.. _`dprc_connection_cfg`:

struct dprc_connection_cfg
==========================

.. c:type:: struct dprc_connection_cfg

    Connection configuration. Used for virtual connections only

.. _`dprc_connection_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dprc_connection_cfg {
        u32 committed_rate;
        u32 max_rate;
    }

.. _`dprc_connection_cfg.members`:

Members
-------

committed_rate
    Committed rate (Mbits/s)

max_rate
    Maximum rate (Mbits/s)

.. This file was automatic generated / don't edit.


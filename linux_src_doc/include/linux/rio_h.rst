.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rio.h

.. _`rio_switch`:

struct rio_switch
=================

.. c:type:: struct rio_switch

    RIO switch info

.. _`rio_switch.definition`:

Definition
----------

.. code-block:: c

    struct rio_switch {
        struct list_head node;
        u8 *route_table;
        u32 port_ok;
        struct rio_switch_ops *ops;
        spinlock_t lock;
        struct rio_dev  *nextdev[0];
    }

.. _`rio_switch.members`:

Members
-------

node
    Node in global list of switches

route_table
    Copy of switch routing table

port_ok
    Status of each port (one bit per port) - OK=1 or UNINIT=0

ops
    pointer to switch-specific operations

lock
    lock to serialize operations updates

nextdev
    Array of per-port pointers to the next attached device

.. _`rio_switch_ops`:

struct rio_switch_ops
=====================

.. c:type:: struct rio_switch_ops

    Per-switch operations

.. _`rio_switch_ops.definition`:

Definition
----------

.. code-block:: c

    struct rio_switch_ops {
        struct module *owner;
        int (*add_entry)(struct rio_mport *mport, u16 destid, u8 hopcount,u16 table, u16 route_destid, u8 route_port);
        int (*get_entry)(struct rio_mport *mport, u16 destid, u8 hopcount,u16 table, u16 route_destid, u8 *route_port);
        int (*clr_table)(struct rio_mport *mport, u16 destid, u8 hopcount,u16 table);
        int (*set_domain)(struct rio_mport *mport, u16 destid, u8 hopcount,u8 sw_domain);
        int (*get_domain)(struct rio_mport *mport, u16 destid, u8 hopcount,u8 *sw_domain);
        int (*em_init)(struct rio_dev *dev);
        int (*em_handle)(struct rio_dev *dev, u8 swport);
    }

.. _`rio_switch_ops.members`:

Members
-------

owner
    The module owner of this structure

add_entry
    Callback for switch-specific route add function

get_entry
    Callback for switch-specific route get function

clr_table
    Callback for switch-specific clear route table function

set_domain
    Callback for switch-specific domain setting function

get_domain
    Callback for switch-specific domain get function

em_init
    Callback for switch-specific error management init function

em_handle
    Callback for switch-specific error management handler function

.. _`rio_switch_ops.description`:

Description
-----------

Defines the operations that are necessary to initialize/control
a particular RIO switch device.

.. _`rio_dev`:

struct rio_dev
==============

.. c:type:: struct rio_dev

    RIO device info

.. _`rio_dev.definition`:

Definition
----------

.. code-block:: c

    struct rio_dev {
        struct list_head global_list;
        struct list_head net_list;
        struct rio_net *net;
        bool do_enum;
        u16 did;
        u16 vid;
        u32 device_rev;
        u16 asm_did;
        u16 asm_vid;
        u16 asm_rev;
        u16 efptr;
        u32 pef;
        u32 swpinfo;
        u32 src_ops;
        u32 dst_ops;
        u32 comp_tag;
        u32 phys_efptr;
        u32 phys_rmap;
        u32 em_efptr;
        u64 dma_mask;
        struct rio_driver *driver;
        struct device dev;
        struct resource riores[RIO_MAX_DEV_RESOURCES];
        int (*pwcback)(struct rio_dev *rdev, union rio_pw_msg *msg, int step);
        u16 destid;
        u8 hopcount;
        struct rio_dev *prev;
        atomic_t state;
        struct rio_switch rswitch[0];
    }

.. _`rio_dev.members`:

Members
-------

global_list
    Node in list of all RIO devices

net_list
    Node in list of RIO devices in a network

net
    Network this device is a part of

do_enum
    Enumeration flag

did
    Device ID

vid
    Vendor ID

device_rev
    Device revision

asm_did
    Assembly device ID

asm_vid
    Assembly vendor ID

asm_rev
    Assembly revision

efptr
    Extended feature pointer

pef
    Processing element features

swpinfo
    Switch port info

src_ops
    Source operation capabilities

dst_ops
    Destination operation capabilities

comp_tag
    RIO component tag

phys_efptr
    RIO device extended features pointer

phys_rmap
    LP-Serial Register Map Type (1 or 2)

em_efptr
    RIO Error Management features pointer

dma_mask
    Mask of bits of RIO address this device implements

driver
    Driver claiming this device

dev
    Device model device

riores
    RIO resources this device owns

pwcback
    port-write callback function for this device

destid
    Network destination ID (or associated destid for switch)

hopcount
    Hopcount to this device

prev
    Previous RIO device connected to the current one

state
    device state

rswitch
    struct rio_switch (if valid for this device)

.. _`rio_msg`:

struct rio_msg
==============

.. c:type:: struct rio_msg

    RIO message event

.. _`rio_msg.definition`:

Definition
----------

.. code-block:: c

    struct rio_msg {
        struct resource *res;
        void (*mcback)(struct rio_mport * mport, void *dev_id, int mbox, int slot);
    }

.. _`rio_msg.members`:

Members
-------

res
    Mailbox resource

mcback
    Message event callback

.. _`rio_dbell`:

struct rio_dbell
================

.. c:type:: struct rio_dbell

    RIO doorbell event

.. _`rio_dbell.definition`:

Definition
----------

.. code-block:: c

    struct rio_dbell {
        struct list_head node;
        struct resource *res;
        void (*dinb)(struct rio_mport *mport, void *dev_id, u16 src, u16 dst, u16 info);
        void *dev_id;
    }

.. _`rio_dbell.members`:

Members
-------

node
    Node in list of doorbell events

res
    Doorbell resource

dinb
    Doorbell event callback

dev_id
    Device specific pointer to pass on event

.. _`rio_mport`:

struct rio_mport
================

.. c:type:: struct rio_mport

    RIO master port info

.. _`rio_mport.definition`:

Definition
----------

.. code-block:: c

    struct rio_mport {
        struct list_head dbells;
        struct list_head pwrites;
        struct list_head node;
        struct list_head nnode;
        struct rio_net *net;
        struct mutex lock;
        struct resource iores;
        struct resource riores[RIO_MAX_MPORT_RESOURCES];
        struct rio_msg inb_msg[RIO_MAX_MBOX];
        struct rio_msg outb_msg[RIO_MAX_MBOX];
        int host_deviceid;
        struct rio_ops *ops;
        unsigned char id;
        unsigned char index;
        unsigned int sys_size;
        u32 phys_efptr;
        u32 phys_rmap;
        unsigned char name[RIO_MAX_MPORT_NAME];
        struct device dev;
        void *priv;
    #ifdef CONFIG_RAPIDIO_DMA_ENGINE
        struct dma_device dma;
    #endif
        struct rio_scan *nscan;
        atomic_t state;
        unsigned int pwe_refcnt;
    }

.. _`rio_mport.members`:

Members
-------

dbells
    List of doorbell events

pwrites
    List of portwrite events

node
    Node in global list of master ports

nnode
    Node in network list of master ports

net
    RIO net this mport is attached to

lock
    lock to synchronize lists manipulations

iores
    I/O mem resource that this master port interface owns

riores
    RIO resources that this master port interfaces owns

inb_msg
    RIO inbound message event descriptors

outb_msg
    RIO outbound message event descriptors

host_deviceid
    Host device ID associated with this master port

ops
    configuration space functions

id
    Port ID, unique among all ports

index
    Port index, unique among all port interfaces of the same type

sys_size
    RapidIO common transport system size

phys_efptr
    RIO port extended features pointer

phys_rmap
    LP-Serial EFB Register Mapping type (1 or 2).

name
    Port name string

dev
    device structure associated with an mport

priv
    Master port private data

dma
    DMA device associated with mport

nscan
    RapidIO network enumeration/discovery operations

state
    mport device state

pwe_refcnt
    port-write enable ref counter to track enable/disable requests

.. _`rio_net`:

struct rio_net
==============

.. c:type:: struct rio_net

    RIO network info

.. _`rio_net.definition`:

Definition
----------

.. code-block:: c

    struct rio_net {
        struct list_head node;
        struct list_head devices;
        struct list_head switches;
        struct list_head mports;
        struct rio_mport *hport;
        unsigned char id;
        struct device dev;
        void *enum_data;
        void (*release)(struct rio_net *net);
    }

.. _`rio_net.members`:

Members
-------

node
    Node in global list of RIO networks

devices
    List of devices in this network

switches
    List of switches in this network

mports
    List of master ports accessing this network

hport
    Default port for accessing this network

id
    RIO network ID

dev
    Device object

enum_data
    private data specific to a network enumerator

release
    enumerator-specific release callback

.. _`rio_mport_attr`:

struct rio_mport_attr
=====================

.. c:type:: struct rio_mport_attr

    RIO mport device attributes

.. _`rio_mport_attr.definition`:

Definition
----------

.. code-block:: c

    struct rio_mport_attr {
        int flags;
        int link_speed;
        int link_width;
        int dma_max_sge;
        int dma_max_size;
        int dma_align;
    }

.. _`rio_mport_attr.members`:

Members
-------

flags
    mport device capability flags

link_speed
    SRIO link speed value (as defined by RapidIO specification)

link_width
    SRIO link width value (as defined by RapidIO specification)

dma_max_sge
    number of SG list entries that can be handled by DMA channel(s)

dma_max_size
    max number of bytes in single DMA transfer (SG entry)

dma_align
    alignment shift for DMA operations (as for other DMA operations)

.. _`rio_ops`:

struct rio_ops
==============

.. c:type:: struct rio_ops

    Low-level RIO configuration space operations

.. _`rio_ops.definition`:

Definition
----------

.. code-block:: c

    struct rio_ops {
        int (*lcread)(struct rio_mport *mport, int index, u32 offset, int len,u32 *data);
        int (*lcwrite)(struct rio_mport *mport, int index, u32 offset, int len,u32 data);
        int (*cread)(struct rio_mport *mport, int index, u16 destid,u8 hopcount, u32 offset, int len, u32 *data);
        int (*cwrite)(struct rio_mport *mport, int index, u16 destid,u8 hopcount, u32 offset, int len, u32 data);
        int (*dsend)(struct rio_mport *mport, int index, u16 destid, u16 data);
        int (*pwenable)(struct rio_mport *mport, int enable);
        int (*open_outb_mbox)(struct rio_mport *mport, void *dev_id,int mbox, int entries);
        void (*close_outb_mbox)(struct rio_mport *mport, int mbox);
        int (*open_inb_mbox)(struct rio_mport *mport, void *dev_id,int mbox, int entries);
        void (*close_inb_mbox)(struct rio_mport *mport, int mbox);
        int (*add_outb_message)(struct rio_mport *mport, struct rio_dev *rdev,int mbox, void *buffer, size_t len);
        int (*add_inb_buffer)(struct rio_mport *mport, int mbox, void *buf);
        void *(*get_inb_message)(struct rio_mport *mport, int mbox);
        int (*map_inb)(struct rio_mport *mport, dma_addr_t lstart,u64 rstart, u64 size, u32 flags);
        void (*unmap_inb)(struct rio_mport *mport, dma_addr_t lstart);
        int (*query_mport)(struct rio_mport *mport,struct rio_mport_attr *attr);
        int (*map_outb)(struct rio_mport *mport, u16 destid, u64 rstart,u32 size, u32 flags, dma_addr_t *laddr);
        void (*unmap_outb)(struct rio_mport *mport, u16 destid, u64 rstart);
    }

.. _`rio_ops.members`:

Members
-------

lcread
    Callback to perform local (master port) read of config space.

lcwrite
    Callback to perform local (master port) write of config space.

cread
    Callback to perform network read of config space.

cwrite
    Callback to perform network write of config space.

dsend
    Callback to send a doorbell message.

pwenable
    Callback to enable/disable port-write message handling.

open_outb_mbox
    Callback to initialize outbound mailbox.

close_outb_mbox
    Callback to shut down outbound mailbox.

open_inb_mbox
    Callback to initialize inbound mailbox.

close_inb_mbox
    Callback to shut down inbound mailbox.

add_outb_message
    Callback to add a message to an outbound mailbox queue.

add_inb_buffer
    Callback to add a buffer to an inbound mailbox queue.

get_inb_message
    Callback to get a message from an inbound mailbox queue.

map_inb
    Callback to map RapidIO address region into local memory space.

unmap_inb
    Callback to unmap RapidIO address region mapped with \ :c:func:`map_inb`\ .

query_mport
    Callback to query mport device attributes.

map_outb
    Callback to map outbound address region into local memory space.

unmap_outb
    Callback to unmap outbound RapidIO address region.

.. _`rio_driver`:

struct rio_driver
=================

.. c:type:: struct rio_driver

    RIO driver info

.. _`rio_driver.definition`:

Definition
----------

.. code-block:: c

    struct rio_driver {
        struct list_head node;
        char *name;
        const struct rio_device_id *id_table;
        int (*probe)(struct rio_dev * dev, const struct rio_device_id * id);
        void (*remove)(struct rio_dev * dev);
        void (*shutdown)(struct rio_dev *dev);
        int (*suspend)(struct rio_dev * dev, u32 state);
        int (*resume)(struct rio_dev * dev);
        int (*enable_wake)(struct rio_dev * dev, u32 state, int enable);
        struct device_driver driver;
    }

.. _`rio_driver.members`:

Members
-------

node
    Node in list of drivers

name
    RIO driver name

id_table
    RIO device ids to be associated with this driver

probe
    RIO device inserted

remove
    RIO device removed

shutdown
    shutdown notification callback

suspend
    RIO device suspended

resume
    RIO device awakened

enable_wake
    RIO device enable wake event

driver
    LDM driver struct

.. _`rio_driver.description`:

Description
-----------

Provides info on a RIO device driver for insertion/removal and
power management purposes.

.. _`rio_scan`:

struct rio_scan
===============

.. c:type:: struct rio_scan

    RIO enumeration and discovery operations

.. _`rio_scan.definition`:

Definition
----------

.. code-block:: c

    struct rio_scan {
        struct module *owner;
        int (*enumerate)(struct rio_mport *mport, u32 flags);
        int (*discover)(struct rio_mport *mport, u32 flags);
    }

.. _`rio_scan.members`:

Members
-------

owner
    The module owner of this structure

enumerate
    Callback to perform RapidIO fabric enumeration.

discover
    Callback to perform RapidIO fabric discovery.

.. _`rio_scan_node`:

struct rio_scan_node
====================

.. c:type:: struct rio_scan_node

    list node to register RapidIO enumeration and discovery methods with RapidIO core.

.. _`rio_scan_node.definition`:

Definition
----------

.. code-block:: c

    struct rio_scan_node {
        int mport_id;
        struct list_head node;
        struct rio_scan *ops;
    }

.. _`rio_scan_node.members`:

Members
-------

mport_id
    ID of an mport (net) serviced by this enumerator

node
    node in global list of registered enumerators

ops
    RIO enumeration and discovery operations

.. This file was automatic generated / don't edit.


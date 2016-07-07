.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/remoteproc.h

.. _`resource_table`:

struct resource_table
=====================

.. c:type:: struct resource_table

    firmware resource table header

.. _`resource_table.definition`:

Definition
----------

.. code-block:: c

    struct resource_table {
        u32 ver;
        u32 num;
        u32 reserved[2];
        u32 offset[0];
    }

.. _`resource_table.members`:

Members
-------

ver
    version number

num
    number of resource entries

reserved
    reserved (must be zero)

offset
    array of offsets pointing at the various resource entries

.. _`resource_table.description`:

Description
-----------

A resource table is essentially a list of system resources required
by the remote processor. It may also include configuration entries.
If needed, the remote processor firmware should contain this table
as a dedicated ".resource_table" ELF section.

Some resources entries are mere announcements, where the host is informed
of specific remoteproc configuration. Other entries require the host to
do something (e.g. allocate a system resource). Sometimes a negotiation
is expected, where the firmware requests a resource, and once allocated,
the host should provide back its details (e.g. address of an allocated
memory region).

The header of the resource table, as expressed by this structure,
contains a version number (should we need to change this format in the
future), the number of available resource entries, and their offsets
in the table.

Immediately following this header are the resource entries themselves,
each of which begins with a resource entry header (as described below).

.. _`fw_rsc_hdr`:

struct fw_rsc_hdr
=================

.. c:type:: struct fw_rsc_hdr

    firmware resource entry header

.. _`fw_rsc_hdr.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_hdr {
        u32 type;
        u8 data[0];
    }

.. _`fw_rsc_hdr.members`:

Members
-------

type
    resource type

data
    resource data

.. _`fw_rsc_hdr.description`:

Description
-----------

Every resource entry begins with a 'struct fw_rsc_hdr' header providing
its \ ``type``\ . The content of the entry itself will immediately follow
this header, and it should be parsed according to the resource type.

.. _`fw_resource_type`:

enum fw_resource_type
=====================

.. c:type:: enum fw_resource_type

    types of resource entries

.. _`fw_resource_type.definition`:

Definition
----------

.. code-block:: c

    enum fw_resource_type {
        RSC_CARVEOUT,
        RSC_DEVMEM,
        RSC_TRACE,
        RSC_VDEV,
        RSC_LAST
    };

.. _`fw_resource_type.constants`:

Constants
---------

RSC_CARVEOUT
    request for allocation of a physically contiguous
    memory region.

RSC_DEVMEM
    request to iommu_map a memory-based peripheral.

RSC_TRACE
    announces the availability of a trace buffer into which
    the remote processor will be writing logs.

RSC_VDEV
    declare support for a virtio device, and serve as its
    virtio header.

RSC_LAST
    just keep this one at the end

.. _`fw_resource_type.description`:

Description
-----------

For more details regarding a specific resource type, please see its
dedicated structure below.

Please note that these values are used as indices to the rproc_handle_rsc
lookup table, so please keep them sane. Moreover, \ ``RSC_LAST``\  is used to
check the validity of an index before the lookup table is accessed, so
please update it as needed.

.. _`fw_rsc_carveout`:

struct fw_rsc_carveout
======================

.. c:type:: struct fw_rsc_carveout

    physically contiguous memory request

.. _`fw_rsc_carveout.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_carveout {
        u32 da;
        u32 pa;
        u32 len;
        u32 flags;
        u32 reserved;
        u8 name[32];
    }

.. _`fw_rsc_carveout.members`:

Members
-------

da
    device address

pa
    physical address

len
    length (in bytes)

flags
    iommu protection flags

reserved
    reserved (must be zero)

name
    human-readable name of the requested memory region

.. _`fw_rsc_carveout.description`:

Description
-----------

This resource entry requests the host to allocate a physically contiguous
memory region.

These request entries should precede other firmware resource entries,
as other entries might request placing other data objects inside
these memory regions (e.g. data/code segments, trace resource entries, ...).

Allocating memory this way helps utilizing the reserved physical memory
(e.g. CMA) more efficiently, and also minimizes the number of TLB entries
needed to map it (in case \ ``rproc``\  is using an IOMMU). Reducing the TLB
pressure is important; it may have a substantial impact on performance.

If the firmware is compiled with static addresses, then \ ``da``\  should specify
the expected device address of this memory region. If \ ``da``\  is set to
FW_RSC_ADDR_ANY, then the host will dynamically allocate it, and then
overwrite \ ``da``\  with the dynamically allocated address.

We will always use \ ``da``\  to negotiate the device addresses, even if it
isn't using an iommu. In that case, though, it will obviously contain
physical addresses.

Some remote processors needs to know the allocated physical address
even if they do use an iommu. This is needed, e.g., if they control
hardware accelerators which access the physical memory directly (this
is the case with OMAP4 for instance). In that case, the host will
overwrite \ ``pa``\  with the dynamically allocated physical address.
Generally we don't want to expose physical addresses if we don't have to
(remote processors are generally \_not\_ trusted), so we might want to
change this to happen \_only\_ when explicitly required by the hardware.

\ ``flags``\  is used to provide IOMMU protection flags, and \ ``name``\  should
(optionally) contain a human readable name of this carveout region
(mainly for debugging purposes).

.. _`fw_rsc_devmem`:

struct fw_rsc_devmem
====================

.. c:type:: struct fw_rsc_devmem

    iommu mapping request

.. _`fw_rsc_devmem.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_devmem {
        u32 da;
        u32 pa;
        u32 len;
        u32 flags;
        u32 reserved;
        u8 name[32];
    }

.. _`fw_rsc_devmem.members`:

Members
-------

da
    device address

pa
    physical address

len
    length (in bytes)

flags
    iommu protection flags

reserved
    reserved (must be zero)

name
    human-readable name of the requested region to be mapped

.. _`fw_rsc_devmem.description`:

Description
-----------

This resource entry requests the host to iommu map a physically contiguous
memory region. This is needed in case the remote processor requires
access to certain memory-based peripherals; \_never\_ use it to access
regular memory.

This is obviously only needed if the remote processor is accessing memory
via an iommu.

\ ``da``\  should specify the required device address, \ ``pa``\  should specify
the physical address we want to map, \ ``len``\  should specify the size of
the mapping and \ ``flags``\  is the IOMMU protection flags. As always, \ ``name``\  may
(optionally) contain a human readable name of this mapping (mainly for
debugging purposes).

.. _`fw_rsc_devmem.note`:

Note
----

at this point we just "trust" those devmem entries to contain valid
physical addresses, but this isn't safe and will be changed: eventually we
want remoteproc implementations to provide us ranges of physical addresses
the firmware is allowed to request, and not allow firmwares to request
access to physical addresses that are outside those ranges.

.. _`fw_rsc_trace`:

struct fw_rsc_trace
===================

.. c:type:: struct fw_rsc_trace

    trace buffer declaration

.. _`fw_rsc_trace.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_trace {
        u32 da;
        u32 len;
        u32 reserved;
        u8 name[32];
    }

.. _`fw_rsc_trace.members`:

Members
-------

da
    device address

len
    length (in bytes)

reserved
    reserved (must be zero)

name
    human-readable name of the trace buffer

.. _`fw_rsc_trace.description`:

Description
-----------

This resource entry provides the host information about a trace buffer
into which the remote processor will write log messages.

\ ``da``\  specifies the device address of the buffer, \ ``len``\  specifies
its size, and \ ``name``\  may contain a human readable name of the trace buffer.

After booting the remote processor, the trace buffers are exposed to the
user via debugfs entries (called trace0, trace1, etc..).

.. _`fw_rsc_vdev_vring`:

struct fw_rsc_vdev_vring
========================

.. c:type:: struct fw_rsc_vdev_vring

    vring descriptor entry

.. _`fw_rsc_vdev_vring.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_vdev_vring {
        u32 da;
        u32 align;
        u32 num;
        u32 notifyid;
        u32 reserved;
    }

.. _`fw_rsc_vdev_vring.members`:

Members
-------

da
    device address

align
    the alignment between the consumer and producer parts of the vring

num
    num of buffers supported by this vring (must be power of two)
    \ ``notifyid``\  is a unique rproc-wide notify index for this vring. This notify
    index is used when kicking a remote processor, to let it know that this
    vring is triggered.

notifyid
    *undescribed*

reserved
    reserved (must be zero)

.. _`fw_rsc_vdev_vring.description`:

Description
-----------

This descriptor is not a resource entry by itself; it is part of the
vdev resource type (see below).

Note that \ ``da``\  should either contain the device address where
the remote processor is expecting the vring, or indicate that
dynamically allocation of the vring's device address is supported.

.. _`fw_rsc_vdev`:

struct fw_rsc_vdev
==================

.. c:type:: struct fw_rsc_vdev

    virtio device header

.. _`fw_rsc_vdev.definition`:

Definition
----------

.. code-block:: c

    struct fw_rsc_vdev {
        u32 id;
        u32 notifyid;
        u32 dfeatures;
        u32 gfeatures;
        u32 config_len;
        u8 status;
        u8 num_of_vrings;
        u8 reserved[2];
        struct fw_rsc_vdev_vring vring[0];
    }

.. _`fw_rsc_vdev.members`:

Members
-------

id
    virtio device id (as in virtio_ids.h)
    \ ``notifyid``\  is a unique rproc-wide notify index for this vdev. This notify
    index is used when kicking a remote processor, to let it know that the
    status/features of this vdev have changes.
    \ ``dfeatures``\  specifies the virtio device features supported by the firmware
    \ ``gfeatures``\  is a place holder used by the host to write back the
    negotiated features that are supported by both sides.
    \ ``config_len``\  is the size of the virtio config space of this vdev. The config
    space lies in the resource table immediate after this vdev header.
    \ ``status``\  is a place holder where the host will indicate its virtio progress.
    \ ``num_of_vrings``\  indicates how many vrings are described in this vdev header

notifyid
    *undescribed*

dfeatures
    *undescribed*

gfeatures
    *undescribed*

config_len
    *undescribed*

status
    *undescribed*

num_of_vrings
    *undescribed*

reserved
    reserved (must be zero)
    \ ``vring``\  is an array of \ ``num_of_vrings``\  entries of 'struct fw_rsc_vdev_vring'.

.. _`fw_rsc_vdev.this-resource-is-a-virtio-device-header`:

This resource is a virtio device header
---------------------------------------

it provides information about
the vdev, and is then used by the host and its peer remote processors
to negotiate and share certain virtio properties.

By providing this resource entry, the firmware essentially asks remoteproc
to statically allocate a vdev upon registration of the rproc (dynamic vdev
allocation is not yet supported).

.. _`fw_rsc_vdev.note`:

Note
----

unlike virtualization systems, the term 'host' here means
the Linux side which is running remoteproc to control the remote
processors. We use the name 'gfeatures' to comply with virtio's terms,
though there isn't really any virtualized guest OS here: it's the host
which is responsible for negotiating the final features.
Yeah, it's a bit confusing.

immediately following this structure is the virtio config space for
this vdev (which is specific to the vdev; for more info, read the virtio
spec). the size of the config space is specified by \ ``config_len``\ .

.. _`rproc_mem_entry`:

struct rproc_mem_entry
======================

.. c:type:: struct rproc_mem_entry

    memory entry descriptor

.. _`rproc_mem_entry.definition`:

Definition
----------

.. code-block:: c

    struct rproc_mem_entry {
        void *va;
        dma_addr_t dma;
        int len;
        u32 da;
        void *priv;
        struct list_head node;
    }

.. _`rproc_mem_entry.members`:

Members
-------

va
    virtual address

dma
    dma address

len
    length, in bytes

da
    device address

priv
    associated data

node
    list node

.. _`rproc_ops`:

struct rproc_ops
================

.. c:type:: struct rproc_ops

    platform-specific device handlers

.. _`rproc_ops.definition`:

Definition
----------

.. code-block:: c

    struct rproc_ops {
        int (* start) (struct rproc *rproc);
        int (* stop) (struct rproc *rproc);
        void (* kick) (struct rproc *rproc, int vqid);
        void * (* da_to_va) (struct rproc *rproc, u64 da, int len);
    }

.. _`rproc_ops.members`:

Members
-------

start
    power on the device and boot it

stop
    power off the device

kick
    kick a virtqueue (virtqueue id given as a parameter)

da_to_va
    optional platform hook to perform address translations

.. _`rproc_state`:

enum rproc_state
================

.. c:type:: enum rproc_state

    remote processor states

.. _`rproc_state.definition`:

Definition
----------

.. code-block:: c

    enum rproc_state {
        RPROC_OFFLINE,
        RPROC_SUSPENDED,
        RPROC_RUNNING,
        RPROC_CRASHED,
        RPROC_LAST
    };

.. _`rproc_state.constants`:

Constants
---------

RPROC_OFFLINE
    device is powered off

RPROC_SUSPENDED
    device is suspended; needs to be woken up to receive
    a message.

RPROC_RUNNING
    device is up and running

RPROC_CRASHED
    device has crashed; need to start recovery

RPROC_LAST
    just keep this one at the end

.. _`rproc_state.description`:

Description
-----------

Please note that the values of these states are used as indices
to rproc_state_string, a state-to-name lookup table,
so please keep the two synchronized. \ ``RPROC_LAST``\  is used to check
the validity of an index before the lookup table is accessed, so
please update it as needed too.

.. _`rproc_crash_type`:

enum rproc_crash_type
=====================

.. c:type:: enum rproc_crash_type

    remote processor crash types

.. _`rproc_crash_type.definition`:

Definition
----------

.. code-block:: c

    enum rproc_crash_type {
        RPROC_MMUFAULT,
        RPROC_WATCHDOG,
        RPROC_FATAL_ERROR
    };

.. _`rproc_crash_type.constants`:

Constants
---------

RPROC_MMUFAULT
    iommu fault

RPROC_WATCHDOG
    watchdog bite
    \ ``RPROC_FATAL_ERROR``\    fatal error

RPROC_FATAL_ERROR
    *undescribed*

.. _`rproc_crash_type.description`:

Description
-----------

Each element of the enum is used as an array index. So that, the value of
the elements should be always something sane.

Feel free to add more types when needed.

.. _`rproc`:

struct rproc
============

.. c:type:: struct rproc

    represents a physical remote processor device

.. _`rproc.definition`:

Definition
----------

.. code-block:: c

    struct rproc {
        struct list_head node;
        struct iommu_domain *domain;
        const char *name;
        const char *firmware;
        void *priv;
        const struct rproc_ops *ops;
        struct device dev;
        const struct rproc_fw_ops *fw_ops;
        atomic_t power;
        unsigned int state;
        struct mutex lock;
        struct dentry *dbg_dir;
        struct list_head traces;
        int num_traces;
        struct list_head carveouts;
        struct list_head mappings;
        struct completion firmware_loading_complete;
        u32 bootaddr;
        struct list_head rvdevs;
        struct idr notifyids;
        int index;
        struct work_struct crash_handler;
        unsigned crash_cnt;
        struct completion crash_comp;
        bool recovery_disabled;
        int max_notifyid;
        struct resource_table *table_ptr;
        struct resource_table *cached_table;
        u32 table_csum;
        bool has_iommu;
    }

.. _`rproc.members`:

Members
-------

node
    list node of this rproc object

domain
    iommu domain

name
    human readable name of the rproc

firmware
    name of firmware file to be loaded

priv
    private data which belongs to the platform-specific rproc module

ops
    platform-specific start/stop rproc handlers

dev
    virtual device for refcounting and common remoteproc behavior

fw_ops
    firmware-specific handlers

power
    refcount of users who need this rproc powered up

state
    state of the device

lock
    lock which protects concurrent manipulations of the rproc

dbg_dir
    debugfs directory of this rproc device

traces
    list of trace buffers

num_traces
    number of trace buffers

carveouts
    list of physically contiguous memory allocations

mappings
    list of iommu mappings we initiated, needed on shutdown

firmware_loading_complete
    marks e/o asynchronous firmware loading

bootaddr
    address of first instruction to boot rproc with (optional)

rvdevs
    list of remote virtio devices

notifyids
    idr for dynamically assigning rproc-wide unique notify ids

index
    index of this rproc device

crash_handler
    workqueue for handling a crash

crash_cnt
    crash counter

crash_comp
    completion used to sync crash handler and the rproc reload

recovery_disabled
    flag that state if recovery was disabled

max_notifyid
    largest allocated notify id.

table_ptr
    pointer to the resource table in effect

cached_table
    copy of the resource table

table_csum
    checksum of the resource table

has_iommu
    flag to indicate if remote processor is behind an MMU

.. _`rproc_vring`:

struct rproc_vring
==================

.. c:type:: struct rproc_vring

    remoteproc vring state

.. _`rproc_vring.definition`:

Definition
----------

.. code-block:: c

    struct rproc_vring {
        void *va;
        dma_addr_t dma;
        int len;
        u32 da;
        u32 align;
        int notifyid;
        struct rproc_vdev *rvdev;
        struct virtqueue *vq;
    }

.. _`rproc_vring.members`:

Members
-------

va
    virtual address

dma
    dma address

len
    length, in bytes

da
    device address

align
    vring alignment

notifyid
    rproc-specific unique vring index

rvdev
    remote vdev

vq
    the virtqueue of this vring

.. _`rproc_vdev`:

struct rproc_vdev
=================

.. c:type:: struct rproc_vdev

    remoteproc state for a supported virtio device

.. _`rproc_vdev.definition`:

Definition
----------

.. code-block:: c

    struct rproc_vdev {
        struct list_head node;
        struct rproc *rproc;
        struct virtio_device vdev;
        struct rproc_vring vring[RVDEV_NUM_VRINGS];
        u32 rsc_offset;
    }

.. _`rproc_vdev.members`:

Members
-------

node
    list node

rproc
    the rproc handle

vdev
    the virio device

vring
    the vrings for this vdev

rsc_offset
    offset of the vdev's resource entry

.. This file was automatic generated / don't edit.


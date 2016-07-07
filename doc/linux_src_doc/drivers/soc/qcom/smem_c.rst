.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smem.c

.. _`smem_proc_comm`:

struct smem_proc_comm
=====================

.. c:type:: struct smem_proc_comm

    proc_comm communication struct (legacy)

.. _`smem_proc_comm.definition`:

Definition
----------

.. code-block:: c

    struct smem_proc_comm {
        __le32 command;
        __le32 status;
        __le32 params[2];
    }

.. _`smem_proc_comm.members`:

Members
-------

command
    current command to be executed

status
    status of the currently requested command

params
    parameters to the command

.. _`smem_global_entry`:

struct smem_global_entry
========================

.. c:type:: struct smem_global_entry

    entry to reference smem items on the heap

.. _`smem_global_entry.definition`:

Definition
----------

.. code-block:: c

    struct smem_global_entry {
        __le32 allocated;
        __le32 offset;
        __le32 size;
        __le32 aux_base;
    }

.. _`smem_global_entry.members`:

Members
-------

allocated
    boolean to indicate if this entry is used

offset
    offset to the allocated space

size
    size of the allocated space, 8 byte aligned

aux_base
    base address for the memory region used by this unit, or 0 for
    the default region. bits 0,1 are reserved

.. _`smem_header`:

struct smem_header
==================

.. c:type:: struct smem_header

    header found in beginning of primary smem region

.. _`smem_header.definition`:

Definition
----------

.. code-block:: c

    struct smem_header {
        struct smem_proc_comm proc_comm[4];
        __le32 version[32];
        __le32 initialized;
        __le32 free_offset;
        __le32 available;
        __le32 reserved;
        struct smem_global_entry toc[SMEM_ITEM_COUNT];
    }

.. _`smem_header.members`:

Members
-------

proc_comm
    proc_comm communication interface (legacy)

version
    array of versions for the various subsystems

initialized
    boolean to indicate that smem is initialized

free_offset
    index of the first unallocated byte in smem

available
    number of bytes available for allocation

reserved
    reserved field, must be 0

.. _`smem_header.toc`:

toc
---

array of references to items

.. _`smem_ptable_entry`:

struct smem_ptable_entry
========================

.. c:type:: struct smem_ptable_entry

    one entry in the \ ``smem_ptable``\  list

.. _`smem_ptable_entry.definition`:

Definition
----------

.. code-block:: c

    struct smem_ptable_entry {
        __le32 offset;
        __le32 size;
        __le32 flags;
        __le16 host0;
        __le16 host1;
        __le32 reserved[8];
    }

.. _`smem_ptable_entry.members`:

Members
-------

offset
    offset, within the main shared memory region, of the partition

size
    size of the partition

flags
    flags for the partition (currently unused)

host0
    first processor/host with access to this partition

host1
    second processor/host with access to this partition

reserved
    reserved entries for later use

.. _`smem_ptable`:

struct smem_ptable
==================

.. c:type:: struct smem_ptable

    partition table for the private partitions

.. _`smem_ptable.definition`:

Definition
----------

.. code-block:: c

    struct smem_ptable {
        u8 magic[4];
        __le32 version;
        __le32 num_entries;
        __le32 reserved[5];
        struct smem_ptable_entry entry[];
    }

.. _`smem_ptable.members`:

Members
-------

magic
    magic number, must be SMEM_PTABLE_MAGIC

version
    version of the partition table

num_entries
    number of partitions in the table

reserved
    for now reserved entries

entry
    list of \ ``smem_ptable_entry``\  for the \ ``num_entries``\  partitions

.. _`smem_partition_header`:

struct smem_partition_header
============================

.. c:type:: struct smem_partition_header

    header of the partitions

.. _`smem_partition_header.definition`:

Definition
----------

.. code-block:: c

    struct smem_partition_header {
        u8 magic[4];
        __le16 host0;
        __le16 host1;
        __le32 size;
        __le32 offset_free_uncached;
        __le32 offset_free_cached;
        __le32 reserved[3];
    }

.. _`smem_partition_header.members`:

Members
-------

magic
    magic number, must be SMEM_PART_MAGIC

host0
    first processor/host with access to this partition

host1
    second processor/host with access to this partition

size
    size of the partition

offset_free_uncached
    offset to the first free byte of uncached memory in
    this partition

offset_free_cached
    offset to the first free byte of cached memory in this
    partition

reserved
    for now reserved entries

.. _`smem_private_entry`:

struct smem_private_entry
=========================

.. c:type:: struct smem_private_entry

    header of each item in the private partition

.. _`smem_private_entry.definition`:

Definition
----------

.. code-block:: c

    struct smem_private_entry {
        u16 canary;
        __le16 item;
        __le32 size;
        __le16 padding_data;
        __le16 padding_hdr;
        __le32 reserved;
    }

.. _`smem_private_entry.members`:

Members
-------

canary
    magic number, must be SMEM_PRIVATE_CANARY

item
    identifying number of the smem item

size
    size of the data, including padding bytes

padding_data
    number of bytes of padding of data

padding_hdr
    number of bytes of padding between the header and the data

reserved
    for now reserved entry

.. _`smem_region`:

struct smem_region
==================

.. c:type:: struct smem_region

    representation of a chunk of memory used for smem

.. _`smem_region.definition`:

Definition
----------

.. code-block:: c

    struct smem_region {
        u32 aux_base;
        void __iomem *virt_base;
        size_t size;
    }

.. _`smem_region.members`:

Members
-------

aux_base
    identifier of aux_mem base

virt_base
    virtual base address of memory with this aux_mem identifier

size
    size of the memory region

.. _`qcom_smem`:

struct qcom_smem
================

.. c:type:: struct qcom_smem

    device data for the smem device

.. _`qcom_smem.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smem {
        struct device *dev;
        struct hwspinlock *hwlock;
        struct smem_partition_header  *partitions[SMEM_HOST_COUNT];
        unsigned num_regions;
        struct smem_region regions[0];
    }

.. _`qcom_smem.members`:

Members
-------

dev
    device pointer

hwlock
    reference to a hwspinlock

partitions
    list of pointers to partitions affecting the current
    processor/host

num_regions
    number of \ ``regions``\ 

regions
    list of the memory regions defining the shared memory

.. _`qcom_smem_alloc`:

qcom_smem_alloc
===============

.. c:function:: int qcom_smem_alloc(unsigned host, unsigned item, size_t size)

    allocate space for a smem item

    :param unsigned host:
        remote processor id, or -1

    :param unsigned item:
        smem item handle

    :param size_t size:
        number of bytes to be allocated

.. _`qcom_smem_alloc.description`:

Description
-----------

Allocate space for a given smem item of size \ ``size``\ , given that the item is
not yet allocated.

.. _`qcom_smem_get`:

qcom_smem_get
=============

.. c:function:: void *qcom_smem_get(unsigned host, unsigned item, size_t *size)

    resolve ptr of size of a smem item

    :param unsigned host:
        the remote processor, or -1

    :param unsigned item:
        smem item handle

    :param size_t \*size:
        pointer to be filled out with size of the item

.. _`qcom_smem_get.description`:

Description
-----------

Looks up smem item and returns pointer to it. Size of smem
item is returned in \ ``size``\ .

.. _`qcom_smem_get_free_space`:

qcom_smem_get_free_space
========================

.. c:function:: int qcom_smem_get_free_space(unsigned host)

    retrieve amount of free space in a partition

    :param unsigned host:
        the remote processor identifying a partition, or -1

.. _`qcom_smem_get_free_space.description`:

Description
-----------

To be used by smem clients as a quick way to determine if any new
allocations has been made.

.. This file was automatic generated / don't edit.


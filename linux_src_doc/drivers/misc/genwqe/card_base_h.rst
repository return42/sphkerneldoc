.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/genwqe/card_base.h

.. _`genwqe_msi_irqs`:

GENWQE_MSI_IRQS
===============

.. c:function::  GENWQE_MSI_IRQS()

.. _`genwqe_msi_irqs.description`:

Description
-----------

(C) Copyright IBM Corp. 2013

.. _`genwqe_msi_irqs.author`:

Author
------

Frank Haverkamp <haver@linux.vnet.ibm.com>

Joerg-Stephan Vogt <jsvogt@de.ibm.com>

Michael Jung <mijung@gmx.net>

Michael Ruettger <michael@ibmra.de>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 2 only)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

.. _`genwqe_reg`:

struct genwqe_reg
=================

.. c:type:: struct genwqe_reg

    Genwqe data dump functionality

.. _`genwqe_reg.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_reg {
        u32 addr;
        u32 idx;
        u64 val;
    }

.. _`genwqe_reg.members`:

Members
-------

addr
    *undescribed*

idx
    *undescribed*

val
    *undescribed*

.. _`dma_mapping`:

struct dma_mapping
==================

.. c:type:: struct dma_mapping

    Information about memory mappings done by the driver

.. _`dma_mapping.definition`:

Definition
----------

.. code-block:: c

    struct dma_mapping {
        enum dma_mapping_type type;
        void *u_vaddr;
        void *k_vaddr;
        dma_addr_t dma_addr;
        struct page **page_list;
        dma_addr_t *dma_list;
        unsigned int nr_pages;
        unsigned int size;
        struct list_head card_list;
        struct list_head pin_list;
    }

.. _`dma_mapping.members`:

Members
-------

type
    *undescribed*

u_vaddr
    *undescribed*

k_vaddr
    *undescribed*

dma_addr
    *undescribed*

page_list
    *undescribed*

dma_list
    *undescribed*

nr_pages
    *undescribed*

size
    *undescribed*

card_list
    *undescribed*

pin_list
    *undescribed*

.. _`ddcb_queue`:

struct ddcb_queue
=================

.. c:type:: struct ddcb_queue

    DDCB queue data

.. _`ddcb_queue.definition`:

Definition
----------

.. code-block:: c

    struct ddcb_queue {
        int ddcb_max;
        int ddcb_next;
        int ddcb_act;
        u16 ddcb_seq;
        unsigned int ddcbs_in_flight;
        unsigned int ddcbs_completed;
        unsigned int ddcbs_max_in_flight;
        unsigned int return_on_busy;
        unsigned int wait_on_busy;
        dma_addr_t ddcb_daddr;
        struct ddcb *ddcb_vaddr;
        struct ddcb_requ **ddcb_req;
        wait_queue_head_t *ddcb_waitqs;
        spinlock_t ddcb_lock;
        wait_queue_head_t busy_waitq;
        u32 IO_QUEUE_CONFIG;
        u32 IO_QUEUE_STATUS;
        u32 IO_QUEUE_SEGMENT;
        u32 IO_QUEUE_INITSQN;
        u32 IO_QUEUE_WRAP;
        u32 IO_QUEUE_OFFSET;
        u32 IO_QUEUE_WTIME;
        u32 IO_QUEUE_ERRCNTS;
        u32 IO_QUEUE_LRW;
    }

.. _`ddcb_queue.members`:

Members
-------

ddcb_max
    Number of DDCBs on the queue

ddcb_next
    Next free DDCB

ddcb_act
    Next DDCB supposed to finish

ddcb_seq
    Sequence number of last DDCB

ddcbs_in_flight
    Currently enqueued DDCBs

ddcbs_completed
    Number of already completed DDCBs

ddcbs_max_in_flight
    *undescribed*

return_on_busy
    Number of -EBUSY returns on full queue

wait_on_busy
    Number of waits on full queue

ddcb_daddr
    DMA address of first DDCB in the queue

ddcb_vaddr
    Kernel virtual address of first DDCB in the queue

ddcb_req
    Associated requests (one per DDCB)

ddcb_waitqs
    Associated wait queues (one per DDCB)

ddcb_lock
    Lock to protect queuing operations

busy_waitq
    *undescribed*

IO_QUEUE_CONFIG
    *undescribed*

IO_QUEUE_STATUS
    *undescribed*

IO_QUEUE_SEGMENT
    *undescribed*

IO_QUEUE_INITSQN
    *undescribed*

IO_QUEUE_WRAP
    *undescribed*

IO_QUEUE_OFFSET
    *undescribed*

IO_QUEUE_WTIME
    *undescribed*

IO_QUEUE_ERRCNTS
    *undescribed*

IO_QUEUE_LRW
    *undescribed*

.. _`genwqe_dev`:

struct genwqe_dev
=================

.. c:type:: struct genwqe_dev

    GenWQE device information

.. _`genwqe_dev.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_dev {
        enum genwqe_card_state card_state;
        spinlock_t print_lock;
        int card_idx;
        u64 flags;
        struct genwqe_ffdc ffdc[GENWQE_DBG_UNITS];
        struct task_struct *card_thread;
        wait_queue_head_t queue_waitq;
        struct ddcb_queue queue;
        unsigned int irqs_processed;
        struct task_struct *health_thread;
        wait_queue_head_t health_waitq;
        int use_platform_recovery;
        dev_t devnum_genwqe;
        struct class *class_genwqe;
        struct device *dev;
        struct cdev cdev_genwqe;
        struct dentry *debugfs_root;
        struct dentry *debugfs_genwqe;
        struct pci_dev *pci_dev;
        void __iomem *mmio;
        unsigned long mmio_len;
        int num_vfs;
        u32 vf_jobtimeout_msec[GENWQE_MAX_VFS];
        int is_privileged;
        u64 slu_unitcfg;
        u64 app_unitcfg;
        u64 softreset;
        u64 err_inject;
        u64 last_gfir;
        char app_name[5];
        spinlock_t file_lock;
        struct list_head file_list;
        int ddcb_software_timeout;
        int skip_recovery;
        int kill_timeout;
    }

.. _`genwqe_dev.members`:

Members
-------

card_state
    Card operation state, see above

print_lock
    *undescribed*

card_idx
    *undescribed*

flags
    *undescribed*

ffdc
    First Failure Data Capture buffers for each unit

card_thread
    Working thread to operate the DDCB queue

queue_waitq
    *undescribed*

queue
    DDCB queue

irqs_processed
    *undescribed*

health_thread
    Card monitoring thread (only for PFs)

health_waitq
    Wait queue used in health_thread

use_platform_recovery
    *undescribed*

devnum_genwqe
    *undescribed*

class_genwqe
    *undescribed*

dev
    *undescribed*

cdev_genwqe
    *undescribed*

debugfs_root
    *undescribed*

debugfs_genwqe
    *undescribed*

pci_dev
    Associated PCI device (function)

mmio
    Base address of 64-bit register space

mmio_len
    Length of register area

num_vfs
    *undescribed*

vf_jobtimeout_msec
    *undescribed*

is_privileged
    *undescribed*

slu_unitcfg
    *undescribed*

app_unitcfg
    *undescribed*

softreset
    *undescribed*

err_inject
    *undescribed*

last_gfir
    *undescribed*

app_name
    *undescribed*

file_lock
    Lock to protect access to file_list

file_list
    List of all processes with open GenWQE file descriptors

ddcb_software_timeout
    *undescribed*

skip_recovery
    *undescribed*

kill_timeout
    *undescribed*

.. _`genwqe_dev.description`:

Description
-----------

This struct contains all information needed to communicate with a
GenWQE card. It is initialized when a GenWQE device is found and
destroyed when it goes away. It holds data to maintain the queue as
well as data needed to feed the user interfaces.

.. _`genwqe_requ_state`:

enum genwqe_requ_state
======================

.. c:type:: enum genwqe_requ_state

    State of a DDCB execution request

.. _`genwqe_requ_state.definition`:

Definition
----------

.. code-block:: c

    enum genwqe_requ_state {
        GENWQE_REQU_NEW,
        GENWQE_REQU_ENQUEUED,
        GENWQE_REQU_TAPPED,
        GENWQE_REQU_FINISHED,
        GENWQE_REQU_STATE_MAX
    };

.. _`genwqe_requ_state.constants`:

Constants
---------

GENWQE_REQU_NEW
    *undescribed*

GENWQE_REQU_ENQUEUED
    *undescribed*

GENWQE_REQU_TAPPED
    *undescribed*

GENWQE_REQU_FINISHED
    *undescribed*

GENWQE_REQU_STATE_MAX
    *undescribed*

.. _`genwqe_sgl`:

struct genwqe_sgl
=================

.. c:type:: struct genwqe_sgl

    Scatter gather list describing user-space memory

.. _`genwqe_sgl.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_sgl {
        dma_addr_t sgl_dma_addr;
        struct sg_entry *sgl;
        size_t sgl_size;
        void __user *user_addr;
        size_t user_size;
        unsigned long nr_pages;
        unsigned long fpage_offs;
        size_t fpage_size;
        size_t lpage_size;
        void *fpage;
        dma_addr_t fpage_dma_addr;
        void *lpage;
        dma_addr_t lpage_dma_addr;
    }

.. _`genwqe_sgl.members`:

Members
-------

sgl_dma_addr
    dma address of sgl

sgl
    scatter gather list needs to be 128 byte aligned

sgl_size
    size of area used for sgl

user_addr
    user-space address of memory area

user_size
    size of user-space memory area

nr_pages
    *undescribed*

fpage_offs
    *undescribed*

fpage_size
    *undescribed*

lpage_size
    *undescribed*

fpage
    *undescribed*

fpage_dma_addr
    *undescribed*

lpage
    *undescribed*

lpage_dma_addr
    *undescribed*

.. _`ddcb_requ`:

struct ddcb_requ
================

.. c:type:: struct ddcb_requ

    Kernel internal representation of the DDCB request

.. _`ddcb_requ.definition`:

Definition
----------

.. code-block:: c

    struct ddcb_requ {
        enum genwqe_requ_state req_state;
        int num;
        struct ddcb_queue *queue;
        struct dma_mapping dma_mappings[DDCB_FIXUPS];
        struct genwqe_sgl sgls[DDCB_FIXUPS];
        struct genwqe_ddcb_cmd cmd;
        struct genwqe_debug_data debug_data;
    }

.. _`ddcb_requ.members`:

Members
-------

req_state
    *undescribed*

num
    *undescribed*

queue
    *undescribed*

dma_mappings
    *undescribed*

sgls
    *undescribed*

cmd
    User space representation of the DDCB execution request

debug_data
    *undescribed*

.. _`genwqe_file`:

struct genwqe_file
==================

.. c:type:: struct genwqe_file

    Information for open GenWQE devices

.. _`genwqe_file.definition`:

Definition
----------

.. code-block:: c

    struct genwqe_file {
        struct genwqe_dev *cd;
        struct genwqe_driver *client;
        struct file *filp;
        struct fasync_struct *async_queue;
        struct task_struct *owner;
        struct list_head list;
        spinlock_t map_lock;
        struct list_head map_list;
        spinlock_t pin_lock;
        struct list_head pin_list;
    }

.. _`genwqe_file.members`:

Members
-------

cd
    *undescribed*

client
    *undescribed*

filp
    *undescribed*

async_queue
    *undescribed*

owner
    *undescribed*

list
    *undescribed*

map_lock
    *undescribed*

map_list
    *undescribed*

pin_lock
    *undescribed*

pin_list
    *undescribed*

.. _`genwqe_get_slu_id`:

genwqe_get_slu_id
=================

.. c:function:: int genwqe_get_slu_id(struct genwqe_dev *cd)

    Read Service Layer Unit Id

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_get_slu_id.return`:

Return
------

0x00: Development code
0x01: SLC1 (old)
0x02: SLC2 (sept2012)
0x03: SLC2 (feb2013, generic driver)

.. _`genwqe_write_vreg`:

genwqe_write_vreg
=================

.. c:function:: int genwqe_write_vreg(struct genwqe_dev *cd, u32 reg, u64 val, int func)

    Write register in VF window

    :param struct genwqe_dev \*cd:
        genwqe device

    :param u32 reg:
        register address

    :param u64 val:
        value to write

    :param int func:
        0: PF, 1: VF0, ..., 15: VF14

.. _`genwqe_read_vreg`:

genwqe_read_vreg
================

.. c:function:: u64 genwqe_read_vreg(struct genwqe_dev *cd, u32 reg, int func)

    Read register in VF window

    :param struct genwqe_dev \*cd:
        genwqe device

    :param u32 reg:
        register address

    :param int func:
        0: PF, 1: VF0, ..., 15: VF14

.. _`genwqe_read_vreg.return`:

Return
------

content of the register

.. _`__genwqe_execute_ddcb`:

__genwqe_execute_ddcb
=====================

.. c:function:: int __genwqe_execute_ddcb(struct genwqe_dev *cd, struct genwqe_ddcb_cmd *cmd, unsigned int f_flags)

    Execute DDCB request with addr translation

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param struct genwqe_ddcb_cmd \*cmd:
        *undescribed*

    :param unsigned int f_flags:
        *undescribed*

.. _`__genwqe_execute_ddcb.description`:

Description
-----------

This function will do the address translation changes to the DDCBs
according to the definitions required by the ATS field. It looks up
the memory allocation buffer or does vmap/vunmap for the respective
user-space buffers, inclusive page pinning and scatter gather list
buildup and teardown.

.. _`__genwqe_execute_raw_ddcb`:

__genwqe_execute_raw_ddcb
=========================

.. c:function:: int __genwqe_execute_raw_ddcb(struct genwqe_dev *cd, struct genwqe_ddcb_cmd *cmd, unsigned int f_flags)

    Execute DDCB request without addr translation

    :param struct genwqe_dev \*cd:
        *undescribed*

    :param struct genwqe_ddcb_cmd \*cmd:
        *undescribed*

    :param unsigned int f_flags:
        *undescribed*

.. _`__genwqe_execute_raw_ddcb.description`:

Description
-----------

This version will not do address translation or any modification of
the DDCB data. It is used e.g. for the MoveFlash DDCB which is
entirely prepared by the driver itself. That means the appropriate
DMA addresses are already in the DDCB and do not need any
modification.

.. _`genwqe_is_privileged`:

genwqe_is_privileged
====================

.. c:function:: int genwqe_is_privileged(struct genwqe_dev *cd)

    Determine operation mode for PCI function

    :param struct genwqe_dev \*cd:
        *undescribed*

.. _`genwqe_is_privileged.on-intel-with-sriov-support-we-see`:

On Intel with SRIOV support we see
----------------------------------

PF: is_physfn = 1 is_virtfn = 0
VF: is_physfn = 0 is_virtfn = 1

.. _`genwqe_is_privileged.on-systems-with-no-sriov-support-_and_-virtualized-systems-we-get`:

On Systems with no SRIOV support \_and\_ virtualized systems we get
-------------------------------------------------------------------

is_physfn = 0 is_virtfn = 0

Other vendors have individual pci device ids to distinguish between
virtual function drivers and physical function drivers. GenWQE
unfortunately has just on pci device id for both, VFs and PF.

The following code is used to distinguish if the card is running in
privileged mode, either as true PF or in a virtualized system with
full register access e.g. currently on PowerPC.

if (pci_dev->is_virtfn)
cd->is_privileged = 0;
else
cd->is_privileged = (__genwqe_readq(cd, IO_SLU_BITSTREAM)
!= IO_ILLEGAL_VALUE);

.. This file was automatic generated / don't edit.


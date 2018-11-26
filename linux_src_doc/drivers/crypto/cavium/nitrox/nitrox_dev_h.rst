.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_dev.h

.. _`nitrox_cmdq`:

struct nitrox_cmdq
==================

.. c:type:: struct nitrox_cmdq

    NITROX command queue

.. _`nitrox_cmdq.definition`:

Definition
----------

.. code-block:: c

    struct nitrox_cmdq {
        spinlock_t cmd_qlock;
        spinlock_t resp_qlock;
        spinlock_t backlog_qlock;
        struct nitrox_device *ndev;
        struct list_head response_head;
        struct list_head backlog_head;
        u8 __iomem *dbell_csr_addr;
        u8 __iomem *compl_cnt_csr_addr;
        u8 *base;
        dma_addr_t dma;
        struct work_struct backlog_qflush;
        atomic_t pending_count;
        atomic_t backlog_count;
        int write_idx;
        u8 instr_size;
        u8 qno;
        u32 qsize;
        u8 *unalign_base;
        dma_addr_t unalign_dma;
    }

.. _`nitrox_cmdq.members`:

Members
-------

cmd_qlock
    command queue lock

resp_qlock
    response queue lock

backlog_qlock
    backlog queue lock

ndev
    NITROX device

response_head
    submitted request list

backlog_head
    backlog queue

dbell_csr_addr
    doorbell register address for this queue

compl_cnt_csr_addr
    completion count register address of the slc port

base
    command queue base address

dma
    dma address of the base

backlog_qflush
    *undescribed*

pending_count
    request pending at device

backlog_count
    backlog request count

write_idx
    next write index for the command

instr_size
    command size

qno
    command queue number

qsize
    command queue size

unalign_base
    unaligned base address

unalign_dma
    unaligned dma address

.. _`nitrox_hw`:

struct nitrox_hw
================

.. c:type:: struct nitrox_hw

    NITROX hardware information

.. _`nitrox_hw.definition`:

Definition
----------

.. code-block:: c

    struct nitrox_hw {
        char partname[IFNAMSIZ * 2];
        char fw_name[VERSION_LEN];
        int freq;
        u16 vendor_id;
        u16 device_id;
        u8 revision_id;
        u8 se_cores;
        u8 ae_cores;
        u8 zip_cores;
    }

.. _`nitrox_hw.members`:

Members
-------

partname
    partname ex: CNN55xxx-xxx

fw_name
    firmware version

freq
    NITROX frequency

vendor_id
    vendor ID

device_id
    device ID

revision_id
    revision ID

se_cores
    number of symmetric cores

ae_cores
    number of asymmetric cores

zip_cores
    number of zip cores

.. _`nitrox_device`:

struct nitrox_device
====================

.. c:type:: struct nitrox_device

    NITROX Device Information.

.. _`nitrox_device.definition`:

Definition
----------

.. code-block:: c

    struct nitrox_device {
        struct list_head list;
        u8 __iomem *bar_addr;
        struct pci_dev *pdev;
        atomic_t state;
        unsigned long flags;
        unsigned long timeout;
        refcount_t refcnt;
        u8 idx;
        int node;
        u16 qlen;
        u16 nr_queues;
        int num_vfs;
        enum vf_mode mode;
        struct dma_pool *ctx_pool;
        struct nitrox_cmdq *pkt_inq;
        struct nitrox_q_vector *qvec;
        int num_vecs;
        struct nitrox_stats stats;
        struct nitrox_hw hw;
    #if IS_ENABLED(CONFIG_DEBUG_FS)
        struct dentry *debugfs_dir;
    #endif
    }

.. _`nitrox_device.members`:

Members
-------

list
    pointer to linked list of devices

bar_addr
    iomap address

pdev
    PCI device information

state
    NITROX device state

flags
    flags to indicate device the features

timeout
    Request timeout in jiffies

refcnt
    Device usage count

idx
    device index (0..N)

node
    NUMA node id attached

qlen
    Command queue length

nr_queues
    Number of command queues

num_vfs
    *undescribed*

mode
    Device mode PF/VF

ctx_pool
    DMA pool for crypto context

pkt_inq
    Packet input rings

qvec
    MSI-X queue vectors information

num_vecs
    *undescribed*

stats
    *undescribed*

hw
    hardware information

debugfs_dir
    debugfs directory

.. _`nitrox_read_csr`:

nitrox_read_csr
===============

.. c:function:: u64 nitrox_read_csr(struct nitrox_device *ndev, u64 offset)

    Read from device register

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

    :param offset:
        offset of the register to read
    :type offset: u64

.. _`nitrox_read_csr.return`:

Return
------

value read

.. _`nitrox_write_csr`:

nitrox_write_csr
================

.. c:function:: void nitrox_write_csr(struct nitrox_device *ndev, u64 offset, u64 value)

    Write to device register

    :param ndev:
        NITROX device
    :type ndev: struct nitrox_device \*

    :param offset:
        offset of the register to write
    :type offset: u64

    :param value:
        value to write
    :type value: u64

.. This file was automatic generated / don't edit.


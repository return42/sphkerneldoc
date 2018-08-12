.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/atom/sst/sst.h

.. _`sst_block`:

struct sst_block
================

.. c:type:: struct sst_block

    This structure is used to block a user/fw data call to another fw/user call

.. _`sst_block.definition`:

Definition
----------

.. code-block:: c

    struct sst_block {
        bool condition;
        int ret_code;
        void *data;
        u32 size;
        bool on;
        u32 msg_id;
        u32 drv_id;
        struct list_head node;
    }

.. _`sst_block.members`:

Members
-------

condition
    condition for blocking check

ret_code
    ret code when block is released

data
    data ptr

size
    size of data

on
    block condition

msg_id
    msg_id = msgid in mfld/ctp, mrfld = NULL

drv_id
    str_id in mfld/ctp, = drv_id in mrfld

node
    list head node

.. _`stream_info`:

struct stream_info
==================

.. c:type:: struct stream_info

    structure that holds the stream information

.. _`stream_info.definition`:

Definition
----------

.. code-block:: c

    struct stream_info {
        unsigned int status;
        unsigned int prev;
        unsigned int resume_status;
        unsigned int resume_prev;
        struct mutex lock;
        struct snd_sst_alloc_mrfld alloc_param;
        void *pcm_substream;
        void (*period_elapsed)(void *pcm_substream);
        unsigned int sfreq;
        u32 cumm_bytes;
        void *compr_cb_param;
        void (*compr_cb)(void *compr_cb_param);
        void *drain_cb_param;
        void (*drain_notify)(void *drain_cb_param);
        unsigned int num_ch;
        unsigned int pipe_id;
        unsigned int task_id;
    }

.. _`stream_info.members`:

Members
-------

status
    stream current state

prev
    stream prev state

resume_status
    stream current state to restore on resume

resume_prev
    stream prev state to restore on resume

lock
    stream mutex for protecting state

alloc_param
    parameters used for stream (re-)allocation

pcm_substream
    PCM substream

period_elapsed
    PCM period elapsed callback

sfreq
    stream sampling freq

cumm_bytes
    cummulative bytes decoded

compr_cb_param
    *undescribed*

compr_cb
    *undescribed*

drain_cb_param
    *undescribed*

drain_notify
    *undescribed*

num_ch
    *undescribed*

pipe_id
    *undescribed*

task_id
    *undescribed*

.. _`sst_fw_header`:

struct sst_fw_header
====================

.. c:type:: struct sst_fw_header

    FW file headers

.. _`sst_fw_header.definition`:

Definition
----------

.. code-block:: c

    struct sst_fw_header {
        unsigned char signature[FW_SIGNATURE_SIZE];
        u32 file_size;
        u32 modules;
        u32 file_format;
        u32 reserved[4];
    }

.. _`sst_fw_header.members`:

Members
-------

signature
    FW signature

file_size
    size of fw image

modules
    # of modules

file_format
    version of header format

reserved
    reserved fields

.. _`fw_module_header`:

struct fw_module_header
=======================

.. c:type:: struct fw_module_header

    module header in FW

.. _`fw_module_header.definition`:

Definition
----------

.. code-block:: c

    struct fw_module_header {
        unsigned char signature[FW_SIGNATURE_SIZE];
        u32 mod_size;
        u32 blocks;
        u32 type;
        u32 entry_point;
    }

.. _`fw_module_header.members`:

Members
-------

signature
    module signature

mod_size
    size of module

blocks
    block count

type
    block type

entry_point
    module netry point

.. _`fw_block_info`:

struct fw_block_info
====================

.. c:type:: struct fw_block_info

    block header for FW

.. _`fw_block_info.definition`:

Definition
----------

.. code-block:: c

    struct fw_block_info {
        enum sst_ram_type type;
        u32 size;
        u32 ram_offset;
        u32 rsvd;
    }

.. _`fw_block_info.members`:

Members
-------

type
    block ram type I/D

size
    size of block

ram_offset
    offset in ram

rsvd
    *undescribed*

.. _`intel_sst_drv`:

struct intel_sst_drv
====================

.. c:type:: struct intel_sst_drv

    driver ops

.. _`intel_sst_drv.definition`:

Definition
----------

.. code-block:: c

    struct intel_sst_drv {
        int sst_state;
        int irq_num;
        unsigned int dev_id;
        void __iomem *ddr;
        void __iomem *shim;
        void __iomem *mailbox;
        void __iomem *iram;
        void __iomem *dram;
        unsigned int mailbox_add;
        unsigned int iram_base;
        unsigned int dram_base;
        unsigned int shim_phy_add;
        unsigned int iram_end;
        unsigned int dram_end;
        unsigned int ddr_end;
        unsigned int ddr_base;
        unsigned int mailbox_recv_offset;
        struct list_head block_list;
        struct list_head ipc_dispatch_list;
        struct sst_platform_info *pdata;
        struct list_head rx_list;
        struct work_struct ipc_post_msg_wq;
        wait_queue_head_t wait_queue;
        struct workqueue_struct *post_msg_wq;
        unsigned int tstamp;
        struct stream_info streams[MAX_NUM_STREAMS+1];
        spinlock_t ipc_spin_lock;
        spinlock_t block_lock;
        spinlock_t rx_msg_lock;
        struct pci_dev *pci;
        struct device *dev;
        volatile long unsigned pvt_id;
        struct mutex sst_lock;
        unsigned int stream_cnt;
        unsigned int csr_value;
        void *fw_in_mem;
        struct sst_sg_list fw_sg_list, library_list;
        struct intel_sst_ops *ops;
        struct sst_info info;
        struct pm_qos_request *qos;
        unsigned int use_dma;
        unsigned int use_lli;
        atomic_t fw_clear_context;
        bool lib_dwnld_reqd;
        struct list_head memcpy_list;
        struct sst_ipc_reg ipc_reg;
        struct sst_mem_mgr lib_mem_mgr;
        char firmware_name[FW_NAME_SIZE];
        struct snd_sst_fw_version fw_version;
        struct sst_fw_save *fw_save;
    }

.. _`intel_sst_drv.members`:

Members
-------

sst_state
    current sst device state

irq_num
    *undescribed*

dev_id
    device identifier, pci_id for pci devices and acpi_id for acpi
    devices

ddr
    *undescribed*

shim
    SST shim pointer

mailbox
    SST mailbox pointer

iram
    SST IRAM pointer

dram
    SST DRAM pointer

mailbox_add
    *undescribed*

iram_base
    *undescribed*

dram_base
    *undescribed*

shim_phy_add
    SST shim phy addr

iram_end
    *undescribed*

dram_end
    *undescribed*

ddr_end
    *undescribed*

ddr_base
    *undescribed*

mailbox_recv_offset
    *undescribed*

block_list
    *undescribed*

ipc_dispatch_list
    ipc messages dispatched

pdata
    SST info passed as a part of pci platform data

rx_list
    to copy the process_reply/process_msg from DSP

ipc_post_msg_wq
    wq to post IPC messages context

wait_queue
    *undescribed*

post_msg_wq
    wq to post IPC messages

tstamp
    *undescribed*

streams
    sst stream contexts

ipc_spin_lock
    spin lock to handle audio shim access and ipc queue

block_lock
    spin lock to add block to block_list and assign pvt_id

rx_msg_lock
    spin lock to handle the rx messages from the DSP

pci
    sst pci device struture

dev
    pointer to current device struct

pvt_id
    sst private id

sst_lock
    sst device lock

stream_cnt
    total sst active stream count

csr_value
    *undescribed*

fw_in_mem
    *undescribed*

fw_sg_list
    *undescribed*

library_list
    *undescribed*

ops
    *undescribed*

info
    *undescribed*

qos
    PM Qos struct
    firmware_name : Firmware / Library name

use_dma
    *undescribed*

use_lli
    *undescribed*

fw_clear_context
    *undescribed*

lib_dwnld_reqd
    *undescribed*

memcpy_list
    *undescribed*

ipc_reg
    *undescribed*

lib_mem_mgr
    *undescribed*

firmware_name
    *undescribed*

fw_version
    *undescribed*

fw_save
    *undescribed*

.. This file was automatic generated / don't edit.


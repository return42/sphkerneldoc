.. -*- coding: utf-8; mode: rst -*-

=====
sst.h
=====


.. _`sst_block`:

struct sst_block
================

.. c:type:: sst_block

    This structure is used to block a user/fw data call to another fw/user call


.. _`sst_block.definition`:

Definition
----------

.. code-block:: c

  struct sst_block {
    bool condition;
    int ret_code;
    void * data;
    u32 size;
    bool on;
    u32 msg_id;
    u32 drv_id;
    struct list_head node;
  };


.. _`sst_block.members`:

Members
-------

:``condition``:
    condition for blocking check

:``ret_code``:
    ret code when block is released

:``data``:
    data ptr

:``size``:
    size of data

:``on``:
    block condition

:``msg_id``:
    msg_id = msgid in mfld/ctp, mrfld = NULL

:``drv_id``:
    str_id in mfld/ctp, = drv_id in mrfld

:``node``:
    list head node




.. _`stream_info`:

struct stream_info
==================

.. c:type:: stream_info

    structure that holds the stream information


.. _`stream_info.definition`:

Definition
----------

.. code-block:: c

  struct stream_info {
    unsigned int status;
    unsigned int prev;
    unsigned int ops;
    struct mutex lock;
    void * pcm_substream;
    void (* period_elapsed) (void *pcm_substream);
    unsigned int sfreq;
    u32 cumm_bytes;
  };


.. _`stream_info.members`:

Members
-------

:``status``:
    stream current state

:``prev``:
    stream prev state

:``ops``:
    stream operation pb/cp/drm...

:``lock``:
    stream mutex for protecting state

:``pcm_substream``:
    PCM substream

:``period_elapsed``:
    PCM period elapsed callback

:``sfreq``:
    stream sampling freq

:``cumm_bytes``:
    cummulative bytes decoded




.. _`sst_fw_header`:

struct sst_fw_header
====================

.. c:type:: sst_fw_header

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
  };


.. _`sst_fw_header.members`:

Members
-------

:``signature[FW_SIGNATURE_SIZE]``:
    FW signature

:``file_size``:
    size of fw image

:``modules``:
    # of modules

:``file_format``:
    version of header format

:``reserved[4]``:
    reserved fields




.. _`fw_module_header`:

struct fw_module_header
=======================

.. c:type:: fw_module_header

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
  };


.. _`fw_module_header.members`:

Members
-------

:``signature[FW_SIGNATURE_SIZE]``:
    module signature

:``mod_size``:
    size of module

:``blocks``:
    block count

:``type``:
    block type

:``entry_point``:
    module netry point




.. _`fw_block_info`:

struct fw_block_info
====================

.. c:type:: fw_block_info

    block header for FW


.. _`fw_block_info.definition`:

Definition
----------

.. code-block:: c

  struct fw_block_info {
    enum sst_ram_type type;
    u32 size;
    u32 ram_offset;
  };


.. _`fw_block_info.members`:

Members
-------

:``type``:
    block ram type I/D

:``size``:
    size of block

:``ram_offset``:
    offset in ram




.. _`intel_sst_drv`:

struct intel_sst_drv
====================

.. c:type:: intel_sst_drv

    driver ops


.. _`intel_sst_drv.definition`:

Definition
----------

.. code-block:: c

  struct intel_sst_drv {
    int sst_state;
    unsigned int dev_id;
    void __iomem * shim;
    void __iomem * mailbox;
    void __iomem * iram;
    void __iomem * dram;
    unsigned int shim_phy_add;
    struct sst_shim_regs64 * shim_regs64;
    struct list_head ipc_dispatch_list;
    struct sst_platform_info * pdata;
    struct list_head rx_list;
    struct work_struct ipc_post_msg_wq;
    struct workqueue_struct * post_msg_wq;
    struct stream_info streams[MAX_NUM_STREAMS+1];
    spinlock_t ipc_spin_lock;
    spinlock_t block_lock;
    spinlock_t rx_msg_lock;
    struct pci_dev * pci;
    struct device * dev;
    volatile long unsigned pvt_id;
    struct mutex sst_lock;
    unsigned int stream_cnt;
    struct pm_qos_request * qos;
  };


.. _`intel_sst_drv.members`:

Members
-------

:``sst_state``:
    current sst device state

:``dev_id``:
    device identifier, pci_id for pci devices and acpi_id for acpi
    devices

:``shim``:
    SST shim pointer

:``mailbox``:
    SST mailbox pointer

:``iram``:
    SST IRAM pointer

:``dram``:
    SST DRAM pointer

:``shim_phy_add``:
    SST shim phy addr

:``shim_regs64``:
    Struct to save shim registers

:``ipc_dispatch_list``:
    ipc messages dispatched

:``pdata``:
    SST info passed as a part of pci platform data

:``rx_list``:
    to copy the process_reply/process_msg from DSP

:``ipc_post_msg_wq``:
    wq to post IPC messages context

:``post_msg_wq``:
    wq to post IPC messages

:``streams[MAX_NUM_STREAMS+1]``:
    sst stream contexts

:``ipc_spin_lock``:
    spin lock to handle audio shim access and ipc queue

:``block_lock``:
    spin lock to add block to block_list and assign pvt_id

:``rx_msg_lock``:
    spin lock to handle the rx messages from the DSP

:``pci``:
    sst pci device struture

:``dev``:
    pointer to current device struct

:``pvt_id``:
    sst private id

:``sst_lock``:
    sst device lock

:``stream_cnt``:
    total sst active stream count

:``qos``:
    PM Qos struct




.. _`intel_sst_drv.firmware_name`:

firmware_name 
--------------

Firmware / Library name


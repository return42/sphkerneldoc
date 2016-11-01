.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/mpt3sas/mpt3sas_base.h

.. _`mpt3sas_target`:

struct MPT3SAS_TARGET
=====================

.. c:type:: struct MPT3SAS_TARGET

    starget private hostdata

.. _`mpt3sas_target.definition`:

Definition
----------

.. code-block:: c

    struct MPT3SAS_TARGET {
        struct scsi_target *starget;
        u64 sas_address;
        struct _raid_device *raid_device;
        u16 handle;
        int num_luns;
        u32 flags;
        u8 deleted;
        u8 tm_busy;
        struct _sas_device *sdev;
    }

.. _`mpt3sas_target.members`:

Members
-------

starget
    starget object

sas_address
    target sas address

raid_device
    raid_device pointer to access volume data

handle
    device handle

num_luns
    number luns

flags
    MPT_TARGET_FLAGS_XXX flags

deleted
    target flaged for deletion

tm_busy
    target is busy with TM request.

sdev
    The sas_device associated with this target

.. _`mpt3sas_device`:

struct MPT3SAS_DEVICE
=====================

.. c:type:: struct MPT3SAS_DEVICE

    sdev private hostdata

.. _`mpt3sas_device.definition`:

Definition
----------

.. code-block:: c

    struct MPT3SAS_DEVICE {
        struct MPT3SAS_TARGET *sas_target;
        unsigned int lun;
        u32 flags;
        u8 configured_lun;
        u8 block;
        u8 tlr_snoop_check;
        u8 ignore_delay_remove;
    }

.. _`mpt3sas_device.members`:

Members
-------

sas_target
    starget private hostdata

lun
    lun number

flags
    MPT_DEVICE_XXX flags

configured_lun
    lun is configured

block
    device is in SDEV_BLOCK state

tlr_snoop_check
    flag used in determining whether to disable TLR

ignore_delay_remove
    *undescribed*

.. _`_internal_cmd`:

struct \_internal_cmd
=====================

.. c:type:: struct _internal_cmd

    internal commands struct

.. _`_internal_cmd.definition`:

Definition
----------

.. code-block:: c

    struct _internal_cmd {
        struct mutex mutex;
        struct completion done;
        void *reply;
        void *sense;
        u16 status;
        u16 smid;
    }

.. _`_internal_cmd.members`:

Members
-------

mutex
    mutex

done
    completion

reply
    reply message pointer

sense
    sense data

status
    MPT3_CMD_XXX status

smid
    system message id

.. _`_sas_device`:

struct \_sas_device
===================

.. c:type:: struct _sas_device

    attached device information

.. _`_sas_device.definition`:

Definition
----------

.. code-block:: c

    struct _sas_device {
        struct list_head list;
        struct scsi_target *starget;
        u64 sas_address;
        u64 device_name;
        u16 handle;
        u64 sas_address_parent;
        u16 enclosure_handle;
        u64 enclosure_logical_id;
        u16 volume_handle;
        u64 volume_wwid;
        u32 device_info;
        int id;
        int channel;
        u16 slot;
        u8 phy;
        u8 responding;
        u8 fast_path;
        u8 pfa_led_on;
        u8 pend_sas_rphy_add;
        u8 enclosure_level;
        u8 connector_name[5];
        struct kref refcount;
    }

.. _`_sas_device.members`:

Members
-------

list
    sas device list

starget
    starget object

sas_address
    device sas address

device_name
    retrieved from the SAS IDENTIFY frame.

handle
    device handle

sas_address_parent
    sas address of parent expander or sas host

enclosure_handle
    enclosure handle

enclosure_logical_id
    enclosure logical identifier

volume_handle
    volume handle (valid when hidden raid member)

volume_wwid
    volume unique identifier

device_info
    bitfield provides detailed info about the device

id
    target id

channel
    target channel

slot
    number number

phy
    phy identifier provided in sas device page 0

responding
    used in \_scsih_sas_device_mark_responding

fast_path
    fast path feature enable bit

pfa_led_on
    flag for PFA LED status

pend_sas_rphy_add
    flag to check if device is in \ :c:func:`sas_rphy_add`\ 
    addition routine.

enclosure_level
    *undescribed*

refcount
    *undescribed*

.. _`_boot_device`:

struct \_boot_device
====================

.. c:type:: struct _boot_device

    boot device info

.. _`_boot_device.definition`:

Definition
----------

.. code-block:: c

    struct _boot_device {
        u8 is_raid;
        void *device;
    }

.. _`_boot_device.members`:

Members
-------

is_raid
    flag to indicate whether this is volume

device
    holds pointer for either struct \_sas_device or
    struct \_raid_device

.. _`_sas_port`:

struct \_sas_port
=================

.. c:type:: struct _sas_port

    wide/narrow sas port information

.. _`_sas_port.definition`:

Definition
----------

.. code-block:: c

    struct _sas_port {
        struct list_head port_list;
        u8 num_phys;
        struct sas_identify remote_identify;
        struct sas_rphy *rphy;
        struct sas_port *port;
        struct list_head phy_list;
    }

.. _`_sas_port.members`:

Members
-------

port_list
    list of ports belonging to expander

num_phys
    number of phys belonging to this port

remote_identify
    attached device identification

rphy
    sas transport rphy object

port
    sas transport wide/narrow port object

phy_list
    _sas_phy list objects belonging to this port

.. _`_sas_phy`:

struct \_sas_phy
================

.. c:type:: struct _sas_phy

    phy information

.. _`_sas_phy.definition`:

Definition
----------

.. code-block:: c

    struct _sas_phy {
        struct list_head port_siblings;
        struct sas_identify identify;
        struct sas_identify remote_identify;
        struct sas_phy *phy;
        u8 phy_id;
        u16 handle;
        u16 attached_handle;
        u8 phy_belongs_to_port;
    }

.. _`_sas_phy.members`:

Members
-------

port_siblings
    list of phys belonging to a port

identify
    phy identification

remote_identify
    attached device identification

phy
    sas transport phy object

phy_id
    unique phy id

handle
    device handle for this phy

attached_handle
    device handle for attached device

phy_belongs_to_port
    port has been created for this phy

.. _`_sas_node`:

struct \_sas_node
=================

.. c:type:: struct _sas_node

    sas_host/expander information

.. _`_sas_node.definition`:

Definition
----------

.. code-block:: c

    struct _sas_node {
        struct list_head list;
        struct device *parent_dev;
        u8 num_phys;
        u64 sas_address;
        u16 handle;
        u64 sas_address_parent;
        u16 enclosure_handle;
        u64 enclosure_logical_id;
        u8 responding;
        struct _sas_phy *phy;
        struct list_head sas_port_list;
    }

.. _`_sas_node.members`:

Members
-------

list
    list of expanders

parent_dev
    parent device class

num_phys
    number phys belonging to this sas_host/expander

sas_address
    sas address of this sas_host/expander

handle
    handle for this sas_host/expander

sas_address_parent
    sas address of parent expander or sas host

enclosure_handle
    handle for this a member of an enclosure

enclosure_logical_id
    *undescribed*

responding
    used in \_scsih_expander_device_mark_responding

phy
    a list of phys that make up this sas_host/expander

sas_port_list
    list of ports attached to this sas_host/expander

.. _`reset_type`:

enum reset_type
===============

.. c:type:: enum reset_type

    reset state

.. _`reset_type.definition`:

Definition
----------

.. code-block:: c

    enum reset_type {
        FORCE_BIG_HAMMER,
        SOFT_RESET
    };

.. _`reset_type.constants`:

Constants
---------

FORCE_BIG_HAMMER
    issue diagnostic reset

SOFT_RESET
    issue message_unit_reset, if fails to to big hammer

.. _`chain_tracker`:

struct chain_tracker
====================

.. c:type:: struct chain_tracker

    firmware chain tracker

.. _`chain_tracker.definition`:

Definition
----------

.. code-block:: c

    struct chain_tracker {
        void *chain_buffer;
        dma_addr_t chain_buffer_dma;
        struct list_head tracker_list;
    }

.. _`chain_tracker.members`:

Members
-------

chain_buffer
    chain buffer

chain_buffer_dma
    physical address

tracker_list
    list of free request (ioc->free_chain_list)

.. _`scsiio_tracker`:

struct scsiio_tracker
=====================

.. c:type:: struct scsiio_tracker

    scsi mf request tracker

.. _`scsiio_tracker.definition`:

Definition
----------

.. code-block:: c

    struct scsiio_tracker {
        u16 smid;
        struct scsi_cmnd *scmd;
        u8 cb_idx;
        u8 direct_io;
        struct list_head chain_list;
        struct list_head tracker_list;
        u16 msix_io;
    }

.. _`scsiio_tracker.members`:

Members
-------

smid
    system message id

scmd
    scsi request pointer

cb_idx
    callback index

direct_io
    To indicate whether I/O is direct (WARPDRIVE)

chain_list
    *undescribed*

tracker_list
    list of free request (ioc->free_list)

msix_io
    IO's msix

.. _`request_tracker`:

struct request_tracker
======================

.. c:type:: struct request_tracker

    firmware request tracker

.. _`request_tracker.definition`:

Definition
----------

.. code-block:: c

    struct request_tracker {
        u16 smid;
        u8 cb_idx;
        struct list_head tracker_list;
    }

.. _`request_tracker.members`:

Members
-------

smid
    system message id

cb_idx
    callback index

tracker_list
    list of free request (ioc->free_list)

.. _`_tr_list`:

struct \_tr_list
================

.. c:type:: struct _tr_list

    target reset list

.. _`_tr_list.definition`:

Definition
----------

.. code-block:: c

    struct _tr_list {
        struct list_head list;
        u16 handle;
        u16 state;
    }

.. _`_tr_list.members`:

Members
-------

list
    *undescribed*

handle
    device handle

state
    state machine

.. _`_sc_list`:

struct \_sc_list
================

.. c:type:: struct _sc_list

    delayed SAS_IO_UNIT_CONTROL message list

.. _`_sc_list.definition`:

Definition
----------

.. code-block:: c

    struct _sc_list {
        struct list_head list;
        u16 handle;
    }

.. _`_sc_list.members`:

Members
-------

list
    *undescribed*

handle
    device handle

.. _`_event_ack_list`:

struct \_event_ack_list
=======================

.. c:type:: struct _event_ack_list

    delayed event acknowledgment list

.. _`_event_ack_list.definition`:

Definition
----------

.. code-block:: c

    struct _event_ack_list {
        struct list_head list;
        u16 Event;
        u32 EventContext;
    }

.. _`_event_ack_list.members`:

Members
-------

list
    *undescribed*

Event
    Event ID

EventContext
    used to track the event uniquely

.. _`adapter_reply_queue`:

struct adapter_reply_queue
==========================

.. c:type:: struct adapter_reply_queue

    the reply queue struct

.. _`adapter_reply_queue.definition`:

Definition
----------

.. code-block:: c

    struct adapter_reply_queue {
        struct MPT3SAS_ADAPTER *ioc;
        u8 msix_index;
        unsigned int vector;
        u32 reply_post_host_index;
        Mpi2ReplyDescriptorsUnion_t *reply_post_free;
        char name[MPT_NAME_LENGTH];
        atomic_t busy;
        cpumask_var_t affinity_hint;
        struct list_head list;
    }

.. _`adapter_reply_queue.members`:

Members
-------

ioc
    per adapter object

msix_index
    msix index into vector table

vector
    irq vector

reply_post_host_index
    head index in the pool where FW completes IO

reply_post_free
    reply post base virt address

name
    the name registered to \ :c:func:`request_irq`\ 

busy
    isr is actively processing replies on another cpu

affinity_hint
    *undescribed*

list
    this list

.. _`mpt3sas_adapter`:

struct MPT3SAS_ADAPTER
======================

.. c:type:: struct MPT3SAS_ADAPTER

    per adapter struct

.. _`mpt3sas_adapter.definition`:

Definition
----------

.. code-block:: c

    struct MPT3SAS_ADAPTER {
        struct list_head list;
        struct Scsi_Host *shost;
        u8 id;
        int cpu_count;
        char name[MPT_NAME_LENGTH];
        char driver_name[MPT_NAME_LENGTH];
        char tmp_string[MPT_STRING_LENGTH];
        struct pci_dev *pdev;
        Mpi2SystemInterfaceRegs_t __iomem *chip;
        resource_size_t chip_phys;
        int logging_level;
        int fwfault_debug;
        u8 ir_firmware;
        int bars;
        u8 mask_interrupts;
        int dma_mask;
        char fault_reset_work_q_name[20];
        struct workqueue_struct *fault_reset_work_q;
        struct delayed_work fault_reset_work;
        char firmware_event_name[20];
        struct workqueue_struct *firmware_event_thread;
        spinlock_t fw_event_lock;
        struct list_head fw_event_list;
        int aen_event_read_flag;
        u8 broadcast_aen_busy;
        u16 broadcast_aen_pending;
        u8 shost_recovery;
        struct mutex reset_in_progress_mutex;
        spinlock_t ioc_reset_in_progress_lock;
        u8 ioc_link_reset_in_progress;
        u8 ioc_reset_in_progress_status;
        u8 ignore_loginfos;
        u8 remove_host;
        u8 pci_error_recovery;
        u8 wait_for_discovery_to_complete;
        u8 is_driver_loading;
        u8 port_enable_failed;
        u8 start_scan;
        u16 start_scan_failed;
        u8 msix_enable;
        u16 msix_vector_count;
        u8 *cpu_msix_table;
        u16 cpu_msix_table_sz;
        resource_size_t __iomem **reply_post_host_index;
        u32 ioc_reset_count;
        MPT3SAS_FLUSH_RUNNING_CMDS schedule_dead_ioc_flush_running_cmds;
        u32 non_operational_loop;
        u8 scsi_io_cb_idx;
        u8 tm_cb_idx;
        u8 transport_cb_idx;
        u8 scsih_cb_idx;
        u8 ctl_cb_idx;
        u8 base_cb_idx;
        u8 port_enable_cb_idx;
        u8 config_cb_idx;
        u8 tm_tr_cb_idx;
        u8 tm_tr_volume_cb_idx;
        u8 tm_sas_control_cb_idx;
        struct _internal_cmd base_cmds;
        struct _internal_cmd port_enable_cmds;
        struct _internal_cmd transport_cmds;
        struct _internal_cmd scsih_cmds;
        struct _internal_cmd tm_cmds;
        struct _internal_cmd ctl_cmds;
        struct _internal_cmd config_cmds;
        MPT_ADD_SGE base_add_sg_single;
        MPT_BUILD_SG_SCMD build_sg_scmd;
        MPT_BUILD_SG build_sg;
        MPT_BUILD_ZERO_LEN_SGE build_zero_len_sge;
        u16 sge_size_ieee;
        u16 hba_mpi_version_belonged;
        MPT_BUILD_SG build_sg_mpi;
        MPT_BUILD_ZERO_LEN_SGE build_zero_len_sge_mpi;
        u32 event_type[MPI2_EVENT_NOTIFY_EVENTMASK_WORDS];
        u32 event_context;
        void *event_log;
        u32 event_masks[MPI2_EVENT_NOTIFY_EVENTMASK_WORDS];
        struct mpt3sas_facts facts;
        struct mpt3sas_port_facts *pfacts;
        Mpi2ManufacturingPage0_t manu_pg0;
        struct Mpi2ManufacturingPage10_t manu_pg10;
        struct Mpi2ManufacturingPage11_t manu_pg11;
        Mpi2BiosPage2_t bios_pg2;
        Mpi2BiosPage3_t bios_pg3;
        Mpi2IOCPage8_t ioc_pg8;
        Mpi2IOUnitPage0_t iounit_pg0;
        Mpi2IOUnitPage1_t iounit_pg1;
        Mpi2IOUnitPage8_t iounit_pg8;
        struct _boot_device req_boot_device;
        struct _boot_device req_alt_boot_device;
        struct _boot_device current_boot_device;
        struct _sas_node sas_hba;
        struct list_head sas_expander_list;
        spinlock_t sas_node_lock;
        struct list_head sas_device_list;
        struct list_head sas_device_init_list;
        spinlock_t sas_device_lock;
        struct list_head raid_device_list;
        spinlock_t raid_device_lock;
        u8 io_missing_delay;
        u16 device_missing_delay;
        int sas_id;
        void *blocking_handles;
        void *pd_handles;
        u16 pd_handles_sz;
        u16 config_page_sz;
        void *config_page;
        dma_addr_t config_page_dma;
        u16 hba_queue_depth;
        u16 sge_size;
        u16 scsiio_depth;
        u16 request_sz;
        u8 *request;
        dma_addr_t request_dma;
        u32 request_dma_sz;
        struct scsiio_tracker *scsi_lookup;
        ulong scsi_lookup_pages;
        spinlock_t scsi_lookup_lock;
        struct list_head free_list;
        int pending_io_count;
        wait_queue_head_t reset_wq;
        struct chain_tracker *chain_lookup;
        struct list_head free_chain_list;
        struct dma_pool *chain_dma_pool;
        ulong chain_pages;
        u16 max_sges_in_main_message;
        u16 max_sges_in_chain_message;
        u16 chains_needed_per_io;
        u32 chain_depth;
        u16 chain_segment_sz;
        u16 hi_priority_smid;
        u8 *hi_priority;
        dma_addr_t hi_priority_dma;
        u16 hi_priority_depth;
        struct request_tracker *hpr_lookup;
        struct list_head hpr_free_list;
        u16 internal_smid;
        u8 *internal;
        dma_addr_t internal_dma;
        u16 internal_depth;
        struct request_tracker *internal_lookup;
        struct list_head internal_free_list;
        u8 *sense;
        dma_addr_t sense_dma;
        struct dma_pool *sense_dma_pool;
        u16 reply_sz;
        u8 *reply;
        dma_addr_t reply_dma;
        u32 reply_dma_max_address;
        u32 reply_dma_min_address;
        struct dma_pool *reply_dma_pool;
        u16 reply_free_queue_depth;
        __le32 *reply_free;
        dma_addr_t reply_free_dma;
        struct dma_pool *reply_free_dma_pool;
        u32 reply_free_host_index;
        u16 reply_post_queue_depth;
        struct reply_post_struct *reply_post;
        u8 rdpq_array_capable;
        u8 rdpq_array_enable;
        u8 rdpq_array_enable_assigned;
        struct dma_pool *reply_post_free_dma_pool;
        u8 reply_queue_count;
        struct list_head reply_queue_list;
        u8 msix96_vector;
        resource_size_t **replyPostRegisterIndex;
        struct list_head delayed_tr_list;
        struct list_head delayed_tr_volume_list;
        struct list_head delayed_sc_list;
        struct list_head delayed_event_ack_list;
        u8 temp_sensors_count;
        struct mutex pci_access_mutex;
        u8  *diag_buffer[MPI2_DIAG_BUF_TYPE_COUNT];
        u32 diag_buffer_sz[MPI2_DIAG_BUF_TYPE_COUNT];
        dma_addr_t diag_buffer_dma[MPI2_DIAG_BUF_TYPE_COUNT];
        u8 diag_buffer_status[MPI2_DIAG_BUF_TYPE_COUNT];
        u32 unique_id[MPI2_DIAG_BUF_TYPE_COUNT];
        u32 product_specific[MPI2_DIAG_BUF_TYPE_COUNT][23];
        u32 diagnostic_flags[MPI2_DIAG_BUF_TYPE_COUNT];
        u32 ring_buffer_offset;
        u32 ring_buffer_sz;
        u8 is_warpdrive;
        u8 hide_ir_msg;
        u8 mfg_pg10_hide_flag;
        u8 hide_drives;
        spinlock_t diag_trigger_lock;
        u8 diag_trigger_active;
        struct SL_WH_MASTER_TRIGGER_T diag_trigger_master;
        struct SL_WH_EVENT_TRIGGERS_T diag_trigger_event;
        struct SL_WH_SCSI_TRIGGERS_T diag_trigger_scsi;
        struct SL_WH_MPI_TRIGGERS_T diag_trigger_mpi;
    }

.. _`mpt3sas_adapter.members`:

Members
-------

list
    ioc_list

shost
    shost object

id
    unique adapter id

cpu_count
    number online cpus

name
    generic ioc string

tmp_string
    tmp string used for logging

pdev
    pci pdev object

chip
    memory mapped register space

chip_phys
    physical addrss prior to mapping

logging_level
    see mpt3sas_debug.h

fwfault_debug
    debuging FW timeouts

ir_firmware
    IR firmware present

bars
    bitmask of BAR's that must be configured

mask_interrupts
    ignore interrupt

dma_mask
    used to set the consistent dma mask

fault_reset_work_q_name
    fw fault work queue

fault_reset_work_q
    ""

fault_reset_work
    ""

firmware_event_name
    fw event work queue

firmware_event_thread
    ""

fw_event_lock
    *undescribed*

fw_event_list
    list of fw events

aen_event_read_flag
    event log was read

broadcast_aen_busy
    broadcast aen waiting to be serviced

broadcast_aen_pending
    *undescribed*

shost_recovery
    host reset in progress

reset_in_progress_mutex
    *undescribed*

ioc_reset_in_progress_lock
    *undescribed*

ioc_link_reset_in_progress
    phy/hard reset in progress

ioc_reset_in_progress_status
    *undescribed*

ignore_loginfos
    ignore loginfos during task management

remove_host
    flag for when driver unloads, to avoid sending dev resets

pci_error_recovery
    flag to prevent ioc access until slot reset completes

wait_for_discovery_to_complete
    flag set at driver load time when
    waiting on reporting devices

is_driver_loading
    flag set at driver load time

port_enable_failed
    flag set when port enable has failed

start_scan
    flag set from scan_start callback, cleared from \_mpt3sas_fw_work

start_scan_failed
    means port enable failed, return's the ioc_status

msix_enable
    flag indicating msix is enabled

msix_vector_count
    number msix vectors

cpu_msix_table
    table for mapping cpus to msix index

cpu_msix_table_sz
    table size

reply_post_host_index
    *undescribed*

ioc_reset_count
    *undescribed*

schedule_dead_ioc_flush_running_cmds
    callback to flush pending commands

non_operational_loop
    *undescribed*

scsi_io_cb_idx
    shost generated commands

tm_cb_idx
    task management commands

transport_cb_idx
    transport internal commands

scsih_cb_idx
    scsih internal commands

ctl_cb_idx
    clt internal commands

base_cb_idx
    base internal commands

port_enable_cb_idx
    *undescribed*

config_cb_idx
    base internal commands

tm_tr_cb_idx
    device removal target reset handshake

tm_tr_volume_cb_idx
    volume removal target reset

tm_sas_control_cb_idx
    *undescribed*

base_cmds
    *undescribed*

port_enable_cmds
    *undescribed*

transport_cmds
    *undescribed*

scsih_cmds
    *undescribed*

tm_cmds
    *undescribed*

ctl_cmds
    *undescribed*

config_cmds
    *undescribed*

base_add_sg_single
    handler for either 32/64 bit sgl's

build_sg_scmd
    *undescribed*

build_sg
    *undescribed*

build_zero_len_sge
    *undescribed*

sge_size_ieee
    *undescribed*

hba_mpi_version_belonged
    *undescribed*

build_sg_mpi
    *undescribed*

build_zero_len_sge_mpi
    *undescribed*

event_type
    bits indicating which events to log

event_context
    unique id for each logged event

event_log
    event log pointer

event_masks
    events that are masked

facts
    static facts data

pfacts
    static port facts data

manu_pg0
    static manufacturing page 0

manu_pg10
    static manufacturing page 10

manu_pg11
    static manufacturing page 11

bios_pg2
    static bios page 2

bios_pg3
    static bios page 3

ioc_pg8
    static ioc page 8

iounit_pg0
    static iounit page 0

iounit_pg1
    static iounit page 1

iounit_pg8
    static iounit page 8

req_boot_device
    *undescribed*

req_alt_boot_device
    *undescribed*

current_boot_device
    *undescribed*

sas_hba
    sas host object

sas_expander_list
    expander object list

sas_node_lock
    *undescribed*

sas_device_list
    sas device object list

sas_device_init_list
    sas device object list (used only at init time)

sas_device_lock
    *undescribed*

raid_device_list
    *undescribed*

raid_device_lock
    *undescribed*

io_missing_delay
    time for IO completed by fw when PDR enabled

device_missing_delay
    time for device missing by fw when PDR enabled

sas_id
    used for setting volume target IDs

blocking_handles
    bitmask used to identify which devices need blocking

pd_handles
    bitmask for PD handles

pd_handles_sz
    size of pd_handle bitmask

config_page_sz
    config page size

config_page
    reserve memory for config page payload

config_page_dma
    *undescribed*

hba_queue_depth
    hba request queue depth

sge_size
    sg element size for either 32/64 bit

scsiio_depth
    SCSI_IO queue depth

request_sz
    per request frame size

request
    pool of request frames

request_dma
    *undescribed*

request_dma_sz
    *undescribed*

scsi_lookup
    firmware request tracker list

scsi_lookup_pages
    *undescribed*

scsi_lookup_lock
    *undescribed*

free_list
    free list of request

pending_io_count
    *undescribed*

reset_wq
    *undescribed*

chain_lookup
    *undescribed*

free_chain_list
    *undescribed*

chain_dma_pool
    *undescribed*

chain_pages
    *undescribed*

max_sges_in_main_message
    number sg elements in main message

max_sges_in_chain_message
    number sg elements per chain

chains_needed_per_io
    max chains per io

chain_depth
    total chains allocated

chain_segment_sz
    gives the max number of
    SGEs accommodate on single chain buffer

hi_priority_smid
    *undescribed*

hi_priority
    *undescribed*

hi_priority_dma
    *undescribed*

hi_priority_depth
    *undescribed*

hpr_lookup
    *undescribed*

hpr_free_list
    *undescribed*

internal_smid
    *undescribed*

internal
    *undescribed*

internal_dma
    *undescribed*

internal_depth
    *undescribed*

internal_lookup
    *undescribed*

internal_free_list
    *undescribed*

sense
    pool of sense

sense_dma
    *undescribed*

sense_dma_pool
    *undescribed*

reply_sz
    per reply frame size:

reply
    pool of replys:

reply_dma
    *undescribed*

reply_dma_max_address
    *undescribed*

reply_dma_min_address
    *undescribed*

reply_dma_pool
    *undescribed*

reply_free_queue_depth
    reply free depth

reply_free
    pool for reply free queue (32 bit addr)

reply_free_dma
    *undescribed*

reply_free_dma_pool
    *undescribed*

reply_free_host_index
    tail index in pool to insert free replys

reply_post_queue_depth
    reply post queue depth

reply_post
    *undescribed*

rdpq_array_capable
    FW supports multiple reply queue addresses in ioc_init

rdpq_array_enable
    rdpq_array support is enabled in the driver

rdpq_array_enable_assigned
    this ensures that rdpq_array_enable flag
    is assigned only ones

reply_post_free_dma_pool
    *undescribed*

reply_queue_count
    number of reply queue's

reply_queue_list
    link list contaning the reply queue info

msix96_vector
    96 MSI-X vector support

replyPostRegisterIndex
    index of next position in Reply Desc Post Queue

delayed_tr_list
    target reset link list

delayed_tr_volume_list
    volume target reset link list

delayed_sc_list
    *undescribed*

delayed_event_ack_list
    *undescribed*

temp_sensors_count
    flag to carry the number of temperature sensors

pci_access_mutex
    Mutex to synchronize ioctl,sysfs show path and
    pci resource handling. PCI resource freeing will lead to free
    vital hardware/memory resource, which might be in use by cli/sysfs
    path functions resulting in Null pointer reference followed by kernel
    crash. To avoid the above race condition we use mutex syncrhonization
    which ensures the syncrhonization between cli/sysfs_show path.

ring_buffer_offset
    *undescribed*

ring_buffer_sz
    *undescribed*

is_warpdrive
    *undescribed*

hide_ir_msg
    *undescribed*

mfg_pg10_hide_flag
    *undescribed*

hide_drives
    *undescribed*

diag_trigger_lock
    *undescribed*

diag_trigger_active
    *undescribed*

diag_trigger_master
    *undescribed*

diag_trigger_event
    *undescribed*

diag_trigger_scsi
    *undescribed*

diag_trigger_mpi
    *undescribed*

.. This file was automatic generated / don't edit.


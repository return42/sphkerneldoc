.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intel/iwlwifi/iwl-trans.h

.. _`transport-layer---what-is-it--`:

Transport layer - what is it ?
==============================

The transport layer is the layer that deals with the HW directly. It provides
an abstraction of the underlying HW to the upper layer. The transport layer
doesn't provide any policy, algorithm or anything of this kind, but only
mechanisms to make the HW do something. It is not completely stateless but
close to it.
We will have an implementation for each different supported bus.

.. _`life-cycle-of-the-transport-layer`:

Life cycle of the transport layer
=================================

The transport layer has a very precise life cycle.

1) A helper function is called during the module initialization and
registers the bus driver's ops with the transport's alloc function.
2) Bus's probe calls to the transport layer's allocation functions.
Of course this function is bus specific.
3) This allocation functions will spawn the upper layer which will
register mac80211.

4) At some point (i.e. mac80211's start call), the op_mode will call
the following sequence:
start_hw
start_fw

5) Then when finished (or reset):
stop_device

6) Eventually, the free function will be called.

.. _`cmd_mode`:

enum CMD_MODE
=============

.. c:type:: enum CMD_MODE

    how to send the host commands ?

.. _`cmd_mode.definition`:

Definition
----------

.. code-block:: c

    enum CMD_MODE {
        CMD_ASYNC,
        CMD_WANT_SKB,
        CMD_SEND_IN_RFKILL,
        CMD_HIGH_PRIO,
        CMD_SEND_IN_IDLE,
        CMD_MAKE_TRANS_IDLE,
        CMD_WAKE_UP_TRANS,
        CMD_WANT_ASYNC_CALLBACK
    };

.. _`cmd_mode.constants`:

Constants
---------

CMD_ASYNC
    Return right away and don't wait for the response

CMD_WANT_SKB
    Not valid with CMD_ASYNC. The caller needs the buffer of
    the response. The caller needs to call iwl_free_resp when done.

CMD_SEND_IN_RFKILL
    *undescribed*

CMD_HIGH_PRIO
    The command is high priority - it goes to the front of the
    command queue, but after other high priority commands. Valid only
    with CMD_ASYNC.

CMD_SEND_IN_IDLE
    The command should be sent even when the trans is idle.

CMD_MAKE_TRANS_IDLE
    The command response should mark the trans as idle.

CMD_WAKE_UP_TRANS
    The command response should wake up the trans
    (i.e. mark it as non-idle).

CMD_WANT_ASYNC_CALLBACK
    the op_mode's async callback function must be
    called after this command completes. Valid only with CMD_ASYNC.

.. _`iwl_device_cmd`:

struct iwl_device_cmd
=====================

.. c:type:: struct iwl_device_cmd


.. _`iwl_device_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_device_cmd {
        union {
            struct {
                struct iwl_cmd_header hdr;
                u8 payload[DEF_CMD_PAYLOAD_SIZE];
            } ;
            struct {
                struct iwl_cmd_header_wide hdr_wide;
                u8 payload_wide[DEF_CMD_PAYLOAD_SIZE -sizeof(struct iwl_cmd_header_wide) + sizeof(struct iwl_cmd_header)];
            } ;
        } ;
    }

.. _`iwl_device_cmd.members`:

Members
-------

struct
    *undescribed*

{unnamed_struct}
    anonymous

.. _`iwl_device_cmd.description`:

Description
-----------

For allocation of the command and tx queues, this establishes the overall
size of the largest command we send to uCode, except for commands that
aren't fully copied and use other TFD space.

.. _`iwl_hcmd_dataflag`:

enum iwl_hcmd_dataflag
======================

.. c:type:: enum iwl_hcmd_dataflag

    flag for each one of the chunks of the command

.. _`iwl_hcmd_dataflag.definition`:

Definition
----------

.. code-block:: c

    enum iwl_hcmd_dataflag {
        IWL_HCMD_DFL_NOCOPY,
        IWL_HCMD_DFL_DUP
    };

.. _`iwl_hcmd_dataflag.constants`:

Constants
---------

IWL_HCMD_DFL_NOCOPY
    By default, the command is copied to the host command's
    ring. The transport layer doesn't map the command's buffer to DMA, but
    rather copies it to a previously allocated DMA buffer. This flag tells
    the transport layer not to copy the command, but to map the existing
    buffer (that is passed in) instead. This saves the memcpy and allows
    commands that are bigger than the fixed buffer to be submitted.
    Note that a TFD entry after a NOCOPY one cannot be a normal copied one.

IWL_HCMD_DFL_DUP
    Only valid without NOCOPY, duplicate the memory for this
    chunk internally and free it again after the command completes. This
    can (currently) be used only once per command.
    Note that a TFD entry after a DUP one cannot be a normal copied one.

.. _`iwl_host_cmd`:

struct iwl_host_cmd
===================

.. c:type:: struct iwl_host_cmd

    Host command to the uCode

.. _`iwl_host_cmd.definition`:

Definition
----------

.. code-block:: c

    struct iwl_host_cmd {
        const void *data[IWL_MAX_CMD_TBS_PER_TFD];
        struct iwl_rx_packet *resp_pkt;
        unsigned long _rx_page_addr;
        u32 _rx_page_order;
        u32 flags;
        u32 id;
        u16 len[IWL_MAX_CMD_TBS_PER_TFD];
        u8 dataflags[IWL_MAX_CMD_TBS_PER_TFD];
    }

.. _`iwl_host_cmd.members`:

Members
-------

data
    array of chunks that composes the data of the host command

resp_pkt
    response packet, if \ ``CMD_WANT_SKB``\  was set

_rx_page_addr
    (internally used to free response packet)

_rx_page_order
    (internally used to free response packet)

flags
    can be CMD\_\*

id
    command id of the host command, for wide commands encoding the
    version and group as well

len
    array of the lengths of the chunks in data

dataflags
    IWL_HCMD_DFL\_\*

.. _`iwl_d3_status`:

enum iwl_d3_status
==================

.. c:type:: enum iwl_d3_status

    WoWLAN image/device status

.. _`iwl_d3_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_d3_status {
        IWL_D3_STATUS_ALIVE,
        IWL_D3_STATUS_RESET
    };

.. _`iwl_d3_status.constants`:

Constants
---------

IWL_D3_STATUS_ALIVE
    firmware is still running after resume

IWL_D3_STATUS_RESET
    device was reset while suspended

.. _`iwl_trans_status`:

enum iwl_trans_status
=====================

.. c:type:: enum iwl_trans_status

    transport status flags

.. _`iwl_trans_status.definition`:

Definition
----------

.. code-block:: c

    enum iwl_trans_status {
        STATUS_SYNC_HCMD_ACTIVE,
        STATUS_DEVICE_ENABLED,
        STATUS_TPOWER_PMI,
        STATUS_INT_ENABLED,
        STATUS_RFKILL_HW,
        STATUS_RFKILL_OPMODE,
        STATUS_FW_ERROR,
        STATUS_TRANS_GOING_IDLE,
        STATUS_TRANS_IDLE,
        STATUS_TRANS_DEAD
    };

.. _`iwl_trans_status.constants`:

Constants
---------

STATUS_SYNC_HCMD_ACTIVE
    a SYNC command is being processed

STATUS_DEVICE_ENABLED
    APM is enabled

STATUS_TPOWER_PMI
    the device might be asleep (need to wake it up)

STATUS_INT_ENABLED
    interrupts are enabled

STATUS_RFKILL_HW
    the actual HW state of the RF-kill switch

STATUS_RFKILL_OPMODE
    RF-kill state reported to opmode

STATUS_FW_ERROR
    the fw is in error state

STATUS_TRANS_GOING_IDLE
    shutting down the trans, only special commands
    are sent

STATUS_TRANS_IDLE
    the trans is idle - general commands are not to be sent

STATUS_TRANS_DEAD
    trans is dead - avoid any read/write operation

.. _`iwl_trans_config`:

struct iwl_trans_config
=======================

.. c:type:: struct iwl_trans_config

    transport configuration

.. _`iwl_trans_config.definition`:

Definition
----------

.. code-block:: c

    struct iwl_trans_config {
        struct iwl_op_mode *op_mode;
        u8 cmd_queue;
        u8 cmd_fifo;
        unsigned int cmd_q_wdg_timeout;
        const u8 *no_reclaim_cmds;
        unsigned int n_no_reclaim_cmds;
        enum iwl_amsdu_size rx_buf_size;
        bool bc_table_dword;
        bool scd_set_active;
        bool sw_csum_tx;
        const struct iwl_hcmd_arr *command_groups;
        int command_groups_size;
        u32 sdio_adma_addr;
        u8 cb_data_offs;
    }

.. _`iwl_trans_config.members`:

Members
-------

op_mode
    pointer to the upper layer.

cmd_queue
    the index of the command queue.
    Must be set before start_fw.

cmd_fifo
    the fifo for host commands

cmd_q_wdg_timeout
    the timeout of the watchdog timer for the command queue.

no_reclaim_cmds
    Some devices erroneously don't set the
    SEQ_RX_FRAME bit on some notifications, this is the
    list of such notifications to filter. Max length is
    \ ``MAX_NO_RECLAIM_CMDS``\ .

n_no_reclaim_cmds
    # of commands in list

rx_buf_size
    RX buffer size needed for A-MSDUs
    if unset 4k will be the RX buffer size

bc_table_dword
    set to true if the BC table expects the byte count to be
    in DWORD (as opposed to bytes)

scd_set_active
    should the transport configure the SCD for HCMD queue

sw_csum_tx
    transport should compute the TCP checksum

command_groups
    array of command groups, each member is an array of the
    commands in the group; for debugging only

command_groups_size
    number of command groups, to avoid illegal access

sdio_adma_addr
    the default address to set for the ADMA in SDIO mode until
    we get the ALIVE from the uCode

cb_data_offs
    offset inside skb->cb to store transport data at, must have
    space for at least two pointers

.. _`iwl_trans_ops`:

struct iwl_trans_ops
====================

.. c:type:: struct iwl_trans_ops

    transport specific operations

.. _`iwl_trans_ops.definition`:

Definition
----------

.. code-block:: c

    struct iwl_trans_ops {
        int (*start_hw)(struct iwl_trans *iwl_trans, bool low_power);
        void (*op_mode_leave)(struct iwl_trans *iwl_trans);
        int (*start_fw)(struct iwl_trans *trans, const struct fw_img *fw, bool run_in_rfkill);
        int (*update_sf)(struct iwl_trans *trans, struct iwl_sf_region *st_fwrd_space);
        void (*fw_alive)(struct iwl_trans *trans, u32 scd_addr);
        void (*stop_device)(struct iwl_trans *trans, bool low_power);
        void (*d3_suspend)(struct iwl_trans *trans, bool test, bool reset);
        int (*d3_resume)(struct iwl_trans *trans, enum iwl_d3_status *status, bool test, bool reset);
        int (*send_cmd)(struct iwl_trans *trans, struct iwl_host_cmd *cmd);
        int (*tx)(struct iwl_trans *trans, struct sk_buff *skb, struct iwl_device_cmd *dev_cmd, int queue);
        void (*reclaim)(struct iwl_trans *trans, int queue, int ssn, struct sk_buff_head *skbs);
        bool (*txq_enable)(struct iwl_trans *trans, int queue, u16 ssn,const struct iwl_trans_txq_scd_cfg *cfg, unsigned int queue_wdg_timeout);
        void (*txq_disable)(struct iwl_trans *trans, int queue, bool configure_scd);
        int (*txq_alloc)(struct iwl_trans *trans,struct iwl_tx_queue_cfg_cmd *cmd,int cmd_id, unsigned int queue_wdg_timeout);
        void (*txq_free)(struct iwl_trans *trans, int queue);
        void (*txq_set_shared_mode)(struct iwl_trans *trans, u32 txq_id, bool shared);
        int (*wait_tx_queues_empty)(struct iwl_trans *trans, u32 txq_bm);
        int (*wait_txq_empty)(struct iwl_trans *trans, int queue);
        void (*freeze_txq_timer)(struct iwl_trans *trans, unsigned long txqs, bool freeze);
        void (*block_txq_ptrs)(struct iwl_trans *trans, bool block);
        void (*write8)(struct iwl_trans *trans, u32 ofs, u8 val);
        void (*write32)(struct iwl_trans *trans, u32 ofs, u32 val);
        u32 (*read32)(struct iwl_trans *trans, u32 ofs);
        u32 (*read_prph)(struct iwl_trans *trans, u32 ofs);
        void (*write_prph)(struct iwl_trans *trans, u32 ofs, u32 val);
        int (*read_mem)(struct iwl_trans *trans, u32 addr, void *buf, int dwords);
        int (*write_mem)(struct iwl_trans *trans, u32 addr, const void *buf, int dwords);
        void (*configure)(struct iwl_trans *trans, const struct iwl_trans_config *trans_cfg);
        void (*set_pmi)(struct iwl_trans *trans, bool state);
        bool (*grab_nic_access)(struct iwl_trans *trans, unsigned long *flags);
        void (*release_nic_access)(struct iwl_trans *trans, unsigned long *flags);
        void (*set_bits_mask)(struct iwl_trans *trans, u32 reg, u32 mask, u32 value);
        void (*ref)(struct iwl_trans *trans);
        void (*unref)(struct iwl_trans *trans);
        int (*suspend)(struct iwl_trans *trans);
        void (*resume)(struct iwl_trans *trans);
        struct iwl_trans_dump_data *(*dump_data)(struct iwl_trans *trans,const struct iwl_fw_dbg_trigger_tlv *trigger);
    }

.. _`iwl_trans_ops.members`:

Members
-------

start_hw
    starts the HW. If low_power is true, the NIC needs to be taken
    out of a low power state. From that point on, the HW can send
    interrupts. May sleep.

op_mode_leave
    Turn off the HW RF kill indication if on
    May sleep

start_fw
    allocates and inits all the resources for the transport
    layer. Also kick a fw image.
    May sleep

update_sf
    *undescribed*

fw_alive
    called when the fw sends alive notification. If the fw provides
    the SCD base address in SRAM, then provide it here, or 0 otherwise.
    May sleep

stop_device
    stops the whole device (embedded CPU put to reset) and stops
    the HW. If low_power is true, the NIC will be put in low power state.
    From that point on, the HW will be stopped but will still issue an
    interrupt if the HW RF kill switch is triggered.
    This callback must do the right thing and not crash even if \ ``start_hw``\ ()
    was called but not \ :c:type:`struct start_fw <start_fw>`\ (). May sleep.

d3_suspend
    put the device into the correct mode for WoWLAN during
    suspend. This is optional, if not implemented WoWLAN will not be
    supported. This callback may sleep.

d3_resume
    resume the device after WoWLAN, enabling the opmode to
    talk to the WoWLAN image to get its status. This is optional, if not
    implemented WoWLAN will not be supported. This callback may sleep.

send_cmd
    send a host command. Must return -ERFKILL if RFkill is asserted.
    If RFkill is asserted in the middle of a SYNC host command, it must
    return -ERFKILL straight away.
    May sleep only if CMD_ASYNC is not set

tx
    send an skb. The transport relies on the op_mode to zero the
    the ieee80211_tx_info->driver_data. If the MPDU is an A-MSDU, all
    the CSUM will be taken care of (TCP CSUM and IP header in case of
    IPv4). If the MPDU is a single MSDU, the op_mode must compute the IP
    header if it is IPv4.
    Must be atomic

reclaim
    free packet until ssn. Returns a list of freed packets.
    Must be atomic

txq_enable
    setup a queue. To setup an AC queue, use the
    iwl_trans_ac_txq_enable wrapper. fw_alive must have been called before
    this one. The op_mode must not configure the HCMD queue. The scheduler
    configuration may be \ ``NULL``\ , in which case the hardware will not be
    configured. If true is returned, the operation mode needs to increment
    the sequence number of the packets routed to this queue because of a
    hardware scheduler bug. May sleep.

txq_disable
    de-configure a Tx queue to send AMPDUs
    Must be atomic

txq_alloc
    *undescribed*

txq_free
    *undescribed*

txq_set_shared_mode
    change Tx queue shared/unshared marking

wait_tx_queues_empty
    wait until tx queues are empty. May sleep.

wait_txq_empty
    wait until specific tx queue is empty. May sleep.

freeze_txq_timer
    prevents the timer of the queue from firing until the
    queue is set to awake. Must be atomic.

block_txq_ptrs
    stop updating the write pointers of the Tx queues. Note
    that the transport needs to refcount the calls since this function
    will be called several times with block = true, and then the queues
    need to be unblocked only after the same number of calls with
    block = false.

write8
    write a u8 to a register at offset ofs from the BAR

write32
    write a u32 to a register at offset ofs from the BAR

read32
    read a u32 register at offset ofs from the BAR

read_prph
    read a DWORD from a periphery register

write_prph
    write a DWORD to a periphery register

read_mem
    read device's SRAM in DWORD

write_mem
    write device's SRAM in DWORD. If \ ``buf``\  is \ ``NULL``\ , then the memory
    will be zeroed.

configure
    configure parameters required by the transport layer from
    the op_mode. May be called several times before start_fw, can't be
    called after that.

set_pmi
    set the power pmi state

grab_nic_access
    wake the NIC to be able to access non-HBUS regs.
    Sleeping is not allowed between grab_nic_access and
    release_nic_access.

release_nic_access
    let the NIC go to sleep. The "flags" parameter
    must be the same one that was sent before to the grab_nic_access.
    \ ``set_bits_mask``\  - set SRAM register according to value and mask.

set_bits_mask
    *undescribed*

ref
    grab a reference to the transport/FW layers, disallowing
    certain low power states

unref
    release a reference previously taken with \ ``ref``\ . Note that
    initially the reference count is 1, making an initial \ ``unref``\ 
    necessary to allow low power states.

suspend
    *undescribed*

resume
    *undescribed*

dump_data
    return a vmalloc'ed buffer with debug data, maybe containing last
    TX'ed commands and similar. The buffer will be vfree'd by the caller.
    Note that the transport must fill in the proper file headers.

.. _`iwl_trans_ops.description`:

Description
-----------

All the handlers MUST be implemented

.. _`iwl_trans_state`:

enum iwl_trans_state
====================

.. c:type:: enum iwl_trans_state

    state of the transport layer

.. _`iwl_trans_state.definition`:

Definition
----------

.. code-block:: c

    enum iwl_trans_state {
        IWL_TRANS_NO_FW,
        IWL_TRANS_FW_ALIVE
    };

.. _`iwl_trans_state.constants`:

Constants
---------

IWL_TRANS_NO_FW
    no fw has sent an alive response

IWL_TRANS_FW_ALIVE
    a fw has sent an alive response

.. _`platform-power-management`:

Platform power management
=========================

There are two types of platform power management: system-wide
(WoWLAN) and runtime.

In system-wide power management the entire platform goes into a low
power state (e.g. idle or suspend to RAM) at the same time and the
device is configured as a wakeup source for the entire platform.
This is usually triggered by userspace activity (e.g. the user
presses the suspend button or a power management daemon decides to
put the platform in low power mode).  The device's behavior in this
mode is dictated by the wake-on-WLAN configuration.

In runtime power management, only the devices which are themselves
idle enter a low power state.  This is done at runtime, which means
that the entire system is still running normally.  This mode is
usually triggered automatically by the device driver and requires
the ability to enter and exit the low power modes in a very short
time, so there is not much impact in usability.

The terms used for the device's behavior are as follows:

- D0: the device is fully powered and the host is awake;
- D3: the device is in low power mode and only reacts to
specific events (e.g. magic-packet received or scan
results found);
- D0I3: the device is in low power mode and reacts to any
activity (e.g. RX);

These terms reflect the power modes in the firmware and are not to
be confused with the physical device power state.  The NIC can be
in D0I3 mode even if, for instance, the PCI device is in D3 state.

.. _`iwl_plat_pm_mode`:

enum iwl_plat_pm_mode
=====================

.. c:type:: enum iwl_plat_pm_mode

    platform power management mode

.. _`iwl_plat_pm_mode.definition`:

Definition
----------

.. code-block:: c

    enum iwl_plat_pm_mode {
        IWL_PLAT_PM_MODE_DISABLED,
        IWL_PLAT_PM_MODE_D3,
        IWL_PLAT_PM_MODE_D0I3
    };

.. _`iwl_plat_pm_mode.constants`:

Constants
---------

IWL_PLAT_PM_MODE_DISABLED
    power management is disabled for this
    device.  At runtime, this means that nothing happens and the
    device always remains in active.  In system-wide suspend mode,
    it means that the all connections will be closed automatically
    by mac80211 before the platform is suspended.

IWL_PLAT_PM_MODE_D3
    the device goes into D3 mode (i.e. WoWLAN).
    For runtime power management, this mode is not officially
    supported.

IWL_PLAT_PM_MODE_D0I3
    the device goes into D0I3 mode.

.. _`iwl_plat_pm_mode.description`:

Description
-----------

This enumeration describes the device's platform power management
behavior when in idle mode (i.e. runtime power management) or when
in system-wide suspend (i.e WoWLAN).

.. _`iwl_trans`:

struct iwl_trans
================

.. c:type:: struct iwl_trans

    transport common data

.. _`iwl_trans.definition`:

Definition
----------

.. code-block:: c

    struct iwl_trans {
        const struct iwl_trans_ops *ops;
        struct iwl_op_mode *op_mode;
        const struct iwl_cfg *cfg;
        struct iwl_drv *drv;
        enum iwl_trans_state state;
        unsigned long status;
        struct device *dev;
        u32 max_skb_frags;
        u32 hw_rev;
        u32 hw_rf_id;
        u32 hw_id;
        char hw_id_str[52];
        u8 rx_mpdu_cmd, rx_mpdu_cmd_hdr_size;
        bool pm_support;
        bool ltr_enabled;
        const struct iwl_hcmd_arr *command_groups;
        int command_groups_size;
        bool wide_cmd_header;
        u8 num_rx_queues;
        struct kmem_cache *dev_cmd_pool;
        char dev_cmd_pool_name[50];
        struct dentry *dbgfs_dir;
    #ifdef CONFIG_LOCKDEP
        struct lockdep_map sync_cmd_lockdep_map;
    #endif
        u64 dflt_pwr_limit;
        const struct iwl_fw_dbg_dest_tlv *dbg_dest_tlv;
        const struct iwl_fw_dbg_conf_tlv *dbg_conf_tlv[FW_DBG_CONF_MAX];
        struct iwl_fw_dbg_trigger_tlv * const *dbg_trigger_tlv;
        u8 dbg_dest_reg_num;
        u32 paging_req_addr;
        struct iwl_fw_paging *paging_db;
        void *paging_download_buf;
        enum iwl_plat_pm_mode system_pm_mode;
        enum iwl_plat_pm_mode runtime_pm_mode;
        bool suspending;
        char trans_specific[0] __aligned(sizeof(void *));
    }

.. _`iwl_trans.members`:

Members
-------

ops
    *undescribed*

op_mode
    *undescribed*

cfg
    *undescribed*

drv
    *undescribed*

state
    *undescribed*

status
    a bit-mask of transport status flags
    \ ``dev``\  - pointer to struct device \* that represents the device

dev
    *undescribed*

max_skb_frags
    maximum number of fragments an SKB can have when transmitted.
    0 indicates that frag SKBs (NETIF_F_SG) aren't supported.
    \ ``hw_rf_id``\  a u32 with the device RF ID

hw_rev
    *undescribed*

hw_rf_id
    *undescribed*

hw_id
    a u32 with the ID of the device / sub-device.
    Set during transport allocation.

hw_id_str
    a string with info about HW ID. Set during transport allocation.

rx_mpdu_cmd
    MPDU RX command ID, must be assigned by opmode before
    starting the firmware, used for tracing

rx_mpdu_cmd_hdr_size
    used for tracing, amount of data before the
    start of the 802.11 header in the \ ``rx_mpdu_cmd``\ 

pm_support
    set to true in start_hw if link pm is supported

ltr_enabled
    set to true if the LTR is enabled

command_groups
    *undescribed*

command_groups_size
    *undescribed*

wide_cmd_header
    true when ucode supports wide command header format

num_rx_queues
    number of RX queues allocated by the transport;
    the transport must set this before calling \ :c:func:`iwl_drv_start`\ 

dev_cmd_pool
    pool for Tx cmd allocation - for internal use only.
    The user should use iwl_trans_{alloc,free}_tx_cmd.

dev_cmd_pool_name
    *undescribed*

dbgfs_dir
    *undescribed*

sync_cmd_lockdep_map
    *undescribed*

dflt_pwr_limit
    default power limit fetched from the platform (ACPI)

dbg_dest_tlv
    points to the destination TLV for debug

dbg_conf_tlv
    array of pointers to configuration TLVs for debug

dbg_trigger_tlv
    array of pointers to triggers TLVs for debug

dbg_dest_reg_num
    num of reg_ops in \ ``dbg_dest_tlv``\ 

paging_req_addr
    The location were the FW will upload / download the pages
    from. The address is set by the opmode

paging_db
    Pointer to the opmode paging data base, the pointer is set by
    the opmode.

paging_download_buf
    Buffer used for copying all of the pages before
    downloading them to the FW. The buffer is allocated in the opmode

system_pm_mode
    the system-wide power management mode in use.
    This mode is set dynamically, depending on the WoWLAN values
    configured from the userspace at runtime.

runtime_pm_mode
    the runtime power management mode in use.  This
    mode is set during the initialization phase and is not
    supposed to change during runtime.

suspending
    *undescribed*

trans_specific
    *undescribed*

.. _`iwl_trans.description`:

Description
-----------

@ops - pointer to iwl_trans_ops
\ ``op_mode``\  - pointer to the op_mode
\ ``cfg``\  - pointer to the configuration
\ ``drv``\  - pointer to iwl_drv

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufshcd.h

.. _`uic_command`:

struct uic_command
==================

.. c:type:: struct uic_command

    UIC command structure

.. _`uic_command.definition`:

Definition
----------

.. code-block:: c

    struct uic_command {
        u32 command;
        u32 argument1;
        u32 argument2;
        u32 argument3;
        int cmd_active;
        int result;
        struct completion done;
    }

.. _`uic_command.members`:

Members
-------

command
    UIC command

argument1
    UIC command argument 1

argument2
    UIC command argument 2

argument3
    UIC command argument 3

cmd_active
    Indicate if UIC command is outstanding

result
    UIC command result

done
    UIC command completion

.. _`ufshcd_lrb`:

struct ufshcd_lrb
=================

.. c:type:: struct ufshcd_lrb

    local reference block

.. _`ufshcd_lrb.definition`:

Definition
----------

.. code-block:: c

    struct ufshcd_lrb {
        struct utp_transfer_req_desc *utr_descriptor_ptr;
        struct utp_upiu_req *ucd_req_ptr;
        struct utp_upiu_rsp *ucd_rsp_ptr;
        struct ufshcd_sg_entry *ucd_prdt_ptr;
        dma_addr_t utrd_dma_addr;
        dma_addr_t ucd_req_dma_addr;
        dma_addr_t ucd_rsp_dma_addr;
        dma_addr_t ucd_prdt_dma_addr;
        struct scsi_cmnd *cmd;
        u8 *sense_buffer;
        unsigned int sense_bufflen;
        int scsi_status;
        int command_type;
        int task_tag;
        u8 lun;
        bool intr_cmd;
        ktime_t issue_time_stamp;
        bool req_abort_skip;
    }

.. _`ufshcd_lrb.members`:

Members
-------

utr_descriptor_ptr
    UTRD address of the command

ucd_req_ptr
    UCD address of the command

ucd_rsp_ptr
    Response UPIU address for this command

ucd_prdt_ptr
    PRDT address of the command

utrd_dma_addr
    UTRD dma address for debug

ucd_req_dma_addr
    UPIU request dma address for debug

ucd_rsp_dma_addr
    UPIU response dma address for debug

ucd_prdt_dma_addr
    PRDT dma address for debug

cmd
    pointer to SCSI command

sense_buffer
    pointer to sense buffer address of the SCSI command

sense_bufflen
    Length of the sense buffer

scsi_status
    SCSI status of the command

command_type
    SCSI, UFS, Query.

task_tag
    Task tag of the command

lun
    LUN of the command

intr_cmd
    Interrupt command (doesn't participate in interrupt aggregation)

issue_time_stamp
    time stamp for debug purposes

req_abort_skip
    skip request abort task flag

.. _`ufs_query`:

struct ufs_query
================

.. c:type:: struct ufs_query

    holds relevant data structures for query request

.. _`ufs_query.definition`:

Definition
----------

.. code-block:: c

    struct ufs_query {
        struct ufs_query_req request;
        u8 *descriptor;
        struct ufs_query_res response;
    }

.. _`ufs_query.members`:

Members
-------

request
    request upiu and function

descriptor
    buffer for sending/receiving descriptor

response
    response upiu and response

.. _`ufs_dev_cmd`:

struct ufs_dev_cmd
==================

.. c:type:: struct ufs_dev_cmd

    all assosiated fields with device management commands

.. _`ufs_dev_cmd.definition`:

Definition
----------

.. code-block:: c

    struct ufs_dev_cmd {
        enum dev_cmd_type type;
        struct mutex lock;
        struct completion *complete;
        wait_queue_head_t tag_wq;
        struct ufs_query query;
    }

.. _`ufs_dev_cmd.members`:

Members
-------

type
    device management command type - Query, NOP OUT

lock
    lock to allow one command at a time

complete
    internal commands completion

tag_wq
    wait queue until free command slot is available

query
    *undescribed*

.. _`ufs_clk_info`:

struct ufs_clk_info
===================

.. c:type:: struct ufs_clk_info

    UFS clock related info

.. _`ufs_clk_info.definition`:

Definition
----------

.. code-block:: c

    struct ufs_clk_info {
        struct list_head list;
        struct clk *clk;
        const char *name;
        u32 max_freq;
        u32 min_freq;
        u32 curr_freq;
        bool enabled;
    }

.. _`ufs_clk_info.members`:

Members
-------

list
    list headed by hba->clk_list_head

clk
    clock node

name
    clock name

max_freq
    maximum frequency supported by the clock

min_freq
    min frequency that can be used for clock scaling

curr_freq
    indicates the current frequency that it is set to

enabled
    variable to check against multiple enable/disable

.. _`ufs_hba_variant_ops`:

struct ufs_hba_variant_ops
==========================

.. c:type:: struct ufs_hba_variant_ops

    variant specific callbacks

.. _`ufs_hba_variant_ops.definition`:

Definition
----------

.. code-block:: c

    struct ufs_hba_variant_ops {
        const char *name;
        int (*init)(struct ufs_hba *);
        void (*exit)(struct ufs_hba *);
        u32 (*get_ufs_hci_version)(struct ufs_hba *);
        int (*clk_scale_notify)(struct ufs_hba *, bool, enum ufs_notify_change_status);
        int (*setup_clocks)(struct ufs_hba *, bool, enum ufs_notify_change_status);
        int (*setup_regulators)(struct ufs_hba *, bool);
        int (*hce_enable_notify)(struct ufs_hba *, enum ufs_notify_change_status);
        int (*link_startup_notify)(struct ufs_hba *, enum ufs_notify_change_status);
        int (*pwr_change_notify)(struct ufs_hba *,enum ufs_notify_change_status status,struct ufs_pa_layer_attr *, struct ufs_pa_layer_attr *);
        void (*setup_xfer_req)(struct ufs_hba *, int, bool);
        void (*setup_task_mgmt)(struct ufs_hba *, int, u8);
        void (*hibern8_notify)(struct ufs_hba *, enum uic_cmd_dme, enum ufs_notify_change_status);
        int (*apply_dev_quirks)(struct ufs_hba *);
        int (*suspend)(struct ufs_hba *, enum ufs_pm_op);
        int (*resume)(struct ufs_hba *, enum ufs_pm_op);
        void (*dbg_register_dump)(struct ufs_hba *hba);
        int (*phy_initialization)(struct ufs_hba *);
    }

.. _`ufs_hba_variant_ops.members`:

Members
-------

name
    variant name

init
    called when the driver is initialized

exit
    called to cleanup everything done in init

get_ufs_hci_version
    called to get UFS HCI version

clk_scale_notify
    notifies that clks are scaled up/down

setup_clocks
    called before touching any of the controller registers

setup_regulators
    called before accessing the host controller

hce_enable_notify
    called before and after HCE enable bit is set to allow
    variant specific Uni-Pro initialization.

link_startup_notify
    called before and after Link startup is carried out
    to allow variant specific Uni-Pro initialization.

pwr_change_notify
    called before and after a power mode change
    is carried out to allow vendor spesific capabilities
    to be set.

setup_xfer_req
    called before any transfer request is issued
    to set some things

setup_task_mgmt
    called before any task management request is issued
    to set some things

hibern8_notify
    called around hibern8 enter/exit

apply_dev_quirks
    called to apply device specific quirks

suspend
    called during host controller PM callback

resume
    called during host controller PM callback

dbg_register_dump
    used to dump controller debug information

phy_initialization
    used to initialize phys

.. _`ufs_clk_gating`:

struct ufs_clk_gating
=====================

.. c:type:: struct ufs_clk_gating

    UFS clock gating related info

.. _`ufs_clk_gating.definition`:

Definition
----------

.. code-block:: c

    struct ufs_clk_gating {
        struct delayed_work gate_work;
        struct work_struct ungate_work;
        enum clk_gating_state state;
        unsigned long delay_ms;
        bool is_suspended;
        struct device_attribute delay_attr;
        struct device_attribute enable_attr;
        bool is_enabled;
        int active_reqs;
    }

.. _`ufs_clk_gating.members`:

Members
-------

gate_work
    worker to turn off clocks after some delay as specified in
    delay_ms

ungate_work
    worker to turn on clocks that will be used in case of
    interrupt context

state
    the current clocks state

delay_ms
    gating delay in ms

is_suspended
    clk gating is suspended when set to 1 which can be used
    during suspend/resume

delay_attr
    sysfs attribute to control delay_attr

enable_attr
    sysfs attribute to enable/disable clock gating

is_enabled
    Indicates the current status of clock gating

active_reqs
    number of requests that are pending and should be waited for
    completion before gating clocks.

.. _`ufs_clk_scaling`:

struct ufs_clk_scaling
======================

.. c:type:: struct ufs_clk_scaling

    UFS clock scaling related data

.. _`ufs_clk_scaling.definition`:

Definition
----------

.. code-block:: c

    struct ufs_clk_scaling {
        int active_reqs;
        unsigned long tot_busy_t;
        unsigned long window_start_t;
        ktime_t busy_start_t;
        struct device_attribute enable_attr;
        struct ufs_saved_pwr_info saved_pwr_info;
        struct workqueue_struct *workq;
        struct work_struct suspend_work;
        struct work_struct resume_work;
        bool is_allowed;
        bool is_busy_started;
        bool is_suspended;
    }

.. _`ufs_clk_scaling.members`:

Members
-------

active_reqs
    number of requests that are pending. If this is zero when
    devfreq ->target() function is called then schedule "suspend_work" to
    suspend devfreq.

tot_busy_t
    Total busy time in current polling window

window_start_t
    Start time (in jiffies) of the current polling window

busy_start_t
    Start time of current busy period

enable_attr
    sysfs attribute to enable/disable clock scaling

saved_pwr_info
    UFS power mode may also be changed during scaling and this
    one keeps track of previous power mode.

workq
    workqueue to schedule devfreq suspend/resume work

suspend_work
    worker to suspend devfreq

resume_work
    worker to resume devfreq

is_allowed
    tracks if scaling is currently allowed or not

is_busy_started
    tracks if busy period has started or not

is_suspended
    tracks if devfreq is suspended or not

.. _`ufs_init_prefetch`:

struct ufs_init_prefetch
========================

.. c:type:: struct ufs_init_prefetch

    contains data that is pre-fetched once during initialization

.. _`ufs_init_prefetch.definition`:

Definition
----------

.. code-block:: c

    struct ufs_init_prefetch {
        u32 icc_level;
    }

.. _`ufs_init_prefetch.members`:

Members
-------

icc_level
    icc level which was read during initialization

.. _`ufs_uic_err_reg_hist`:

struct ufs_uic_err_reg_hist
===========================

.. c:type:: struct ufs_uic_err_reg_hist

    keeps history of uic errors

.. _`ufs_uic_err_reg_hist.definition`:

Definition
----------

.. code-block:: c

    struct ufs_uic_err_reg_hist {
        int pos;
        u32 reg;
        ktime_t tstamp;
    }

.. _`ufs_uic_err_reg_hist.members`:

Members
-------

pos
    index to indicate cyclic buffer position

reg
    cyclic buffer for registers value

tstamp
    cyclic buffer for time stamp

.. _`ufs_stats`:

struct ufs_stats
================

.. c:type:: struct ufs_stats

    keeps usage/err statistics

.. _`ufs_stats.definition`:

Definition
----------

.. code-block:: c

    struct ufs_stats {
        u32 hibern8_exit_cnt;
        ktime_t last_hibern8_exit_tstamp;
        struct ufs_uic_err_reg_hist pa_err;
        struct ufs_uic_err_reg_hist dl_err;
        struct ufs_uic_err_reg_hist nl_err;
        struct ufs_uic_err_reg_hist tl_err;
        struct ufs_uic_err_reg_hist dme_err;
    }

.. _`ufs_stats.members`:

Members
-------

hibern8_exit_cnt
    Counter to keep track of number of exits,
    reset this after link-startup.

last_hibern8_exit_tstamp
    Set time after the hibern8 exit.
    Clear after the first successful command completion.

pa_err
    tracks pa-uic errors

dl_err
    tracks dl-uic errors

nl_err
    tracks nl-uic errors

tl_err
    tracks tl-uic errors

dme_err
    tracks dme errors

.. _`ufs_hba`:

struct ufs_hba
==============

.. c:type:: struct ufs_hba

    per adapter private structure

.. _`ufs_hba.definition`:

Definition
----------

.. code-block:: c

    struct ufs_hba {
        void __iomem *mmio_base;
        struct utp_transfer_cmd_desc *ucdl_base_addr;
        struct utp_transfer_req_desc *utrdl_base_addr;
        struct utp_task_req_desc *utmrdl_base_addr;
        dma_addr_t ucdl_dma_addr;
        dma_addr_t utrdl_dma_addr;
        dma_addr_t utmrdl_dma_addr;
        struct Scsi_Host *host;
        struct device *dev;
        struct scsi_device *sdev_ufs_device;
        enum ufs_dev_pwr_mode curr_dev_pwr_mode;
        enum uic_link_state uic_link_state;
        enum ufs_pm_level rpm_lvl;
        enum ufs_pm_level spm_lvl;
        struct device_attribute rpm_lvl_attr;
        struct device_attribute spm_lvl_attr;
        int pm_op_in_progress;
        struct ufshcd_lrb *lrb;
        unsigned long lrb_in_use;
        unsigned long outstanding_tasks;
        unsigned long outstanding_reqs;
        u32 capabilities;
        int nutrs;
        int nutmrs;
        u32 ufs_version;
        struct ufs_hba_variant_ops *vops;
        void *priv;
        unsigned int irq;
        bool is_irq_enabled;
    #define UFSHCD_QUIRK_BROKEN_INTR_AGGR UFS_BIT(0)
    #define UFSHCD_QUIRK_DELAY_BEFORE_DME_CMDS UFS_BIT(1)
    #define UFSHCD_QUIRK_BROKEN_LCC UFS_BIT(2)
    #define UFSHCD_QUIRK_BROKEN_PA_RXHSUNTERMCAP UFS_BIT(3)
    #define UFSHCD_QUIRK_DME_PEER_ACCESS_AUTO_MODE UFS_BIT(4)
    #define UFSHCD_QUIRK_BROKEN_UFS_HCI_VERSION UFS_BIT(5)
    #define UFSHCD_QUIRK_PRDT_BYTE_GRAN UFS_BIT(7)
        unsigned int quirks;
        unsigned int dev_quirks;
        wait_queue_head_t tm_wq;
        wait_queue_head_t tm_tag_wq;
        unsigned long tm_condition;
        unsigned long tm_slots_in_use;
        struct uic_command *active_uic_cmd;
        struct mutex uic_cmd_mutex;
        struct completion *uic_async_done;
        u32 ufshcd_state;
        u32 eh_flags;
        u32 intr_mask;
        u16 ee_ctrl_mask;
        bool is_powered;
        bool is_init_prefetch;
        struct ufs_init_prefetch init_prefetch_data;
        struct work_struct eh_work;
        struct work_struct eeh_work;
        u32 errors;
        u32 uic_error;
        u32 saved_err;
        u32 saved_uic_err;
        struct ufs_stats ufs_stats;
        struct ufs_dev_cmd dev_cmd;
        ktime_t last_dme_cmd_tstamp;
        struct ufs_dev_info dev_info;
        bool auto_bkops_enabled;
        struct ufs_vreg_info vreg_info;
        struct list_head clk_list_head;
        bool wlun_dev_clr_ua;
        int req_abort_count;
        u32 lanes_per_direction;
        struct ufs_pa_layer_attr pwr_info;
        struct ufs_pwr_mode_info max_pwr_info;
        struct ufs_clk_gating clk_gating;
        u32 caps;
    #define UFSHCD_CAP_CLK_GATING (1 << 0)
    #define UFSHCD_CAP_HIBERN8_WITH_CLK_GATING (1 << 1)
    #define UFSHCD_CAP_CLK_SCALING (1 << 2)
    #define UFSHCD_CAP_AUTO_BKOPS_SUSPEND (1 << 3)
    #define UFSHCD_CAP_INTR_AGGR (1 << 4)
    #define UFSHCD_CAP_KEEP_AUTO_BKOPS_ENABLED_EXCEPT_SUSPEND (1 << 5)
        struct devfreq *devfreq;
        struct ufs_clk_scaling clk_scaling;
        bool is_sys_suspended;
        enum bkops_status urgent_bkops_lvl;
        bool is_urgent_bkops_lvl_checked;
        struct rw_semaphore clk_scaling_lock;
        struct ufs_desc_size desc_size;
    }

.. _`ufs_hba.members`:

Members
-------

mmio_base
    UFSHCI base register address

ucdl_base_addr
    UFS Command Descriptor base address

utrdl_base_addr
    UTP Transfer Request Descriptor base address

utmrdl_base_addr
    UTP Task Management Descriptor base address

ucdl_dma_addr
    UFS Command Descriptor DMA address

utrdl_dma_addr
    UTRDL DMA address

utmrdl_dma_addr
    UTMRDL DMA address

host
    Scsi_Host instance of the driver

dev
    device handle

sdev_ufs_device
    *undescribed*

curr_dev_pwr_mode
    *undescribed*

uic_link_state
    *undescribed*

rpm_lvl
    *undescribed*

spm_lvl
    *undescribed*

rpm_lvl_attr
    *undescribed*

spm_lvl_attr
    *undescribed*

pm_op_in_progress
    *undescribed*

lrb
    local reference block

lrb_in_use
    lrb in use

outstanding_tasks
    Bits representing outstanding task requests

outstanding_reqs
    Bits representing outstanding transfer requests

capabilities
    UFS Controller Capabilities

nutrs
    Transfer Request Queue depth supported by controller

nutmrs
    Task Management Queue depth supported by controller

ufs_version
    UFS Version to which controller complies

vops
    pointer to variant specific operations

priv
    pointer to variant specific private data

irq
    Irq number of the controller

is_irq_enabled
    *undescribed*

quirks
    *undescribed*

dev_quirks
    *undescribed*

tm_wq
    wait queue for task management

tm_tag_wq
    wait queue for free task management slots

tm_condition
    condition variable for task management

tm_slots_in_use
    bit map of task management request slots in use

active_uic_cmd
    handle of active UIC command

uic_cmd_mutex
    mutex for uic command

uic_async_done
    *undescribed*

ufshcd_state
    UFSHCD states

eh_flags
    Error handling flags

intr_mask
    Interrupt Mask Bits

ee_ctrl_mask
    Exception event control mask

is_powered
    flag to check if HBA is powered

is_init_prefetch
    flag to check if data was pre-fetched in initialization

init_prefetch_data
    data pre-fetched during initialization

eh_work
    Worker to handle UFS errors that require s/w attention

eeh_work
    Worker to handle exception events

errors
    HBA errors

uic_error
    UFS interconnect layer error status

saved_err
    sticky error mask

saved_uic_err
    sticky UIC error mask

ufs_stats
    *undescribed*

dev_cmd
    ufs device management command information

last_dme_cmd_tstamp
    time stamp of the last completed DME command

dev_info
    *undescribed*

auto_bkops_enabled
    to track whether bkops is enabled in device

vreg_info
    UFS device voltage regulator information

clk_list_head
    UFS host controller clocks list node head

wlun_dev_clr_ua
    *undescribed*

req_abort_count
    *undescribed*

lanes_per_direction
    *undescribed*

pwr_info
    holds current power mode

max_pwr_info
    keeps the device max valid pwm

clk_gating
    *undescribed*

caps
    *undescribed*

devfreq
    *undescribed*

clk_scaling
    *undescribed*

is_sys_suspended
    *undescribed*

urgent_bkops_lvl
    keeps track of urgent bkops level for device

is_urgent_bkops_lvl_checked
    keeps track if the urgent bkops level for
    device is known or not.

clk_scaling_lock
    *undescribed*

desc_size
    descriptor sizes reported by device

.. _`ufshcd_rmwl`:

ufshcd_rmwl
===========

.. c:function:: void ufshcd_rmwl(struct ufs_hba *hba, u32 mask, u32 val, u32 reg)

    read modify write into a register \ ``hba``\  - per adapter instance \ ``mask``\  - mask to apply on read value \ ``val``\  - actual value to write \ ``reg``\  - register address

    :param struct ufs_hba \*hba:
        *undescribed*

    :param u32 mask:
        *undescribed*

    :param u32 val:
        *undescribed*

    :param u32 reg:
        *undescribed*

.. _`ufshcd_set_variant`:

ufshcd_set_variant
==================

.. c:function:: void ufshcd_set_variant(struct ufs_hba *hba, void *variant)

    set variant specific data to the hba \ ``hba``\  - per adapter instance \ ``variant``\  - pointer to variant specific data

    :param struct ufs_hba \*hba:
        *undescribed*

    :param void \*variant:
        *undescribed*

.. _`ufshcd_get_variant`:

ufshcd_get_variant
==================

.. c:function:: void *ufshcd_get_variant(struct ufs_hba *hba)

    get variant specific data from the hba \ ``hba``\  - per adapter instance

    :param struct ufs_hba \*hba:
        *undescribed*

.. This file was automatic generated / don't edit.


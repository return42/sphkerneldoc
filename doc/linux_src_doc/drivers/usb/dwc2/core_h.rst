.. -*- coding: utf-8; mode: rst -*-

======
core.h
======


.. _`dwc2_hsotg_ep`:

struct dwc2_hsotg_ep
====================

.. c:type:: dwc2_hsotg_ep

    driver endpoint definition.


.. _`dwc2_hsotg_ep.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hsotg_ep {
    struct usb_ep ep;
    struct list_head queue;
    struct dwc2_hsotg * parent;
    struct dwc2_hsotg_req * req;
    struct dentry * debugfs;
    unsigned long total_data;
    unsigned int size_loaded;
    unsigned int last_load;
    unsigned int fifo_load;
    unsigned short fifo_size;
    unsigned char dir_in;
    unsigned char index;
    unsigned char mc;
    unsigned int halted:1;
    unsigned int periodic:1;
    unsigned int isochronous:1;
    unsigned int send_zlp:1;
    char name[10];
  };


.. _`dwc2_hsotg_ep.members`:

Members
-------

:``ep``:
    The gadget layer representation of the endpoint.

:``queue``:
    Queue of requests for this endpoint.

:``parent``:
    Reference back to the parent device structure.

:``req``:
    The current request that the endpoint is processing. This is
    used to indicate an request has been loaded onto the endpoint
    and has yet to be completed (maybe due to data move, or simply
    awaiting an ack from the core all the data has been completed).

:``debugfs``:
    File entry for debugfs file for this endpoint.

:``total_data``:
    The total number of data bytes done.

:``size_loaded``:
    The last loaded size for DxEPTSIZE for periodic IN

:``last_load``:
    The offset of data for the last start of request.

:``fifo_load``:
    The amount of data loaded into the FIFO (periodic IN)

:``fifo_size``:
    The size of the FIFO (for periodic IN endpoints)

:``dir_in``:
    Set to true if this endpoint is of the IN direction, which
    means that it is sending data to the Host.

:``index``:
    The index for the endpoint registers.

:``mc``:
    Multi Count - number of transactions per microframe
    ``interval`` - Interval for periodic endpoints

:``halted``:
    Set if the endpoint has been halted.

:``periodic``:
    Set if this is a periodic ep, such as Interrupt

:``isochronous``:
    Set if this is a isochronous ep

:``send_zlp``:
    Set if we need to send a zero-length packet.

:``name[10]``:
    The name array passed to the USB core.




.. _`dwc2_hsotg_ep.description`:

Description
-----------

This is the driver's state for each registered enpoint, allowing it
to keep track of transactions that need doing. Each endpoint has a
lock to protect the state, to try and avoid using an overall lock
for the host controller as much as possible.

For periodic IN endpoints, we have fifo_size and fifo_load to try
and keep track of the amount of data in the periodic FIFO for each
of these as we don't have a status register that tells us how much
is in each of them. (note, this may actually be useless information
as in shared-fifo mode periodic in acts like a single-frame packet
buffer than a fifo)



.. _`dwc2_hsotg_req`:

struct dwc2_hsotg_req
=====================

.. c:type:: dwc2_hsotg_req

    data transfer request


.. _`dwc2_hsotg_req.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hsotg_req {
    struct usb_request req;
    struct list_head queue;
    void * saved_req_buf;
  };


.. _`dwc2_hsotg_req.members`:

Members
-------

:``req``:
    The USB gadget request

:``queue``:
    The list of requests for the endpoint this is queued for.

:``saved_req_buf``:
    variable to save req.buf when bounce buffers are used.




.. _`dwc2_core_params`:

struct dwc2_core_params
=======================

.. c:type:: dwc2_core_params

    Parameters for configuring the core


.. _`dwc2_core_params.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_core_params {
    int otg_cap;
    int otg_ver;
    int dma_enable;
    int dma_desc_enable;
    int dma_desc_fs_enable;
    int speed;
    int enable_dynamic_fifo;
    int en_multiple_tx_fifo;
    int host_rx_fifo_size;
    int host_nperio_tx_fifo_size;
    int host_perio_tx_fifo_size;
    int max_transfer_size;
    int max_packet_count;
    int host_channels;
    int phy_type;
    int phy_utmi_width;
    int phy_ulpi_ddr;
    int phy_ulpi_ext_vbus;
    int i2c_enable;
    int ulpi_fs_ls;
    int host_support_fs_ls_low_power;
    int host_ls_low_power_phy_clk;
    int ts_dline;
    int reload_ctl;
    int ahbcfg;
    int uframe_sched;
    int external_id_pin_ctl;
    int hibernation;
  };


.. _`dwc2_core_params.members`:

Members
-------

:``otg_cap``:
    Specifies the OTG capabilities.

                          0 - HNP and SRP capable
                          1 - SRP Only capable
                          2 - No HNP/SRP capable (always available)
                         Defaults to best available option (0, 1, then 2)

:``otg_ver``:
    OTG version supported

                          0 - 1.3 (default)
                          1 - 2.0

:``dma_enable``:
    Specifies whether to use slave or DMA mode for accessing
    the data FIFOs. The driver will automatically detect the
    value for this parameter if none is specified.
    0 - Slave (always available)
    1 - DMA (default, if available)

:``dma_desc_enable``:
    When DMA mode is enabled, specifies whether to use
    address DMA mode or descriptor DMA mode for accessing
    the data FIFOs. The driver will automatically detect the
    value for this if none is specified.
    0 - Address DMA
    1 - Descriptor DMA (default, if available)

:``dma_desc_fs_enable``:
    When DMA mode is enabled, specifies whether to use
    address DMA mode or descriptor DMA mode for accessing
    the data FIFOs in Full Speed mode only. The driver
    will automatically detect the value for this if none is
    specified.
    0 - Address DMA
    1 - Descriptor DMA in FS (default, if available)

:``speed``:
    Specifies the maximum speed of operation in host and
    device mode. The actual speed depends on the speed of
    the attached device and the value of phy_type.
    0 - High Speed
    (default when phy_type is UTMI+ or ULPI)
    1 - Full Speed
    (default when phy_type is Full Speed)

:``enable_dynamic_fifo``:
    0 - Use coreConsultant-specified FIFO size parameters

                          1 - Allow dynamic FIFO sizing (default, if available)

:``en_multiple_tx_fifo``:
    Specifies whether dedicated per-endpoint transmit FIFOs
    are enabled

:``host_rx_fifo_size``:
    Number of 4-byte words in the Rx FIFO in host mode when
    dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

:``host_nperio_tx_fifo_size``:
    Number of 4-byte words in the non-periodic Tx FIFO
    in host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

:``host_perio_tx_fifo_size``:
    Number of 4-byte words in the periodic Tx FIFO in
    host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

:``max_transfer_size``:
    The maximum transfer size supported, in bytes

                          2047 to 65,535
                         Actual maximum value is autodetected and also
                         the default.

:``max_packet_count``:
    The maximum number of packets in a transfer

                          15 to 511
                         Actual maximum value is autodetected and also
                         the default.

:``host_channels``:
    The number of host channel registers to use

                          1 to 16
                         Actual maximum value is autodetected and also
                         the default.

:``phy_type``:
    Specifies the type of PHY interface to use. By default,
    the driver will automatically detect the phy_type.
    0 - Full Speed Phy
    1 - UTMI+ Phy
    2 - ULPI Phy
    Defaults to best available option (2, 1, then 0)

:``phy_utmi_width``:
    Specifies the UTMI+ Data Width (in bits). This parameter
    is applicable for a phy_type of UTMI+ or ULPI. (For a
    ULPI phy_type, this parameter indicates the data width
    between the MAC and the ULPI Wrapper.) Also, this
    parameter is applicable only if the OTG_HSPHY_WIDTH cC
    parameter was set to "8 and 16 bits", meaning that the
    core has been configured to work at either data path
    width.
    8 or 16 (default 16 if available)

:``phy_ulpi_ddr``:
    Specifies whether the ULPI operates at double or single
    data rate. This parameter is only applicable if phy_type
    is ULPI.
    0 - single data rate ULPI interface with 8 bit wide
    data bus (default)
    1 - double data rate ULPI interface with 4 bit wide
    data bus

:``phy_ulpi_ext_vbus``:
    For a ULPI phy, specifies whether to use the internal or
    external supply to drive the VBus
    0 - Internal supply (default)
    1 - External supply

:``i2c_enable``:
    Specifies whether to use the I2Cinterface for a full
    speed PHY. This parameter is only applicable if phy_type
    is FS.
    0 - No (default)
    1 - Yes

:``ulpi_fs_ls``:
    Make ULPI phy operate in FS/LS mode only

                          0 - No (default)
                          1 - Yes

:``host_support_fs_ls_low_power``:
    Specifies whether low power mode is supported
    when attached to a Full Speed or Low Speed device in
    host mode.
    0 - Don't support low power mode (default)
    1 - Support low power mode

:``host_ls_low_power_phy_clk``:
    Specifies the PHY clock rate in low power mode
    when connected to a Low Speed device in host
    mode. This parameter is applicable only if
    host_support_fs_ls_low_power is enabled.
    0 - 48 MHz
    (default when phy_type is UTMI+ or ULPI)
    1 - 6 MHz
    (default when phy_type is Full Speed)

:``ts_dline``:
    Enable Term Select Dline pulsing

                          0 - No (default)
                          1 - Yes

:``reload_ctl``:
    Allow dynamic reloading of HFIR register during runtime

                          0 - No (default for core < 2.92a)
                          1 - Yes (default for core >= 2.92a)

:``ahbcfg``:
    This field allows the default value of the GAHBCFG
    register to be overridden
    -1         - GAHBCFG value will be set to 0x06
    (INCR4, default)
    all others - GAHBCFG value will be overridden with
    this value
    Not all bits can be controlled like this, the
    bits defined by GAHBCFG_CTRL_MASK are controlled
    by the driver and are ignored in this
    configuration value.

:``uframe_sched``:
    True to enable the microframe scheduler

:``external_id_pin_ctl``:
    Specifies whether ID pin is handled externally.
    Disable CONIDSTSCHNG controller interrupt in such
    case.
    0 - No (default)
    1 - Yes

:``hibernation``:
    Specifies whether the controller support hibernation.
    If hibernation is enabled, the controller will enter
    hibernation in both peripheral and host mode when
    needed.
    0 - No (default)
    1 - Yes




.. _`dwc2_core_params.description`:

Description
-----------

The following parameters may be specified when starting the module. These
parameters define how the DWC_otg controller should be configured. A
value of -1 (or any other out of range value) for any parameter means
to read the value from hardware (if possible) or use the builtin
default described above.



.. _`dwc2_hw_params`:

struct dwc2_hw_params
=====================

.. c:type:: dwc2_hw_params

    Autodetected parameters.


.. _`dwc2_hw_params.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hw_params {
    unsigned total_fifo_size:16;
    u32 snpsid;
    u32 dev_ep_dirs;
  };


.. _`dwc2_hw_params.members`:

Members
-------

:``total_fifo_size``:
    Total internal RAM for FIFOs (bytes)
    ``utmi_phy_data_width`` UTMI+ PHY data width

                          0 - 8 bits
                          1 - 16 bits
                          2 - 8 or 16 bits

:``snpsid``:
    Value from SNPSID register

:``dev_ep_dirs``:
    Direction of device endpoints (GHWCFG1)




.. _`dwc2_hw_params.description`:

Description
-----------


These parameters are the various parameters read from hardware
registers during initialization. They typically contain the best
supported or maximum value that can be configured in the
corresponding dwc2_core_params value.

The values that are not in dwc2_core_params are documented below.

``op_mode``             Mode of Operation

                      0 - HNP- and SRP-Capable OTG (Host & Device)
                      1 - SRP-Capable OTG (Host & Device)
                      2 - Non-HNP and Non-SRP Capable OTG (Host & Device)
                      3 - SRP-Capable Device
                      4 - Non-OTG Device
                      5 - SRP-Capable Host
                      6 - Non-OTG Host

``arch``                Architecture

                      0 - Slave only
                      1 - External DMA
                      2 - Internal DMA

``power_optimized``     Are power optimizations enabled?
``num_dev_ep``          Number of device endpoints available
``num_dev_perio_in_ep`` Number of device periodic IN endpoints
available

``dev_token_q_depth``   Device Mode IN Token Sequence Learning Queue
Depth
0 to 30

``host_perio_tx_q_depth``
Host Mode Periodic Request Queue Depth
2, 4 or 8

``nperio_tx_q_depth``
Non-Periodic Request Queue Depth
2, 4 or 8

``hs_phy_type``         High-speed PHY interface type

                      0 - High-speed interface not supported
                      1 - UTMI+
                      2 - ULPI
                      3 - UTMI+ and ULPI

``fs_phy_type``         Full-speed PHY interface type

                      0 - Full speed interface not supported
                      1 - Dedicated full speed interface
                      2 - FS pins shared with UTMI+ pins
                      3 - FS pins shared with ULPI pins



.. _`dwc2_gregs_backup`:

struct dwc2_gregs_backup
========================

.. c:type:: dwc2_gregs_backup

    Holds global registers state before entering partial power down


.. _`dwc2_gregs_backup.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_gregs_backup {
    u32 gotgctl;
    u32 gintmsk;
    u32 gahbcfg;
    u32 gusbcfg;
    u32 grxfsiz;
    u32 gnptxfsiz;
    u32 gi2cctl;
    u32 hptxfsiz;
    u32 gdfifocfg;
    u32 dtxfsiz[MAX_EPS_CHANNELS];
    u32 gpwrdn;
  };


.. _`dwc2_gregs_backup.members`:

Members
-------

:``gotgctl``:
    Backup of GOTGCTL register

:``gintmsk``:
    Backup of GINTMSK register

:``gahbcfg``:
    Backup of GAHBCFG register

:``gusbcfg``:
    Backup of GUSBCFG register

:``grxfsiz``:
    Backup of GRXFSIZ register

:``gnptxfsiz``:
    Backup of GNPTXFSIZ register

:``gi2cctl``:
    Backup of GI2CCTL register

:``hptxfsiz``:
    Backup of HPTXFSIZ register

:``gdfifocfg``:
    Backup of GDFIFOCFG register

:``dtxfsiz[MAX_EPS_CHANNELS]``:
    Backup of DTXFSIZ registers for each endpoint

:``gpwrdn``:
    Backup of GPWRDN register




.. _`dwc2_dregs_backup`:

struct dwc2_dregs_backup
========================

.. c:type:: dwc2_dregs_backup

    Holds device registers state before entering partial power down


.. _`dwc2_dregs_backup.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_dregs_backup {
    u32 dcfg;
    u32 dctl;
    u32 daintmsk;
    u32 diepmsk;
    u32 doepmsk;
    u32 diepctl[MAX_EPS_CHANNELS];
    u32 dieptsiz[MAX_EPS_CHANNELS];
    u32 diepdma[MAX_EPS_CHANNELS];
    u32 doepctl[MAX_EPS_CHANNELS];
    u32 doeptsiz[MAX_EPS_CHANNELS];
    u32 doepdma[MAX_EPS_CHANNELS];
  };


.. _`dwc2_dregs_backup.members`:

Members
-------

:``dcfg``:
    Backup of DCFG register

:``dctl``:
    Backup of DCTL register

:``daintmsk``:
    Backup of DAINTMSK register

:``diepmsk``:
    Backup of DIEPMSK register

:``doepmsk``:
    Backup of DOEPMSK register

:``diepctl[MAX_EPS_CHANNELS]``:
    Backup of DIEPCTL register

:``dieptsiz[MAX_EPS_CHANNELS]``:
    Backup of DIEPTSIZ register

:``diepdma[MAX_EPS_CHANNELS]``:
    Backup of DIEPDMA register

:``doepctl[MAX_EPS_CHANNELS]``:
    Backup of DOEPCTL register

:``doeptsiz[MAX_EPS_CHANNELS]``:
    Backup of DOEPTSIZ register

:``doepdma[MAX_EPS_CHANNELS]``:
    Backup of DOEPDMA register




.. _`dwc2_hregs_backup`:

struct dwc2_hregs_backup
========================

.. c:type:: dwc2_hregs_backup

    Holds host registers state before entering partial power down


.. _`dwc2_hregs_backup.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hregs_backup {
    u32 hcfg;
    u32 haintmsk;
    u32 hcintmsk[MAX_EPS_CHANNELS];
    u32 hfir;
  };


.. _`dwc2_hregs_backup.members`:

Members
-------

:``hcfg``:
    Backup of HCFG register

:``haintmsk``:
    Backup of HAINTMSK register

:``hcintmsk[MAX_EPS_CHANNELS]``:
    Backup of HCINTMSK register

:``hfir``:
    Backup of HFIR register




.. _`dwc2_hsotg`:

struct dwc2_hsotg
=================

.. c:type:: dwc2_hsotg

    Holds the state of the driver, including the non-periodic and periodic schedules


.. _`dwc2_hsotg.definition`:

Definition
----------

.. code-block:: c

  struct dwc2_hsotg {
    struct device * dev;
    void __iomem * regs;
    struct dwc2_hw_params hw_params;
    struct dwc2_core_params * core_params;
    enum usb_otg_state op_state;
    enum usb_dr_mode dr_mode;
    struct phy * phy;
    struct usb_phy * uphy;
    struct dwc2_hsotg_plat * plat;
    struct regulator_bulk_data supplies[ARRAY_SIZE(dwc2_hsotg_supply_names)];
    u32 phyif;
    spinlock_t lock;
    void * priv;
    unsigned int queuing_high_bandwidth:1;
    unsigned int srp_success:1;
    struct workqueue_struct * wq_otg;
    struct work_struct wf_otg;
    struct timer_list wkp_timer;
    enum dwc2_lx_state lx_state;
    struct dentry * debug_root;
    #define DWC2_CORE_REV_2_71a	0x4f54271a
    #define DWC2_CORE_REV_2_90a	0x4f54290a
    #define DWC2_CORE_REV_2_92a	0x4f54292a
    #define DWC2_CORE_REV_2_94a	0x4f54294a
    #define DWC2_CORE_REV_3_00a	0x4f54300a
    #if IS_ENABLED(CONFIG_USB_DWC2_HOST) || IS_ENABLED(CONFIG_USB_DWC2_DUAL_ROLE)
    union dwc2_hcd_internal_flags flags;
    struct list_head non_periodic_sched_inactive;
    struct list_head non_periodic_sched_active;
    struct list_head * non_periodic_qh_ptr;
    struct list_head periodic_sched_inactive;
    struct list_head periodic_sched_ready;
    struct list_head periodic_sched_assigned;
    struct list_head periodic_sched_queued;
    struct list_head split_order;
    u16 periodic_usecs;
    unsigned long hs_periodic_bitmap[DIV_ROUND_UP(DWC2_HS_SCHEDULE_US# BITS_PER_LONG)];
    u16 frame_number;
    u16 periodic_qh_count;
    #ifdef CONFIG_USB_DWC2_TRACK_MISSED_SOFS
    #define FRAME_NUM_ARRAY_SIZE 1000
    #endif
    struct list_head free_hc_list;
    int periodic_channels;
    int non_periodic_channels;
    struct dwc2_host_chan * hc_ptr_array[MAX_EPS_CHANNELS];
    u8 * status_buf;
    dma_addr_t status_buf_dma;
    #define DWC2_HCD_STATUS_BUF_SIZE 64
    struct delayed_work start_work;
    struct delayed_work reset_work;
    u8 otg_port;
    u32 * frame_list;
    dma_addr_t frame_list_dma;
    u32 frame_list_sz;
    struct kmem_cache * desc_gen_cache;
    struct kmem_cache * desc_hsisoc_cache;
    #ifdef DEBUG
    #endif
    #endif
    #if IS_ENABLED(CONFIG_USB_DWC2_PERIPHERAL) || IS_ENABLED(CONFIG_USB_DWC2_DUAL_ROLE)
    struct usb_gadget_driver * driver;
    unsigned int dedicated_fifos:1;
    unsigned char num_of_eps;
    struct usb_request * ep0_reply;
    struct usb_request * ctrl_req;
    void * ep0_buff;
    void * ctrl_buff;
    enum dwc2_ep0_state ep0_state;
    u8 test_mode;
    u32 g_using_dma;
    u32 g_rx_fifo_sz;
    u32 g_np_g_tx_fifo_sz;
    u32 g_tx_fifo_sz[MAX_EPS_CHANNELS];
    #endif
  };


.. _`dwc2_hsotg.members`:

Members
-------

:``dev``:
    The struct device pointer

:``regs``:
    Pointer to controller regs

:``hw_params``:
    Parameters that were autodetected from the
    hardware registers

:``core_params``:
    Parameters that define how the core should be configured

:``op_state``:
    The operational State, during transitions (a_host=>
    a_peripheral and b_device=>b_host) this may not match
    the core, but allows the software to determine
    transitions

:``dr_mode``:
    Requested mode of operation, one of following:

                         - USB_DR_MODE_PERIPHERAL
                         - USB_DR_MODE_HOST
                         - USB_DR_MODE_OTG

    ``hcd_enabled``                Host mode sub-driver initialization indicator.
    ``gadget_enabled``        Peripheral mode sub-driver initialization indicator.
    ``ll_hw_enabled``        Status of low-level hardware resources.

:``phy``:
    The otg phy transceiver structure for phy control.

:``uphy``:
    The otg phy transceiver structure for old USB phy control.

:``plat``:
    The platform specific configuration data. This can be removed once
    all SoCs support usb transceiver.

:``supplies[ARRAY_SIZE(dwc2_hsotg_supply_names)]``:
    Definition of USB power supplies

:``phyif``:
    PHY interface width

:``lock``:
    Spinlock that protects all the driver data structures

:``priv``:
    Stores a pointer to the struct usb_hcd

:``queuing_high_bandwidth``:
    True if multiple packets of a high-bandwidth
    transfer are in process of being queued

:``srp_success``:
    Stores status of SRP request in the case of a FS PHY
    with an I2C interface

:``wq_otg``:
    Workqueue object used for handling of some interrupts

:``wf_otg``:
    Work object for handling Connector ID Status Change
    interrupt

:``wkp_timer``:
    Timer object for handling Wakeup Detected interrupt

:``lx_state``:
    Lx state of connected device

:``debug_root``:
    Root directrory for debugfs.

:``flags``:
    Flags for handling root port state changes

:``non_periodic_sched_inactive``:
    Inactive QHs in the non-periodic schedule.
    Transfers associated with these QHs are not currently
    assigned to a host channel.

:``non_periodic_sched_active``:
    Active QHs in the non-periodic schedule.
    Transfers associated with these QHs are currently
    assigned to a host channel.

:``non_periodic_qh_ptr``:
    Pointer to next QH to process in the active
    non-periodic schedule

:``periodic_sched_inactive``:
    Inactive QHs in the periodic schedule. This is a
    list of QHs for periodic transfers that are _not_
    scheduled for the next frame. Each QH in the list has an
    interval counter that determines when it needs to be
    scheduled for execution. This scheduling mechanism
    allows only a simple calculation for periodic bandwidth
    used (i.e. must assume that all periodic transfers may
    need to execute in the same frame). However, it greatly
    simplifies scheduling and should be sufficient for the
    vast majority of OTG hosts, which need to connect to a
    small number of peripherals at one time. Items move from
    this list to periodic_sched_ready when the QH interval
    counter is 0 at SOF.

:``periodic_sched_ready``:
    List of periodic QHs that are ready for execution in
    the next frame, but have not yet been assigned to host
    channels. Items move from this list to
    periodic_sched_assigned as host channels become
    available during the current frame.

:``periodic_sched_assigned``:
    List of periodic QHs to be executed in the next
    frame that are assigned to host channels. Items move
    from this list to periodic_sched_queued as the
    transactions for the QH are queued to the DWC_otg
    controller.

:``periodic_sched_queued``:
    List of periodic QHs that have been queued for
    execution. Items move from this list to either
    periodic_sched_inactive or periodic_sched_ready when the
    channel associated with the transfer is released. If the
    interval for the QH is 1, the item moves to
    periodic_sched_ready because it must be rescheduled for
    the next frame. Otherwise, the item moves to
    periodic_sched_inactive.

:``split_order``:
    List keeping track of channels doing splits, in order.

:``periodic_usecs``:
    Total bandwidth claimed so far for periodic transfers.
    This value is in microseconds per (micro)frame. The
    assumption is that all periodic transfers may occur in
    the same (micro)frame.

:``hs_periodic_bitmap[DIV_ROUND_UP(DWC2_HS_SCHEDULE_US# BITS_PER_LONG)]``:
    Bitmap used by the microframe scheduler any time the
    host is in high speed mode; low speed schedules are
    stored elsewhere since we need one per TT.

:``frame_number``:
    Frame number read from the core at SOF. The value ranges
    from 0 to HFNUM_MAX_FRNUM.

:``periodic_qh_count``:
    Count of periodic QHs, if using several eps. Used for
    SOF enable/disable.

:``free_hc_list``:
    Free host channels in the controller. This is a list of
    struct dwc2_host_chan items.

:``periodic_channels``:
    Number of host channels assigned to periodic transfers.
    Currently assuming that there is a dedicated host
    channel for each periodic transaction and at least one
    host channel is available for non-periodic transactions.

:``non_periodic_channels``:
    Number of host channels assigned to non-periodic
    transfers

    ``available_host_channels`` Number of host channels available for the microframe
    scheduler to use

:``hc_ptr_array[MAX_EPS_CHANNELS]``:
    Array of pointers to the host channel descriptors.
    Allows accessing a host channel descriptor given the
    host channel number. This is useful in interrupt
    handlers.

:``status_buf``:
    Buffer used for data received during the status phase of
    a control transfer.

:``status_buf_dma``:
    DMA address for status_buf

:``start_work``:
    Delayed work for handling host A-cable connection

:``reset_work``:
    Delayed work for handling a port reset

:``otg_port``:
    OTG port number

:``frame_list``:
    Frame list

:``frame_list_dma``:
    Frame list DMA address

:``frame_list_sz``:
    Frame list size

:``desc_gen_cache``:
    Kmem cache for generic descriptors

:``desc_hsisoc_cache``:
    Kmem cache for hs isochronous descriptors

:``driver``:
    USB gadget driver

:``dedicated_fifos``:
    Set if the hardware has dedicated IN-EP fifos.

:``num_of_eps``:
    Number of available EPs (excluding EP0)

:``ep0_reply``:
    Request used for ep0 reply.

:``ctrl_req``:
    Request for EP0 control packets.

:``ep0_buff``:
    Buffer for EP0 reply data, if needed.

:``ctrl_buff``:
    Buffer for EP0 control requests.

:``ep0_state``:
    EP0 control transfers state

:``test_mode``:
    USB test mode requested by the host

:``g_using_dma``:
    Indicate if dma usage is enabled

:``g_rx_fifo_sz``:
    Contains rx fifo size value

:``g_np_g_tx_fifo_sz``:
    Contains Non-Periodic tx fifo size value

:``g_tx_fifo_sz[MAX_EPS_CHANNELS]``:
    Contains tx fifo size value per endpoints



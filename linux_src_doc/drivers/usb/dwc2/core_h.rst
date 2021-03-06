.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/core.h

.. _`dwc2_hsotg_ep`:

struct dwc2_hsotg_ep
====================

.. c:type:: struct dwc2_hsotg_ep

    driver endpoint definition.

.. _`dwc2_hsotg_ep.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hsotg_ep {
        struct usb_ep ep;
        struct list_head queue;
        struct dwc2_hsotg *parent;
        struct dwc2_hsotg_req *req;
        struct dentry *debugfs;
        unsigned long total_data;
        unsigned int size_loaded;
        unsigned int last_load;
        unsigned int fifo_load;
        unsigned short fifo_size;
        unsigned short fifo_index;
        unsigned char dir_in;
        unsigned char index;
        unsigned char mc;
        u16 interval;
        unsigned int halted:1;
        unsigned int periodic:1;
        unsigned int isochronous:1;
        unsigned int send_zlp:1;
        unsigned int target_frame;
    #define TARGET_FRAME_INITIAL 0xFFFFFFFF
        bool frame_overrun;
        dma_addr_t desc_list_dma;
        struct dwc2_dma_desc *desc_list;
        u8 desc_count;
        unsigned int next_desc;
        unsigned int compl_desc;
        char name[10];
    }

.. _`dwc2_hsotg_ep.members`:

Members
-------

ep
    The gadget layer representation of the endpoint.

queue
    Queue of requests for this endpoint.

parent
    Reference back to the parent device structure.

req
    The current request that the endpoint is processing. This is
    used to indicate an request has been loaded onto the endpoint
    and has yet to be completed (maybe due to data move, or simply
    awaiting an ack from the core all the data has been completed).

debugfs
    File entry for debugfs file for this endpoint.

total_data
    The total number of data bytes done.

size_loaded
    The last loaded size for DxEPTSIZE for periodic IN

last_load
    The offset of data for the last start of request.

fifo_load
    The amount of data loaded into the FIFO (periodic IN)

fifo_size
    The size of the FIFO (for periodic IN endpoints)

fifo_index
    For Dedicated FIFO operation, only FIFO0 can be used for EP0.

dir_in
    Set to true if this endpoint is of the IN direction, which
    means that it is sending data to the Host.

index
    The index for the endpoint registers.

mc
    Multi Count - number of transactions per microframe

interval
    Interval for periodic endpoints, in frames or microframes.

halted
    Set if the endpoint has been halted.

periodic
    Set if this is a periodic ep, such as Interrupt

isochronous
    Set if this is a isochronous ep

send_zlp
    Set if we need to send a zero-length packet.

target_frame
    Targeted frame num to setup next ISOC transfer

frame_overrun
    Indicates SOF number overrun in DSTS

desc_list_dma
    The DMA address of descriptor chain currently in use.

desc_list
    Pointer to descriptor DMA chain head currently in use.

desc_count
    Count of entries within the DMA descriptor chain of EP.

next_desc
    index of next free descriptor in the ISOC chain under SW control.

compl_desc
    index of next descriptor to be completed by xFerComplete

name
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

.. c:type:: struct dwc2_hsotg_req

    data transfer request

.. _`dwc2_hsotg_req.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hsotg_req {
        struct usb_request req;
        struct list_head queue;
        void *saved_req_buf;
    }

.. _`dwc2_hsotg_req.members`:

Members
-------

req
    The USB gadget request

queue
    The list of requests for the endpoint this is queued for.

saved_req_buf
    variable to save req.buf when bounce buffers are used.

.. _`dwc2_core_params`:

struct dwc2_core_params
=======================

.. c:type:: struct dwc2_core_params

    Parameters for configuring the core

.. _`dwc2_core_params.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_core_params {
        u8 otg_cap;
    #define DWC2_CAP_PARAM_HNP_SRP_CAPABLE 0
    #define DWC2_CAP_PARAM_SRP_ONLY_CAPABLE 1
    #define DWC2_CAP_PARAM_NO_HNP_SRP_CAPABLE 2
        u8 phy_type;
    #define DWC2_PHY_TYPE_PARAM_FS 0
    #define DWC2_PHY_TYPE_PARAM_UTMI 1
    #define DWC2_PHY_TYPE_PARAM_ULPI 2
        u8 speed;
    #define DWC2_SPEED_PARAM_HIGH 0
    #define DWC2_SPEED_PARAM_FULL 1
    #define DWC2_SPEED_PARAM_LOW 2
        u8 phy_utmi_width;
        bool phy_ulpi_ddr;
        bool phy_ulpi_ext_vbus;
        bool enable_dynamic_fifo;
        bool en_multiple_tx_fifo;
        bool i2c_enable;
        bool acg_enable;
        bool ulpi_fs_ls;
        bool ts_dline;
        bool reload_ctl;
        bool uframe_sched;
        bool external_id_pin_ctl;
        int power_down;
    #define DWC2_POWER_DOWN_PARAM_NONE 0
    #define DWC2_POWER_DOWN_PARAM_PARTIAL 1
    #define DWC2_POWER_DOWN_PARAM_HIBERNATION 2
        bool lpm;
        bool lpm_clock_gating;
        bool besl;
        bool hird_threshold_en;
        bool service_interval;
        u8 hird_threshold;
        bool activate_stm_fs_transceiver;
        bool ipg_isoc_en;
        u16 max_packet_count;
        u32 max_transfer_size;
        u32 ahbcfg;
        u32 ref_clk_per;
        u16 sof_cnt_wkup_alert;
        bool host_dma;
        bool dma_desc_enable;
        bool dma_desc_fs_enable;
        bool host_support_fs_ls_low_power;
        bool host_ls_low_power_phy_clk;
        bool oc_disable;
        u8 host_channels;
        u16 host_rx_fifo_size;
        u16 host_nperio_tx_fifo_size;
        u16 host_perio_tx_fifo_size;
        bool g_dma;
        bool g_dma_desc;
        u32 g_rx_fifo_size;
        u32 g_np_tx_fifo_size;
        u32 g_tx_fifo_size[MAX_EPS_CHANNELS];
        bool change_speed_quirk;
    }

.. _`dwc2_core_params.members`:

Members
-------

otg_cap
    Specifies the OTG capabilities.
    0 - HNP and SRP capable
    1 - SRP Only capable
    2 - No HNP/SRP capable (always available)
    Defaults to best available option (0, 1, then 2)

phy_type
    Specifies the type of PHY interface to use. By default,
    the driver will automatically detect the phy_type.
    0 - Full Speed Phy
    1 - UTMI+ Phy
    2 - ULPI Phy
    Defaults to best available option (2, 1, then 0)

speed
    Specifies the maximum speed of operation in host and
    device mode. The actual speed depends on the speed of
    the attached device and the value of phy_type.
    0 - High Speed
    (default when phy_type is UTMI+ or ULPI)
    1 - Full Speed
    (default when phy_type is Full Speed)

phy_utmi_width
    Specifies the UTMI+ Data Width (in bits). This parameter
    is applicable for a phy_type of UTMI+ or ULPI. (For a
    ULPI phy_type, this parameter indicates the data width
    between the MAC and the ULPI Wrapper.) Also, this
    parameter is applicable only if the OTG_HSPHY_WIDTH cC
    parameter was set to "8 and 16 bits", meaning that the
    core has been configured to work at either data path
    width.
    8 or 16 (default 16 if available)

phy_ulpi_ddr
    Specifies whether the ULPI operates at double or single
    data rate. This parameter is only applicable if phy_type
    is ULPI.
    0 - single data rate ULPI interface with 8 bit wide
    data bus (default)
    1 - double data rate ULPI interface with 4 bit wide
    data bus

phy_ulpi_ext_vbus
    For a ULPI phy, specifies whether to use the internal or
    external supply to drive the VBus
    0 - Internal supply (default)
    1 - External supply

enable_dynamic_fifo
    0 - Use coreConsultant-specified FIFO size parameters
    1 - Allow dynamic FIFO sizing (default, if available)

en_multiple_tx_fifo
    Specifies whether dedicated per-endpoint transmit FIFOs
    are enabled for non-periodic IN endpoints in device
    mode.

i2c_enable
    Specifies whether to use the I2Cinterface for a full
    speed PHY. This parameter is only applicable if phy_type
    is FS.
    0 - No (default)
    1 - Yes

acg_enable
    For enabling Active Clock Gating in the controller
    0 - No
    1 - Yes

ulpi_fs_ls
    Make ULPI phy operate in FS/LS mode only
    0 - No (default)
    1 - Yes

ts_dline
    Enable Term Select Dline pulsing
    0 - No (default)
    1 - Yes

reload_ctl
    Allow dynamic reloading of HFIR register during runtime
    0 - No (default for core < 2.92a)
    1 - Yes (default for core >= 2.92a)

uframe_sched
    True to enable the microframe scheduler

external_id_pin_ctl
    Specifies whether ID pin is handled externally.
    Disable CONIDSTSCHNG controller interrupt in such
    case.
    0 - No (default)
    1 - Yes

power_down
    Specifies whether the controller support power_down.
    If power_down is enabled, the controller will enter
    power_down in both peripheral and host mode when
    needed.
    0 - No (default)
    1 - Partial power down
    2 - Hibernation

lpm
    Enable LPM support.
    0 - No
    1 - Yes

lpm_clock_gating
    Enable core PHY clock gating.
    0 - No
    1 - Yes

besl
    Enable LPM Errata support.
    0 - No
    1 - Yes

hird_threshold_en
    HIRD or HIRD Threshold enable.
    0 - No
    1 - Yes

service_interval
    Enable service interval based scheduling.
    0 - No
    1 - Yes

hird_threshold
    Value of BESL or HIRD Threshold.

activate_stm_fs_transceiver
    Activate internal transceiver using GGPIO
    register.
    0 - Deactivate the transceiver (default)
    1 - Activate the transceiver

ipg_isoc_en
    Indicates the IPG supports is enabled or disabled.
    0 - Disable (default)
    1 - Enable

max_packet_count
    The maximum number of packets in a transfer
    15 to 511
    Actual maximum value is autodetected and also
    the default.

max_transfer_size
    The maximum transfer size supported, in bytes
    2047 to 65,535
    Actual maximum value is autodetected and also
    the default.

ahbcfg
    This field allows the default value of the GAHBCFG
    register to be overridden
    -1         - GAHBCFG value will be set to 0x06
    (INCR, default)
    all others - GAHBCFG value will be overridden with
    this value
    Not all bits can be controlled like this, the
    bits defined by GAHBCFG_CTRL_MASK are controlled
    by the driver and are ignored in this
    configuration value.

ref_clk_per
    Indicates in terms of pico seconds the period
    of ref_clk.
    62500 - 16MHz
    58823 - 17MHz
    52083 - 19.2MHz
    50000 - 20MHz
    41666 - 24MHz
    33333 - 30MHz (default)
    25000 - 40MHz

sof_cnt_wkup_alert
    Indicates in term of number of SOF's after which
    the controller should generate an interrupt if the
    device had been in L1 state until that period.
    This is used by SW to initiate Remote WakeUp in the
    controller so as to sync to the uF number from the host.

host_dma
    Specifies whether to use slave or DMA mode for accessing
    the data FIFOs. The driver will automatically detect the
    value for this parameter if none is specified.
    0 - Slave (always available)
    1 - DMA (default, if available)

dma_desc_enable
    When DMA mode is enabled, specifies whether to use
    address DMA mode or descriptor DMA mode for accessing
    the data FIFOs. The driver will automatically detect the
    value for this if none is specified.
    0 - Address DMA
    1 - Descriptor DMA (default, if available)

dma_desc_fs_enable
    When DMA mode is enabled, specifies whether to use
    address DMA mode or descriptor DMA mode for accessing
    the data FIFOs in Full Speed mode only. The driver
    will automatically detect the value for this if none is
    specified.
    0 - Address DMA
    1 - Descriptor DMA in FS (default, if available)

host_support_fs_ls_low_power
    Specifies whether low power mode is supported
    when attached to a Full Speed or Low Speed device in
    host mode.
    0 - Don't support low power mode (default)
    1 - Support low power mode

host_ls_low_power_phy_clk
    Specifies the PHY clock rate in low power mode
    when connected to a Low Speed device in host
    mode. This parameter is applicable only if
    host_support_fs_ls_low_power is enabled.
    0 - 48 MHz
    (default when phy_type is UTMI+ or ULPI)
    1 - 6 MHz
    (default when phy_type is Full Speed)

oc_disable
    Flag to disable overcurrent condition.
    0 - Allow overcurrent condition to get detected
    1 - Disable overcurrent condtion to get detected

host_channels
    The number of host channel registers to use
    1 to 16
    Actual maximum value is autodetected and also
    the default.

host_rx_fifo_size
    Number of 4-byte words in the Rx FIFO in host mode when
    dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

host_nperio_tx_fifo_size
    Number of 4-byte words in the non-periodic Tx FIFO
    in host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

host_perio_tx_fifo_size
    Number of 4-byte words in the periodic Tx FIFO in
    host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

g_dma
    Enables gadget dma usage (default: autodetect).

g_dma_desc
    Enables gadget descriptor DMA (default: autodetect).

g_rx_fifo_size
    The periodic rx fifo size for the device, in
    DWORDS from 16-32768 (default: 2048 if
    possible, otherwise autodetect).

g_np_tx_fifo_size
    The non-periodic tx fifo size for the device in
    DWORDS from 16-32768 (default: 1024 if
    possible, otherwise autodetect).

g_tx_fifo_size
    An array of TX fifo sizes in dedicated fifo
    mode. Each value corresponds to one EP
    starting from EP1 (max 15 values). Sizes are
    in DWORDS with possible values from from
    16-32768 (default: 256, 256, 256, 256, 768,
    768, 768, 768, 0, 0, 0, 0, 0, 0, 0).

change_speed_quirk
    Change speed configuration to DWC2_SPEED_PARAM_FULL
    while full&low speed device connect. And change speed
    back to DWC2_SPEED_PARAM_HIGH while device is gone.
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

.. c:type:: struct dwc2_hw_params

    Autodetected parameters.

.. _`dwc2_hw_params.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hw_params {
        unsigned op_mode:3;
        unsigned arch:2;
        unsigned dma_desc_enable:1;
        unsigned enable_dynamic_fifo:1;
        unsigned en_multiple_tx_fifo:1;
        unsigned rx_fifo_size:16;
        unsigned host_nperio_tx_fifo_size:16;
        unsigned dev_nperio_tx_fifo_size:16;
        unsigned host_perio_tx_fifo_size:16;
        unsigned nperio_tx_q_depth:3;
        unsigned host_perio_tx_q_depth:3;
        unsigned dev_token_q_depth:5;
        unsigned max_transfer_size:26;
        unsigned max_packet_count:11;
        unsigned host_channels:5;
        unsigned hs_phy_type:2;
        unsigned fs_phy_type:2;
        unsigned i2c_enable:1;
        unsigned acg_enable:1;
        unsigned num_dev_ep:4;
        unsigned num_dev_in_eps : 4;
        unsigned num_dev_perio_in_ep:4;
        unsigned total_fifo_size:16;
        unsigned power_optimized:1;
        unsigned hibernation:1;
        unsigned utmi_phy_data_width:2;
        unsigned lpm_mode:1;
        unsigned ipg_isoc_en:1;
        unsigned service_interval_mode:1;
        u32 snpsid;
        u32 dev_ep_dirs;
        u32 g_tx_fifo_size[MAX_EPS_CHANNELS];
    }

.. _`dwc2_hw_params.members`:

Members
-------

op_mode
    Mode of Operation
    0 - HNP- and SRP-Capable OTG (Host & Device)
    1 - SRP-Capable OTG (Host & Device)
    2 - Non-HNP and Non-SRP Capable OTG (Host & Device)
    3 - SRP-Capable Device
    4 - Non-OTG Device
    5 - SRP-Capable Host
    6 - Non-OTG Host

arch
    Architecture
    0 - Slave only
    1 - External DMA
    2 - Internal DMA

dma_desc_enable
    When DMA mode is enabled, specifies whether to use
    address DMA mode or descriptor DMA mode for accessing
    the data FIFOs. The driver will automatically detect the
    value for this if none is specified.
    0 - Address DMA
    1 - Descriptor DMA (default, if available)

enable_dynamic_fifo
    0 - Use coreConsultant-specified FIFO size parameters
    1 - Allow dynamic FIFO sizing (default, if available)

en_multiple_tx_fifo
    Specifies whether dedicated per-endpoint transmit FIFOs
    are enabled for non-periodic IN endpoints in device
    mode.

rx_fifo_size
    Number of 4-byte words in the  Rx FIFO when dynamic
    FIFO sizing is enabled 16 to 32768
    Actual maximum value is autodetected and also
    the default.

host_nperio_tx_fifo_size
    Number of 4-byte words in the non-periodic Tx FIFO
    in host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

dev_nperio_tx_fifo_size
    Number of 4-byte words in the non-periodic Tx FIFO
    in device mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

host_perio_tx_fifo_size
    Number of 4-byte words in the periodic Tx FIFO in
    host mode when dynamic FIFO sizing is enabled
    16 to 32768
    Actual maximum value is autodetected and also
    the default.

nperio_tx_q_depth
    Non-Periodic Request Queue Depth
    2, 4 or 8

host_perio_tx_q_depth
    Host Mode Periodic Request Queue Depth
    2, 4 or 8

dev_token_q_depth
    Device Mode IN Token Sequence Learning Queue
    Depth
    0 to 30

max_transfer_size
    The maximum transfer size supported, in bytes
    2047 to 65,535
    Actual maximum value is autodetected and also
    the default.

max_packet_count
    The maximum number of packets in a transfer
    15 to 511
    Actual maximum value is autodetected and also
    the default.

host_channels
    The number of host channel registers to use
    1 to 16
    Actual maximum value is autodetected and also
    the default.

hs_phy_type
    High-speed PHY interface type
    0 - High-speed interface not supported
    1 - UTMI+
    2 - ULPI
    3 - UTMI+ and ULPI

fs_phy_type
    Full-speed PHY interface type
    0 - Full speed interface not supported
    1 - Dedicated full speed interface
    2 - FS pins shared with UTMI+ pins
    3 - FS pins shared with ULPI pins

i2c_enable
    Specifies whether to use the I2Cinterface for a full
    speed PHY. This parameter is only applicable if phy_type
    is FS.
    0 - No (default)
    1 - Yes

acg_enable
    For enabling Active Clock Gating in the controller
    0 - Disable
    1 - Enable

num_dev_ep
    Number of device endpoints available

num_dev_in_eps
    Number of device IN endpoints available

num_dev_perio_in_ep
    Number of device periodic IN endpoints
    available

total_fifo_size
    Total internal RAM for FIFOs (bytes)

power_optimized
    Are power optimizations enabled?

hibernation
    Is hibernation enabled?

utmi_phy_data_width
    UTMI+ PHY data width
    0 - 8 bits
    1 - 16 bits
    2 - 8 or 16 bits

lpm_mode
    For enabling Link Power Management in the controller
    0 - Disable
    1 - Enable

ipg_isoc_en
    This feature indicates that the controller supports
    the worst-case scenario of Rx followed by Rx
    Interpacket Gap (IPG) (32 bitTimes) as per the utmi
    specification for any token following ISOC OUT token.
    0 - Don't support
    1 - Support

service_interval_mode
    For enabling service interval based scheduling in the
    controller.
    0 - Disable
    1 - Enable

snpsid
    Value from SNPSID register

dev_ep_dirs
    Direction of device endpoints (GHWCFG1)

g_tx_fifo_size
    Power-on values of TxFIFO sizes

.. _`dwc2_hw_params.description`:

Description
-----------

These parameters are the various parameters read from hardware
registers during initialization. They typically contain the best
supported or maximum value that can be configured in the
corresponding dwc2_core_params value.

The values that are not in dwc2_core_params are documented below.

.. _`dwc2_gregs_backup`:

struct dwc2_gregs_backup
========================

.. c:type:: struct dwc2_gregs_backup

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
        u32 glpmcfg;
        u32 pcgcctl;
        u32 pcgcctl1;
        u32 gdfifocfg;
        u32 gpwrdn;
        bool valid;
    }

.. _`dwc2_gregs_backup.members`:

Members
-------

gotgctl
    Backup of GOTGCTL register

gintmsk
    Backup of GINTMSK register

gahbcfg
    Backup of GAHBCFG register

gusbcfg
    Backup of GUSBCFG register

grxfsiz
    Backup of GRXFSIZ register

gnptxfsiz
    Backup of GNPTXFSIZ register

gi2cctl
    Backup of GI2CCTL register

glpmcfg
    Backup of GLPMCFG register

pcgcctl
    Backup of PCGCCTL register

pcgcctl1
    Backup of PCGCCTL1 register

gdfifocfg
    Backup of GDFIFOCFG register

gpwrdn
    Backup of GPWRDN register

valid
    True if registers values backuped.

.. _`dwc2_dregs_backup`:

struct dwc2_dregs_backup
========================

.. c:type:: struct dwc2_dregs_backup

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
        u32 dtxfsiz[MAX_EPS_CHANNELS];
        bool valid;
    }

.. _`dwc2_dregs_backup.members`:

Members
-------

dcfg
    Backup of DCFG register

dctl
    Backup of DCTL register

daintmsk
    Backup of DAINTMSK register

diepmsk
    Backup of DIEPMSK register

doepmsk
    Backup of DOEPMSK register

diepctl
    Backup of DIEPCTL register

dieptsiz
    Backup of DIEPTSIZ register

diepdma
    Backup of DIEPDMA register

doepctl
    Backup of DOEPCTL register

doeptsiz
    Backup of DOEPTSIZ register

doepdma
    Backup of DOEPDMA register

dtxfsiz
    Backup of DTXFSIZ registers for each endpoint

valid
    True if registers values backuped.

.. _`dwc2_hregs_backup`:

struct dwc2_hregs_backup
========================

.. c:type:: struct dwc2_hregs_backup

    Holds host registers state before entering partial power down

.. _`dwc2_hregs_backup.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hregs_backup {
        u32 hcfg;
        u32 haintmsk;
        u32 hcintmsk[MAX_EPS_CHANNELS];
        u32 hprt0;
        u32 hfir;
        u32 hptxfsiz;
        bool valid;
    }

.. _`dwc2_hregs_backup.members`:

Members
-------

hcfg
    Backup of HCFG register

haintmsk
    Backup of HAINTMSK register

hcintmsk
    Backup of HCINTMSK register

hprt0
    Backup of HPTR0 register

hfir
    Backup of HFIR register

hptxfsiz
    Backup of HPTXFSIZ register

valid
    True if registers values backuped.

.. _`dwc2_hsotg`:

struct dwc2_hsotg
=================

.. c:type:: struct dwc2_hsotg

    Holds the state of the driver, including the non-periodic and periodic schedules

.. _`dwc2_hsotg.definition`:

Definition
----------

.. code-block:: c

    struct dwc2_hsotg {
        struct device *dev;
        void __iomem *regs;
        struct dwc2_hw_params hw_params;
        struct dwc2_core_params params;
        enum usb_otg_state op_state;
        enum usb_dr_mode dr_mode;
        unsigned int hcd_enabled:1;
        unsigned int gadget_enabled:1;
        unsigned int ll_hw_enabled:1;
        unsigned int hibernated:1;
        u16 frame_number;
        struct phy *phy;
        struct usb_phy *uphy;
        struct dwc2_hsotg_plat *plat;
        struct regulator_bulk_data supplies[DWC2_NUM_SUPPLIES];
        struct regulator *vbus_supply;
        u32 phyif;
        spinlock_t lock;
        void *priv;
        int irq;
        struct clk *clk;
        struct reset_control *reset;
        struct reset_control *reset_ecc;
        unsigned int queuing_high_bandwidth:1;
        unsigned int srp_success:1;
        struct workqueue_struct *wq_otg;
        struct work_struct wf_otg;
        struct timer_list wkp_timer;
        enum dwc2_lx_state lx_state;
        struct dwc2_gregs_backup gr_backup;
        struct dwc2_dregs_backup dr_backup;
        struct dwc2_hregs_backup hr_backup;
        struct dentry *debug_root;
        struct debugfs_regset32 *regset;
        bool needs_byte_swap;
    #define DWC2_CORE_REV_2_71a 0x4f54271a
    #define DWC2_CORE_REV_2_72a 0x4f54272a
    #define DWC2_CORE_REV_2_80a 0x4f54280a
    #define DWC2_CORE_REV_2_90a 0x4f54290a
    #define DWC2_CORE_REV_2_91a 0x4f54291a
    #define DWC2_CORE_REV_2_92a 0x4f54292a
    #define DWC2_CORE_REV_2_94a 0x4f54294a
    #define DWC2_CORE_REV_3_00a 0x4f54300a
    #define DWC2_CORE_REV_3_10a 0x4f54310a
    #define DWC2_CORE_REV_4_00a 0x4f54400a
    #define DWC2_FS_IOT_REV_1_00a 0x5531100a
    #define DWC2_HS_IOT_REV_1_00a 0x5532100a
    #define DWC2_OTG_ID 0x4f540000
    #define DWC2_FS_IOT_ID 0x55310000
    #define DWC2_HS_IOT_ID 0x55320000
    #if IS_ENABLED(CONFIG_USB_DWC2_HOST) || IS_ENABLED(CONFIG_USB_DWC2_DUAL_ROLE)
        union dwc2_hcd_internal_flags {
            u32 d32;
            struct {
                unsigned port_connect_status_change:1;
                unsigned port_connect_status:1;
                unsigned port_reset_change:1;
                unsigned port_enable_change:1;
                unsigned port_suspend_change:1;
                unsigned port_over_current_change:1;
                unsigned port_l1_change:1;
                unsigned reserved:25;
            } b;
        } flags;
        struct list_head non_periodic_sched_inactive;
        struct list_head non_periodic_sched_waiting;
        struct list_head non_periodic_sched_active;
        struct list_head *non_periodic_qh_ptr;
        struct list_head periodic_sched_inactive;
        struct list_head periodic_sched_ready;
        struct list_head periodic_sched_assigned;
        struct list_head periodic_sched_queued;
        struct list_head split_order;
        u16 periodic_usecs;
        unsigned long hs_periodic_bitmap[ DIV_ROUND_UP(DWC2_HS_SCHEDULE_US, BITS_PER_LONG)];
        u16 periodic_qh_count;
        bool bus_suspended;
        bool new_connection;
        u16 last_frame_num;
    #ifdef CONFIG_USB_DWC2_TRACK_MISSED_SOFS
    #define FRAME_NUM_ARRAY_SIZE 1000
        u16 *frame_num_array;
        u16 *last_frame_num_array;
        int frame_num_idx;
        int dumped_frame_num_array;
    #endif
        struct list_head free_hc_list;
        int periodic_channels;
        int non_periodic_channels;
        int available_host_channels;
        struct dwc2_host_chan *hc_ptr_array[MAX_EPS_CHANNELS];
        u8 *status_buf;
        dma_addr_t status_buf_dma;
    #define DWC2_HCD_STATUS_BUF_SIZE 64
        struct delayed_work start_work;
        struct delayed_work reset_work;
        u8 otg_port;
        u32 *frame_list;
        dma_addr_t frame_list_dma;
        u32 frame_list_sz;
        struct kmem_cache *desc_gen_cache;
        struct kmem_cache *desc_hsisoc_cache;
        struct kmem_cache *unaligned_cache;
    #define DWC2_KMEM_UNALIGNED_BUF_SIZE 1024
    #endif
    #if IS_ENABLED(CONFIG_USB_DWC2_PERIPHERAL) || \
        IS_ENABLED(CONFIG_USB_DWC2_DUAL_ROLE) struct usb_gadget_driver *driver;
        int fifo_mem;
        unsigned int dedicated_fifos:1;
        unsigned char num_of_eps;
        u32 fifo_map;
        struct usb_request *ep0_reply;
        struct usb_request *ctrl_req;
        void *ep0_buff;
        void *ctrl_buff;
        enum dwc2_ep0_state ep0_state;
        u8 test_mode;
        dma_addr_t setup_desc_dma[2];
        struct dwc2_dma_desc *setup_desc[2];
        dma_addr_t ctrl_in_desc_dma;
        struct dwc2_dma_desc *ctrl_in_desc;
        dma_addr_t ctrl_out_desc_dma;
        struct dwc2_dma_desc *ctrl_out_desc;
        struct usb_gadget gadget;
        unsigned int enabled:1;
        unsigned int connected:1;
        unsigned int remote_wakeup_allowed:1;
        struct dwc2_hsotg_ep *eps_in[MAX_EPS_CHANNELS];
        struct dwc2_hsotg_ep *eps_out[MAX_EPS_CHANNELS];
    #endif
    }

.. _`dwc2_hsotg.members`:

Members
-------

dev
    The struct device pointer

regs
    Pointer to controller regs

hw_params
    Parameters that were autodetected from the
    hardware registers

params
    Parameters that define how the core should be configured

op_state
    The operational State, during transitions (a_host=>
    a_peripheral and b_device=>b_host) this may not match
    the core, but allows the software to determine
    transitions

dr_mode
    Requested mode of operation, one of following:
    - USB_DR_MODE_PERIPHERAL
    - USB_DR_MODE_HOST
    - USB_DR_MODE_OTG

hcd_enabled
    Host mode sub-driver initialization indicator.

gadget_enabled
    Peripheral mode sub-driver initialization indicator.

ll_hw_enabled
    Status of low-level hardware resources.

hibernated
    True if core is hibernated

frame_number
    Frame number read from the core. For both device
    and host modes. The value ranges are from 0
    to HFNUM_MAX_FRNUM.

phy
    The otg phy transceiver structure for phy control.

uphy
    The otg phy transceiver structure for old USB phy
    control.

plat
    The platform specific configuration data. This can be
    removed once all SoCs support usb transceiver.

supplies
    Definition of USB power supplies

vbus_supply
    Regulator supplying vbus.

phyif
    PHY interface width

lock
    Spinlock that protects all the driver data structures

priv
    Stores a pointer to the struct usb_hcd

irq
    Interrupt request line number

clk
    Pointer to otg clock

reset
    Pointer to dwc2 reset controller

reset_ecc
    Pointer to dwc2 optional reset controller in Stratix10.

queuing_high_bandwidth
    True if multiple packets of a high-bandwidth
    transfer are in process of being queued

srp_success
    Stores status of SRP request in the case of a FS PHY
    with an I2C interface

wq_otg
    Workqueue object used for handling of some interrupts

wf_otg
    Work object for handling Connector ID Status Change
    interrupt

wkp_timer
    Timer object for handling Wakeup Detected interrupt

lx_state
    Lx state of connected device

gr_backup
    Backup of global registers during suspend

dr_backup
    Backup of device registers during suspend

hr_backup
    Backup of host registers during suspend

debug_root
    Root directrory for debugfs.

regset
    A pointer to a struct debugfs_regset32, which contains
    a pointer to an array of register definitions, the
    array size and the base address where the register bank
    is to be found.

needs_byte_swap
    Specifies whether the opposite endianness.

flags
    Flags for handling root port state changes

flags.d32
    Contain all root port flags

flags.b
    Separate root port flags from each other

flags.b.port_connect_status_change
    True if root port connect status
    changed

flags.b.port_connect_status
    True if device connected to root port

flags.b.port_reset_change
    True if root port reset status changed

flags.b.port_enable_change
    True if root port enable status changed

flags.b.port_suspend_change
    True if root port suspend status changed

flags.b.port_over_current_change
    True if root port over current state
    changed.

flags.b.port_l1_change
    True if root port l1 status changed

flags.b.reserved
    Reserved bits of root port register

non_periodic_sched_inactive
    Inactive QHs in the non-periodic schedule.
    Transfers associated with these QHs are not currently
    assigned to a host channel.

non_periodic_sched_waiting
    Waiting QHs in the non-periodic schedule.
    Transfers associated with these QHs are not currently
    assigned to a host channel.

non_periodic_sched_active
    Active QHs in the non-periodic schedule.
    Transfers associated with these QHs are currently
    assigned to a host channel.

non_periodic_qh_ptr
    Pointer to next QH to process in the active
    non-periodic schedule

periodic_sched_inactive
    Inactive QHs in the periodic schedule. This is a
    list of QHs for periodic transfers that are \_not_
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

periodic_sched_ready
    List of periodic QHs that are ready for execution in
    the next frame, but have not yet been assigned to host
    channels. Items move from this list to
    periodic_sched_assigned as host channels become
    available during the current frame.

periodic_sched_assigned
    List of periodic QHs to be executed in the next
    frame that are assigned to host channels. Items move
    from this list to periodic_sched_queued as the
    transactions for the QH are queued to the DWC_otg
    controller.

periodic_sched_queued
    List of periodic QHs that have been queued for
    execution. Items move from this list to either
    periodic_sched_inactive or periodic_sched_ready when the
    channel associated with the transfer is released. If the
    interval for the QH is 1, the item moves to
    periodic_sched_ready because it must be rescheduled for
    the next frame. Otherwise, the item moves to
    periodic_sched_inactive.

split_order
    List keeping track of channels doing splits, in order.

periodic_usecs
    Total bandwidth claimed so far for periodic transfers.
    This value is in microseconds per (micro)frame. The
    assumption is that all periodic transfers may occur in
    the same (micro)frame.

hs_periodic_bitmap
    Bitmap used by the microframe scheduler any time the
    host is in high speed mode; low speed schedules are
    stored elsewhere since we need one per TT.

periodic_qh_count
    Count of periodic QHs, if using several eps. Used for
    SOF enable/disable.

bus_suspended
    True if bus is suspended

new_connection
    Used in host mode. True if there are new connected
    device

last_frame_num
    Number of last frame. Range from 0 to  32768

frame_num_array
    Used only  if CONFIG_USB_DWC2_TRACK_MISSED_SOFS is
    defined, for missed SOFs tracking. Array holds that
    frame numbers, which not equal to last_frame_num +1

last_frame_num_array
    Used only  if CONFIG_USB_DWC2_TRACK_MISSED_SOFS is
    defined, for missed SOFs tracking.
    If current_frame_number != last_frame_num+1
    then last_frame_num added to this array

frame_num_idx
    Actual size of frame_num_array and last_frame_num_array

dumped_frame_num_array
    1 - if missed SOFs frame numbers dumbed
    0 - if missed SOFs frame numbers not dumbed

free_hc_list
    Free host channels in the controller. This is a list of
    struct dwc2_host_chan items.

periodic_channels
    Number of host channels assigned to periodic transfers.
    Currently assuming that there is a dedicated host
    channel for each periodic transaction and at least one
    host channel is available for non-periodic transactions.

non_periodic_channels
    Number of host channels assigned to non-periodic
    transfers

available_host_channels
    Number of host channels available for the
    microframe scheduler to use

hc_ptr_array
    Array of pointers to the host channel descriptors.
    Allows accessing a host channel descriptor given the
    host channel number. This is useful in interrupt
    handlers.

status_buf
    Buffer used for data received during the status phase of
    a control transfer.

status_buf_dma
    DMA address for status_buf

start_work
    Delayed work for handling host A-cable connection

reset_work
    Delayed work for handling a port reset

otg_port
    OTG port number

frame_list
    Frame list

frame_list_dma
    Frame list DMA address

frame_list_sz
    Frame list size

desc_gen_cache
    Kmem cache for generic descriptors

desc_hsisoc_cache
    Kmem cache for hs isochronous descriptors

unaligned_cache
    Kmem cache for DMA mode to handle non-aligned buf

driver
    USB gadget driver

fifo_mem
    Total internal RAM for FIFOs (bytes)

dedicated_fifos
    Set if the hardware has dedicated IN-EP fifos.

num_of_eps
    Number of available EPs (excluding EP0)

fifo_map
    Each bit intend for concrete fifo. If that bit is set,
    then that fifo is used

ep0_reply
    Request used for ep0 reply.

ctrl_req
    Request for EP0 control packets.

ep0_buff
    Buffer for EP0 reply data, if needed.

ctrl_buff
    Buffer for EP0 control requests.

ep0_state
    EP0 control transfers state

test_mode
    USB test mode requested by the host

setup_desc_dma
    EP0 setup stage desc chain DMA address

setup_desc
    EP0 setup stage desc chain pointer

ctrl_in_desc_dma
    EP0 IN data phase desc chain DMA address

ctrl_in_desc
    EP0 IN data phase desc chain pointer

ctrl_out_desc_dma
    EP0 OUT data phase desc chain DMA address

ctrl_out_desc
    EP0 OUT data phase desc chain pointer

gadget
    Represents a usb slave device

enabled
    Indicates the enabling state of controller

connected
    Used in slave mode. True if device connected with host

remote_wakeup_allowed
    True if device is allowed to wake-up host by
    remote-wakeup signalling

eps_in
    The IN endpoints being supplied to the gadget framework

eps_out
    The OUT endpoints being supplied to the gadget framework

.. This file was automatic generated / don't edit.


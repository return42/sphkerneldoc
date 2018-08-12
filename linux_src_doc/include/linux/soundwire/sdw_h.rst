.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soundwire/sdw.h

.. _`sdw_slave_status`:

enum sdw_slave_status
=====================

.. c:type:: enum sdw_slave_status

    Slave status

.. _`sdw_slave_status.definition`:

Definition
----------

.. code-block:: c

    enum sdw_slave_status {
        SDW_SLAVE_UNATTACHED,
        SDW_SLAVE_ATTACHED,
        SDW_SLAVE_ALERT,
        SDW_SLAVE_RESERVED
    };

.. _`sdw_slave_status.constants`:

Constants
---------

SDW_SLAVE_UNATTACHED
    Slave is not attached with the bus.

SDW_SLAVE_ATTACHED
    Slave is attached with bus.

SDW_SLAVE_ALERT
    Some alert condition on the Slave

SDW_SLAVE_RESERVED
    Reserved for future use

.. _`sdw_command_response`:

enum sdw_command_response
=========================

.. c:type:: enum sdw_command_response

    Command response as defined by SDW spec

.. _`sdw_command_response.definition`:

Definition
----------

.. code-block:: c

    enum sdw_command_response {
        SDW_CMD_OK,
        SDW_CMD_IGNORED,
        SDW_CMD_FAIL,
        SDW_CMD_TIMEOUT,
        SDW_CMD_FAIL_OTHER
    };

.. _`sdw_command_response.constants`:

Constants
---------

SDW_CMD_OK
    cmd was successful

SDW_CMD_IGNORED
    cmd was ignored

SDW_CMD_FAIL
    cmd was NACKed

SDW_CMD_TIMEOUT
    cmd timedout

SDW_CMD_FAIL_OTHER
    cmd failed due to other reason than above

.. _`sdw_command_response.note`:

NOTE
----

The enum is different than actual Spec as response in the Spec is
combination of ACK/NAK bits

SDW_CMD_TIMEOUT/FAIL_OTHER is defined for SW use, not in spec

.. _`sdw_stream_type`:

enum sdw_stream_type
====================

.. c:type:: enum sdw_stream_type

    data stream type

.. _`sdw_stream_type.definition`:

Definition
----------

.. code-block:: c

    enum sdw_stream_type {
        SDW_STREAM_PCM,
        SDW_STREAM_PDM
    };

.. _`sdw_stream_type.constants`:

Constants
---------

SDW_STREAM_PCM
    PCM data stream

SDW_STREAM_PDM
    PDM data stream

.. _`sdw_stream_type.description`:

Description
-----------

spec doesn't define this, but is used in implementation

.. _`sdw_data_direction`:

enum sdw_data_direction
=======================

.. c:type:: enum sdw_data_direction

    Data direction

.. _`sdw_data_direction.definition`:

Definition
----------

.. code-block:: c

    enum sdw_data_direction {
        SDW_DATA_DIR_RX,
        SDW_DATA_DIR_TX
    };

.. _`sdw_data_direction.constants`:

Constants
---------

SDW_DATA_DIR_RX
    Data into Port

SDW_DATA_DIR_TX
    Data out of Port

.. _`sdw_p15_behave`:

enum sdw_p15_behave
===================

.. c:type:: enum sdw_p15_behave

    Slave Port 15 behaviour when the Master attempts a read

.. _`sdw_p15_behave.definition`:

Definition
----------

.. code-block:: c

    enum sdw_p15_behave {
        SDW_P15_READ_IGNORED,
        SDW_P15_CMD_OK
    };

.. _`sdw_p15_behave.constants`:

Constants
---------

SDW_P15_READ_IGNORED
    Read is ignored

SDW_P15_CMD_OK
    Command is ok

.. _`sdw_dpn_type`:

enum sdw_dpn_type
=================

.. c:type:: enum sdw_dpn_type

    Data port types

.. _`sdw_dpn_type.definition`:

Definition
----------

.. code-block:: c

    enum sdw_dpn_type {
        SDW_DPN_FULL,
        SDW_DPN_SIMPLE,
        SDW_DPN_REDUCED
    };

.. _`sdw_dpn_type.constants`:

Constants
---------

SDW_DPN_FULL
    Full Data Port is supported

SDW_DPN_SIMPLE
    Simplified Data Port as defined in spec.
    DPN_SampleCtrl2, DPN_OffsetCtrl2, DPN_HCtrl and DPN_BlockCtrl3
    are not implemented.

SDW_DPN_REDUCED
    Reduced Data Port as defined in spec.
    DPN_SampleCtrl2, DPN_HCtrl are not implemented.

.. _`sdw_clk_stop_mode`:

enum sdw_clk_stop_mode
======================

.. c:type:: enum sdw_clk_stop_mode

    Clock Stop modes

.. _`sdw_clk_stop_mode.definition`:

Definition
----------

.. code-block:: c

    enum sdw_clk_stop_mode {
        SDW_CLK_STOP_MODE0,
        SDW_CLK_STOP_MODE1
    };

.. _`sdw_clk_stop_mode.constants`:

Constants
---------

SDW_CLK_STOP_MODE0
    Slave can continue operation seamlessly on clock
    restart

SDW_CLK_STOP_MODE1
    Slave may have entered a deeper power-saving mode,
    not capable of continuing operation seamlessly when the clock restarts

.. _`sdw_dp0_prop`:

struct sdw_dp0_prop
===================

.. c:type:: struct sdw_dp0_prop

    DP0 properties

.. _`sdw_dp0_prop.definition`:

Definition
----------

.. code-block:: c

    struct sdw_dp0_prop {
        u32 max_word;
        u32 min_word;
        u32 num_words;
        u32 *words;
        bool flow_controlled;
        bool simple_ch_prep_sm;
        bool device_interrupts;
    }

.. _`sdw_dp0_prop.members`:

Members
-------

max_word
    Maximum number of bits in a Payload Channel Sample, 1 to 64
    (inclusive)

min_word
    Minimum number of bits in a Payload Channel Sample, 1 to 64
    (inclusive)

num_words
    number of wordlengths supported

words
    wordlengths supported

flow_controlled
    Slave implementation results in an OK_NotReady
    response

simple_ch_prep_sm
    If channel prepare sequence is required

device_interrupts
    If implementation-defined interrupts are supported

.. _`sdw_dp0_prop.description`:

Description
-----------

The wordlengths are specified by Spec as max, min AND number of
discrete values, implementation can define based on the wordlengths they
support

.. _`sdw_dpn_audio_mode`:

struct sdw_dpn_audio_mode
=========================

.. c:type:: struct sdw_dpn_audio_mode

    Audio mode properties for DPn

.. _`sdw_dpn_audio_mode.definition`:

Definition
----------

.. code-block:: c

    struct sdw_dpn_audio_mode {
        u32 bus_min_freq;
        u32 bus_max_freq;
        u32 bus_num_freq;
        u32 *bus_freq;
        u32 max_freq;
        u32 min_freq;
        u32 num_freq;
        u32 *freq;
        u32 prep_ch_behave;
        u32 glitchless;
    }

.. _`sdw_dpn_audio_mode.members`:

Members
-------

bus_min_freq
    Minimum bus frequency, in Hz

bus_max_freq
    Maximum bus frequency, in Hz

bus_num_freq
    Number of discrete frequencies supported

bus_freq
    Discrete bus frequencies, in Hz

max_freq
    Maximum sampling bus frequency, in Hz

min_freq
    Minimum sampling frequency, in Hz

num_freq
    Number of discrete sampling frequency supported

freq
    Discrete sampling frequencies, in Hz

prep_ch_behave
    Specifies the dependencies between Channel Prepare
    sequence and bus clock configuration
    If 0, Channel Prepare can happen at any Bus clock rate
    If 1, Channel Prepare sequence shall happen only after Bus clock is
    changed to a frequency supported by this mode or compatible modes
    described by the next field

glitchless
    Bitmap describing possible glitchless transitions from this
    Audio Mode to other Audio Modes

.. _`sdw_dpn_prop`:

struct sdw_dpn_prop
===================

.. c:type:: struct sdw_dpn_prop

    Data Port DPn properties

.. _`sdw_dpn_prop.definition`:

Definition
----------

.. code-block:: c

    struct sdw_dpn_prop {
        u32 num;
        u32 max_word;
        u32 min_word;
        u32 num_words;
        u32 *words;
        enum sdw_dpn_type type;
        u32 max_grouping;
        bool simple_ch_prep_sm;
        u32 ch_prep_timeout;
        u32 device_interrupts;
        u32 max_ch;
        u32 min_ch;
        u32 num_ch;
        u32 *ch;
        u32 num_ch_combinations;
        u32 *ch_combinations;
        u32 modes;
        u32 max_async_buffer;
        bool block_pack_mode;
        u32 port_encoding;
        struct sdw_dpn_audio_mode *audio_modes;
    }

.. _`sdw_dpn_prop.members`:

Members
-------

num
    port number

max_word
    Maximum number of bits in a Payload Channel Sample, 1 to 64
    (inclusive)

min_word
    Minimum number of bits in a Payload Channel Sample, 1 to 64
    (inclusive)

num_words
    Number of discrete supported wordlengths

words
    Discrete supported wordlength

type
    Data port type. Full, Simplified or Reduced

max_grouping
    Maximum number of samples that can be grouped together for
    a full data port

simple_ch_prep_sm
    If the port supports simplified channel prepare state
    machine

ch_prep_timeout
    Port-specific timeout value, in milliseconds

device_interrupts
    If set, each bit corresponds to support for
    implementation-defined interrupts

max_ch
    Maximum channels supported

min_ch
    Minimum channels supported

num_ch
    Number of discrete channels supported

ch
    Discrete channels supported

num_ch_combinations
    Number of channel combinations supported

ch_combinations
    Channel combinations supported

modes
    SDW mode supported

max_async_buffer
    Number of samples that this port can buffer in
    asynchronous modes

block_pack_mode
    Type of block port mode supported

port_encoding
    Payload Channel Sample encoding schemes supported

audio_modes
    Audio modes supported

.. _`sdw_slave_prop`:

struct sdw_slave_prop
=====================

.. c:type:: struct sdw_slave_prop

    SoundWire Slave properties

.. _`sdw_slave_prop.definition`:

Definition
----------

.. code-block:: c

    struct sdw_slave_prop {
        u32 mipi_revision;
        bool wake_capable;
        bool test_mode_capable;
        bool clk_stop_mode1;
        bool simple_clk_stop_capable;
        u32 clk_stop_timeout;
        u32 ch_prep_timeout;
        enum sdw_clk_stop_reset_behave reset_behave;
        bool high_PHY_capable;
        bool paging_support;
        bool bank_delay_support;
        enum sdw_p15_behave p15_behave;
        bool lane_control_support;
        u32 master_count;
        u32 source_ports;
        u32 sink_ports;
        struct sdw_dp0_prop *dp0_prop;
        struct sdw_dpn_prop *src_dpn_prop;
        struct sdw_dpn_prop *sink_dpn_prop;
    }

.. _`sdw_slave_prop.members`:

Members
-------

mipi_revision
    Spec version of the implementation

wake_capable
    Wake-up events are supported

test_mode_capable
    If test mode is supported

clk_stop_mode1
    Clock-Stop Mode 1 is supported

simple_clk_stop_capable
    Simple clock mode is supported

clk_stop_timeout
    Worst-case latency of the Clock Stop Prepare State
    Machine transitions, in milliseconds

ch_prep_timeout
    Worst-case latency of the Channel Prepare State Machine
    transitions, in milliseconds

reset_behave
    Slave keeps the status of the SlaveStopClockPrepare
    state machine (P=1 SCSP_SM) after exit from clock-stop mode1

high_PHY_capable
    Slave is HighPHY capable

paging_support
    Slave implements paging registers SCP_AddrPage1 and
    SCP_AddrPage2

bank_delay_support
    Slave implements bank delay/bridge support registers
    SCP_BankDelay and SCP_NextFrame

p15_behave
    Slave behavior when the Master attempts a read to the Port15
    alias

lane_control_support
    Slave supports lane control

master_count
    Number of Masters present on this Slave

source_ports
    Bitmap identifying source ports

sink_ports
    Bitmap identifying sink ports

dp0_prop
    Data Port 0 properties

src_dpn_prop
    Source Data Port N properties

sink_dpn_prop
    Sink Data Port N properties

.. _`sdw_master_prop`:

struct sdw_master_prop
======================

.. c:type:: struct sdw_master_prop

    Master properties

.. _`sdw_master_prop.definition`:

Definition
----------

.. code-block:: c

    struct sdw_master_prop {
        u32 revision;
        u32 master_count;
        enum sdw_clk_stop_mode clk_stop_mode;
        u32 max_freq;
        u32 num_clk_gears;
        u32 *clk_gears;
        u32 num_freq;
        u32 *freq;
        u32 default_frame_rate;
        u32 default_row;
        u32 default_col;
        bool dynamic_frame;
        u32 err_threshold;
        struct sdw_dpn_prop *dpn_prop;
    }

.. _`sdw_master_prop.members`:

Members
-------

revision
    MIPI spec version of the implementation

master_count
    Number of masters

clk_stop_mode
    Bitmap for Clock Stop modes supported

max_freq
    Maximum Bus clock frequency, in Hz

num_clk_gears
    Number of clock gears supported

clk_gears
    Clock gears supported

num_freq
    Number of clock frequencies supported, in Hz

freq
    Clock frequencies supported, in Hz

default_frame_rate
    Controller default Frame rate, in Hz

default_row
    Number of rows

default_col
    Number of columns

dynamic_frame
    Dynamic frame supported

err_threshold
    Number of times that software may retry sending a single
    command

dpn_prop
    Data Port N properties

.. _`sdw_slave_id`:

struct sdw_slave_id
===================

.. c:type:: struct sdw_slave_id

    Slave ID

.. _`sdw_slave_id.definition`:

Definition
----------

.. code-block:: c

    struct sdw_slave_id {
        __u16 mfg_id;
        __u16 part_id;
        __u8 class_id;
        __u8 unique_id:4;
        __u8 sdw_version:4;
    }

.. _`sdw_slave_id.members`:

Members
-------

mfg_id
    MIPI Manufacturer ID

part_id
    Device Part ID

class_id
    MIPI Class ID, unused now.
    Currently a placeholder in MIPI SoundWire Spec

unique_id
    Device unique ID

sdw_version
    SDW version implemented

.. _`sdw_slave_id.description`:

Description
-----------

The order of the IDs here does not follow the DisCo spec definitions

.. _`sdw_slave_intr_status`:

struct sdw_slave_intr_status
============================

.. c:type:: struct sdw_slave_intr_status

    Slave interrupt status

.. _`sdw_slave_intr_status.definition`:

Definition
----------

.. code-block:: c

    struct sdw_slave_intr_status {
        u8 control_port;
        u8 port[15];
    }

.. _`sdw_slave_intr_status.members`:

Members
-------

control_port
    control port status

port
    data port status

.. _`sdw_bus_conf`:

struct sdw_bus_conf
===================

.. c:type:: struct sdw_bus_conf

    Bus configuration

.. _`sdw_bus_conf.definition`:

Definition
----------

.. code-block:: c

    struct sdw_bus_conf {
        unsigned int clk_freq;
        unsigned int num_rows;
        unsigned int num_cols;
        unsigned int bank;
    }

.. _`sdw_bus_conf.members`:

Members
-------

clk_freq
    Clock frequency, in Hz

num_rows
    Number of rows in frame

num_cols
    Number of columns in frame

bank
    Next register bank

.. _`sdw_prepare_ch`:

struct sdw_prepare_ch
=====================

.. c:type:: struct sdw_prepare_ch

    Prepare/De-prepare Data Port channel

.. _`sdw_prepare_ch.definition`:

Definition
----------

.. code-block:: c

    struct sdw_prepare_ch {
        unsigned int num;
        unsigned int ch_mask;
        bool prepare;
        unsigned int bank;
    }

.. _`sdw_prepare_ch.members`:

Members
-------

num
    Port number

ch_mask
    Active channel mask

prepare
    Prepare (true) /de-prepare (false) channel

bank
    Register bank, which bank Slave/Master driver should program for
    implementation defined registers. This is always updated to next_bank
    value read from bus params.

.. _`sdw_port_prep_ops`:

enum sdw_port_prep_ops
======================

.. c:type:: enum sdw_port_prep_ops

    Prepare operations for Data Port

.. _`sdw_port_prep_ops.definition`:

Definition
----------

.. code-block:: c

    enum sdw_port_prep_ops {
        SDW_OPS_PORT_PRE_PREP,
        SDW_OPS_PORT_PREP,
        SDW_OPS_PORT_POST_PREP
    };

.. _`sdw_port_prep_ops.constants`:

Constants
---------

SDW_OPS_PORT_PRE_PREP
    Pre prepare operation for the Port

SDW_OPS_PORT_PREP
    Prepare operation for the Port

SDW_OPS_PORT_POST_PREP
    Post prepare operation for the Port

.. _`sdw_bus_params`:

struct sdw_bus_params
=====================

.. c:type:: struct sdw_bus_params

    Structure holding bus configuration

.. _`sdw_bus_params.definition`:

Definition
----------

.. code-block:: c

    struct sdw_bus_params {
        enum sdw_reg_bank curr_bank;
        enum sdw_reg_bank next_bank;
        unsigned int max_dr_freq;
        unsigned int curr_dr_freq;
        unsigned int bandwidth;
        unsigned int col;
        unsigned int row;
    }

.. _`sdw_bus_params.members`:

Members
-------

curr_bank
    Current bank in use (BANK0/BANK1)

next_bank
    Next bank to use (BANK0/BANK1). next_bank will always be
    set to !curr_bank

max_dr_freq
    Maximum double rate clock frequency supported, in Hz

curr_dr_freq
    Current double rate clock frequency, in Hz

bandwidth
    Current bandwidth

col
    Active columns

row
    Active rows

.. _`sdw_slave_ops`:

struct sdw_slave_ops
====================

.. c:type:: struct sdw_slave_ops

    Slave driver callback ops

.. _`sdw_slave_ops.definition`:

Definition
----------

.. code-block:: c

    struct sdw_slave_ops {
        int (*read_prop)(struct sdw_slave *sdw);
        int (*interrupt_callback)(struct sdw_slave *slave, struct sdw_slave_intr_status *status);
        int (*update_status)(struct sdw_slave *slave, enum sdw_slave_status status);
        int (*bus_config)(struct sdw_slave *slave, struct sdw_bus_params *params);
        int (*port_prep)(struct sdw_slave *slave,struct sdw_prepare_ch *prepare_ch, enum sdw_port_prep_ops pre_ops);
    }

.. _`sdw_slave_ops.members`:

Members
-------

read_prop
    Read Slave properties

interrupt_callback
    Device interrupt notification (invoked in thread
    context)

update_status
    Update Slave status

bus_config
    Update the bus config for Slave

port_prep
    Prepare the port with parameters

.. _`sdw_slave`:

struct sdw_slave
================

.. c:type:: struct sdw_slave

    SoundWire Slave

.. _`sdw_slave.definition`:

Definition
----------

.. code-block:: c

    struct sdw_slave {
        struct sdw_slave_id id;
        struct device dev;
        enum sdw_slave_status status;
        struct sdw_bus *bus;
        const struct sdw_slave_ops *ops;
        struct sdw_slave_prop prop;
        struct list_head node;
        struct completion *port_ready;
        u16 dev_num;
    }

.. _`sdw_slave.members`:

Members
-------

id
    MIPI device ID

dev
    Linux device

status
    Status reported by the Slave

bus
    Bus handle

ops
    Slave callback ops

prop
    Slave properties

node
    node for bus list

port_ready
    Port ready completion flag for each Slave port

dev_num
    Device Number assigned by Bus

.. _`sdw_port_params`:

struct sdw_port_params
======================

.. c:type:: struct sdw_port_params

    Data Port parameters

.. _`sdw_port_params.definition`:

Definition
----------

.. code-block:: c

    struct sdw_port_params {
        unsigned int num;
        unsigned int bps;
        unsigned int flow_mode;
        unsigned int data_mode;
    }

.. _`sdw_port_params.members`:

Members
-------

num
    Port number

bps
    Word length of the Port

flow_mode
    Port Data flow mode

data_mode
    Test modes or normal mode

.. _`sdw_port_params.description`:

Description
-----------

This is used to program the Data Port based on Data Port stream
parameters.

.. _`sdw_transport_params`:

struct sdw_transport_params
===========================

.. c:type:: struct sdw_transport_params

    Data Port Transport Parameters

.. _`sdw_transport_params.definition`:

Definition
----------

.. code-block:: c

    struct sdw_transport_params {
        bool blk_grp_ctrl_valid;
        unsigned int port_num;
        unsigned int blk_grp_ctrl;
        unsigned int sample_interval;
        unsigned int offset1;
        unsigned int offset2;
        unsigned int hstart;
        unsigned int hstop;
        unsigned int blk_pkg_mode;
        unsigned int lane_ctrl;
    }

.. _`sdw_transport_params.members`:

Members
-------

blk_grp_ctrl_valid
    Port implements block group control

port_num
    *undescribed*

blk_grp_ctrl
    Block group control value

sample_interval
    Sample interval

offset1
    Blockoffset of the payload data

offset2
    Blockoffset of the payload data

hstart
    Horizontal start of the payload data

hstop
    Horizontal stop of the payload data

blk_pkg_mode
    Block per channel or block per port

lane_ctrl
    Data lane Port uses for Data transfer. Currently only single
    data lane is supported in bus

.. _`sdw_transport_params.description`:

Description
-----------

This is used to program the Data Port based on Data Port transport
parameters. All these parameters are banked and can be modified
during a bank switch without any artifacts in audio stream.

.. _`sdw_enable_ch`:

struct sdw_enable_ch
====================

.. c:type:: struct sdw_enable_ch

    Enable/disable Data Port channel

.. _`sdw_enable_ch.definition`:

Definition
----------

.. code-block:: c

    struct sdw_enable_ch {
        unsigned int port_num;
        unsigned int ch_mask;
        bool enable;
    }

.. _`sdw_enable_ch.members`:

Members
-------

port_num
    *undescribed*

ch_mask
    Active channel mask

enable
    Enable (true) /disable (false) channel

.. _`sdw_master_port_ops`:

struct sdw_master_port_ops
==========================

.. c:type:: struct sdw_master_port_ops

    Callback functions from bus to Master driver to set Master Data ports.

.. _`sdw_master_port_ops.definition`:

Definition
----------

.. code-block:: c

    struct sdw_master_port_ops {
        int (*dpn_set_port_params)(struct sdw_bus *bus,struct sdw_port_params *port_params, unsigned int bank);
        int (*dpn_set_port_transport_params)(struct sdw_bus *bus,struct sdw_transport_params *transport_params, enum sdw_reg_bank bank);
        int (*dpn_port_prep)(struct sdw_bus *bus, struct sdw_prepare_ch *prepare_ch);
        int (*dpn_port_enable_ch)(struct sdw_bus *bus, struct sdw_enable_ch *enable_ch, unsigned int bank);
    }

.. _`sdw_master_port_ops.members`:

Members
-------

dpn_set_port_params
    Set the Port parameters for the Master Port.
    Mandatory callback

dpn_set_port_transport_params
    Set transport parameters for the Master
    Port. Mandatory callback

dpn_port_prep
    Port prepare operations for the Master Data Port.

dpn_port_enable_ch
    Enable the channels of Master Port.

.. _`sdw_defer`:

struct sdw_defer
================

.. c:type:: struct sdw_defer

    SDW deffered message

.. _`sdw_defer.definition`:

Definition
----------

.. code-block:: c

    struct sdw_defer {
        int length;
        struct completion complete;
        struct sdw_msg *msg;
    }

.. _`sdw_defer.members`:

Members
-------

length
    message length

complete
    message completion

msg
    SDW message

.. _`sdw_master_ops`:

struct sdw_master_ops
=====================

.. c:type:: struct sdw_master_ops

    Master driver ops

.. _`sdw_master_ops.definition`:

Definition
----------

.. code-block:: c

    struct sdw_master_ops {
        int (*read_prop)(struct sdw_bus *bus);
        enum sdw_command_response (*xfer_msg) (struct sdw_bus *bus, struct sdw_msg *msg);
        enum sdw_command_response (*xfer_msg_defer)(struct sdw_bus *bus, struct sdw_msg *msg, struct sdw_defer *defer);
        enum sdw_command_response (*reset_page_addr) (struct sdw_bus *bus, unsigned int dev_num);
        int (*set_bus_conf)(struct sdw_bus *bus, struct sdw_bus_params *params);
        int (*pre_bank_switch)(struct sdw_bus *bus);
        int (*post_bank_switch)(struct sdw_bus *bus);
    }

.. _`sdw_master_ops.members`:

Members
-------

read_prop
    Read Master properties

xfer_msg
    Transfer message callback

xfer_msg_defer
    Defer version of transfer message callback

reset_page_addr
    Reset the SCP page address registers

set_bus_conf
    Set the bus configuration

pre_bank_switch
    Callback for pre bank switch

post_bank_switch
    Callback for post bank switch

.. _`sdw_bus`:

struct sdw_bus
==============

.. c:type:: struct sdw_bus

    SoundWire bus

.. _`sdw_bus.definition`:

Definition
----------

.. code-block:: c

    struct sdw_bus {
        struct device *dev;
        unsigned int link_id;
        struct list_head slaves;
        DECLARE_BITMAP(assigned, SDW_MAX_DEVICES);
        struct mutex bus_lock;
        struct mutex msg_lock;
        const struct sdw_master_ops *ops;
        const struct sdw_master_port_ops *port_ops;
        struct sdw_bus_params params;
        struct sdw_master_prop prop;
        struct list_head m_rt_list;
        struct sdw_defer defer_msg;
        unsigned int clk_stop_timeout;
        u32 bank_switch_timeout;
    }

.. _`sdw_bus.members`:

Members
-------

dev
    Master linux device

link_id
    Link id number, can be 0 to N, unique for each Master

slaves
    list of Slaves on this bus

assigned
    Bitmap for Slave device numbers.
    Bit set implies used number, bit clear implies unused number.

bus_lock
    bus lock

msg_lock
    message lock

ops
    Master callback ops

port_ops
    Master port callback ops

params
    Current bus parameters

prop
    Master properties

m_rt_list
    List of Master instance of all stream(s) running on Bus. This
    is used to compute and program bus bandwidth, clock, frame shape,
    transport and port parameters

defer_msg
    Defer message

clk_stop_timeout
    Clock stop timeout computed

bank_switch_timeout
    Bank switch timeout computed

.. This file was automatic generated / don't edit.


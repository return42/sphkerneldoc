.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/slimbus/slimbus.h

.. _`slim_framer`:

struct slim_framer
==================

.. c:type:: struct slim_framer

    Represents SLIMbus framer. Every controller may have multiple framers. There is 1 active framer device responsible for clocking the bus. Manager is responsible for framer hand-over.

.. _`slim_framer.definition`:

Definition
----------

.. code-block:: c

    struct slim_framer {
        struct device dev;
        struct slim_eaddr e_addr;
        int rootfreq;
        int superfreq;
    }

.. _`slim_framer.members`:

Members
-------

dev
    Driver model representation of the device.

e_addr
    Enumeration address of the framer.

rootfreq
    Root Frequency at which the framer can run. This is maximum
    frequency ('clock gear 10') at which the bus can operate.

superfreq
    Superframes per root frequency. Every frame is 6144 bits.

.. _`slim_msg_txn`:

struct slim_msg_txn
===================

.. c:type:: struct slim_msg_txn

    Message to be sent by the controller. This structure has packet header, payload and buffer to be filled (if any)

.. _`slim_msg_txn.definition`:

Definition
----------

.. code-block:: c

    struct slim_msg_txn {
        u8 rl;
        u8 mt;
        u8 mc;
        u8 dt;
        u16 ec;
        u8 tid;
        u8 la;
        struct slim_val_inf *msg;
        struct completion *comp;
    }

.. _`slim_msg_txn.members`:

Members
-------

rl
    Header field. remaining length.

mt
    Header field. Message type.

mc
    Header field. LSB is message code for type mt.

dt
    Header field. Destination type.

ec
    Element code. Used for elemental access APIs.

tid
    Transaction ID. Used for messages expecting response.
    (relevant for message-codes involving read operation)

la
    Logical address of the device this message is going to.
    (Not used when destination type is broadcast.)

msg
    Elemental access message to be read/written

comp
    completion if read/write is synchronous, used internally
    for tid based transactions.

.. _`slim_clk_state`:

enum slim_clk_state
===================

.. c:type:: enum slim_clk_state

    SLIMbus controller's clock state used internally for maintaining current clock state.

.. _`slim_clk_state.definition`:

Definition
----------

.. code-block:: c

    enum slim_clk_state {
        SLIM_CLK_ACTIVE,
        SLIM_CLK_ENTERING_PAUSE,
        SLIM_CLK_PAUSED
    };

.. _`slim_clk_state.constants`:

Constants
---------

SLIM_CLK_ACTIVE
    SLIMbus clock is active

SLIM_CLK_ENTERING_PAUSE
    SLIMbus clock pause sequence is being sent on the
    bus. If this succeeds, state changes to SLIM_CLK_PAUSED. If the
    transition fails, state changes back to SLIM_CLK_ACTIVE

SLIM_CLK_PAUSED
    SLIMbus controller clock has paused.

.. _`slim_sched`:

struct slim_sched
=================

.. c:type:: struct slim_sched

    Framework uses this structure internally for scheduling.

.. _`slim_sched.definition`:

Definition
----------

.. code-block:: c

    struct slim_sched {
        enum slim_clk_state clk_state;
        struct completion pause_comp;
        struct mutex m_reconf;
    }

.. _`slim_sched.members`:

Members
-------

clk_state
    Controller's clock state from enum slim_clk_state

pause_comp
    Signals completion of clock pause sequence. This is useful when
    client tries to call SLIMbus transaction when controller is entering
    clock pause.

m_reconf
    This mutex is held until current reconfiguration (data channel
    scheduling, message bandwidth reservation) is done. Message APIs can
    use the bus concurrently when this mutex is held since elemental access
    messages can be sent on the bus when reconfiguration is in progress.

.. _`slim_port_direction`:

enum slim_port_direction
========================

.. c:type:: enum slim_port_direction

    SLIMbus port direction

.. _`slim_port_direction.definition`:

Definition
----------

.. code-block:: c

    enum slim_port_direction {
        SLIM_PORT_SINK,
        SLIM_PORT_SOURCE
    };

.. _`slim_port_direction.constants`:

Constants
---------

SLIM_PORT_SINK
    SLIMbus port is a sink

SLIM_PORT_SOURCE
    SLIMbus port is a source

.. _`slim_port_state`:

enum slim_port_state
====================

.. c:type:: enum slim_port_state

    SLIMbus Port/Endpoint state machine according to SLIMbus Spec 2.0

.. _`slim_port_state.definition`:

Definition
----------

.. code-block:: c

    enum slim_port_state {
        SLIM_PORT_DISCONNECTED,
        SLIM_PORT_UNCONFIGURED,
        SLIM_PORT_CONFIGURED
    };

.. _`slim_port_state.constants`:

Constants
---------

SLIM_PORT_DISCONNECTED
    SLIMbus port is disconnected
    entered from Unconfigure/configured state after
    DISCONNECT_PORT or REMOVE_CHANNEL core command

SLIM_PORT_UNCONFIGURED
    SLIMbus port is in unconfigured state.
    entered from disconnect state after CONNECT_SOURCE/SINK core command

SLIM_PORT_CONFIGURED
    SLIMbus port is in configured state.
    entered from unconfigured state after DEFINE_CHANNEL, DEFINE_CONTENT
    and ACTIVATE_CHANNEL core commands. Ready for data transmission.

.. _`slim_channel_state`:

enum slim_channel_state
=======================

.. c:type:: enum slim_channel_state

    SLIMbus channel state machine used by core.

.. _`slim_channel_state.definition`:

Definition
----------

.. code-block:: c

    enum slim_channel_state {
        SLIM_CH_STATE_DISCONNECTED,
        SLIM_CH_STATE_ALLOCATED,
        SLIM_CH_STATE_ASSOCIATED,
        SLIM_CH_STATE_DEFINED,
        SLIM_CH_STATE_CONTENT_DEFINED,
        SLIM_CH_STATE_ACTIVE,
        SLIM_CH_STATE_REMOVED
    };

.. _`slim_channel_state.constants`:

Constants
---------

SLIM_CH_STATE_DISCONNECTED
    SLIMbus channel is disconnected

SLIM_CH_STATE_ALLOCATED
    SLIMbus channel is allocated

SLIM_CH_STATE_ASSOCIATED
    SLIMbus channel is associated with port

SLIM_CH_STATE_DEFINED
    SLIMbus channel parameters are defined

SLIM_CH_STATE_CONTENT_DEFINED
    SLIMbus channel content is defined

SLIM_CH_STATE_ACTIVE
    SLIMbus channel is active and ready for data

SLIM_CH_STATE_REMOVED
    SLIMbus channel is inactive and removed

.. _`slim_ch_data_fmt`:

enum slim_ch_data_fmt
=====================

.. c:type:: enum slim_ch_data_fmt

    SLIMbus channel data Type identifiers according to Table 60 of SLIMbus Spec 1.01.01

.. _`slim_ch_data_fmt.definition`:

Definition
----------

.. code-block:: c

    enum slim_ch_data_fmt {
        SLIM_CH_DATA_FMT_NOT_DEFINED,
        SLIM_CH_DATA_FMT_LPCM_AUDIO,
        SLIM_CH_DATA_FMT_IEC61937_COMP_AUDIO,
        SLIM_CH_DATA_FMT_PACKED_PDM_AUDIO
    };

.. _`slim_ch_data_fmt.constants`:

Constants
---------

SLIM_CH_DATA_FMT_NOT_DEFINED
    Undefined

SLIM_CH_DATA_FMT_LPCM_AUDIO
    LPCM audio

SLIM_CH_DATA_FMT_IEC61937_COMP_AUDIO
    IEC61937 Compressed audio

SLIM_CH_DATA_FMT_PACKED_PDM_AUDIO
    Packed PDM audio

.. _`slim_ch_aux_bit_fmt`:

enum slim_ch_aux_bit_fmt
========================

.. c:type:: enum slim_ch_aux_bit_fmt

    SLIMbus channel Aux Field format IDs according to Table 63 of SLIMbus Spec 2.0

.. _`slim_ch_aux_bit_fmt.definition`:

Definition
----------

.. code-block:: c

    enum slim_ch_aux_bit_fmt {
        SLIM_CH_AUX_FMT_NOT_APPLICABLE,
        SLIM_CH_AUX_FMT_ZCUV_TUNNEL_IEC60958,
        SLIM_CH_AUX_FMT_USER_DEFINED
    };

.. _`slim_ch_aux_bit_fmt.constants`:

Constants
---------

SLIM_CH_AUX_FMT_NOT_APPLICABLE
    Undefined

SLIM_CH_AUX_FMT_ZCUV_TUNNEL_IEC60958
    ZCUV for tunneling IEC60958

SLIM_CH_AUX_FMT_USER_DEFINED
    User defined

.. _`slim_channel`:

struct slim_channel
===================

.. c:type:: struct slim_channel

    SLIMbus channel, used for state machine

.. _`slim_channel.definition`:

Definition
----------

.. code-block:: c

    struct slim_channel {
        int id;
        int prrate;
        int seg_dist;
        enum slim_ch_data_fmt data_fmt;
        enum slim_ch_aux_bit_fmt aux_fmt;
        enum slim_channel_state state;
    }

.. _`slim_channel.members`:

Members
-------

id
    ID of channel

prrate
    Presense rate of channel from Table 66 of SLIMbus 2.0 Specs

seg_dist
    segment distribution code from Table 20 of SLIMbus 2.0 Specs

data_fmt
    Data format of channel.

aux_fmt
    Aux format for this channel.

state
    channel state machine

.. _`slim_port`:

struct slim_port
================

.. c:type:: struct slim_port

    SLIMbus port

.. _`slim_port.definition`:

Definition
----------

.. code-block:: c

    struct slim_port {
        int id;
        enum slim_port_direction direction;
        enum slim_port_state state;
        struct slim_channel ch;
    }

.. _`slim_port.members`:

Members
-------

id
    Port id

direction
    Port direction, Source or Sink.

state
    state machine of port.

ch
    channel associated with this port.

.. _`slim_transport_protocol`:

enum slim_transport_protocol
============================

.. c:type:: enum slim_transport_protocol

    SLIMbus Transport protocol list from Table 47 of SLIMbus 2.0 specs.

.. _`slim_transport_protocol.definition`:

Definition
----------

.. code-block:: c

    enum slim_transport_protocol {
        SLIM_PROTO_ISO,
        SLIM_PROTO_PUSH,
        SLIM_PROTO_PULL,
        SLIM_PROTO_LOCKED,
        SLIM_PROTO_ASYNC_SMPLX,
        SLIM_PROTO_ASYNC_HALF_DUP,
        SLIM_PROTO_EXT_SMPLX,
        SLIM_PROTO_EXT_HALF_DUP
    };

.. _`slim_transport_protocol.constants`:

Constants
---------

SLIM_PROTO_ISO
    Isochronous Protocol, no flow control as data rate match
    channel rate flow control embedded in the data.

SLIM_PROTO_PUSH
    Pushed Protocol, includes flow control, Used to carry
    data whose rate is equal to, or lower than the channel rate.

SLIM_PROTO_PULL
    Pulled Protocol, similar usage as pushed protocol
    but pull is a unicast.

SLIM_PROTO_LOCKED
    Locked Protocol

SLIM_PROTO_ASYNC_SMPLX
    Asynchronous Protocol-Simplex

SLIM_PROTO_ASYNC_HALF_DUP
    Asynchronous Protocol-Half-duplex

SLIM_PROTO_EXT_SMPLX
    Extended Asynchronous Protocol-Simplex

SLIM_PROTO_EXT_HALF_DUP
    Extended Asynchronous Protocol-Half-duplex

.. _`slim_stream_runtime`:

struct slim_stream_runtime
==========================

.. c:type:: struct slim_stream_runtime

    SLIMbus stream runtime instance

.. _`slim_stream_runtime.definition`:

Definition
----------

.. code-block:: c

    struct slim_stream_runtime {
        const char *name;
        struct slim_device *dev;
        int direction;
        enum slim_transport_protocol prot;
        unsigned int rate;
        unsigned int bps;
        unsigned int ratem;
        int num_ports;
        struct slim_port *ports;
        struct list_head node;
    }

.. _`slim_stream_runtime.members`:

Members
-------

name
    Name of the stream

dev
    SLIM Device instance associated with this stream

direction
    direction of stream

prot
    Transport protocol used in this stream

rate
    Data rate of samples *

bps
    bits per sample

ratem
    rate multipler which is super frame rate/data rate

num_ports
    number of ports

ports
    pointer to instance of ports

node
    list head for stream associated with slim device.

.. _`slim_controller`:

struct slim_controller
======================

.. c:type:: struct slim_controller

    Controls every instance of SLIMbus (similar to 'master' on SPI)

.. _`slim_controller.definition`:

Definition
----------

.. code-block:: c

    struct slim_controller {
        struct device *dev;
        unsigned int id;
        char name[SLIMBUS_NAME_SIZE];
        int min_cg;
        int max_cg;
        int clkgear;
        struct ida laddr_ida;
        struct slim_framer *a_framer;
        struct mutex lock;
        struct list_head devices;
        struct idr tid_idr;
        spinlock_t txn_lock;
        struct slim_sched sched;
        int (*xfer_msg)(struct slim_controller *ctrl, struct slim_msg_txn *tx);
        int (*set_laddr)(struct slim_controller *ctrl, struct slim_eaddr *ea, u8 laddr);
        int (*get_laddr)(struct slim_controller *ctrl, struct slim_eaddr *ea, u8 *laddr);
        int (*enable_stream)(struct slim_stream_runtime *rt);
        int (*disable_stream)(struct slim_stream_runtime *rt);
        int (*wakeup)(struct slim_controller *ctrl);
    }

.. _`slim_controller.members`:

Members
-------

dev
    Device interface to this driver

id
    Board-specific number identifier for this controller/bus

name
    Name for this controller

min_cg
    Minimum clock gear supported by this controller (default value: 1)

max_cg
    Maximum clock gear supported by this controller (default value: 10)

clkgear
    Current clock gear in which this bus is running

laddr_ida
    logical address id allocator

a_framer
    Active framer which is clocking the bus managed by this controller

lock
    Mutex protecting controller data structures

devices
    Slim device list

tid_idr
    tid id allocator

txn_lock
    Lock to protect table of transactions

sched
    scheduler structure used by the controller

xfer_msg
    Transfer a message on this controller (this can be a broadcast
    control/status message like data channel setup, or a unicast message
    like value element read/write.

set_laddr
    Setup logical address at laddr for the slave with elemental
    address e_addr. Drivers implementing controller will be expected to
    send unicast message to this device with its logical address.

get_laddr
    It is possible that controller needs to set fixed logical
    address table and get_laddr can be used in that case so that controller
    can do this assignment. Use case is when the master is on the remote
    processor side, who is resposible for allocating laddr.

enable_stream
    This function pointer implements controller-specific procedure
    to enable a stream.

disable_stream
    This function pointer implements controller-specific procedure
    to disable stream.

wakeup
    This function pointer implements controller-specific procedure
    to wake it up from clock-pause. Framework will call this to bring
    the controller out of clock pause.

.. _`slim_controller.description`:

Description
-----------

     'Manager device' is responsible for  device management, bandwidth
     allocation, channel setup, and port associations per channel.
     Device management means Logical address assignment/removal based on
     enumeration (report-present, report-absent) of a device.
     Bandwidth allocation is done dynamically by the manager based on active
     channels on the bus, message-bandwidth requests made by SLIMbus devices.
     Based on current bandwidth usage, manager chooses a frequency to run
     the bus at (in steps of 'clock-gear', 1 through 10, each clock gear
     representing twice the frequency than the previous gear).
     Manager is also responsible for entering (and exiting) low-power-mode
     (known as 'clock pause').
     Manager can do handover of framer if there are multiple framers on the
     bus and a certain usecase warrants using certain framer to avoid keeping
     previous framer being powered-on.

     Controller here performs duties of the manager device, and 'interface
     device'. Interface device is responsible for monitoring the bus and
     reporting information such as loss-of-synchronization, data
     slot-collision.

.. This file was automatic generated / don't edit.


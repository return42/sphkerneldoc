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


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/mei_dev.h

.. _`mei_cb_file_ops`:

enum mei_cb_file_ops
====================

.. c:type:: enum mei_cb_file_ops

    file operation associated with the callback

.. _`mei_cb_file_ops.definition`:

Definition
----------

.. code-block:: c

    enum mei_cb_file_ops {
        MEI_FOP_READ,
        MEI_FOP_WRITE,
        MEI_FOP_CONNECT,
        MEI_FOP_DISCONNECT,
        MEI_FOP_DISCONNECT_RSP,
        MEI_FOP_NOTIFY_START,
        MEI_FOP_NOTIFY_STOP
    };

.. _`mei_cb_file_ops.constants`:

Constants
---------

MEI_FOP_READ
    read

MEI_FOP_WRITE
    write

MEI_FOP_CONNECT
    connect

MEI_FOP_DISCONNECT
    disconnect

MEI_FOP_DISCONNECT_RSP
    disconnect response

MEI_FOP_NOTIFY_START
    start notification

MEI_FOP_NOTIFY_STOP
    stop notification

.. _`mei_cl_io_mode`:

enum mei_cl_io_mode
===================

.. c:type:: enum mei_cl_io_mode

    io mode between driver and fw

.. _`mei_cl_io_mode.definition`:

Definition
----------

.. code-block:: c

    enum mei_cl_io_mode {
        MEI_CL_IO_TX_BLOCKING,
        MEI_CL_IO_TX_INTERNAL,
        MEI_CL_IO_RX_NONBLOCK
    };

.. _`mei_cl_io_mode.constants`:

Constants
---------

MEI_CL_IO_TX_BLOCKING
    send is blocking

MEI_CL_IO_TX_INTERNAL
    internal communication between driver and FW

MEI_CL_IO_RX_NONBLOCK
    recv is non-blocking

.. _`mei_me_client`:

struct mei_me_client
====================

.. c:type:: struct mei_me_client

    representation of me (fw) client

.. _`mei_me_client.definition`:

Definition
----------

.. code-block:: c

    struct mei_me_client {
        struct list_head list;
        struct kref refcnt;
        struct mei_client_properties props;
        u8 client_id;
        u8 tx_flow_ctrl_creds;
        u8 connect_count;
        u8 bus_added;
    }

.. _`mei_me_client.members`:

Members
-------

list
    link in me client list

refcnt
    struct reference count

props
    client properties

client_id
    me client id

tx_flow_ctrl_creds
    flow control credits

connect_count
    number connections to this client

bus_added
    added to bus

.. _`mei_cl_cb`:

struct mei_cl_cb
================

.. c:type:: struct mei_cl_cb

    file operation callback structure

.. _`mei_cl_cb.definition`:

Definition
----------

.. code-block:: c

    struct mei_cl_cb {
        struct list_head list;
        struct mei_cl *cl;
        enum mei_cb_file_ops fop_type;
        struct mei_msg_data buf;
        size_t buf_idx;
        const struct file *fp;
        int status;
        u32 internal:1;
        u32 blocking:1;
        u32 completed:1;
    }

.. _`mei_cl_cb.members`:

Members
-------

list
    link in callback queue

cl
    file client who is running this operation

fop_type
    file operation type

buf
    buffer for data associated with the callback

buf_idx
    last read index

fp
    pointer to file structure

status
    io status of the cb

internal
    communication between driver and FW flag

blocking
    transmission blocking mode

completed
    the transfer or reception has completed

.. _`mei_cl`:

struct mei_cl
=============

.. c:type:: struct mei_cl

    me client host representation carried in file->private_data

.. _`mei_cl.definition`:

Definition
----------

.. code-block:: c

    struct mei_cl {
        struct list_head link;
        struct mei_device *dev;
        enum file_state state;
        wait_queue_head_t tx_wait;
        wait_queue_head_t rx_wait;
        wait_queue_head_t wait;
        wait_queue_head_t ev_wait;
        struct fasync_struct *ev_async;
        int status;
        struct mei_me_client *me_cl;
        const struct file *fp;
        u8 host_client_id;
        u8 tx_flow_ctrl_creds;
        u8 rx_flow_ctrl_creds;
        u8 timer_count;
        u8 notify_en;
        u8 notify_ev;
        u8 tx_cb_queued;
        enum mei_file_transaction_states writing_state;
        struct list_head rd_pending;
        struct list_head rd_completed;
        struct mei_cl_device *cldev;
    }

.. _`mei_cl.members`:

Members
-------

link
    link in the clients list

dev
    mei parent device

state
    file operation state

tx_wait
    wait queue for tx completion

rx_wait
    wait queue for rx completion

wait
    wait queue for management operation

ev_wait
    notification wait queue

ev_async
    event async notification

status
    connection status

me_cl
    fw client connected

fp
    file associated with client

host_client_id
    host id

tx_flow_ctrl_creds
    transmit flow credentials

rx_flow_ctrl_creds
    receive flow credentials

timer_count
    watchdog timer for operation completion

notify_en
    notification - enabled/disabled

notify_ev
    pending notification event

tx_cb_queued
    number of tx callbacks in queue

writing_state
    state of the tx

rd_pending
    pending read credits

rd_completed
    completed read

cldev
    device on the mei client bus

.. _`mei_hw_ops`:

struct mei_hw_ops
=================

.. c:type:: struct mei_hw_ops

    hw specific ops

.. _`mei_hw_ops.definition`:

Definition
----------

.. code-block:: c

    struct mei_hw_ops {
        bool (*host_is_ready)(struct mei_device *dev);
        bool (*hw_is_ready)(struct mei_device *dev);
        int (*hw_reset)(struct mei_device *dev, bool enable);
        int (*hw_start)(struct mei_device *dev);
        void (*hw_config)(struct mei_device *dev);
        int (*fw_status)(struct mei_device *dev, struct mei_fw_status *fw_sts);
        enum mei_pg_state (*pg_state)(struct mei_device *dev);
        bool (*pg_in_transition)(struct mei_device *dev);
        bool (*pg_is_enabled)(struct mei_device *dev);
        void (*intr_clear)(struct mei_device *dev);
        void (*intr_enable)(struct mei_device *dev);
        void (*intr_disable)(struct mei_device *dev);
        void (*synchronize_irq)(struct mei_device *dev);
        int (*hbuf_free_slots)(struct mei_device *dev);
        bool (*hbuf_is_ready)(struct mei_device *dev);
        size_t (*hbuf_max_len)(const struct mei_device *dev);
        int (*write)(struct mei_device *dev,struct mei_msg_hdr *hdr, const unsigned char *buf);
        int (*rdbuf_full_slots)(struct mei_device *dev);
        u32 (*read_hdr)(const struct mei_device *dev);
        int (*read)(struct mei_device *dev, unsigned char *buf, unsigned long len);
    }

.. _`mei_hw_ops.members`:

Members
-------

host_is_ready
    query for host readiness

hw_is_ready
    query if hw is ready

hw_reset
    reset hw

hw_start
    start hw after reset

hw_config
    configure hw

fw_status
    get fw status registers

pg_state
    power gating state of the device

pg_in_transition
    is device now in pg transition

pg_is_enabled
    is power gating enabled

intr_clear
    clear pending interrupts

intr_enable
    enable interrupts

intr_disable
    disable interrupts

synchronize_irq
    synchronize irqs

hbuf_free_slots
    query for write buffer empty slots

hbuf_is_ready
    query if write buffer is empty

hbuf_max_len
    query for write buffer max len

write
    write a message to FW

rdbuf_full_slots
    query how many slots are filled

read_hdr
    get first 4 bytes (header)

read
    read a buffer from the FW

.. _`mei_pg_event`:

enum mei_pg_event
=================

.. c:type:: enum mei_pg_event

    power gating transition events

.. _`mei_pg_event.definition`:

Definition
----------

.. code-block:: c

    enum mei_pg_event {
        MEI_PG_EVENT_IDLE,
        MEI_PG_EVENT_WAIT,
        MEI_PG_EVENT_RECEIVED,
        MEI_PG_EVENT_INTR_WAIT,
        MEI_PG_EVENT_INTR_RECEIVED
    };

.. _`mei_pg_event.constants`:

Constants
---------

MEI_PG_EVENT_IDLE
    the driver is not in power gating transition

MEI_PG_EVENT_WAIT
    the driver is waiting for a pg event to complete

MEI_PG_EVENT_RECEIVED
    the driver received pg event

MEI_PG_EVENT_INTR_WAIT
    the driver is waiting for a pg event interrupt

MEI_PG_EVENT_INTR_RECEIVED
    the driver received pg event interrupt

.. _`mei_pg_state`:

enum mei_pg_state
=================

.. c:type:: enum mei_pg_state

    device internal power gating state

.. _`mei_pg_state.definition`:

Definition
----------

.. code-block:: c

    enum mei_pg_state {
        MEI_PG_OFF,
        MEI_PG_ON
    };

.. _`mei_pg_state.constants`:

Constants
---------

MEI_PG_OFF
    device is not power gated - it is active

MEI_PG_ON
    device is power gated - it is in lower power state

.. _`mei_device`:

struct mei_device
=================

.. c:type:: struct mei_device

    MEI private device struct

.. _`mei_device.definition`:

Definition
----------

.. code-block:: c

    struct mei_device {
        struct device *dev;
        struct cdev cdev;
        int minor;
        struct list_head write_list;
        struct list_head write_waiting_list;
        struct list_head ctrl_wr_list;
        struct list_head ctrl_rd_list;
        u8 tx_queue_limit;
        struct list_head file_list;
        long open_handle_count;
        struct mutex device_lock;
        struct delayed_work timer_work;
        bool recvd_hw_ready;
        wait_queue_head_t wait_hw_ready;
        wait_queue_head_t wait_pg;
        wait_queue_head_t wait_hbm_start;
        unsigned long reset_count;
        enum mei_dev_state dev_state;
        enum mei_hbm_state hbm_state;
        u16 init_clients_timer;
        enum mei_pg_event pg_event;
    #ifdef CONFIG_PM
        struct dev_pm_domain pg_domain;
    #endif
        unsigned char rd_msg_buf[MEI_RD_MSG_BUF_SIZE];
        u32 rd_msg_hdr;
        u8 hbuf_depth;
        bool hbuf_is_ready;
        struct hbm_version version;
        unsigned int hbm_f_pg_supported:1;
        unsigned int hbm_f_dc_supported:1;
        unsigned int hbm_f_dot_supported:1;
        unsigned int hbm_f_ev_supported:1;
        unsigned int hbm_f_fa_supported:1;
        unsigned int hbm_f_ie_supported:1;
        unsigned int hbm_f_os_supported:1;
        struct rw_semaphore me_clients_rwsem;
        struct list_head me_clients;
        DECLARE_BITMAP(me_clients_map, MEI_CLIENTS_MAX);
        DECLARE_BITMAP(host_clients_map, MEI_CLIENTS_MAX);
        bool allow_fixed_address;
        bool override_fixed_address;
        struct work_struct reset_work;
        struct work_struct bus_rescan_work;
        struct list_head device_list;
        struct mutex cl_bus_lock;
    #if IS_ENABLED(CONFIG_DEBUG_FS)
        struct dentry *dbgfs_dir;
    #endif
        const struct mei_hw_ops *ops;
        char hw[0] __aligned(sizeof(void *));
    }

.. _`mei_device.members`:

Members
-------

dev
    device on a bus

cdev
    character device

minor
    minor number allocated for device

write_list
    write pending list

write_waiting_list
    write completion list

ctrl_wr_list
    pending control write list

ctrl_rd_list
    pending control read list

tx_queue_limit
    tx queues per client linit

file_list
    list of opened handles

open_handle_count
    number of opened handles

device_lock
    big device lock

timer_work
    MEI timer delayed work (timeouts)

recvd_hw_ready
    hw ready message received flag

wait_hw_ready
    wait queue for receive HW ready message form FW

wait_pg
    wait queue for receive PG message from FW

wait_hbm_start
    wait queue for receive HBM start message from FW

reset_count
    number of consecutive resets

dev_state
    device state

hbm_state
    state of host bus message protocol

init_clients_timer
    HBM init handshake timeout

pg_event
    power gating event

pg_domain
    runtime PM domain

rd_msg_buf
    control messages buffer

rd_msg_hdr
    read message header storage

hbuf_depth
    depth of hardware host/write buffer is slots

hbuf_is_ready
    query if the host host/write buffer is ready

version
    HBM protocol version in use

hbm_f_pg_supported
    hbm feature pgi protocol

hbm_f_dc_supported
    hbm feature dynamic clients

hbm_f_dot_supported
    hbm feature disconnect on timeout

hbm_f_ev_supported
    hbm feature event notification

hbm_f_fa_supported
    hbm feature fixed address client

hbm_f_ie_supported
    hbm feature immediate reply to enum request

hbm_f_os_supported
    hbm feature support OS ver message

me_clients_rwsem
    rw lock over me_clients list

me_clients
    list of FW clients

me_clients_map
    FW clients bit map

host_clients_map
    host clients id pool

allow_fixed_address
    allow user space to connect a fixed client

override_fixed_address
    force allow fixed address behavior

reset_work
    work item for the device reset

bus_rescan_work
    work item for the bus rescan

device_list
    mei client bus list

cl_bus_lock
    client bus list lock

dbgfs_dir
    debugfs mei root directory

ops
    : hw specific operations

hw
    hw specific data

.. _`mei_data2slots`:

mei_data2slots
==============

.. c:function:: u32 mei_data2slots(size_t length)

    get slots - number of (dwords) from a message length + size of the mei header

    :param size_t length:
        size of the messages in bytes

.. _`mei_data2slots.return`:

Return
------

number of slots

.. _`mei_slots2data`:

mei_slots2data
==============

.. c:function:: u32 mei_slots2data(int slots)

    get data in slots - bytes from slots

    :param int slots:
        number of available slots

.. _`mei_slots2data.return`:

Return
------

number of bytes in slots

.. _`mei_fw_status_str`:

mei_fw_status_str
=================

.. c:function:: ssize_t mei_fw_status_str(struct mei_device *dev, char *buf, size_t len)

    fetch and convert fw status registers to printable string

    :param struct mei_device \*dev:
        the device structure

    :param char \*buf:
        string buffer at minimal size MEI_FW_STATUS_STR_SZ

    :param size_t len:
        buffer len must be >= MEI_FW_STATUS_STR_SZ

.. _`mei_fw_status_str.return`:

Return
------

number of bytes written or < 0 on failure

.. This file was automatic generated / don't edit.


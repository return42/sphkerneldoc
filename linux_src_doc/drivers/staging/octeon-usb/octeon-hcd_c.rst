.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/octeon-usb/octeon-hcd.c

.. _`cvmx_usb_speed`:

enum cvmx_usb_speed
===================

.. c:type:: enum cvmx_usb_speed

    the possible USB device speeds

.. _`cvmx_usb_speed.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_speed {
        CVMX_USB_SPEED_HIGH,
        CVMX_USB_SPEED_FULL,
        CVMX_USB_SPEED_LOW
    };

.. _`cvmx_usb_speed.constants`:

Constants
---------

CVMX_USB_SPEED_HIGH
    Device is operation at 480Mbps

CVMX_USB_SPEED_FULL
    Device is operation at 12Mbps

CVMX_USB_SPEED_LOW
    Device is operation at 1.5Mbps

.. _`cvmx_usb_transfer`:

enum cvmx_usb_transfer
======================

.. c:type:: enum cvmx_usb_transfer

    the possible USB transfer types

.. _`cvmx_usb_transfer.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_transfer {
        CVMX_USB_TRANSFER_CONTROL,
        CVMX_USB_TRANSFER_ISOCHRONOUS,
        CVMX_USB_TRANSFER_BULK,
        CVMX_USB_TRANSFER_INTERRUPT
    };

.. _`cvmx_usb_transfer.constants`:

Constants
---------

CVMX_USB_TRANSFER_CONTROL
    USB transfer type control for hub and status
    transfers

CVMX_USB_TRANSFER_ISOCHRONOUS
    USB transfer type isochronous for low
    priority periodic transfers

CVMX_USB_TRANSFER_BULK
    USB transfer type bulk for large low priority
    transfers

CVMX_USB_TRANSFER_INTERRUPT
    USB transfer type interrupt for high priority
    periodic transfers

.. _`cvmx_usb_direction`:

enum cvmx_usb_direction
=======================

.. c:type:: enum cvmx_usb_direction

    the transfer directions

.. _`cvmx_usb_direction.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_direction {
        CVMX_USB_DIRECTION_OUT,
        CVMX_USB_DIRECTION_IN
    };

.. _`cvmx_usb_direction.constants`:

Constants
---------

CVMX_USB_DIRECTION_OUT
    Data is transferring from Octeon to the device/host

CVMX_USB_DIRECTION_IN
    Data is transferring from the device/host to Octeon

.. _`cvmx_usb_status`:

enum cvmx_usb_status
====================

.. c:type:: enum cvmx_usb_status

    possible callback function status codes

.. _`cvmx_usb_status.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_status {
        CVMX_USB_STATUS_OK,
        CVMX_USB_STATUS_SHORT,
        CVMX_USB_STATUS_CANCEL,
        CVMX_USB_STATUS_ERROR,
        CVMX_USB_STATUS_STALL,
        CVMX_USB_STATUS_XACTERR,
        CVMX_USB_STATUS_DATATGLERR,
        CVMX_USB_STATUS_BABBLEERR,
        CVMX_USB_STATUS_FRAMEERR
    };

.. _`cvmx_usb_status.constants`:

Constants
---------

CVMX_USB_STATUS_OK
    The transaction / operation finished without
    any errors

CVMX_USB_STATUS_SHORT
    FIXME: This is currently not implemented

CVMX_USB_STATUS_CANCEL
    The transaction was canceled while in flight
    by a user call to cvmx_usb_cancel

CVMX_USB_STATUS_ERROR
    The transaction aborted with an unexpected
    error status

CVMX_USB_STATUS_STALL
    The transaction received a USB STALL response
    from the device

CVMX_USB_STATUS_XACTERR
    The transaction failed with an error from the
    device even after a number of retries

CVMX_USB_STATUS_DATATGLERR
    The transaction failed with a data toggle
    error even after a number of retries

CVMX_USB_STATUS_BABBLEERR
    The transaction failed with a babble error

CVMX_USB_STATUS_FRAMEERR
    The transaction failed with a frame error
    even after a number of retries

.. _`cvmx_usb_port_status`:

struct cvmx_usb_port_status
===========================

.. c:type:: struct cvmx_usb_port_status

    the USB port status information

.. _`cvmx_usb_port_status.definition`:

Definition
----------

.. code-block:: c

    struct cvmx_usb_port_status {
        u32 reserved : 25;
        u32 port_enabled : 1;
        u32 port_over_current : 1;
        u32 port_powered : 1;
        enum cvmx_usb_speed port_speed : 2;
        u32 connected : 1;
        u32 connect_change : 1;
    }

.. _`cvmx_usb_port_status.members`:

Members
-------

reserved
    *undescribed*

port_enabled
    1 = Usb port is enabled, 0 = disabled

port_over_current
    1 = Over current detected, 0 = Over current not
    detected. Octeon doesn't support over current detection.

port_powered
    1 = Port power is being supplied to the device, 0 =
    power is off. Octeon doesn't support turning port power
    off.

port_speed
    Current port speed.

connected
    1 = A device is connected to the port, 0 = No device is
    connected.

connect_change
    1 = Device connected state changed since the last set
    status call.

.. _`cvmx_usb_iso_packet`:

struct cvmx_usb_iso_packet
==========================

.. c:type:: struct cvmx_usb_iso_packet

    descriptor for Isochronous packets

.. _`cvmx_usb_iso_packet.definition`:

Definition
----------

.. code-block:: c

    struct cvmx_usb_iso_packet {
        int offset;
        int length;
        enum cvmx_usb_status status;
    }

.. _`cvmx_usb_iso_packet.members`:

Members
-------

offset
    This is the offset in bytes into the main buffer where this data
    is stored.

length
    This is the length in bytes of the data.

status
    This is the status of this individual packet transfer.

.. _`cvmx_usb_initialize_flags`:

enum cvmx_usb_initialize_flags
==============================

.. c:type:: enum cvmx_usb_initialize_flags

    flags used by the initialization function

.. _`cvmx_usb_initialize_flags.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_initialize_flags {
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_XO_XI,
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_XO_GND,
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_MHZ_MASK,
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_12MHZ,
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_24MHZ,
        CVMX_USB_INITIALIZE_FLAGS_CLOCK_48MHZ,
        CVMX_USB_INITIALIZE_FLAGS_NO_DMA
    };

.. _`cvmx_usb_initialize_flags.constants`:

Constants
---------

CVMX_USB_INITIALIZE_FLAGS_CLOCK_XO_XI
    The USB port uses a 12MHz crystal
    as clock source at USB_XO and
    USB_XI.

CVMX_USB_INITIALIZE_FLAGS_CLOCK_XO_GND
    The USB port uses 12/24/48MHz 2.5V
    board clock source at USB_XO.
    USB_XI should be tied to GND.

CVMX_USB_INITIALIZE_FLAGS_CLOCK_MHZ_MASK
    Mask for clock speed field

CVMX_USB_INITIALIZE_FLAGS_CLOCK_12MHZ
    Speed of reference clock or
    crystal

CVMX_USB_INITIALIZE_FLAGS_CLOCK_24MHZ
    Speed of reference clock

CVMX_USB_INITIALIZE_FLAGS_CLOCK_48MHZ
    Speed of reference clock

CVMX_USB_INITIALIZE_FLAGS_NO_DMA
    Disable DMA and used polled IO for
    data transfer use for the USB

.. _`cvmx_usb_pipe_flags`:

enum cvmx_usb_pipe_flags
========================

.. c:type:: enum cvmx_usb_pipe_flags

    internal flags for a pipe.

.. _`cvmx_usb_pipe_flags.definition`:

Definition
----------

.. code-block:: c

    enum cvmx_usb_pipe_flags {
        CVMX_USB_PIPE_FLAGS_SCHEDULED,
        CVMX_USB_PIPE_FLAGS_NEED_PING
    };

.. _`cvmx_usb_pipe_flags.constants`:

Constants
---------

CVMX_USB_PIPE_FLAGS_SCHEDULED
    Used internally to determine if a pipe is
    actively using hardware.

CVMX_USB_PIPE_FLAGS_NEED_PING
    Used internally to determine if a high speed
    pipe is in the ping state.

.. _`cvmx_usb_transaction`:

struct cvmx_usb_transaction
===========================

.. c:type:: struct cvmx_usb_transaction

    describes each pending USB transaction regardless of type. These are linked together to form a list of pending requests for a pipe.

.. _`cvmx_usb_transaction.definition`:

Definition
----------

.. code-block:: c

    struct cvmx_usb_transaction {
        struct list_head node;
        enum cvmx_usb_transfer type;
        u64 buffer;
        int buffer_length;
        u64 control_header;
        int iso_start_frame;
        int iso_number_packets;
        struct cvmx_usb_iso_packet *iso_packets;
        int xfersize;
        int pktcnt;
        int retries;
        int actual_bytes;
        enum cvmx_usb_stage stage;
        struct urb *urb;
    }

.. _`cvmx_usb_transaction.members`:

Members
-------

node
    List node for transactions in the pipe.

type
    Type of transaction, duplicated of the pipe.

buffer
    User's physical buffer address to read/write.

buffer_length
    Size of the user's buffer in bytes.

control_header
    For control transactions, physical address of the 8
    byte standard header.

iso_start_frame
    For ISO transactions, the starting frame number.

iso_number_packets
    For ISO transactions, the number of packets in the
    request.

iso_packets
    For ISO transactions, the sub packets in the request.

xfersize
    *undescribed*

pktcnt
    *undescribed*

retries
    *undescribed*

actual_bytes
    Actual bytes transfer for this transaction.

stage
    For control transactions, the current stage.

urb
    URB.

.. _`cvmx_usb_pipe`:

struct cvmx_usb_pipe
====================

.. c:type:: struct cvmx_usb_pipe

    a pipe represents a virtual connection between Octeon and some USB device. It contains a list of pending request to the device.

.. _`cvmx_usb_pipe.definition`:

Definition
----------

.. code-block:: c

    struct cvmx_usb_pipe {
        struct list_head node;
        struct list_head transactions;
        u64 interval;
        u64 next_tx_frame;
        enum cvmx_usb_pipe_flags flags;
        enum cvmx_usb_speed device_speed;
        enum cvmx_usb_transfer transfer_type;
        enum cvmx_usb_direction transfer_dir;
        int multi_count;
        u16 max_packet;
        u8 device_addr;
        u8 endpoint_num;
        u8 hub_device_addr;
        u8 hub_port;
        u8 pid_toggle;
        u8 channel;
        s8 split_sc_frame;
    }

.. _`cvmx_usb_pipe.members`:

Members
-------

node
    List node for pipe list

transactions
    List of pending transactions

interval
    For periodic pipes, the interval between packets in
    frames

next_tx_frame
    The next frame this pipe is allowed to transmit on

flags
    State flags for this pipe

device_speed
    Speed of device connected to this pipe

transfer_type
    Type of transaction supported by this pipe

transfer_dir
    IN or OUT. Ignored for Control

multi_count
    Max packet in a row for the device

max_packet
    The device's maximum packet size in bytes

device_addr
    USB device address at other end of pipe

endpoint_num
    USB endpoint number at other end of pipe

hub_device_addr
    Hub address this device is connected to

hub_port
    Hub port this device is connected to

pid_toggle
    This toggles between 0/1 on every packet send to track
    the data pid needed

channel
    Hardware DMA channel for this pipe

split_sc_frame
    The low order bits of the frame number the split
    complete should be sent on

.. _`octeon_hcd`:

struct octeon_hcd
=================

.. c:type:: struct octeon_hcd

    the state of the USB block

.. _`octeon_hcd.definition`:

Definition
----------

.. code-block:: c

    struct octeon_hcd {
        spinlock_t lock;
        int init_flags;
        int index;
        int idle_hardware_channels;
        union cvmx_usbcx_hprt usbcx_hprt;
        struct cvmx_usb_pipe *pipe_for_channel[MAX_CHANNELS];
        int indent;
        struct cvmx_usb_port_status port_status;
        struct list_head idle_pipes;
        struct list_head active_pipes[4];
        u64 frame_number;
        struct cvmx_usb_transaction *active_split;
        struct cvmx_usb_tx_fifo periodic;
        struct cvmx_usb_tx_fifo nonperiodic;
    }

.. _`octeon_hcd.members`:

Members
-------

lock
    *undescribed*

init_flags
    *undescribed*

index
    *undescribed*

idle_hardware_channels
    *undescribed*

usbcx_hprt
    *undescribed*

pipe_for_channel
    *undescribed*

indent
    *undescribed*

port_status
    *undescribed*

idle_pipes
    *undescribed*

active_pipes
    *undescribed*

frame_number
    *undescribed*

active_split
    *undescribed*

periodic
    *undescribed*

nonperiodic
    *undescribed*

.. _`octeon_hcd.lock`:

lock
----

Serialization lock.

.. _`octeon_hcd.init_flags`:

init_flags
----------

Flags passed to initialize.

.. _`octeon_hcd.index`:

index
-----

Which USB block this is for.

.. _`octeon_hcd.idle_hardware_channels`:

idle_hardware_channels
----------------------

Bit set for every idle hardware channel.

.. _`octeon_hcd.usbcx_hprt`:

usbcx_hprt
----------

Stored port status so we don't need to read a CSR to
determine splits.

.. _`octeon_hcd.pipe_for_channel`:

pipe_for_channel
----------------

Map channels to pipes.

.. _`octeon_hcd.pipe`:

pipe
----

Storage for pipes.

.. _`octeon_hcd.indent`:

indent
------

Used by debug output to indent functions.

.. _`octeon_hcd.port_status`:

port_status
-----------

Last port status used for change notification.

.. _`octeon_hcd.idle_pipes`:

idle_pipes
----------

List of open pipes that have no transactions.

.. _`octeon_hcd.active_pipes`:

active_pipes
------------

Active pipes indexed by transfer type.

.. _`octeon_hcd.frame_number`:

frame_number
------------

Increments every SOF interrupt for time keeping.

.. _`octeon_hcd.active_split`:

active_split
------------

Points to the current active split, or NULL.

.. _`octeon_temp_buffer`:

struct octeon_temp_buffer
=========================

.. c:type:: struct octeon_temp_buffer

    a bounce buffer for USB transfers

.. _`octeon_temp_buffer.definition`:

Definition
----------

.. code-block:: c

    struct octeon_temp_buffer {
        void *orig_buffer;
        u8 data[0];
    }

.. _`octeon_temp_buffer.members`:

Members
-------

orig_buffer
    the original buffer passed by the USB stack

data
    the newly allocated temporary buffer (excluding meta-data)

.. _`octeon_temp_buffer.description`:

Description
-----------

Both the DMA engine and FIFO mode will always transfer full 32-bit words. If
the buffer is too short, we need to allocate a temporary one, and this struct
represents it.

.. _`octeon_alloc_temp_buffer`:

octeon_alloc_temp_buffer
========================

.. c:function:: int octeon_alloc_temp_buffer(struct urb *urb, gfp_t mem_flags)

    allocate a temporary buffer for USB transfer (if needed)

    :param urb:
        URB.
    :type urb: struct urb \*

    :param mem_flags:
        Memory allocation flags.
    :type mem_flags: gfp_t

.. _`octeon_alloc_temp_buffer.description`:

Description
-----------

This function allocates a temporary bounce buffer whenever it's needed
due to HW limitations.

.. _`octeon_free_temp_buffer`:

octeon_free_temp_buffer
=======================

.. c:function:: void octeon_free_temp_buffer(struct urb *urb)

    free a temporary buffer used by USB transfers.

    :param urb:
        URB.
    :type urb: struct urb \*

.. _`octeon_free_temp_buffer.description`:

Description
-----------

Frees a buffer allocated by \ :c:func:`octeon_alloc_temp_buffer`\ .

.. _`octeon_map_urb_for_dma`:

octeon_map_urb_for_dma
======================

.. c:function:: int octeon_map_urb_for_dma(struct usb_hcd *hcd, struct urb *urb, gfp_t mem_flags)

    Octeon-specific \ :c:func:`map_urb_for_dma`\ .

    :param hcd:
        USB HCD structure.
    :type hcd: struct usb_hcd \*

    :param urb:
        URB.
    :type urb: struct urb \*

    :param mem_flags:
        Memory allocation flags.
    :type mem_flags: gfp_t

.. _`octeon_unmap_urb_for_dma`:

octeon_unmap_urb_for_dma
========================

.. c:function:: void octeon_unmap_urb_for_dma(struct usb_hcd *hcd, struct urb *urb)

    Octeon-specific \ :c:func:`unmap_urb_for_dma`\ 

    :param hcd:
        USB HCD structure.
    :type hcd: struct usb_hcd \*

    :param urb:
        URB.
    :type urb: struct urb \*

.. _`cvmx_usb_read_csr32`:

cvmx_usb_read_csr32
===================

.. c:function:: u32 cvmx_usb_read_csr32(struct octeon_hcd *usb, u64 address)

    for 32bit CSRs and logs the value in a readable format if debugging is on.

    :param usb:
        USB block this access is for
    :type usb: struct octeon_hcd \*

    :param address:
        64bit address to read
    :type address: u64

.. _`cvmx_usb_read_csr32.return`:

Return
------

Result of the read

.. _`cvmx_usb_write_csr32`:

cvmx_usb_write_csr32
====================

.. c:function:: void cvmx_usb_write_csr32(struct octeon_hcd *usb, u64 address, u32 value)

    swizzle for 32bit CSRs and logs the value in a readable format if debugging is on.

    :param usb:
        USB block this access is for
    :type usb: struct octeon_hcd \*

    :param address:
        64bit address to write
    :type address: u64

    :param value:
        Value to write
    :type value: u32

.. _`cvmx_usb_pipe_needs_split`:

cvmx_usb_pipe_needs_split
=========================

.. c:function:: int cvmx_usb_pipe_needs_split(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe)

    device through a high speed hub.

    :param usb:
        USB block this access is for
    :type usb: struct octeon_hcd \*

    :param pipe:
        Pipe to check
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_pipe_needs_split.return`:

Return
------

Non zero if we need to do split transactions

.. _`cvmx_usb_get_data_pid`:

cvmx_usb_get_data_pid
=====================

.. c:function:: int cvmx_usb_get_data_pid(struct cvmx_usb_pipe *pipe)

    :param pipe:
        pipe to check
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_get_data_pid.return`:

Return
------

PID for pipe

.. _`cvmx_usb_shutdown`:

cvmx_usb_shutdown
=================

.. c:function:: int cvmx_usb_shutdown(struct octeon_hcd *usb)

    The port should be disabled with all pipes closed when this function is called.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_shutdown.return`:

Return
------

0 or a negative error code.

.. _`cvmx_usb_initialize`:

cvmx_usb_initialize
===================

.. c:function:: int cvmx_usb_initialize(struct device *dev, struct octeon_hcd *usb)

    other access to the Octeon USB port is made. The port starts off in the disabled state.

    :param dev:
        Pointer to struct device for logging purposes.
    :type dev: struct device \*

    :param usb:
        Pointer to struct octeon_hcd.
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_initialize.return`:

Return
------

0 or a negative error code.

.. _`cvmx_usb_reset_port`:

cvmx_usb_reset_port
===================

.. c:function:: void cvmx_usb_reset_port(struct octeon_hcd *usb)

    online and servicing requests.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_disable`:

cvmx_usb_disable
================

.. c:function:: int cvmx_usb_disable(struct octeon_hcd *usb)

    generate data transfers and will not generate events. Transactions in process will fail and call their associated callbacks.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_disable.return`:

Return
------

0 or a negative error code.

.. _`cvmx_usb_get_status`:

cvmx_usb_get_status
===================

.. c:function:: struct cvmx_usb_port_status cvmx_usb_get_status(struct octeon_hcd *usb)

    determine if the usb port has anything connected, is enabled, or has some sort of error condition. The return value of this call has "changed" bits to signal of the value of some fields have changed between calls.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_get_status.return`:

Return
------

Port status information

.. _`cvmx_usb_open_pipe`:

cvmx_usb_open_pipe
==================

.. c:function:: struct cvmx_usb_pipe *cvmx_usb_open_pipe(struct octeon_hcd *usb, int device_addr, int endpoint_num, enum cvmx_usb_speed device_speed, int max_packet, enum cvmx_usb_transfer transfer_type, enum cvmx_usb_direction transfer_dir, int interval, int multi_count, int hub_device_addr, int hub_port)

    must be opened before data can be transferred between a device and Octeon.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param device_addr:
        USB device address to open the pipe to
        (0-127).
    :type device_addr: int

    :param endpoint_num:
        USB endpoint number to open the pipe to
        (0-15).
    :type endpoint_num: int

    :param device_speed:
        The speed of the device the pipe is going
        to. This must match the device's speed,
        which may be different than the port speed.
    :type device_speed: enum cvmx_usb_speed

    :param max_packet:
        The maximum packet length the device can
        transmit/receive (low speed=0-8, full
        speed=0-1023, high speed=0-1024). This value
        comes from the standard endpoint descriptor
        field wMaxPacketSize bits <10:0>.
    :type max_packet: int

    :param transfer_type:
        The type of transfer this pipe is for.
    :type transfer_type: enum cvmx_usb_transfer

    :param transfer_dir:
        The direction the pipe is in. This is not
        used for control pipes.
    :type transfer_dir: enum cvmx_usb_direction

    :param interval:
        For ISOCHRONOUS and INTERRUPT transfers,
        this is how often the transfer is scheduled
        for. All other transfers should specify
        zero. The units are in frames (8000/sec at
        high speed, 1000/sec for full speed).
    :type interval: int

    :param multi_count:
        For high speed devices, this is the maximum
        allowed number of packet per microframe.
        Specify zero for non high speed devices. This
        value comes from the standard endpoint descriptor
        field wMaxPacketSize bits <12:11>.
    :type multi_count: int

    :param hub_device_addr:
        Hub device address this device is connected
        to. Devices connected directly to Octeon
        use zero. This is only used when the device
        is full/low speed behind a high speed hub.
        The address will be of the high speed hub,
        not and full speed hubs after it.
    :type hub_device_addr: int

    :param hub_port:
        Which port on the hub the device is
        connected. Use zero for devices connected
        directly to Octeon. Like hub_device_addr,
        this is only used for full/low speed
        devices behind a high speed hub.
    :type hub_port: int

.. _`cvmx_usb_open_pipe.return`:

Return
------

A non-NULL value is a pipe. NULL means an error.

.. _`cvmx_usb_poll_rx_fifo`:

cvmx_usb_poll_rx_fifo
=====================

.. c:function:: void cvmx_usb_poll_rx_fifo(struct octeon_hcd *usb)

    in non DMA mode. It is very important that this function be called quickly enough to prevent FIFO overflow.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_fill_tx_hw`:

cvmx_usb_fill_tx_hw
===================

.. c:function:: int cvmx_usb_fill_tx_hw(struct octeon_hcd *usb, struct cvmx_usb_tx_fifo *fifo, int available)

    fifos

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param fifo:
        Software fifo to use
    :type fifo: struct cvmx_usb_tx_fifo \*

    :param available:
        Amount of space in the hardware fifo
    :type available: int

.. _`cvmx_usb_fill_tx_hw.return`:

Return
------

Non zero if the hardware fifo was too small and needs
to be serviced again.

.. _`cvmx_usb_poll_tx_fifo`:

cvmx_usb_poll_tx_fifo
=====================

.. c:function:: void cvmx_usb_poll_tx_fifo(struct octeon_hcd *usb)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_fill_tx_fifo`:

cvmx_usb_fill_tx_fifo
=====================

.. c:function:: void cvmx_usb_fill_tx_fifo(struct octeon_hcd *usb, int channel)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param channel:
        Channel number to get packet from
    :type channel: int

.. _`cvmx_usb_start_channel_control`:

cvmx_usb_start_channel_control
==============================

.. c:function:: void cvmx_usb_start_channel_control(struct octeon_hcd *usb, int channel, struct cvmx_usb_pipe *pipe)

    the generic stuff will already have been done in \ :c:func:`cvmx_usb_start_channel`\ .

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param channel:
        Channel to setup
    :type channel: int

    :param pipe:
        Pipe for control transaction
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_start_channel`:

cvmx_usb_start_channel
======================

.. c:function:: void cvmx_usb_start_channel(struct octeon_hcd *usb, int channel, struct cvmx_usb_pipe *pipe)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param channel:
        Channel to setup
    :type channel: int

    :param pipe:
        Pipe to start
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_find_ready_pipe`:

cvmx_usb_find_ready_pipe
========================

.. c:function:: struct cvmx_usb_pipe *cvmx_usb_find_ready_pipe(struct octeon_hcd *usb, enum cvmx_usb_transfer xfer_type)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param xfer_type:
        Transfer type
    :type xfer_type: enum cvmx_usb_transfer

.. _`cvmx_usb_find_ready_pipe.return`:

Return
------

Pipe or NULL if none are ready

.. _`cvmx_usb_schedule`:

cvmx_usb_schedule
=================

.. c:function:: void cvmx_usb_schedule(struct octeon_hcd *usb, int is_sof)

    hardware.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param is_sof:
        True if this schedule was called on a SOF interrupt.
    :type is_sof: int

.. _`cvmx_usb_complete`:

cvmx_usb_complete
=================

.. c:function:: void cvmx_usb_complete(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct cvmx_usb_transaction *transaction, enum cvmx_usb_status complete_code)

    transaction will be removed from the pipe transaction list.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Pipe the transaction is on
    :type pipe: struct cvmx_usb_pipe \*

    :param transaction:
        Transaction that completed
    :type transaction: struct cvmx_usb_transaction \*

    :param complete_code:
        Completion code
    :type complete_code: enum cvmx_usb_status

.. _`cvmx_usb_submit_transaction`:

cvmx_usb_submit_transaction
===========================

.. c:function:: struct cvmx_usb_transaction *cvmx_usb_submit_transaction(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, enum cvmx_usb_transfer type, u64 buffer, int buffer_length, u64 control_header, int iso_start_frame, int iso_number_packets, struct cvmx_usb_iso_packet *iso_packets, struct urb *urb)

    of transactions.

    :param usb:
        *undescribed*
    :type usb: struct octeon_hcd \*

    :param pipe:
        Which pipe to submit to.
    :type pipe: struct cvmx_usb_pipe \*

    :param type:
        Transaction type
    :type type: enum cvmx_usb_transfer

    :param buffer:
        User buffer for the transaction
    :type buffer: u64

    :param buffer_length:
        User buffer's length in bytes
    :type buffer_length: int

    :param control_header:
        For control transactions, the 8 byte standard header
    :type control_header: u64

    :param iso_start_frame:
        For ISO transactions, the start frame
    :type iso_start_frame: int

    :param iso_number_packets:
        For ISO, the number of packet in the transaction.
    :type iso_number_packets: int

    :param iso_packets:
        A description of each ISO packet
    :type iso_packets: struct cvmx_usb_iso_packet \*

    :param urb:
        URB for the callback
    :type urb: struct urb \*

.. _`cvmx_usb_submit_transaction.return`:

Return
------

Transaction or NULL on failure.

.. _`cvmx_usb_submit_bulk`:

cvmx_usb_submit_bulk
====================

.. c:function:: struct cvmx_usb_transaction *cvmx_usb_submit_bulk(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct urb *urb)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Handle to the pipe for the transfer.
    :type pipe: struct cvmx_usb_pipe \*

    :param urb:
        URB.
    :type urb: struct urb \*

.. _`cvmx_usb_submit_bulk.return`:

Return
------

A submitted transaction or NULL on failure.

.. _`cvmx_usb_submit_interrupt`:

cvmx_usb_submit_interrupt
=========================

.. c:function:: struct cvmx_usb_transaction *cvmx_usb_submit_interrupt(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct urb *urb)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Handle to the pipe for the transfer.
    :type pipe: struct cvmx_usb_pipe \*

    :param urb:
        URB returned when the callback is called.
    :type urb: struct urb \*

.. _`cvmx_usb_submit_interrupt.return`:

Return
------

A submitted transaction or NULL on failure.

.. _`cvmx_usb_submit_control`:

cvmx_usb_submit_control
=======================

.. c:function:: struct cvmx_usb_transaction *cvmx_usb_submit_control(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct urb *urb)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Handle to the pipe for the transfer.
    :type pipe: struct cvmx_usb_pipe \*

    :param urb:
        URB.
    :type urb: struct urb \*

.. _`cvmx_usb_submit_control.return`:

Return
------

A submitted transaction or NULL on failure.

.. _`cvmx_usb_submit_isochronous`:

cvmx_usb_submit_isochronous
===========================

.. c:function:: struct cvmx_usb_transaction *cvmx_usb_submit_isochronous(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct urb *urb)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Handle to the pipe for the transfer.
    :type pipe: struct cvmx_usb_pipe \*

    :param urb:
        URB returned when the callback is called.
    :type urb: struct urb \*

.. _`cvmx_usb_submit_isochronous.return`:

Return
------

A submitted transaction or NULL on failure.

.. _`cvmx_usb_cancel`:

cvmx_usb_cancel
===============

.. c:function:: int cvmx_usb_cancel(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe, struct cvmx_usb_transaction *transaction)

    can fail if the transaction has already completed before cancel is called. Even after a successful cancel call, it may take a frame or two for the \ :c:func:`cvmx_usb_poll`\  function to call the associated callback.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Pipe to cancel requests in.
    :type pipe: struct cvmx_usb_pipe \*

    :param transaction:
        Transaction to cancel, returned by the submit function.
    :type transaction: struct cvmx_usb_transaction \*

.. _`cvmx_usb_cancel.return`:

Return
------

0 or a negative error code.

.. _`cvmx_usb_cancel_all`:

cvmx_usb_cancel_all
===================

.. c:function:: int cvmx_usb_cancel_all(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe)

    does is call \ :c:func:`cvmx_usb_cancel`\  in a loop.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Pipe to cancel requests in.
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_cancel_all.return`:

Return
------

0 or a negative error code.

.. _`cvmx_usb_close_pipe`:

cvmx_usb_close_pipe
===================

.. c:function:: int cvmx_usb_close_pipe(struct octeon_hcd *usb, struct cvmx_usb_pipe *pipe)

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

    :param pipe:
        Pipe to close.
    :type pipe: struct cvmx_usb_pipe \*

.. _`cvmx_usb_close_pipe.return`:

Return
------

0 or a negative error code. EBUSY is returned if the pipe has
outstanding transfers.

.. _`cvmx_usb_get_frame_number`:

cvmx_usb_get_frame_number
=========================

.. c:function:: int cvmx_usb_get_frame_number(struct octeon_hcd *usb)

    number is always in the range of 0-0x7ff.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_get_frame_number.return`:

Return
------

USB frame number

.. _`cvmx_usb_poll_channel`:

cvmx_usb_poll_channel
=====================

.. c:function:: int cvmx_usb_poll_channel(struct octeon_hcd *usb, int channel)

    :param usb:
        USB device
    :type usb: struct octeon_hcd \*

    :param channel:
        Channel to poll
    :type channel: int

.. _`cvmx_usb_poll_channel.return`:

Return
------

Zero on success

.. _`cvmx_usb_poll`:

cvmx_usb_poll
=============

.. c:function:: int cvmx_usb_poll(struct octeon_hcd *usb)

    handlers. This function is meant to be called in the interrupt handler for the USB controller. It can also be called periodically in a loop for non-interrupt based operation.

    :param usb:
        USB device state populated by \ :c:func:`cvmx_usb_initialize`\ .
    :type usb: struct octeon_hcd \*

.. _`cvmx_usb_poll.return`:

Return
------

0 or a negative error code.

.. This file was automatic generated / don't edit.


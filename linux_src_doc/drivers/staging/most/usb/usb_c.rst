.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/usb/usb.c

.. _`most_dci_obj`:

struct most_dci_obj
===================

.. c:type:: struct most_dci_obj

    Direct Communication Interface

.. _`most_dci_obj.definition`:

Definition
----------

.. code-block:: c

    struct most_dci_obj {
        struct device dev;
        struct usb_device *usb_device;
        u16 reg_addr;
    }

.. _`most_dci_obj.members`:

Members
-------

dev
    *undescribed*

usb_device
    pointer to the usb device

reg_addr
    register address for arbitrary DCI access

.. _`most_dev`:

struct most_dev
===============

.. c:type:: struct most_dev

    holds all usb interface specific stuff

.. _`most_dev.definition`:

Definition
----------

.. code-block:: c

    struct most_dev {
        struct usb_device *usb_device;
        struct most_interface iface;
        struct most_channel_capability *cap;
        struct most_channel_config *conf;
        struct most_dci_obj *dci;
        u8 *ep_address;
        char description[MAX_STRING_LEN];
        char suffix[MAX_NUM_ENDPOINTS][MAX_SUFFIX_LEN];
        spinlock_t channel_lock[MAX_NUM_ENDPOINTS];
        bool padding_active[MAX_NUM_ENDPOINTS];
        bool is_channel_healthy[MAX_NUM_ENDPOINTS];
        struct clear_hold_work clear_work[MAX_NUM_ENDPOINTS];
        struct usb_anchor *busy_urbs;
        struct mutex io_mutex;
        struct timer_list link_stat_timer;
        struct work_struct poll_work_obj;
        void (*on_netinfo)(struct most_interface *most_iface, unsigned char link_state, unsigned char *addrs);
    }

.. _`most_dev.members`:

Members
-------

usb_device
    pointer to usb device

iface
    hardware interface

cap
    channel capabilities

conf
    channel configuration

dci
    direct communication interface of hardware

ep_address
    endpoint address table

description
    device description

suffix
    suffix for channel name

channel_lock
    synchronize channel access

padding_active
    indicates channel uses padding

is_channel_healthy
    health status table of each channel

clear_work
    *undescribed*

busy_urbs
    list of anchored items

io_mutex
    synchronize I/O with disconnect

link_stat_timer
    timer for link status reports

poll_work_obj
    work for polling link status

on_netinfo
    *undescribed*

.. _`drci_rd_reg`:

drci_rd_reg
===========

.. c:function:: int drci_rd_reg(struct usb_device *dev, u16 reg, u16 *buf)

    read a DCI register

    :param dev:
        usb device
    :type dev: struct usb_device \*

    :param reg:
        register address
    :type reg: u16

    :param buf:
        buffer to store data
    :type buf: u16 \*

.. _`drci_rd_reg.description`:

Description
-----------

This is reads data from INIC's direct register communication interface

.. _`drci_wr_reg`:

drci_wr_reg
===========

.. c:function:: int drci_wr_reg(struct usb_device *dev, u16 reg, u16 data)

    write a DCI register

    :param dev:
        usb device
    :type dev: struct usb_device \*

    :param reg:
        register address
    :type reg: u16

    :param data:
        data to write
    :type data: u16

.. _`drci_wr_reg.description`:

Description
-----------

This is writes data to INIC's direct register communication interface

.. _`get_stream_frame_size`:

get_stream_frame_size
=====================

.. c:function:: unsigned int get_stream_frame_size(struct most_channel_config *cfg)

    calculate frame size of current configuration

    :param cfg:
        channel configuration
    :type cfg: struct most_channel_config \*

.. _`hdm_poison_channel`:

hdm_poison_channel
==================

.. c:function:: int hdm_poison_channel(struct most_interface *iface, int channel)

    mark buffers of this channel as invalid

    :param iface:
        pointer to the interface
    :type iface: struct most_interface \*

    :param channel:
        channel ID
    :type channel: int

.. _`hdm_poison_channel.description`:

Description
-----------

This unlinks all URBs submitted to the HCD,
calls the associated completion function of the core and removes
them from the list.

Returns 0 on success or error code otherwise.

.. _`hdm_add_padding`:

hdm_add_padding
===============

.. c:function:: int hdm_add_padding(struct most_dev *mdev, int channel, struct mbo *mbo)

    add padding bytes

    :param mdev:
        most device
    :type mdev: struct most_dev \*

    :param channel:
        channel ID
    :type channel: int

    :param mbo:
        buffer object
    :type mbo: struct mbo \*

.. _`hdm_add_padding.description`:

Description
-----------

This inserts the INIC hardware specific padding bytes into a streaming
channel's buffer

.. _`hdm_remove_padding`:

hdm_remove_padding
==================

.. c:function:: int hdm_remove_padding(struct most_dev *mdev, int channel, struct mbo *mbo)

    remove padding bytes

    :param mdev:
        most device
    :type mdev: struct most_dev \*

    :param channel:
        channel ID
    :type channel: int

    :param mbo:
        buffer object
    :type mbo: struct mbo \*

.. _`hdm_remove_padding.description`:

Description
-----------

This takes the INIC hardware specific padding bytes off a streaming
channel's buffer.

.. _`hdm_write_completion`:

hdm_write_completion
====================

.. c:function:: void hdm_write_completion(struct urb *urb)

    completion function for submitted Tx URBs

    :param urb:
        the URB that has been completed
    :type urb: struct urb \*

.. _`hdm_write_completion.description`:

Description
-----------

This checks the status of the completed URB. In case the URB has been
unlinked before, it is immediately freed. On any other error the MBO
transfer flag is set. On success it frees allocated resources and calls
the completion function.

.. _`hdm_write_completion.context`:

Context
-------

interrupt!

.. _`hdm_read_completion`:

hdm_read_completion
===================

.. c:function:: void hdm_read_completion(struct urb *urb)

    completion function for submitted Rx URBs

    :param urb:
        the URB that has been completed
    :type urb: struct urb \*

.. _`hdm_read_completion.description`:

Description
-----------

This checks the status of the completed URB. In case the URB has been
unlinked before it is immediately freed. On any other error the MBO transfer
flag is set. On success it frees allocated resources, removes
padding bytes -if necessary- and calls the completion function.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Error codes returned by in urb->status
or in iso_frame_desc[n].status (for ISO)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

USB device drivers may only test urb status values in completion handlers.
This is because otherwise there would be a race between HCDs updating
these values on one CPU, and device drivers testing them on another CPU.

A transfer's actual_length may be positive even when an error has been
reported.  That's because transfers often involve several packets, so that
one or more packets could finish before an error stops further endpoint I/O.

For isochronous URBs, the urb status value is non-zero only if the URB is
unlinked, the device is removed, the host controller is disabled or the total
transferred length is less than the requested length and the URB_SHORT_NOT_OK
flag is set.  Completion handlers for isochronous URBs should only see
urb->status set to zero, -ENOENT, -ECONNRESET, -ESHUTDOWN, or -EREMOTEIO.
Individual frame descriptor status fields may report more status codes.


0                    Transfer completed successfully

-ENOENT              URB was synchronously unlinked by usb_unlink_urb

-EINPROGRESS         URB still pending, no results yet
(That is, if drivers see this it's a bug.)

-EPROTO (\*, \*\*)      a) bitstuff error
b) no response packet received within the
prescribed bus turn-around time
c) unknown USB error

-EILSEQ (\*, \*\*)      a) CRC mismatch
b) no response packet received within the
prescribed bus turn-around time
c) unknown USB error

Note that often the controller hardware does not
distinguish among cases a), b), and c), so a
driver cannot tell whether there was a protocol
error, a failure to respond (often caused by
device disconnect), or some other fault.

-ETIME (\*\*)          No response packet received within the prescribed
bus turn-around time.  This error may instead be
reported as -EPROTO or -EILSEQ.

-ETIMEDOUT           Synchronous USB message functions use this code
to indicate timeout expired before the transfer
completed, and no other error was reported by HC.

-EPIPE (\*\*)          Endpoint stalled.  For non-control endpoints,
reset this status with \ :c:func:`usb_clear_halt`\ .

-ECOMM               During an IN transfer, the host controller
received data from an endpoint faster than it
could be written to system memory

-ENOSR               During an OUT transfer, the host controller
could not retrieve data from system memory fast
enough to keep up with the USB data rate

-EOVERFLOW (\*)       The amount of data returned by the endpoint was
greater than either the max packet size of the
endpoint or the remaining buffer size.  "Babble".

-EREMOTEIO           The data read from the endpoint did not fill the
specified buffer, and URB_SHORT_NOT_OK was set in
urb->transfer_flags.

-ENODEV              Device was removed.  Often preceded by a burst of
other errors, since the hub driver doesn't detect
device removal events immediately.

-EXDEV               ISO transfer only partially completed
(only set in iso_frame_desc[n].status, not urb->status)

-EINVAL              ISO madness, if this happens: Log off and go home

-ECONNRESET          URB was asynchronously unlinked by usb_unlink_urb

-ESHUTDOWN           The device or host controller has been disabled due
to some problem that could not be worked around,
such as a physical disconnect.


(\*) Error codes like -EPROTO, -EILSEQ and -EOVERFLOW normally indicate
hardware problems such as bad devices (including firmware) or cables.

(\*\*) This is also one of several codes that different kinds of host
controller use to indicate a transfer has failed because of device
disconnect.  In the interval before the hub driver starts disconnect
processing, devices may receive such fault reports for every request.

See <https://www.kernel.org/doc/Documentation/driver-api/usb/error-codes.rst>

.. _`hdm_read_completion.context`:

Context
-------

interrupt!

.. _`hdm_enqueue`:

hdm_enqueue
===========

.. c:function:: int hdm_enqueue(struct most_interface *iface, int channel, struct mbo *mbo)

    receive a buffer to be used for data transfer

    :param iface:
        interface to enqueue to
    :type iface: struct most_interface \*

    :param channel:
        ID of the channel
    :type channel: int

    :param mbo:
        pointer to the buffer object
    :type mbo: struct mbo \*

.. _`hdm_enqueue.description`:

Description
-----------

This allocates a new URB and fills it according to the channel
that is being used for transmission of data. Before the URB is
submitted it is stored in the private anchor list.

Returns 0 on success. On any error the URB is freed and a error code
is returned.

.. _`hdm_enqueue.context`:

Context
-------

Could in \_some\_ cases be interrupt!

.. _`hdm_configure_channel`:

hdm_configure_channel
=====================

.. c:function:: int hdm_configure_channel(struct most_interface *iface, int channel, struct most_channel_config *conf)

    receive channel configuration from core

    :param iface:
        interface
    :type iface: struct most_interface \*

    :param channel:
        channel ID
    :type channel: int

    :param conf:
        structure that holds the configuration information
    :type conf: struct most_channel_config \*

.. _`hdm_configure_channel.description`:

Description
-----------

The attached network interface controller (NIC) supports a padding mode
to avoid short packets on USB, hence increasing the performance due to a
lower interrupt load. This mode is default for synchronous data and can
be switched on for isochronous data. In case padding is active the
driver needs to know the frame size of the payload in order to calculate
the number of bytes it needs to pad when transmitting or to cut off when
receiving data.

.. _`hdm_request_netinfo`:

hdm_request_netinfo
===================

.. c:function:: void hdm_request_netinfo(struct most_interface *iface, int channel, void (*on_netinfo)(struct most_interface *, unsigned char, unsigned char *))

    request network information

    :param iface:
        pointer to interface
    :type iface: struct most_interface \*

    :param channel:
        channel ID
    :type channel: int

    :param void (\*on_netinfo)(struct most_interface \*, unsigned char, unsigned char \*):
        *undescribed*

.. _`hdm_request_netinfo.description`:

Description
-----------

This is used as trigger to set up the link status timer that
polls for the NI state of the INIC every 2 seconds.

.. _`link_stat_timer_handler`:

link_stat_timer_handler
=======================

.. c:function:: void link_stat_timer_handler(struct timer_list *t)

    schedule work obtaining mac address and link status

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`link_stat_timer_handler.description`:

Description
-----------

The handler runs in interrupt context. That's why we need to defer the
tasks to a work queue.

.. _`wq_netinfo`:

wq_netinfo
==========

.. c:function:: void wq_netinfo(struct work_struct *wq_obj)

    work queue function to deliver latest networking information

    :param wq_obj:
        object that holds data for our deferred work to do
    :type wq_obj: struct work_struct \*

.. _`wq_netinfo.description`:

Description
-----------

This retrieves the network interface status of the USB INIC

.. _`wq_clear_halt`:

wq_clear_halt
=============

.. c:function:: void wq_clear_halt(struct work_struct *wq_obj)

    work queue function

    :param wq_obj:
        work_struct object to execute
    :type wq_obj: struct work_struct \*

.. _`wq_clear_halt.description`:

Description
-----------

This sends a clear_halt to the given USB pipe.

.. _`hdm_probe`:

hdm_probe
=========

.. c:function:: int hdm_probe(struct usb_interface *interface, const struct usb_device_id *id)

    probe function of USB device driver

    :param interface:
        Interface of the attached USB device
    :type interface: struct usb_interface \*

    :param id:
        Pointer to the USB ID table.
    :type id: const struct usb_device_id \*

.. _`hdm_probe.description`:

Description
-----------

This allocates and initializes the device instance, adds the new
entry to the internal list, scans the USB descriptors and registers
the interface with the core.
Additionally, the DCI objects are created and the hardware is sync'd.

Return 0 on success. In case of an error a negative number is returned.

.. _`hdm_disconnect`:

hdm_disconnect
==============

.. c:function:: void hdm_disconnect(struct usb_interface *interface)

    disconnect function of USB device driver

    :param interface:
        Interface of the attached USB device
    :type interface: struct usb_interface \*

.. _`hdm_disconnect.description`:

Description
-----------

This deregisters the interface with the core, removes the kernel timer
and frees resources.

.. _`hdm_disconnect.context`:

Context
-------

hub kernel thread

.. This file was automatic generated / don't edit.


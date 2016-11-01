.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visornic/visornic_main.c

.. _`visor_copy_fragsinfo_from_skb`:

visor_copy_fragsinfo_from_skb
=============================

.. c:function:: int visor_copy_fragsinfo_from_skb(struct sk_buff *skb, unsigned int firstfraglen, unsigned int frags_max, struct phys_info frags[])

    :param struct sk_buff \*skb:
        *undescribed*

    :param unsigned int firstfraglen:
        length of first fragment in skb

    :param unsigned int frags_max:
        max len of frags array

    :param struct phys_info frags:
        frags array filled in on output

.. _`visor_copy_fragsinfo_from_skb.description`:

Description
-----------

Copy the fragment list in the SKB to a phys_info
array that the IOPART understands.
Return value indicates number of entries filled in frags
Negative values indicate an error.

.. _`visornic_serverdown_complete`:

visornic_serverdown_complete
============================

.. c:function:: void visornic_serverdown_complete(struct visornic_devdata *devdata)

    IOPART went down, pause device

    :param struct visornic_devdata \*devdata:
        *undescribed*

.. _`visornic_serverdown_complete.description`:

Description
-----------

The IO partition has gone down and we need to do some cleanup
for when it comes back. Treat the IO partition as the link
being down.
Returns void.

.. _`visornic_serverdown`:

visornic_serverdown
===================

.. c:function:: int visornic_serverdown(struct visornic_devdata *devdata, visorbus_state_complete_func complete_func)

    Command has notified us that IOPART is down

    :param struct visornic_devdata \*devdata:
        device that is being managed by IOPART

    :param visorbus_state_complete_func complete_func:
        *undescribed*

.. _`visornic_serverdown.description`:

Description
-----------

Schedule the work needed to handle the server down request. Make
sure we haven't already handled the server change state event.
Returns 0 if we scheduled the work, -EINVAL on error.

.. _`alloc_rcv_buf`:

alloc_rcv_buf
=============

.. c:function:: struct sk_buff *alloc_rcv_buf(struct net_device *netdev)

    alloc rcv buffer to be given to the IO Partition.

    :param struct net_device \*netdev:
        network adapter the rcv bufs are attached too.

.. _`alloc_rcv_buf.description`:

Description
-----------

Create an sk_buff (rcv_buf) that will be passed to the IO Partition
so that it can write rcv data into our memory space.
Return pointer to sk_buff

.. _`post_skb`:

post_skb
========

.. c:function:: void post_skb(struct uiscmdrsp *cmdrsp, struct visornic_devdata *devdata, struct sk_buff *skb)

    post a skb to the IO Partition.

    :param struct uiscmdrsp \*cmdrsp:
        cmdrsp packet to be send to the IO Partition

    :param struct visornic_devdata \*devdata:
        visornic_devdata to post the skb too

    :param struct sk_buff \*skb:
        skb to give to the IO partition

.. _`post_skb.description`:

Description
-----------

Send the skb to the IO Partition.
Returns void

.. _`send_enbdis`:

send_enbdis
===========

.. c:function:: void send_enbdis(struct net_device *netdev, int state, struct visornic_devdata *devdata)

    send NET_RCV_ENBDIS to IO Partition

    :param struct net_device \*netdev:
        netdevice we are enable/disable, used as context
        return value

    :param int state:
        enable = 1/disable = 0

    :param struct visornic_devdata \*devdata:
        visornic device we are enabling/disabling

.. _`send_enbdis.description`:

Description
-----------

Send the enable/disable message to the IO Partition.
Returns void

.. _`visornic_disable_with_timeout`:

visornic_disable_with_timeout
=============================

.. c:function:: int visornic_disable_with_timeout(struct net_device *netdev, const int timeout)

    Disable network adapter

    :param struct net_device \*netdev:
        netdevice to disale

    :param const int timeout:
        timeout to wait for disable

.. _`visornic_disable_with_timeout.description`:

Description
-----------

Disable the network adapter and inform the IO Partition that we
are disabled, reclaim memory from rcv bufs.
Returns 0 on success, negative for failure of IO Partition
responding.

.. _`init_rcv_bufs`:

init_rcv_bufs
=============

.. c:function:: int init_rcv_bufs(struct net_device *netdev, struct visornic_devdata *devdata)

    - initialize receive bufs and send them to the IO Part

    :param struct net_device \*netdev:
        struct netdevice

    :param struct visornic_devdata \*devdata:
        visornic_devdata

.. _`init_rcv_bufs.description`:

Description
-----------

Allocate rcv buffers and post them to the IO Partition.
Return 0 for success, and negative for failure.

.. _`visornic_enable_with_timeout`:

visornic_enable_with_timeout
============================

.. c:function:: int visornic_enable_with_timeout(struct net_device *netdev, const int timeout)

    send enable to IO Part

    :param struct net_device \*netdev:
        struct net_device

    :param const int timeout:
        Time to wait for the ACK from the enable

.. _`visornic_enable_with_timeout.description`:

Description
-----------

Sends enable to IOVM, inits, and posts receive buffers to IOVM
timeout is defined in msecs (timeout of 0 specifies infinite wait)
Return 0 for success, negavite for failure.

.. _`visornic_timeout_reset`:

visornic_timeout_reset
======================

.. c:function:: void visornic_timeout_reset(struct work_struct *work)

    handle xmit timeout resets \ ``work``\    work item that scheduled the work

    :param struct work_struct \*work:
        *undescribed*

.. _`visornic_timeout_reset.description`:

Description
-----------

Transmit Timeouts are typically handled by resetting the
device for our virtual NIC we will send a Disable and Enable
to the IOVM. If it doesn't respond we will trigger a serverdown.

.. _`visornic_open`:

visornic_open
=============

.. c:function:: int visornic_open(struct net_device *netdev)

    Enable the visornic device and mark the queue started

    :param struct net_device \*netdev:
        netdevice to start

.. _`visornic_open.description`:

Description
-----------

Enable the device and start the transmit queue.
Return 0 for success

.. _`visornic_close`:

visornic_close
==============

.. c:function:: int visornic_close(struct net_device *netdev)

    Disables the visornic device and stops the queues

    :param struct net_device \*netdev:
        netdevice to start

.. _`visornic_close.description`:

Description
-----------

Disable the device and stop the transmit queue.
Return 0 for success

.. _`devdata_xmits_outstanding`:

devdata_xmits_outstanding
=========================

.. c:function:: unsigned long devdata_xmits_outstanding(struct visornic_devdata *devdata)

    compute outstanding xmits

    :param struct visornic_devdata \*devdata:
        visornic_devdata for device

.. _`devdata_xmits_outstanding.description`:

Description
-----------

Return value is the number of outstanding xmits.

.. _`vnic_hit_high_watermark`:

vnic_hit_high_watermark
=======================

.. c:function:: bool vnic_hit_high_watermark(struct visornic_devdata *devdata, ulong high_watermark)

    :param struct visornic_devdata \*devdata:
        indicates visornic device we are checking

    :param ulong high_watermark:
        max num of unacked xmits we will tolerate,
        before we will start throttling

.. _`vnic_hit_high_watermark.description`:

Description
-----------

Returns true iff the number of unacked xmits sent to
the IO partition is >= high_watermark.

.. _`vnic_hit_low_watermark`:

vnic_hit_low_watermark
======================

.. c:function:: bool vnic_hit_low_watermark(struct visornic_devdata *devdata, ulong low_watermark)

    :param struct visornic_devdata \*devdata:
        indicates visornic device we are checking

    :param ulong low_watermark:
        we will wait until the num of unacked xmits
        drops to this value or lower before we start
        transmitting again

.. _`vnic_hit_low_watermark.description`:

Description
-----------

Returns true iff the number of unacked xmits sent to
the IO partition is <= low_watermark.

.. _`visornic_xmit`:

visornic_xmit
=============

.. c:function:: int visornic_xmit(struct sk_buff *skb, struct net_device *netdev)

    send a packet to the IO Partition

    :param struct sk_buff \*skb:
        Packet to be sent

    :param struct net_device \*netdev:
        net device the packet is being sent from

.. _`visornic_xmit.description`:

Description
-----------

Convert the skb to a cmdrsp so the IO Partition can undersand it.
Send the XMIT command to the IO Partition for processing. This
function is protected from concurrent calls by a spinlock xmit_lock
in the net_device struct, but as soon as the function returns it
can be called again.
Returns NETDEV_TX_OK.

.. _`visornic_get_stats`:

visornic_get_stats
==================

.. c:function:: struct net_device_stats *visornic_get_stats(struct net_device *netdev)

    returns net_stats of the visornic device

    :param struct net_device \*netdev:
        netdevice

.. _`visornic_get_stats.description`:

Description
-----------

Returns the net_device_stats for the device

.. _`visornic_change_mtu`:

visornic_change_mtu
===================

.. c:function:: int visornic_change_mtu(struct net_device *netdev, int new_mtu)

    changes mtu of device.

    :param struct net_device \*netdev:
        netdevice

    :param int new_mtu:
        value of new mtu

.. _`visornic_change_mtu.description`:

Description
-----------

MTU cannot be changed by system, must be changed via
CONTROLVM message. All vnics and pnics in a switch have
to have the same MTU for everything to work.
Currently not supported.
Returns EINVAL

.. _`visornic_set_multi`:

visornic_set_multi
==================

.. c:function:: void visornic_set_multi(struct net_device *netdev)

    changes mtu of device.

    :param struct net_device \*netdev:
        netdevice

.. _`visornic_set_multi.description`:

Description
-----------

Only flag we support currently is IFF_PROMISC
Returns void

.. _`visornic_xmit_timeout`:

visornic_xmit_timeout
=====================

.. c:function:: void visornic_xmit_timeout(struct net_device *netdev)

    request to timeout the xmit \ ``netdev``\ 

    :param struct net_device \*netdev:
        *undescribed*

.. _`visornic_xmit_timeout.description`:

Description
-----------

Queue the work and return. Make sure we have not already
been informed the IO Partition is gone, if it is gone
we will already timeout the xmits.

.. _`repost_return`:

repost_return
=============

.. c:function:: int repost_return(struct uiscmdrsp *cmdrsp, struct visornic_devdata *devdata, struct sk_buff *skb, struct net_device *netdev)

    repost rcv bufs that have come back

    :param struct uiscmdrsp \*cmdrsp:
        io channel command struct to post

    :param struct visornic_devdata \*devdata:
        visornic devdata for the device

    :param struct sk_buff \*skb:
        skb

    :param struct net_device \*netdev:
        netdevice

.. _`repost_return.description`:

Description
-----------

Repost rcv buffers that have been returned to us when
we are finished with them.
Returns 0 for success, -1 for error.

.. _`visornic_rx`:

visornic_rx
===========

.. c:function:: int visornic_rx(struct uiscmdrsp *cmdrsp)

    Handle receive packets coming back from IO Part

    :param struct uiscmdrsp \*cmdrsp:
        Receive packet returned from IO Part

.. _`visornic_rx.description`:

Description
-----------

Got a receive packet back from the IO Part, handle it and send
it up the stack.
Returns 1 iff an skb was receieved, otherwise 0

.. _`devdata_initialize`:

devdata_initialize
==================

.. c:function:: struct visornic_devdata *devdata_initialize(struct visornic_devdata *devdata, struct visor_device *dev)

    Initialize devdata structure

    :param struct visornic_devdata \*devdata:
        visornic_devdata structure to initialize
        #dev: visorbus_deviced it belongs to

    :param struct visor_device \*dev:
        *undescribed*

.. _`devdata_initialize.description`:

Description
-----------

Setup initial values for the visornic based on channel and default
values.
Returns a pointer to the devdata structure

.. _`devdata_release`:

devdata_release
===============

.. c:function:: void devdata_release(struct visornic_devdata *devdata)

    Frees up references in devdata

    :param struct visornic_devdata \*devdata:
        struct to clean up

.. _`devdata_release.description`:

Description
-----------

Frees up references in devdata.
Returns void

.. _`send_rcv_posts_if_needed`:

send_rcv_posts_if_needed
========================

.. c:function:: void send_rcv_posts_if_needed(struct visornic_devdata *devdata)

    :param struct visornic_devdata \*devdata:
        visornic device

.. _`send_rcv_posts_if_needed.description`:

Description
-----------

Send receive buffers to the IO Partition.
Returns void

.. _`drain_resp_queue`:

drain_resp_queue
================

.. c:function:: void drain_resp_queue(struct uiscmdrsp *cmdrsp, struct visornic_devdata *devdata)

    drains and ignores all messages from the resp queue

    :param struct uiscmdrsp \*cmdrsp:
        io channel command response message

    :param struct visornic_devdata \*devdata:
        visornic device to drain

.. _`service_resp_queue`:

service_resp_queue
==================

.. c:function:: void service_resp_queue(struct uiscmdrsp *cmdrsp, struct visornic_devdata *devdata, int *rx_work_done, int budget)

    drains the response queue

    :param struct uiscmdrsp \*cmdrsp:
        io channel command response message

    :param struct visornic_devdata \*devdata:
        visornic device to drain

    :param int \*rx_work_done:
        *undescribed*

    :param int budget:
        *undescribed*

.. _`service_resp_queue.description`:

Description
-----------

Drain the respones queue of any responses from the IO partition.
Process the responses as we get them.
Returns when response queue is empty or when the thread stops.

.. _`poll_for_irq`:

poll_for_irq
============

.. c:function:: void poll_for_irq(unsigned long v)

    Checks the status of the response queue.

    :param unsigned long v:
        void pointer to the visronic devdata

.. _`poll_for_irq.description`:

Description
-----------

Main function of the vnic_incoming thread. Peridocially check the
response queue and drain it if needed.
Returns when thread has stopped.

.. _`visornic_probe`:

visornic_probe
==============

.. c:function:: int visornic_probe(struct visor_device *dev)

    probe function for visornic devices

    :param struct visor_device \*dev:
        The visor device discovered

.. _`visornic_probe.description`:

Description
-----------

Called when visorbus discovers a visornic device on its
bus. It creates a new visornic ethernet adapter.
Returns 0 or negative for error.

.. _`host_side_disappeared`:

host_side_disappeared
=====================

.. c:function:: void host_side_disappeared(struct visornic_devdata *devdata)

    IO part is gone.

    :param struct visornic_devdata \*devdata:
        device object

.. _`host_side_disappeared.description`:

Description
-----------

IO partition servicing this device is gone, do cleanup
Returns void.

.. _`visornic_remove`:

visornic_remove
===============

.. c:function:: void visornic_remove(struct visor_device *dev)

    Called when visornic dev goes away

    :param struct visor_device \*dev:
        visornic device that is being removed

.. _`visornic_remove.description`:

Description
-----------

Called when DEVICE_DESTROY gets called to remove device.
Returns void

.. _`visornic_pause`:

visornic_pause
==============

.. c:function:: int visornic_pause(struct visor_device *dev, visorbus_state_complete_func complete_func)

    Called when IO Part disappears

    :param struct visor_device \*dev:
        visornic device that is being serviced

    :param visorbus_state_complete_func complete_func:
        call when finished.

.. _`visornic_pause.description`:

Description
-----------

Called when the IO Partition has gone down. Need to free
up resources and wait for IO partition to come back. Mark
link as down and don't attempt any DMA. When we have freed
memory call the complete_func so that Command knows we are
done. If we don't call complete_func, IO part will never
come back.
Returns 0 for success.

.. _`visornic_resume`:

visornic_resume
===============

.. c:function:: int visornic_resume(struct visor_device *dev, visorbus_state_complete_func complete_func)

    Called when IO part has recovered

    :param struct visor_device \*dev:
        visornic device that is being serviced

    :param visorbus_state_complete_func complete_func:
        *undescribed*

.. _`visornic_resume.description`:

Description
-----------

Called when the IO partition has recovered. Reestablish
connection to the IO part and set the link up. Okay to do
DMA again.
Returns 0 for success.

.. _`visornic_init`:

visornic_init
=============

.. c:function:: int visornic_init( void)

    Init function

    :param  void:
        no arguments

.. _`visornic_init.description`:

Description
-----------

Init function for the visornic driver. Do initial driver setup
and wait for devices.
Returns 0 for success, negative for error.

.. _`visornic_cleanup`:

visornic_cleanup
================

.. c:function:: void visornic_cleanup( void)

    driver exit routine

    :param  void:
        no arguments

.. _`visornic_cleanup.description`:

Description
-----------

Unregister driver from the bus and free up memory.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wimax/i2400m/i2400m-usb.h

.. _`edc_inc`:

edc_inc
=======

.. c:function:: int edc_inc(struct edc *edc, u16 max_err, u16 timeframe)

    report a soft error and check if we are over the watermark

    :param struct edc \*edc:
        pointer to error density counter.

    :param u16 max_err:
        maximum number of errors we can accept over the timeframe

    :param u16 timeframe:
        length of the timeframe (in jiffies).

.. _`edc_inc.return`:

Return
------

!0 1 if maximum acceptable errors per timeframe has been
exceeded. 0 otherwise.

This is way to determine if the number of acceptable errors per time
period has been exceeded. It is not accurate as there are cases in which
this scheme will not work, for example if there are periodic occurrences
of errors that straddle updates to the start time. This scheme is
sufficient for our usage.

To use, embed a 'struct edc' somewhere, initialize it with
\ :c:func:`edc_init`\  and when an error hits:

if (do_something_fails_with_a_soft_error) {
if (edc_inc(&my->edc, MAX_ERRORS, MAX_TIMEFRAME))
Ops, hard error, do something about it
else
Retry or ignore, depending on whatever
}

.. _`i2400mu`:

struct i2400mu
==============

.. c:type:: struct i2400mu

    descriptor for a USB connected i2400m

.. _`i2400mu.definition`:

Definition
----------

.. code-block:: c

    struct i2400mu {
        struct i2400m i2400m;
        struct usb_device *usb_dev;
        struct usb_interface *usb_iface;
        struct edc urb_edc;
        struct i2400m_endpoint_cfg endpoint_cfg;
        struct urb *notif_urb;
        struct task_struct *tx_kthread;
        wait_queue_head_t tx_wq;
        struct task_struct *rx_kthread;
        wait_queue_head_t rx_wq;
        atomic_t rx_pending_count;
        size_t rx_size;
        size_t rx_size_acc;
        size_t rx_size_cnt;
        atomic_t do_autopm;
        u8 rx_size_auto_shrink;
        struct dentry *debugfs_dentry;
        unsigned i6050:1;
    }

.. _`i2400mu.members`:

Members
-------

i2400m
    bus-generic i2400m implementation; has to be first (see
    it's documentation in i2400m.h).

usb_dev
    pointer to our USB device

usb_iface
    pointer to our USB interface

urb_edc
    error density counter; used to keep a density-on-time tab
    on how many soft (retryable or ignorable) errors we get. If we
    go over the threshold, we consider the bus transport is failing
    too much and reset.

endpoint_cfg
    *undescribed*

notif_urb
    URB for receiving notifications from the device.

tx_kthread
    thread we use for data TX. We use a thread because in
    order to do deep power saving and put the device to sleep, we
    need to call usb_autopm\_\*() [blocking functions].

tx_wq
    waitqueue for the TX kthread to sleep when there is no data
    to be sent; when more data is available, it is woken up by
    \ :c:func:`i2400mu_bus_tx_kick`\ .

rx_kthread
    thread we use for data RX. We use a thread because in
    order to do deep power saving and put the device to sleep, we
    need to call usb_autopm\_\*() [blocking functions].

rx_wq
    waitqueue for the RX kthread to sleep when there is no data
    to receive. When data is available, it is woken up by
    usb-notif.c:i2400mu_notification_grok().

rx_pending_count
    number of rx-data-ready notifications that were
    still not handled by the RX kthread.

rx_size
    current RX buffer size that is being used.

rx_size_acc
    accumulator of the sizes of the previous read
    transactions.

rx_size_cnt
    number of read transactions accumulated in
    \ ``rx_size_acc``\ .

do_autopm
    disable(0)/enable(>0) calling the
    usb_autopm_get/put_interface() barriers when executing
    commands. See doc in \ :c:func:`i2400mu_suspend`\  for more information.

rx_size_auto_shrink
    if true, the rx_size is shrunk
    automatically based on the average size of the received
    transactions. This allows the receive code to allocate smaller
    chunks of memory and thus reduce pressure on the memory
    allocator by not wasting so much space. By default it is
    enabled.

debugfs_dentry
    hookup for debugfs files.
    These have to be in a separate directory, a child of
    (wimax_dev->debugfs_dentry) so they can be removed when the
    module unloads, as we don't keep each dentry.

i6050
    *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wimax/i2400m/control.c

.. _`i2400m_msg_to_dev`:

i2400m_msg_to_dev
=================

.. c:function:: struct sk_buff *i2400m_msg_to_dev(struct i2400m *i2400m, const void *buf, size_t buf_len)

    Send a control message to the device and get a response

    :param struct i2400m \*i2400m:
        device descriptor

    :param const void \*buf:
        pointer to the buffer containing the message to be sent; it
        has to start with a \ :c:type:`struct i2400M_l3l4_hdr <i2400M_l3l4_hdr>`\  and then
        followed by the payload. Once this function returns, the
        buffer can be reused.

    :param size_t buf_len:
        buffer size

.. _`i2400m_msg_to_dev.return`:

Return
------


Pointer to skb containing the ack message. You need to check the
pointer with \ :c:func:`IS_ERR`\ , as it might be an error code. Error codes

.. _`i2400m_msg_to_dev.could-happen-because`:

could happen because
--------------------


- the message wasn't formatted correctly
- couldn't send the message
- failed waiting for a response
- the ack message wasn't formatted correctly

The returned skb has been allocated with \ :c:func:`wimax_msg_to_user_alloc`\ ,
it contains the response in a netlink attribute and is ready to be
passed up to user space with \ :c:func:`wimax_msg_to_user_send`\ . To access
the payload and its length, use wimax_msg_{data,len}() on the skb.

The skb has to be freed with \ :c:func:`kfree_skb`\  once done.

.. _`i2400m_msg_to_dev.description`:

Description
-----------


This function delivers a message/command to the device and waits
for an ack to be received. The format is described in
linux/wimax/i2400m.h. In summary, a command/get/set is followed by an
ack.

This function will not check the ack status, that's left up to the
caller.  Once done with the ack skb, it has to be \ :c:func:`kfree_skb`\ ed.

The i2400m handles only one message at the same time, thus we need
the mutex to exclude other players.

We write the message and then wait for an answer to come back. The
RX path intercepts control messages and handles them in
\ :c:func:`i2400m_rx_ctl`\ . Reports (notifications) are (maybe) processed
locally and then forwarded (as needed) to user space on the WiMAX
stack message pipe. Acks are saved and passed back to us through an
skb in i2400m->ack_skb which is ready to be given to generic
netlink if need be.

.. _`i2400m_get_device_info`:

i2400m_get_device_info
======================

.. c:function:: struct sk_buff *i2400m_get_device_info(struct i2400m *i2400m)

    Query the device for detailed device information

    :param struct i2400m \*i2400m:
        device descriptor

.. _`i2400m_get_device_info.return`:

Return
------

an skb whose skb->data points to a 'struct
i2400m_tlv_detailed_device_info'. When done, \ :c:func:`kfree_skb`\  it. The
skb is \*guaranteed\* to contain the whole TLV data structure.

On error, IS_ERR(skb) is true and ERR_PTR(skb) is the error
code.

.. _`i2400m_firmware_check`:

i2400m_firmware_check
=====================

.. c:function:: int i2400m_firmware_check(struct i2400m *i2400m)

    check firmware versions are compatible with the driver

    :param struct i2400m \*i2400m:
        device descriptor

.. _`i2400m_firmware_check.return`:

Return
------

0 if ok, < 0 errno code an error and a message in the
kernel log.

Long function, but quite simple; first chunk launches the command
and double checks the reply for the right TLV. Then we process the
TLV (where the meat is).

Once we process the TLV that gives us the firmware's interface
version, we encode it and save it in i2400m->fw_version for future
reference.

.. _`i2400m_set_init_config`:

i2400m_set_init_config
======================

.. c:function:: int i2400m_set_init_config(struct i2400m *i2400m, const struct i2400m_tlv_hdr **arg, size_t args)

    :param struct i2400m \*i2400m:
        device descriptor

    :param const struct i2400m_tlv_hdr \*\*arg:
        *undescribed*

    :param size_t args:
        array of pointers to the TLV headers to send for
        configuration (each followed by its payload).
        TLV headers and payloads must be properly initialized, with the
        right endianess (LE).

.. _`i2400m_set_idle_timeout`:

i2400m_set_idle_timeout
=======================

.. c:function:: int i2400m_set_idle_timeout(struct i2400m *i2400m, unsigned msecs)

    Set the device's idle mode timeout

    :param struct i2400m \*i2400m:
        i2400m device descriptor

    :param unsigned msecs:
        milliseconds for the timeout to enter idle mode. Between
        100 to 300000 (5m); 0 to disable. In increments of 100.

.. _`i2400m_set_idle_timeout.description`:

Description
-----------

After this \ ``msecs``\  of the link being idle (no data being sent or
received), the device will negotiate with the basestation entering
idle mode for saving power. The connection is maintained, but
getting out of it (done in tx.c) will require some negotiation,
possible crypto re-handshake and a possible DHCP re-lease.

Only available if fw_version >= 0x00090002.

.. _`i2400m_set_idle_timeout.return`:

Return
------

0 if ok, < 0 errno code on error.

.. _`i2400m_dev_initialize`:

i2400m_dev_initialize
=====================

.. c:function:: int i2400m_dev_initialize(struct i2400m *i2400m)

    Initialize the device once communications are ready

    :param struct i2400m \*i2400m:
        device descriptor

.. _`i2400m_dev_initialize.return`:

Return
------

0 if ok, < 0 errno code on error.

Configures the device to work the way we like it.

At the point of this call, the device is registered with the WiMAX
and netdev stacks, firmware is uploaded and we can talk to the
device normally.

.. _`i2400m_dev_shutdown`:

i2400m_dev_shutdown
===================

.. c:function:: void i2400m_dev_shutdown(struct i2400m *i2400m)

    Shutdown a running device

    :param struct i2400m \*i2400m:
        device descriptor

.. _`i2400m_dev_shutdown.description`:

Description
-----------

Release resources acquired during the running of the device; in
theory, should also tell the device to go to sleep, switch off the
radio, all that, but at this point, in most cases (driver
disconnection, reset handling) we can't even talk to the device.

.. This file was automatic generated / don't edit.


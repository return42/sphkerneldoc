.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/rpmsg_core.c

.. _`rpmsg_create_ept`:

rpmsg_create_ept
================

.. c:function:: struct rpmsg_endpoint *rpmsg_create_ept(struct rpmsg_device *rpdev, rpmsg_rx_cb_t cb, void *priv, struct rpmsg_channel_info chinfo)

    create a new rpmsg_endpoint

    :param rpdev:
        rpmsg channel device
    :type rpdev: struct rpmsg_device \*

    :param cb:
        rx callback handler
    :type cb: rpmsg_rx_cb_t

    :param priv:
        private data for the driver's use
    :type priv: void \*

    :param chinfo:
        channel_info with the local rpmsg address to bind with \ ``cb``\ 
    :type chinfo: struct rpmsg_channel_info

.. _`rpmsg_create_ept.description`:

Description
-----------

Every rpmsg address in the system is bound to an rx callback (so when
inbound messages arrive, they are dispatched by the rpmsg bus using the
appropriate callback handler) by means of an rpmsg_endpoint struct.

This function allows drivers to create such an endpoint, and by that,
bind a callback, and possibly some private data too, to an rpmsg address
(either one that is known in advance, or one that will be dynamically
assigned for them).

Simple rpmsg drivers need not call rpmsg_create_ept, because an endpoint
is already created for them when they are probed by the rpmsg bus
(using the rx callback provided when they registered to the rpmsg bus).

.. _`rpmsg_create_ept.so-things-should-just-work-for-simple-drivers`:

So things should just work for simple drivers
---------------------------------------------

they already have an
endpoint, their rx callback is bound to their rpmsg address, and when
relevant inbound messages arrive (i.e. messages which their dst address
equals to the src address of their rpmsg channel), the driver's handler
is invoked to process it.

That said, more complicated drivers might do need to allocate
additional rpmsg addresses, and bind them to different rx callbacks.
To accomplish that, those drivers need to call this function.

Drivers should provide their \ ``rpdev``\  channel (so the new endpoint would belong
to the same remote processor their channel belongs to), an rx callback
function, an optional private data (which is provided back when the
rx callback is invoked), and an address they want to bind with the
callback. If \ ``addr``\  is RPMSG_ADDR_ANY, then rpmsg_create_ept will
dynamically assign them an available rpmsg address (drivers should have
a very good reason why not to always use RPMSG_ADDR_ANY here).

Returns a pointer to the endpoint on success, or NULL on error.

.. _`rpmsg_destroy_ept`:

rpmsg_destroy_ept
=================

.. c:function:: void rpmsg_destroy_ept(struct rpmsg_endpoint *ept)

    destroy an existing rpmsg endpoint

    :param ept:
        endpoing to destroy
    :type ept: struct rpmsg_endpoint \*

.. _`rpmsg_destroy_ept.description`:

Description
-----------

Should be used by drivers to destroy an rpmsg endpoint previously
created with \ :c:func:`rpmsg_create_ept`\ . As with other types of "free" NULL
is a valid parameter.

.. _`rpmsg_send`:

rpmsg_send
==========

.. c:function:: int rpmsg_send(struct rpmsg_endpoint *ept, void *data, int len)

    send a message across to the remote processor

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

.. _`rpmsg_send.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  on the \ ``ept``\  endpoint.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to, using \ ``ept``\ 's address and its associated rpmsg
device destination addresses.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`rpmsg_sendto`:

rpmsg_sendto
============

.. c:function:: int rpmsg_sendto(struct rpmsg_endpoint *ept, void *data, int len, u32 dst)

    send a message across to the remote processor, specify dst

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

    :param dst:
        destination address
    :type dst: u32

.. _`rpmsg_sendto.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  to the remote \ ``dst``\  address.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to, using \ ``ept``\ 's address as source.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`rpmsg_send_offchannel`:

rpmsg_send_offchannel
=====================

.. c:function:: int rpmsg_send_offchannel(struct rpmsg_endpoint *ept, u32 src, u32 dst, void *data, int len)

    send a message using explicit src/dst addresses

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param src:
        source address
    :type src: u32

    :param dst:
        destination address
    :type dst: u32

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

.. _`rpmsg_send_offchannel.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  to the remote \ ``dst``\  address,
and uses \ ``src``\  as the source address.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`rpmsg_trysend`:

rpmsg_trysend
=============

.. c:function:: int rpmsg_trysend(struct rpmsg_endpoint *ept, void *data, int len)

    send a message across to the remote processor

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

.. _`rpmsg_trysend.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  on the \ ``ept``\  endpoint.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to, using \ ``ept``\ 's address as source and its associated
rpdev's address as destination.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`rpmsg_trysendto`:

rpmsg_trysendto
===============

.. c:function:: int rpmsg_trysendto(struct rpmsg_endpoint *ept, void *data, int len, u32 dst)

    send a message across to the remote processor, specify dst

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

    :param dst:
        destination address
    :type dst: u32

.. _`rpmsg_trysendto.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  to the remote \ ``dst``\  address.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to, using \ ``ept``\ 's address as source.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`rpmsg_poll`:

rpmsg_poll
==========

.. c:function:: __poll_t rpmsg_poll(struct rpmsg_endpoint *ept, struct file *filp, poll_table *wait)

    poll the endpoint's send buffers

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param filp:
        file for \ :c:func:`poll_wait`\ 
    :type filp: struct file \*

    :param wait:
        poll_table for \ :c:func:`poll_wait`\ 
    :type wait: poll_table \*

.. _`rpmsg_poll.description`:

Description
-----------

Returns mask representing the current state of the endpoint's send buffers

.. _`rpmsg_trysend_offchannel`:

rpmsg_trysend_offchannel
========================

.. c:function:: int rpmsg_trysend_offchannel(struct rpmsg_endpoint *ept, u32 src, u32 dst, void *data, int len)

    send a message using explicit src/dst addresses

    :param ept:
        the rpmsg endpoint
    :type ept: struct rpmsg_endpoint \*

    :param src:
        source address
    :type src: u32

    :param dst:
        destination address
    :type dst: u32

    :param data:
        payload of message
    :type data: void \*

    :param len:
        length of payload
    :type len: int

.. _`rpmsg_trysend_offchannel.description`:

Description
-----------

This function sends \ ``data``\  of length \ ``len``\  to the remote \ ``dst``\  address,
and uses \ ``src``\  as the source address.
The message will be sent to the remote processor which the \ ``ept``\ 
endpoint belongs to.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

.. _`__register_rpmsg_driver`:

\__register_rpmsg_driver
========================

.. c:function:: int __register_rpmsg_driver(struct rpmsg_driver *rpdrv, struct module *owner)

    register an rpmsg driver with the rpmsg bus

    :param rpdrv:
        pointer to a struct rpmsg_driver
    :type rpdrv: struct rpmsg_driver \*

    :param owner:
        owning module/driver
    :type owner: struct module \*

.. _`__register_rpmsg_driver.description`:

Description
-----------

Returns 0 on success, and an appropriate error value on failure.

.. _`unregister_rpmsg_driver`:

unregister_rpmsg_driver
=======================

.. c:function:: void unregister_rpmsg_driver(struct rpmsg_driver *rpdrv)

    unregister an rpmsg driver from the rpmsg bus

    :param rpdrv:
        pointer to a struct rpmsg_driver
    :type rpdrv: struct rpmsg_driver \*

.. _`unregister_rpmsg_driver.description`:

Description
-----------

Returns 0 on success, and an appropriate error value on failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hsi/hsi_core.c

.. _`hsi_port_unregister_clients`:

hsi_port_unregister_clients
===========================

.. c:function:: void hsi_port_unregister_clients(struct hsi_port *port)

    Unregister an HSI port

    :param port:
        The HSI port to unregister
    :type port: struct hsi_port \*

.. _`hsi_unregister_controller`:

hsi_unregister_controller
=========================

.. c:function:: void hsi_unregister_controller(struct hsi_controller *hsi)

    Unregister an HSI controller

    :param hsi:
        The HSI controller to register
    :type hsi: struct hsi_controller \*

.. _`hsi_register_controller`:

hsi_register_controller
=======================

.. c:function:: int hsi_register_controller(struct hsi_controller *hsi)

    Register an HSI controller and its ports

    :param hsi:
        The HSI controller to register
    :type hsi: struct hsi_controller \*

.. _`hsi_register_controller.description`:

Description
-----------

Returns -errno on failure, 0 on success.

.. _`hsi_register_client_driver`:

hsi_register_client_driver
==========================

.. c:function:: int hsi_register_client_driver(struct hsi_client_driver *drv)

    Register an HSI client to the HSI bus

    :param drv:
        HSI client driver to register
    :type drv: struct hsi_client_driver \*

.. _`hsi_register_client_driver.description`:

Description
-----------

Returns -errno on failure, 0 on success.

.. _`hsi_put_controller`:

hsi_put_controller
==================

.. c:function:: void hsi_put_controller(struct hsi_controller *hsi)

    Free an HSI controller

    :param hsi:
        Pointer to the HSI controller to freed
    :type hsi: struct hsi_controller \*

.. _`hsi_put_controller.description`:

Description
-----------

HSI controller drivers should only use this function if they need
to free their allocated hsi_controller structures before a successful
call to hsi_register_controller. Other use is not allowed.

.. _`hsi_alloc_controller`:

hsi_alloc_controller
====================

.. c:function:: struct hsi_controller *hsi_alloc_controller(unsigned int n_ports, gfp_t flags)

    Allocate an HSI controller and its ports

    :param n_ports:
        Number of ports on the HSI controller
    :type n_ports: unsigned int

    :param flags:
        Kernel allocation flags
    :type flags: gfp_t

.. _`hsi_alloc_controller.description`:

Description
-----------

Return NULL on failure or a pointer to an hsi_controller on success.

.. _`hsi_free_msg`:

hsi_free_msg
============

.. c:function:: void hsi_free_msg(struct hsi_msg *msg)

    Free an HSI message

    :param msg:
        Pointer to the HSI message
    :type msg: struct hsi_msg \*

.. _`hsi_free_msg.description`:

Description
-----------

Client is responsible to free the buffers pointed by the scatterlists.

.. _`hsi_alloc_msg`:

hsi_alloc_msg
=============

.. c:function:: struct hsi_msg *hsi_alloc_msg(unsigned int nents, gfp_t flags)

    Allocate an HSI message

    :param nents:
        Number of memory entries
    :type nents: unsigned int

    :param flags:
        Kernel allocation flags
    :type flags: gfp_t

.. _`hsi_alloc_msg.description`:

Description
-----------

nents can be 0. This mainly makes sense for read transfer.
In that case, HSI drivers will call the complete callback when
there is data to be read without consuming it.

Return NULL on failure or a pointer to an hsi_msg on success.

.. _`hsi_async`:

hsi_async
=========

.. c:function:: int hsi_async(struct hsi_client *cl, struct hsi_msg *msg)

    Submit an HSI transfer to the controller

    :param cl:
        HSI client sending the transfer
    :type cl: struct hsi_client \*

    :param msg:
        The HSI transfer passed to controller
    :type msg: struct hsi_msg \*

.. _`hsi_async.description`:

Description
-----------

The HSI message must have the channel, ttype, complete and destructor
fields set beforehand. If nents > 0 then the client has to initialize
also the scatterlists to point to the buffers to write to or read from.

HSI controllers relay on pre-allocated buffers from their clients and they
do not allocate buffers on their own.

Once the HSI message transfer finishes, the HSI controller calls the
complete callback with the status and actual_len fields of the HSI message
updated. The complete callback can be called before returning from
hsi_async.

Returns -errno on failure or 0 on success

.. _`hsi_claim_port`:

hsi_claim_port
==============

.. c:function:: int hsi_claim_port(struct hsi_client *cl, unsigned int share)

    Claim the HSI client's port

    :param cl:
        HSI client that wants to claim its port
    :type cl: struct hsi_client \*

    :param share:
        Flag to indicate if the client wants to share the port or not.
    :type share: unsigned int

.. _`hsi_claim_port.description`:

Description
-----------

Returns -errno on failure, 0 on success.

.. _`hsi_release_port`:

hsi_release_port
================

.. c:function:: void hsi_release_port(struct hsi_client *cl)

    Release the HSI client's port

    :param cl:
        HSI client which previously claimed its port
    :type cl: struct hsi_client \*

.. _`hsi_register_port_event`:

hsi_register_port_event
=======================

.. c:function:: int hsi_register_port_event(struct hsi_client *cl, void (*handler)(struct hsi_client *, unsigned long))

    Register a client to receive port events

    :param cl:
        HSI client that wants to receive port events
    :type cl: struct hsi_client \*

    :param void (\*handler)(struct hsi_client \*, unsigned long):
        Event handler callback

.. _`hsi_register_port_event.description`:

Description
-----------

Clients should register a callback to be able to receive
events from the ports. Registration should happen after
claiming the port.
The handler can be called in interrupt context.

Returns -errno on error, or 0 on success.

.. _`hsi_unregister_port_event`:

hsi_unregister_port_event
=========================

.. c:function:: int hsi_unregister_port_event(struct hsi_client *cl)

    Stop receiving port events for a client

    :param cl:
        HSI client that wants to stop receiving port events
    :type cl: struct hsi_client \*

.. _`hsi_unregister_port_event.description`:

Description
-----------

Clients should call this function before releasing their associated
port.

Returns -errno on error, or 0 on success.

.. _`hsi_event`:

hsi_event
=========

.. c:function:: int hsi_event(struct hsi_port *port, unsigned long event)

    Notifies clients about port events

    :param port:
        Port where the event occurred
    :type port: struct hsi_port \*

    :param event:
        The event type
    :type event: unsigned long

.. _`hsi_event.description`:

Description
-----------

Clients should not be concerned about wake line behavior. However, due
to a race condition in HSI HW protocol, clients need to be notified
about wake line changes, so they can implement a workaround for it.

.. _`hsi_event.events`:

Events
------

HSI_EVENT_START_RX - Incoming wake line high
HSI_EVENT_STOP_RX - Incoming wake line down

Returns -errno on error, or 0 on success.

.. _`hsi_get_channel_id_by_name`:

hsi_get_channel_id_by_name
==========================

.. c:function:: int hsi_get_channel_id_by_name(struct hsi_client *cl, char *name)

    acquire channel id by channel name

    :param cl:
        HSI client, which uses the channel
    :type cl: struct hsi_client \*

    :param name:
        name the channel is known under
    :type name: char \*

.. _`hsi_get_channel_id_by_name.description`:

Description
-----------

Clients can call this function to get the hsi channel ids similar to
requesting IRQs or GPIOs by name. This function assumes the same
channel configuration is used for RX and TX.

Returns -errno on error or channel id on success.

.. This file was automatic generated / don't edit.


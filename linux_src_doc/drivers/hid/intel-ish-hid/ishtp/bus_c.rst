.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/bus.c

.. _`ishtp_recv`:

ishtp_recv
==========

.. c:function:: void ishtp_recv(struct ishtp_device *dev)

    process ishtp message

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

.. _`ishtp_recv.description`:

Description
-----------

If a message with valid header and size is received, then
this function calls appropriate handler. The host or firmware
address is zero, then they are host bus management message,
otherwise they are message fo clients.

.. _`ishtp_send_msg`:

ishtp_send_msg
==============

.. c:function:: int ishtp_send_msg(struct ishtp_device *dev, struct ishtp_msg_hdr *hdr, void *msg, void(*ipc_send_compl)(void *), void *ipc_send_compl_prm)

    Send ishtp message

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

    :param hdr:
        Message header
    :type hdr: struct ishtp_msg_hdr \*

    :param msg:
        Message contents
    :type msg: void \*

    :param void(\*ipc_send_compl)(void \*):
        completion callback

    :param ipc_send_compl_prm:
        completion callback parameter
    :type ipc_send_compl_prm: void \*

.. _`ishtp_send_msg.description`:

Description
-----------

Send a multi fragment message via IPC. After sending the first fragment
the completion callback is called to schedule transmit of next fragment.

.. _`ishtp_send_msg.return`:

Return
------

This returns IPC send message status.

.. _`ishtp_write_message`:

ishtp_write_message
===================

.. c:function:: int ishtp_write_message(struct ishtp_device *dev, struct ishtp_msg_hdr *hdr, unsigned char *buf)

    Send ishtp single fragment message

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

    :param hdr:
        Message header
    :type hdr: struct ishtp_msg_hdr \*

    :param buf:
        message data
    :type buf: unsigned char \*

.. _`ishtp_write_message.description`:

Description
-----------

Send a single fragment message via IPC.  This returns IPC send message
status.

.. _`ishtp_write_message.return`:

Return
------

This returns IPC send message status.

.. _`ishtp_fw_cl_by_uuid`:

ishtp_fw_cl_by_uuid
===================

.. c:function:: int ishtp_fw_cl_by_uuid(struct ishtp_device *dev, const uuid_le *uuid)

    locate index of fw client

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

    :param uuid:
        uuid of the client to search
    :type uuid: const uuid_le \*

.. _`ishtp_fw_cl_by_uuid.description`:

Description
-----------

Search firmware client using UUID.

.. _`ishtp_fw_cl_by_uuid.return`:

Return
------

fw client index or -ENOENT if not found

.. _`ishtp_fw_cl_get_client`:

ishtp_fw_cl_get_client
======================

.. c:function:: struct ishtp_fw_client *ishtp_fw_cl_get_client(struct ishtp_device *dev, const uuid_le *uuid)

    return client information to client

    :param dev:
        the ishtp device structure
    :type dev: struct ishtp_device \*

    :param uuid:
        uuid of the client to search
    :type uuid: const uuid_le \*

.. _`ishtp_fw_cl_get_client.description`:

Description
-----------

Search firmware client using UUID and reture related client information.

.. _`ishtp_fw_cl_get_client.return`:

Return
------

pointer of client information on success, NULL on failure.

.. _`ishtp_fw_cl_by_id`:

ishtp_fw_cl_by_id
=================

.. c:function:: int ishtp_fw_cl_by_id(struct ishtp_device *dev, uint8_t client_id)

    return index to fw_clients for client_id

    :param dev:
        the ishtp device structure
    :type dev: struct ishtp_device \*

    :param client_id:
        fw client id to search
    :type client_id: uint8_t

.. _`ishtp_fw_cl_by_id.description`:

Description
-----------

Search firmware client using client id.

.. _`ishtp_fw_cl_by_id.return`:

Return
------

index on success, -ENOENT on failure.

.. _`ishtp_cl_device_probe`:

ishtp_cl_device_probe
=====================

.. c:function:: int ishtp_cl_device_probe(struct device *dev)

    Bus \ :c:func:`probe`\  callback

    :param dev:
        the device structure
    :type dev: struct device \*

.. _`ishtp_cl_device_probe.description`:

Description
-----------

This is a bus probe callback and calls the drive probe function.

.. _`ishtp_cl_device_probe.return`:

Return
------

Return value from driver \ :c:func:`probe`\  call.

.. _`ishtp_cl_device_remove`:

ishtp_cl_device_remove
======================

.. c:function:: int ishtp_cl_device_remove(struct device *dev)

    Bus \ :c:func:`remove`\  callback

    :param dev:
        the device structure
    :type dev: struct device \*

.. _`ishtp_cl_device_remove.description`:

Description
-----------

This is a bus remove callback and calls the drive remove function.
Since the ISH driver model supports only built in, this is
primarily can be called during pci driver init failure.

.. _`ishtp_cl_device_remove.return`:

Return
------

Return value from driver \ :c:func:`remove`\  call.

.. _`ishtp_cl_device_suspend`:

ishtp_cl_device_suspend
=======================

.. c:function:: int ishtp_cl_device_suspend(struct device *dev)

    Bus suspend callback

    :param dev:
        device
    :type dev: struct device \*

.. _`ishtp_cl_device_suspend.description`:

Description
-----------

Called during device suspend process.

.. _`ishtp_cl_device_suspend.return`:

Return
------

Return value from driver \ :c:func:`suspend`\  call.

.. _`ishtp_cl_device_resume`:

ishtp_cl_device_resume
======================

.. c:function:: int ishtp_cl_device_resume(struct device *dev)

    Bus resume callback

    :param dev:
        device
    :type dev: struct device \*

.. _`ishtp_cl_device_resume.description`:

Description
-----------

Called during device resume process.

.. _`ishtp_cl_device_resume.return`:

Return
------

Return value from driver \ :c:func:`resume`\  call.

.. _`ishtp_cl_device_reset`:

ishtp_cl_device_reset
=====================

.. c:function:: int ishtp_cl_device_reset(struct ishtp_cl_device *device)

    Reset callback

    :param device:
        ishtp client device instance
    :type device: struct ishtp_cl_device \*

.. _`ishtp_cl_device_reset.description`:

Description
-----------

This is a callback when HW reset is done and the device need
reinit.

.. _`ishtp_cl_device_reset.return`:

Return
------

Return value from driver \ :c:func:`reset`\  call.

.. _`ishtp_bus_add_device`:

ishtp_bus_add_device
====================

.. c:function:: struct ishtp_cl_device *ishtp_bus_add_device(struct ishtp_device *dev, uuid_le uuid, char *name)

    Function to create device on bus

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

    :param uuid:
        uuid of the client
    :type uuid: uuid_le

    :param name:
        Name of the client
    :type name: char \*

.. _`ishtp_bus_add_device.description`:

Description
-----------

Allocate ISHTP bus client device, attach it to uuid
and register with ISHTP bus.

.. _`ishtp_bus_add_device.return`:

Return
------

ishtp_cl_device pointer or NULL on failure

.. _`ishtp_bus_remove_device`:

ishtp_bus_remove_device
=======================

.. c:function:: void ishtp_bus_remove_device(struct ishtp_cl_device *device)

    Function to relase device on bus

    :param device:
        client device instance
    :type device: struct ishtp_cl_device \*

.. _`ishtp_bus_remove_device.description`:

Description
-----------

This is a counterpart of ishtp_bus_add_device.
Device is unregistered.
the device structure is freed in 'ishtp_cl_dev_release' function
Called only during error in pci driver init path.

.. _`__ishtp_cl_driver_register`:

\__ishtp_cl_driver_register
===========================

.. c:function:: int __ishtp_cl_driver_register(struct ishtp_cl_driver *driver, struct module *owner)

    Client driver register

    :param driver:
        the client driver instance
    :type driver: struct ishtp_cl_driver \*

    :param owner:
        Owner of this driver module
    :type owner: struct module \*

.. _`__ishtp_cl_driver_register.description`:

Description
-----------

Once a client driver is probed, it created a client
instance and registers with the bus.

.. _`__ishtp_cl_driver_register.return`:

Return
------

Return value of driver_register or -ENODEV if not ready

.. _`ishtp_cl_driver_unregister`:

ishtp_cl_driver_unregister
==========================

.. c:function:: void ishtp_cl_driver_unregister(struct ishtp_cl_driver *driver)

    Client driver unregister

    :param driver:
        the client driver instance
    :type driver: struct ishtp_cl_driver \*

.. _`ishtp_cl_driver_unregister.description`:

Description
-----------

Unregister client during device removal process.

.. _`ishtp_bus_event_work`:

ishtp_bus_event_work
====================

.. c:function:: void ishtp_bus_event_work(struct work_struct *work)

    event work function

    :param work:
        work struct pointer
    :type work: struct work_struct \*

.. _`ishtp_bus_event_work.description`:

Description
-----------

Once an event is received for a client this work
function is called. If the device has registered a
callback then the callback is called.

.. _`ishtp_cl_bus_rx_event`:

ishtp_cl_bus_rx_event
=====================

.. c:function:: void ishtp_cl_bus_rx_event(struct ishtp_cl_device *device)

    schedule event work

    :param device:
        client device instance
    :type device: struct ishtp_cl_device \*

.. _`ishtp_cl_bus_rx_event.description`:

Description
-----------

Once an event is received for a client this schedules
a work function to process.

.. _`ishtp_register_event_cb`:

ishtp_register_event_cb
=======================

.. c:function:: int ishtp_register_event_cb(struct ishtp_cl_device *device, void (*event_cb)(struct ishtp_cl_device *))

    Register callback

    :param device:
        client device instance
    :type device: struct ishtp_cl_device \*

    :param void (\*event_cb)(struct ishtp_cl_device \*):
        Event processor for an client

.. _`ishtp_register_event_cb.description`:

Description
-----------

Register a callback for events, called from client driver

.. _`ishtp_register_event_cb.return`:

Return
------

Return 0 or -EALREADY if already registered

.. _`ishtp_get_device`:

ishtp_get_device
================

.. c:function:: void ishtp_get_device(struct ishtp_cl_device *cl_device)

    update usage count for the device

    :param cl_device:
        client device instance
    :type cl_device: struct ishtp_cl_device \*

.. _`ishtp_get_device.description`:

Description
-----------

Increment the usage count. The device can't be deleted

.. _`ishtp_put_device`:

ishtp_put_device
================

.. c:function:: void ishtp_put_device(struct ishtp_cl_device *cl_device)

    decrement usage count for the device

    :param cl_device:
        client device instance
    :type cl_device: struct ishtp_cl_device \*

.. _`ishtp_put_device.description`:

Description
-----------

Decrement the usage count. The device can be deleted is count = 0

.. _`ishtp_set_drvdata`:

ishtp_set_drvdata
=================

.. c:function:: void ishtp_set_drvdata(struct ishtp_cl_device *cl_device, void *data)

    set client driver data

    :param cl_device:
        client device instance
    :type cl_device: struct ishtp_cl_device \*

    :param data:
        driver data need to be set
    :type data: void \*

.. _`ishtp_set_drvdata.description`:

Description
-----------

Set client driver data to cl_device->driver_data.

.. _`ishtp_get_drvdata`:

ishtp_get_drvdata
=================

.. c:function:: void *ishtp_get_drvdata(struct ishtp_cl_device *cl_device)

    get client driver data

    :param cl_device:
        client device instance
    :type cl_device: struct ishtp_cl_device \*

.. _`ishtp_get_drvdata.description`:

Description
-----------

Get client driver data from cl_device->driver_data.

.. _`ishtp_get_drvdata.return`:

Return
------

pointer of driver data

.. _`ishtp_bus_new_client`:

ishtp_bus_new_client
====================

.. c:function:: int ishtp_bus_new_client(struct ishtp_device *dev)

    Create a new client

    :param dev:
        ISHTP device instance
    :type dev: struct ishtp_device \*

.. _`ishtp_bus_new_client.description`:

Description
-----------

Once bus protocol enumerates a client, this is called
to add a device for the client.

.. _`ishtp_bus_new_client.return`:

Return
------

0 on success or error code on failure

.. _`ishtp_cl_device_bind`:

ishtp_cl_device_bind
====================

.. c:function:: int ishtp_cl_device_bind(struct ishtp_cl *cl)

    bind a device

    :param cl:
        ishtp client device
    :type cl: struct ishtp_cl \*

.. _`ishtp_cl_device_bind.description`:

Description
-----------

Binds connected ishtp_cl to ISHTP bus device

.. _`ishtp_cl_device_bind.return`:

Return
------

0 on success or fault code

.. _`ishtp_bus_remove_all_clients`:

ishtp_bus_remove_all_clients
============================

.. c:function:: void ishtp_bus_remove_all_clients(struct ishtp_device *ishtp_dev, bool warm_reset)

    Remove all clients

    :param ishtp_dev:
        ishtp device
    :type ishtp_dev: struct ishtp_device \*

    :param warm_reset:
        Reset due to FW reset dure to errors or S3 suspend
    :type warm_reset: bool

.. _`ishtp_bus_remove_all_clients.description`:

Description
-----------

This is part of reset/remove flow. This function the main processing
only targets error processing, if the FW has forced reset or
error to remove connected clients. When warm reset the client devices are
not removed.

.. _`ishtp_reset_handler`:

ishtp_reset_handler
===================

.. c:function:: void ishtp_reset_handler(struct ishtp_device *dev)

    IPC reset handler

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

.. _`ishtp_reset_handler.description`:

Description
-----------

ISHTP Handler for IPC_RESET notification

.. _`ishtp_reset_compl_handler`:

ishtp_reset_compl_handler
=========================

.. c:function:: void ishtp_reset_compl_handler(struct ishtp_device *dev)

    Reset completion handler

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

.. _`ishtp_reset_compl_handler.description`:

Description
-----------

ISHTP handler for IPC_RESET sequence completion to start
host message bus start protocol sequence.

.. _`ishtp_use_dma_transfer`:

ishtp_use_dma_transfer
======================

.. c:function:: int ishtp_use_dma_transfer( void)

    Function to use DMA

    :param void:
        no arguments
    :type void: 

.. _`ishtp_use_dma_transfer.description`:

Description
-----------

This interface is used to enable usage of DMA

Return non zero if DMA can be enabled

.. _`ishtp_bus_register`:

ishtp_bus_register
==================

.. c:function:: int ishtp_bus_register( void)

    Function to register bus

    :param void:
        no arguments
    :type void: 

.. _`ishtp_bus_register.description`:

Description
-----------

This register ishtp bus

.. _`ishtp_bus_register.return`:

Return
------

Return output of bus_register

.. _`ishtp_bus_unregister`:

ishtp_bus_unregister
====================

.. c:function:: void __exit ishtp_bus_unregister( void)

    Function to unregister bus

    :param void:
        no arguments
    :type void: 

.. _`ishtp_bus_unregister.description`:

Description
-----------

This unregister ishtp bus

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/bus.c

.. _`__mei_cl_send`:

\__mei_cl_send
==============

.. c:function:: ssize_t __mei_cl_send(struct mei_cl *cl, u8 *buf, size_t length, unsigned int mode)

    internal client send (write)

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param buf:
        buffer to send
    :type buf: u8 \*

    :param length:
        buffer length
    :type length: size_t

    :param mode:
        sending mode
    :type mode: unsigned int

.. _`__mei_cl_send.return`:

Return
------

written size bytes or < 0 on error

.. _`__mei_cl_recv`:

\__mei_cl_recv
==============

.. c:function:: ssize_t __mei_cl_recv(struct mei_cl *cl, u8 *buf, size_t length, unsigned int mode, unsigned long timeout)

    internal client receive (read)

    :param cl:
        host client
    :type cl: struct mei_cl \*

    :param buf:
        buffer to receive
    :type buf: u8 \*

    :param length:
        buffer length
    :type length: size_t

    :param mode:
        io mode
    :type mode: unsigned int

    :param timeout:
        recv timeout, 0 for infinite timeout
    :type timeout: unsigned long

.. _`__mei_cl_recv.return`:

Return
------

read size in bytes of < 0 on error

.. _`mei_cldev_send`:

mei_cldev_send
==============

.. c:function:: ssize_t mei_cldev_send(struct mei_cl_device *cldev, u8 *buf, size_t length)

    me device send  (write)

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

    :param buf:
        buffer to send
    :type buf: u8 \*

    :param length:
        buffer length
    :type length: size_t

.. _`mei_cldev_send.return`:

Return
------

written size in bytes or < 0 on error

.. _`mei_cldev_recv_nonblock`:

mei_cldev_recv_nonblock
=======================

.. c:function:: ssize_t mei_cldev_recv_nonblock(struct mei_cl_device *cldev, u8 *buf, size_t length)

    non block client receive (read)

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

    :param buf:
        buffer to receive
    :type buf: u8 \*

    :param length:
        buffer length
    :type length: size_t

.. _`mei_cldev_recv_nonblock.return`:

Return
------

read size in bytes of < 0 on error
-EAGAIN if function will block.

.. _`mei_cldev_recv`:

mei_cldev_recv
==============

.. c:function:: ssize_t mei_cldev_recv(struct mei_cl_device *cldev, u8 *buf, size_t length)

    client receive (read)

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

    :param buf:
        buffer to receive
    :type buf: u8 \*

    :param length:
        buffer length
    :type length: size_t

.. _`mei_cldev_recv.return`:

Return
------

read size in bytes of < 0 on error

.. _`mei_cl_bus_rx_work`:

mei_cl_bus_rx_work
==================

.. c:function:: void mei_cl_bus_rx_work(struct work_struct *work)

    dispatch rx event for a bus device

    :param work:
        work
    :type work: struct work_struct \*

.. _`mei_cl_bus_notif_work`:

mei_cl_bus_notif_work
=====================

.. c:function:: void mei_cl_bus_notif_work(struct work_struct *work)

    dispatch FW notif event for a bus device

    :param work:
        work
    :type work: struct work_struct \*

.. _`mei_cl_bus_notify_event`:

mei_cl_bus_notify_event
=======================

.. c:function:: bool mei_cl_bus_notify_event(struct mei_cl *cl)

    schedule notify cb on bus client

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_bus_notify_event.return`:

Return
------

true if event was scheduled
false if the client is not waiting for event

.. _`mei_cl_bus_rx_event`:

mei_cl_bus_rx_event
===================

.. c:function:: bool mei_cl_bus_rx_event(struct mei_cl *cl)

    schedule rx event

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_bus_rx_event.return`:

Return
------

true if event was scheduled
false if the client is not waiting for event

.. _`mei_cldev_register_rx_cb`:

mei_cldev_register_rx_cb
========================

.. c:function:: int mei_cldev_register_rx_cb(struct mei_cl_device *cldev, mei_cldev_cb_t rx_cb)

    register Rx event callback

    :param cldev:
        me client devices
    :type cldev: struct mei_cl_device \*

    :param rx_cb:
        callback function
    :type rx_cb: mei_cldev_cb_t

.. _`mei_cldev_register_rx_cb.return`:

Return
------

0 on success
-EALREADY if an callback is already registered
<0 on other errors

.. _`mei_cldev_register_notif_cb`:

mei_cldev_register_notif_cb
===========================

.. c:function:: int mei_cldev_register_notif_cb(struct mei_cl_device *cldev, mei_cldev_cb_t notif_cb)

    register FW notification event callback

    :param cldev:
        me client devices
    :type cldev: struct mei_cl_device \*

    :param notif_cb:
        callback function
    :type notif_cb: mei_cldev_cb_t

.. _`mei_cldev_register_notif_cb.return`:

Return
------

0 on success
-EALREADY if an callback is already registered
<0 on other errors

.. _`mei_cldev_get_drvdata`:

mei_cldev_get_drvdata
=====================

.. c:function:: void *mei_cldev_get_drvdata(const struct mei_cl_device *cldev)

    driver data getter

    :param cldev:
        mei client device
    :type cldev: const struct mei_cl_device \*

.. _`mei_cldev_get_drvdata.return`:

Return
------

driver private data

.. _`mei_cldev_set_drvdata`:

mei_cldev_set_drvdata
=====================

.. c:function:: void mei_cldev_set_drvdata(struct mei_cl_device *cldev, void *data)

    driver data setter

    :param cldev:
        mei client device
    :type cldev: struct mei_cl_device \*

    :param data:
        data to store
    :type data: void \*

.. _`mei_cldev_uuid`:

mei_cldev_uuid
==============

.. c:function:: const uuid_le *mei_cldev_uuid(const struct mei_cl_device *cldev)

    return uuid of the underlying me client

    :param cldev:
        mei client device
    :type cldev: const struct mei_cl_device \*

.. _`mei_cldev_uuid.return`:

Return
------

me client uuid

.. _`mei_cldev_ver`:

mei_cldev_ver
=============

.. c:function:: u8 mei_cldev_ver(const struct mei_cl_device *cldev)

    return protocol version of the underlying me client

    :param cldev:
        mei client device
    :type cldev: const struct mei_cl_device \*

.. _`mei_cldev_ver.return`:

Return
------

me client protocol version

.. _`mei_cldev_enabled`:

mei_cldev_enabled
=================

.. c:function:: bool mei_cldev_enabled(struct mei_cl_device *cldev)

    check whether the device is enabled

    :param cldev:
        mei client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cldev_enabled.return`:

Return
------

true if me client is initialized and connected

.. _`mei_cl_bus_module_get`:

mei_cl_bus_module_get
=====================

.. c:function:: bool mei_cl_bus_module_get(struct mei_cl_device *cldev)

    acquire module of the underlying hw driver.

    :param cldev:
        mei client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_module_get.return`:

Return
------

true on success; false if the module was removed.

.. _`mei_cl_bus_module_put`:

mei_cl_bus_module_put
=====================

.. c:function:: void mei_cl_bus_module_put(struct mei_cl_device *cldev)

    release the underlying hw module.

    :param cldev:
        mei client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cldev_enable`:

mei_cldev_enable
================

.. c:function:: int mei_cldev_enable(struct mei_cl_device *cldev)

    enable me client device create connection with me client

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cldev_enable.return`:

Return
------

0 on success and < 0 on error

.. _`mei_cldev_unregister_callbacks`:

mei_cldev_unregister_callbacks
==============================

.. c:function:: void mei_cldev_unregister_callbacks(struct mei_cl_device *cldev)

    internal wrapper for unregistering callbacks.

    :param cldev:
        client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cldev_disable`:

mei_cldev_disable
=================

.. c:function:: int mei_cldev_disable(struct mei_cl_device *cldev)

    disable me client device disconnect form the me client

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cldev_disable.return`:

Return
------

0 on success and < 0 on error

.. _`mei_cl_device_find`:

mei_cl_device_find
==================

.. c:function:: const struct mei_cl_device_id *mei_cl_device_find(struct mei_cl_device *cldev, struct mei_cl_driver *cldrv)

    find matching entry in the driver id table

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

    :param cldrv:
        me client driver
    :type cldrv: struct mei_cl_driver \*

.. _`mei_cl_device_find.return`:

Return
------

id on success; NULL if no id is matching

.. _`mei_cl_device_match`:

mei_cl_device_match
===================

.. c:function:: int mei_cl_device_match(struct device *dev, struct device_driver *drv)

    device match function

    :param dev:
        device
    :type dev: struct device \*

    :param drv:
        driver
    :type drv: struct device_driver \*

.. _`mei_cl_device_match.return`:

Return
------

1 if matching device was found 0 otherwise

.. _`mei_cl_device_probe`:

mei_cl_device_probe
===================

.. c:function:: int mei_cl_device_probe(struct device *dev)

    bus probe function

    :param dev:
        device
    :type dev: struct device \*

.. _`mei_cl_device_probe.return`:

Return
------

0 on success; < 0 otherwise

.. _`mei_cl_device_remove`:

mei_cl_device_remove
====================

.. c:function:: int mei_cl_device_remove(struct device *dev)

    remove device from the bus

    :param dev:
        device
    :type dev: struct device \*

.. _`mei_cl_device_remove.return`:

Return
------

0 on success; < 0 otherwise

.. _`mei_cl_device_uevent`:

mei_cl_device_uevent
====================

.. c:function:: int mei_cl_device_uevent(struct device *dev, struct kobj_uevent_env *env)

    me client bus uevent handler

    :param dev:
        device
    :type dev: struct device \*

    :param env:
        uevent kobject
    :type env: struct kobj_uevent_env \*

.. _`mei_cl_device_uevent.return`:

Return
------

0 on success -ENOMEM on when add_uevent_var fails

.. _`mei_cl_bus_set_name`:

mei_cl_bus_set_name
===================

.. c:function:: void mei_cl_bus_set_name(struct mei_cl_device *cldev)

    set device name for me client device

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_dev_alloc`:

mei_cl_bus_dev_alloc
====================

.. c:function:: struct mei_cl_device *mei_cl_bus_dev_alloc(struct mei_device *bus, struct mei_me_client *me_cl)

    initialize and allocate mei client device

    :param bus:
        mei device
    :type bus: struct mei_device \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`mei_cl_bus_dev_alloc.return`:

Return
------

allocated device structur or NULL on allocation failure

.. _`mei_cl_bus_dev_setup`:

mei_cl_bus_dev_setup
====================

.. c:function:: bool mei_cl_bus_dev_setup(struct mei_device *bus, struct mei_cl_device *cldev)

    setup me client device run fix up routines and set the device name

    :param bus:
        mei device
    :type bus: struct mei_device \*

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_dev_setup.return`:

Return
------

true if the device is eligible for enumeration

.. _`mei_cl_bus_dev_add`:

mei_cl_bus_dev_add
==================

.. c:function:: int mei_cl_bus_dev_add(struct mei_cl_device *cldev)

    add me client devices

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_dev_add.return`:

Return
------

0 on success; < 0 on failre

.. _`mei_cl_bus_dev_stop`:

mei_cl_bus_dev_stop
===================

.. c:function:: void mei_cl_bus_dev_stop(struct mei_cl_device *cldev)

    stop the driver

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_dev_destroy`:

mei_cl_bus_dev_destroy
======================

.. c:function:: void mei_cl_bus_dev_destroy(struct mei_cl_device *cldev)

    destroy me client devices object

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_dev_destroy.locking`:

Locking
-------

called under "dev->cl_bus_lock" lock

.. _`mei_cl_bus_remove_device`:

mei_cl_bus_remove_device
========================

.. c:function:: void mei_cl_bus_remove_device(struct mei_cl_device *cldev)

    remove a devices form the bus

    :param cldev:
        me client device
    :type cldev: struct mei_cl_device \*

.. _`mei_cl_bus_remove_devices`:

mei_cl_bus_remove_devices
=========================

.. c:function:: void mei_cl_bus_remove_devices(struct mei_device *bus)

    remove all devices form the bus

    :param bus:
        mei device
    :type bus: struct mei_device \*

.. _`mei_cl_bus_dev_init`:

mei_cl_bus_dev_init
===================

.. c:function:: void mei_cl_bus_dev_init(struct mei_device *bus, struct mei_me_client *me_cl)

    allocate and initializes an mei client devices based on me client

    :param bus:
        mei device
    :type bus: struct mei_device \*

    :param me_cl:
        me client
    :type me_cl: struct mei_me_client \*

.. _`mei_cl_bus_dev_init.locking`:

Locking
-------

called under "dev->cl_bus_lock" lock

.. _`mei_cl_bus_rescan`:

mei_cl_bus_rescan
=================

.. c:function:: void mei_cl_bus_rescan(struct mei_device *bus)

    scan me clients list and add create devices for eligible clients

    :param bus:
        mei device
    :type bus: struct mei_device \*

.. This file was automatic generated / don't edit.


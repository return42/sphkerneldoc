.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/bus.c

.. _`__mei_cl_send`:

\__mei_cl_send
==============

.. c:function:: ssize_t __mei_cl_send(struct mei_cl *cl, u8 *buf, size_t length, unsigned int mode)

    internal client send (write)

    :param struct mei_cl \*cl:
        host client

    :param u8 \*buf:
        buffer to send

    :param size_t length:
        buffer length

    :param unsigned int mode:
        sending mode

.. _`__mei_cl_send.return`:

Return
------

written size bytes or < 0 on error

.. _`__mei_cl_recv`:

\__mei_cl_recv
==============

.. c:function:: ssize_t __mei_cl_recv(struct mei_cl *cl, u8 *buf, size_t length, unsigned int mode)

    internal client receive (read)

    :param struct mei_cl \*cl:
        host client

    :param u8 \*buf:
        buffer to receive

    :param size_t length:
        buffer length

    :param unsigned int mode:
        io mode

.. _`__mei_cl_recv.return`:

Return
------

read size in bytes of < 0 on error

.. _`mei_cldev_send`:

mei_cldev_send
==============

.. c:function:: ssize_t mei_cldev_send(struct mei_cl_device *cldev, u8 *buf, size_t length)

    me device send  (write)

    :param struct mei_cl_device \*cldev:
        me client device

    :param u8 \*buf:
        buffer to send

    :param size_t length:
        buffer length

.. _`mei_cldev_send.return`:

Return
------

written size in bytes or < 0 on error

.. _`mei_cldev_recv_nonblock`:

mei_cldev_recv_nonblock
=======================

.. c:function:: ssize_t mei_cldev_recv_nonblock(struct mei_cl_device *cldev, u8 *buf, size_t length)

    non block client receive (read)

    :param struct mei_cl_device \*cldev:
        me client device

    :param u8 \*buf:
        buffer to receive

    :param size_t length:
        buffer length

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

    :param struct mei_cl_device \*cldev:
        me client device

    :param u8 \*buf:
        buffer to receive

    :param size_t length:
        buffer length

.. _`mei_cldev_recv.return`:

Return
------

read size in bytes of < 0 on error

.. _`mei_cl_bus_rx_work`:

mei_cl_bus_rx_work
==================

.. c:function:: void mei_cl_bus_rx_work(struct work_struct *work)

    dispatch rx event for a bus device

    :param struct work_struct \*work:
        work

.. _`mei_cl_bus_notif_work`:

mei_cl_bus_notif_work
=====================

.. c:function:: void mei_cl_bus_notif_work(struct work_struct *work)

    dispatch FW notif event for a bus device

    :param struct work_struct \*work:
        work

.. _`mei_cl_bus_notify_event`:

mei_cl_bus_notify_event
=======================

.. c:function:: bool mei_cl_bus_notify_event(struct mei_cl *cl)

    schedule notify cb on bus client

    :param struct mei_cl \*cl:
        host client

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

    :param struct mei_cl \*cl:
        host client

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

    :param struct mei_cl_device \*cldev:
        me client devices

    :param mei_cldev_cb_t rx_cb:
        callback function

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

    :param struct mei_cl_device \*cldev:
        me client devices

    :param mei_cldev_cb_t notif_cb:
        callback function

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

    :param const struct mei_cl_device \*cldev:
        mei client device

.. _`mei_cldev_get_drvdata.return`:

Return
------

driver private data

.. _`mei_cldev_set_drvdata`:

mei_cldev_set_drvdata
=====================

.. c:function:: void mei_cldev_set_drvdata(struct mei_cl_device *cldev, void *data)

    driver data setter

    :param struct mei_cl_device \*cldev:
        mei client device

    :param void \*data:
        data to store

.. _`mei_cldev_uuid`:

mei_cldev_uuid
==============

.. c:function:: const uuid_le *mei_cldev_uuid(const struct mei_cl_device *cldev)

    return uuid of the underlying me client

    :param const struct mei_cl_device \*cldev:
        mei client device

.. _`mei_cldev_uuid.return`:

Return
------

me client uuid

.. _`mei_cldev_ver`:

mei_cldev_ver
=============

.. c:function:: u8 mei_cldev_ver(const struct mei_cl_device *cldev)

    return protocol version of the underlying me client

    :param const struct mei_cl_device \*cldev:
        mei client device

.. _`mei_cldev_ver.return`:

Return
------

me client protocol version

.. _`mei_cldev_enabled`:

mei_cldev_enabled
=================

.. c:function:: bool mei_cldev_enabled(struct mei_cl_device *cldev)

    check whether the device is enabled

    :param struct mei_cl_device \*cldev:
        mei client device

.. _`mei_cldev_enabled.return`:

Return
------

true if me client is initialized and connected

.. _`mei_cldev_enable`:

mei_cldev_enable
================

.. c:function:: int mei_cldev_enable(struct mei_cl_device *cldev)

    enable me client device create connection with me client

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cldev_enable.return`:

Return
------

0 on success and < 0 on error

.. _`mei_cldev_unregister_callbacks`:

mei_cldev_unregister_callbacks
==============================

.. c:function:: void mei_cldev_unregister_callbacks(struct mei_cl_device *cldev)

    internal wrapper for unregistering callbacks.

    :param struct mei_cl_device \*cldev:
        client device

.. _`mei_cldev_disable`:

mei_cldev_disable
=================

.. c:function:: int mei_cldev_disable(struct mei_cl_device *cldev)

    disable me client device disconnect form the me client

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cldev_disable.return`:

Return
------

0 on success and < 0 on error

.. _`mei_cl_bus_module_get`:

mei_cl_bus_module_get
=====================

.. c:function:: bool mei_cl_bus_module_get(struct mei_cl *cl)

    acquire module of the underlying hw module.

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_bus_module_get.return`:

Return
------

true on success; false if the module was removed.

.. _`mei_cl_bus_module_put`:

mei_cl_bus_module_put
=====================

.. c:function:: void mei_cl_bus_module_put(struct mei_cl *cl)

    release the underlying hw module.

    :param struct mei_cl \*cl:
        host client

.. _`mei_cl_device_find`:

mei_cl_device_find
==================

.. c:function:: const struct mei_cl_device_id *mei_cl_device_find(struct mei_cl_device *cldev, struct mei_cl_driver *cldrv)

    find matching entry in the driver id table

    :param struct mei_cl_device \*cldev:
        me client device

    :param struct mei_cl_driver \*cldrv:
        me client driver

.. _`mei_cl_device_find.return`:

Return
------

id on success; NULL if no id is matching

.. _`mei_cl_device_match`:

mei_cl_device_match
===================

.. c:function:: int mei_cl_device_match(struct device *dev, struct device_driver *drv)

    device match function

    :param struct device \*dev:
        device

    :param struct device_driver \*drv:
        driver

.. _`mei_cl_device_match.return`:

Return
------

1 if matching device was found 0 otherwise

.. _`mei_cl_device_probe`:

mei_cl_device_probe
===================

.. c:function:: int mei_cl_device_probe(struct device *dev)

    bus probe function

    :param struct device \*dev:
        device

.. _`mei_cl_device_probe.return`:

Return
------

0 on success; < 0 otherwise

.. _`mei_cl_device_remove`:

mei_cl_device_remove
====================

.. c:function:: int mei_cl_device_remove(struct device *dev)

    remove device from the bus

    :param struct device \*dev:
        device

.. _`mei_cl_device_remove.return`:

Return
------

0 on success; < 0 otherwise

.. _`mei_cl_device_uevent`:

mei_cl_device_uevent
====================

.. c:function:: int mei_cl_device_uevent(struct device *dev, struct kobj_uevent_env *env)

    me client bus uevent handler

    :param struct device \*dev:
        device

    :param struct kobj_uevent_env \*env:
        uevent kobject

.. _`mei_cl_device_uevent.return`:

Return
------

0 on success -ENOMEM on when add_uevent_var fails

.. _`mei_cl_bus_set_name`:

mei_cl_bus_set_name
===================

.. c:function:: void mei_cl_bus_set_name(struct mei_cl_device *cldev)

    set device name for me client device

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_dev_alloc`:

mei_cl_bus_dev_alloc
====================

.. c:function:: struct mei_cl_device *mei_cl_bus_dev_alloc(struct mei_device *bus, struct mei_me_client *me_cl)

    initialize and allocate mei client device

    :param struct mei_device \*bus:
        mei device

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_cl_bus_dev_alloc.return`:

Return
------

allocated device structur or NULL on allocation failure

.. _`mei_cl_bus_dev_setup`:

mei_cl_bus_dev_setup
====================

.. c:function:: bool mei_cl_bus_dev_setup(struct mei_device *bus, struct mei_cl_device *cldev)

    setup me client device run fix up routines and set the device name

    :param struct mei_device \*bus:
        mei device

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_dev_setup.return`:

Return
------

true if the device is eligible for enumeration

.. _`mei_cl_bus_dev_add`:

mei_cl_bus_dev_add
==================

.. c:function:: int mei_cl_bus_dev_add(struct mei_cl_device *cldev)

    add me client devices

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_dev_add.return`:

Return
------

0 on success; < 0 on failre

.. _`mei_cl_bus_dev_stop`:

mei_cl_bus_dev_stop
===================

.. c:function:: void mei_cl_bus_dev_stop(struct mei_cl_device *cldev)

    stop the driver

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_dev_destroy`:

mei_cl_bus_dev_destroy
======================

.. c:function:: void mei_cl_bus_dev_destroy(struct mei_cl_device *cldev)

    destroy me client devices object

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_dev_destroy.locking`:

Locking
-------

called under "dev->cl_bus_lock" lock

.. _`mei_cl_bus_remove_device`:

mei_cl_bus_remove_device
========================

.. c:function:: void mei_cl_bus_remove_device(struct mei_cl_device *cldev)

    remove a devices form the bus

    :param struct mei_cl_device \*cldev:
        me client device

.. _`mei_cl_bus_remove_devices`:

mei_cl_bus_remove_devices
=========================

.. c:function:: void mei_cl_bus_remove_devices(struct mei_device *bus)

    remove all devices form the bus

    :param struct mei_device \*bus:
        mei device

.. _`mei_cl_bus_dev_init`:

mei_cl_bus_dev_init
===================

.. c:function:: void mei_cl_bus_dev_init(struct mei_device *bus, struct mei_me_client *me_cl)

    allocate and initializes an mei client devices based on me client

    :param struct mei_device \*bus:
        mei device

    :param struct mei_me_client \*me_cl:
        me client

.. _`mei_cl_bus_dev_init.locking`:

Locking
-------

called under "dev->cl_bus_lock" lock

.. _`mei_cl_bus_rescan`:

mei_cl_bus_rescan
=================

.. c:function:: void mei_cl_bus_rescan(struct mei_device *bus)

    scan me clients list and add create devices for eligible clients

    :param struct mei_device \*bus:
        mei device

.. This file was automatic generated / don't edit.


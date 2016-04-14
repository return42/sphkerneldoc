.. -*- coding: utf-8; mode: rst -*-

========
device.c
========

.. _`ccw_device_set_offline`:

ccw_device_set_offline
======================

.. c:function:: int ccw_device_set_offline (struct ccw_device *cdev)

    disable a ccw device for I/O

    :param struct ccw_device \*cdev:
        target ccw device


.. _`ccw_device_set_offline.description`:

Description
-----------

This function calls the driver's :c:func:`set_offline` function for ``cdev``\ , if
given, and then disables ``cdev``\ .
Returns::

  ``0`` on success and a negative error value on failure.

Context::

 enabled, ccw device lock not held


.. _`ccw_device_set_online`:

ccw_device_set_online
=====================

.. c:function:: int ccw_device_set_online (struct ccw_device *cdev)

    enable a ccw device for I/O

    :param struct ccw_device \*cdev:
        target ccw device


.. _`ccw_device_set_online.description`:

Description
-----------

This function first enables ``cdev`` and then calls the driver's :c:func:`set_online`
function for ``cdev``\ , if given. If :c:func:`set_online` returns an error, ``cdev`` is
disabled again.
Returns::

  ``0`` on success and a negative error value on failure.

Context::

 enabled, ccw device lock not held


.. _`get_ccwdev_by_dev_id`:

get_ccwdev_by_dev_id
====================

.. c:function:: struct ccw_device *get_ccwdev_by_dev_id (struct ccw_dev_id *dev_id)

    obtain device from a ccw device id

    :param struct ccw_dev_id \*dev_id:
        id of the device to be searched


.. _`get_ccwdev_by_dev_id.description`:

Description
-----------

This function searches all devices attached to the ccw bus for a device
matching ``dev_id``\ .
Returns::

 If a device is found its reference count is increased and returned;
 else ``NULL`` is returned.


.. _`ccw_purge_blacklisted`:

ccw_purge_blacklisted
=====================

.. c:function:: int ccw_purge_blacklisted ( void)

    purge unused, blacklisted devices

    :param void:
        no arguments


.. _`ccw_purge_blacklisted.description`:

Description
-----------


Unregister all ccw devices that are offline and on the blacklist.


.. _`io_subchannel_sch_event`:

io_subchannel_sch_event
=======================

.. c:function:: int io_subchannel_sch_event (struct subchannel *sch, int process)

    process subchannel event

    :param struct subchannel \*sch:
        subchannel

    :param int process:
        non-zero if function is called in process context


.. _`io_subchannel_sch_event.description`:

Description
-----------

An unspecified event occurred for this subchannel. Adjust data according
to the current operational state of the subchannel and device. Return
zero when the event has been handled sufficiently or -EAGAIN when this
function should be called again in process context.


.. _`ccw_device_wait_idle`:

ccw_device_wait_idle
====================

.. c:function:: void ccw_device_wait_idle (struct ccw_device *cdev)

    busy wait for device to become idle

    :param struct ccw_device \*cdev:
        ccw device


.. _`ccw_device_wait_idle.description`:

Description
-----------

Poll until activity control is zero, that is, no function or data
transfer is pending/active.
Called with device lock being held.


.. _`get_ccwdev_by_busid`:

get_ccwdev_by_busid
===================

.. c:function:: struct ccw_device *get_ccwdev_by_busid (struct ccw_driver *cdrv, const char *bus_id)

    obtain device from a bus id

    :param struct ccw_driver \*cdrv:
        driver the device is owned by

    :param const char \*bus_id:
        bus id of the device to be searched


.. _`get_ccwdev_by_busid.description`:

Description
-----------

This function searches all devices owned by ``cdrv`` for a device with a bus
id matching ``bus_id``\ .
Returns::

 If a match is found, its reference count of the found device is increased
 and it is returned; else ``NULL`` is returned.


.. _`ccw_driver_register`:

ccw_driver_register
===================

.. c:function:: int ccw_driver_register (struct ccw_driver *cdriver)

    register a ccw driver

    :param struct ccw_driver \*cdriver:
        driver to be registered


.. _`ccw_driver_register.description`:

Description
-----------

This function is mainly a wrapper around :c:func:`driver_register`.
Returns::

  ``0`` on success and a negative error value on failure.


.. _`ccw_driver_unregister`:

ccw_driver_unregister
=====================

.. c:function:: void ccw_driver_unregister (struct ccw_driver *cdriver)

    deregister a ccw driver

    :param struct ccw_driver \*cdriver:
        driver to be deregistered


.. _`ccw_driver_unregister.description`:

Description
-----------

This function is mainly a wrapper around :c:func:`driver_unregister`.


.. _`ccw_device_sched_todo`:

ccw_device_sched_todo
=====================

.. c:function:: void ccw_device_sched_todo (struct ccw_device *cdev, enum cdev_todo todo)

    schedule ccw device operation

    :param struct ccw_device \*cdev:
        ccw device

    :param enum cdev_todo todo:
        todo


.. _`ccw_device_sched_todo.description`:

Description
-----------

Schedule the operation identified by ``todo`` to be performed on the slow path
workqueue. Do nothing if another operation with higher priority is already
scheduled. Needs to be called with ccwdev lock held.


.. _`ccw_device_siosl`:

ccw_device_siosl
================

.. c:function:: int ccw_device_siosl (struct ccw_device *cdev)

    initiate logging

    :param struct ccw_device \*cdev:
        ccw device


.. _`ccw_device_siosl.description`:

Description
-----------

This function is used to invoke model-dependent logging within the channel
subsystem.


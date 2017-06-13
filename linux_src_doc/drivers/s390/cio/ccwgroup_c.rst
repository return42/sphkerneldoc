.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/ccwgroup.c

.. _`ccwgroup_set_online`:

ccwgroup_set_online
===================

.. c:function:: int ccwgroup_set_online(struct ccwgroup_device *gdev)

    enable a ccwgroup device

    :param struct ccwgroup_device \*gdev:
        target ccwgroup device

.. _`ccwgroup_set_online.description`:

Description
-----------

This function attempts to put the ccwgroup device into the online state.

.. _`ccwgroup_set_online.return`:

Return
------

 \ ``0``\  on success and a negative error value on failure.

.. _`ccwgroup_set_offline`:

ccwgroup_set_offline
====================

.. c:function:: int ccwgroup_set_offline(struct ccwgroup_device *gdev)

    disable a ccwgroup device

    :param struct ccwgroup_device \*gdev:
        target ccwgroup device

.. _`ccwgroup_set_offline.description`:

Description
-----------

This function attempts to put the ccwgroup device into the offline state.

.. _`ccwgroup_set_offline.return`:

Return
------

 \ ``0``\  on success and a negative error value on failure.

.. _`ccwgroup_create_dev`:

ccwgroup_create_dev
===================

.. c:function:: int ccwgroup_create_dev(struct device *parent, struct ccwgroup_driver *gdrv, int num_devices, const char *buf)

    create and register a ccw group device

    :param struct device \*parent:
        parent device for the new device

    :param struct ccwgroup_driver \*gdrv:
        driver for the new group device

    :param int num_devices:
        number of slave devices

    :param const char \*buf:
        buffer containing comma separated bus ids of slave devices

.. _`ccwgroup_create_dev.description`:

Description
-----------

Create and register a new ccw group device as a child of \ ``parent``\ . Slave
devices are obtained from the list of bus ids given in \ ``buf``\ .

.. _`ccwgroup_create_dev.return`:

Return
------

 \ ``0``\  on success and an error code on failure.

.. _`ccwgroup_create_dev.context`:

Context
-------

 non-atomic

.. _`ccwgroup_driver_register`:

ccwgroup_driver_register
========================

.. c:function:: int ccwgroup_driver_register(struct ccwgroup_driver *cdriver)

    register a ccw group driver

    :param struct ccwgroup_driver \*cdriver:
        driver to be registered

.. _`ccwgroup_driver_register.description`:

Description
-----------

This function is mainly a wrapper around \ :c:func:`driver_register`\ .

.. _`ccwgroup_driver_unregister`:

ccwgroup_driver_unregister
==========================

.. c:function:: void ccwgroup_driver_unregister(struct ccwgroup_driver *cdriver)

    deregister a ccw group driver

    :param struct ccwgroup_driver \*cdriver:
        driver to be deregistered

.. _`ccwgroup_driver_unregister.description`:

Description
-----------

This function is mainly a wrapper around \ :c:func:`driver_unregister`\ .

.. _`ccwgroup_probe_ccwdev`:

ccwgroup_probe_ccwdev
=====================

.. c:function:: int ccwgroup_probe_ccwdev(struct ccw_device *cdev)

    probe function for slave devices

    :param struct ccw_device \*cdev:
        ccw device to be probed

.. _`ccwgroup_probe_ccwdev.description`:

Description
-----------

This is a dummy probe function for ccw devices that are slave devices in
a ccw group device.

.. _`ccwgroup_probe_ccwdev.return`:

Return
------

 always \ ``0``\ 

.. _`ccwgroup_remove_ccwdev`:

ccwgroup_remove_ccwdev
======================

.. c:function:: void ccwgroup_remove_ccwdev(struct ccw_device *cdev)

    remove function for slave devices

    :param struct ccw_device \*cdev:
        ccw device to be removed

.. _`ccwgroup_remove_ccwdev.description`:

Description
-----------

This is a remove function for ccw devices that are slave devices in a ccw
group device. It sets the ccw device offline and also deregisters the
embedding ccw group device.

.. This file was automatic generated / don't edit.


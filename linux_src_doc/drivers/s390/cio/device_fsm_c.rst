.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/device_fsm.c

.. _`ccw_device_notify`:

ccw_device_notify
=================

.. c:function:: int ccw_device_notify(struct ccw_device *cdev, int event)

    inform the device's driver about an event

    :param struct ccw_device \*cdev:
        device for which an event occurred

    :param int event:
        event that occurred

.. _`ccw_device_notify.return`:

Return
------

-%EINVAL if the device is offline or has no driver.
-%EOPNOTSUPP if the device's driver has no notifier registered.
\ ``NOTIFY_OK``\  if the driver wants to keep the device.
\ ``NOTIFY_BAD``\  if the driver doesn't want to keep the device.

.. This file was automatic generated / don't edit.


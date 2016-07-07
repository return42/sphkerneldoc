.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/remote_device.h

.. _`sci_remote_device_stop`:

sci_remote_device_stop
======================

.. c:function:: enum sci_status sci_remote_device_stop(struct isci_remote_device *idev, u32 timeout)

    This method will stop both transmission and reception of link activity for the supplied remote device.  This method disables normal IO requests from flowing through to the remote device.

    :param struct isci_remote_device \*idev:
        *undescribed*

    :param u32 timeout:
        This parameter specifies the number of milliseconds in which the
        stop operation should complete.

.. _`sci_remote_device_stop.description`:

Description
-----------

An indication of whether the device was successfully stopped. SCI_SUCCESS
This value is returned if the transmission and reception for the device was
successfully stopped.

.. _`sci_remote_device_reset`:

sci_remote_device_reset
=======================

.. c:function:: enum sci_status sci_remote_device_reset(struct isci_remote_device *idev)

    This method will reset the device making it ready for operation. This method must be called anytime the device is reset either through a SMP phy control or a port hard reset request.

    :param struct isci_remote_device \*idev:
        *undescribed*

.. _`sci_remote_device_reset.description`:

Description
-----------

This method does not actually cause the device hardware to be reset. This
method resets the software object so that it will be operational after a
device hardware reset completes. An indication of whether the device reset
was accepted. SCI_SUCCESS This value is returned if the device reset is
started.

.. _`sci_remote_device_reset_complete`:

sci_remote_device_reset_complete
================================

.. c:function:: enum sci_status sci_remote_device_reset_complete(struct isci_remote_device *idev)

    This method informs the device object that the reset operation is complete and the device can resume operation again.

    :param struct isci_remote_device \*idev:
        *undescribed*

.. _`sci_remote_device_reset_complete.description`:

Description
-----------

An indication that the device is resuming operation. SCI_SUCCESS the device
is resuming operation.

.. This file was automatic generated / don't edit.


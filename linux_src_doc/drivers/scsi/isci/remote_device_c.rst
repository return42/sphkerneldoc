.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/remote_device.c

.. _`isci_remote_device_ready`:

isci_remote_device_ready
========================

.. c:function:: void isci_remote_device_ready(struct isci_host *ihost, struct isci_remote_device *idev)

    This function is called by the ihost when the remote device is ready. We mark the isci device as ready and signal the waiting proccess.

    :param ihost:
        our valid isci_host
    :type ihost: struct isci_host \*

    :param idev:
        remote device
    :type idev: struct isci_remote_device \*

.. _`isci_remote_device_not_ready`:

isci_remote_device_not_ready
============================

.. c:function:: void isci_remote_device_not_ready(struct isci_host *ihost, struct isci_remote_device *idev, u32 reason)

    This function is called by the ihost when the remote device is not ready. We mark the isci device as ready (not "ready_for_io") and signal the waiting proccess.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

    :param reason:
        *undescribed*
    :type reason: u32

.. _`isci_remote_device_not_ready.description`:

Description
-----------

sci_lock is held on entrance to this function.

.. _`sci_remote_device_destruct`:

sci_remote_device_destruct
==========================

.. c:function:: enum sci_status sci_remote_device_destruct(struct isci_remote_device *idev)

    free remote node context and destruct

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`sci_remote_device_destruct.description`:

Description
-----------

Remote device objects are a limited resource.  As such, they must be
protected.  Thus calls to construct and destruct are mutually exclusive and
non-reentrant. The return value shall indicate if the device was
successfully destructed or if some failure occurred. enum sci_status This value
is returned if the device is successfully destructed.
SCI_FAILURE_INVALID_REMOTE_DEVICE This value is returned if the supplied
device isn't valid (e.g. it's already been destoryed, the handle isn't
valid, etc.).

.. _`isci_remote_device_deconstruct`:

isci_remote_device_deconstruct
==============================

.. c:function:: void isci_remote_device_deconstruct(struct isci_host *ihost, struct isci_remote_device *idev)

    This function frees an isci_remote_device.

    :param ihost:
        This parameter specifies the isci host object.
    :type ihost: struct isci_host \*

    :param idev:
        This parameter specifies the remote device to be freed.
    :type idev: struct isci_remote_device \*

.. _`sci_remote_device_construct`:

sci_remote_device_construct
===========================

.. c:function:: void sci_remote_device_construct(struct isci_port *iport, struct isci_remote_device *idev)

    common construction

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`sci_remote_device_construct.description`:

Description
-----------

This routine just performs benign initialization and does not
allocate the remote_node_context which is left to
sci_remote_device_[de]a_construct().  \ :c:func:`sci_remote_device_destruct`\ 
frees the remote_node_context(s) for the device.

.. _`sci_remote_device_da_construct`:

sci_remote_device_da_construct
==============================

.. c:function:: enum sci_status sci_remote_device_da_construct(struct isci_port *iport, struct isci_remote_device *idev)

    construct direct attached device.

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`sci_remote_device_da_construct.description`:

Description
-----------

The information (e.g. IAF, Signature FIS, etc.) necessary to build
the device is known to the SCI Core since it is contained in the
sci_phy object.  Remote node context(s) is/are a global resource
allocated by this routine, freed by \ :c:func:`sci_remote_device_destruct`\ .

.. _`sci_remote_device_da_construct.return`:

Return
------

SCI_FAILURE_DEVICE_EXISTS - device has already been constructed.
SCI_FAILURE_UNSUPPORTED_PROTOCOL - e.g. sas device attached to
sata-only controller instance.
SCI_FAILURE_INSUFFICIENT_RESOURCES - remote node contexts exhausted.

.. _`sci_remote_device_ea_construct`:

sci_remote_device_ea_construct
==============================

.. c:function:: enum sci_status sci_remote_device_ea_construct(struct isci_port *iport, struct isci_remote_device *idev)

    construct expander attached device

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`sci_remote_device_ea_construct.description`:

Description
-----------

Remote node context(s) is/are a global resource allocated by this
routine, freed by \ :c:func:`sci_remote_device_destruct`\ .

.. _`sci_remote_device_ea_construct.return`:

Return
------

SCI_FAILURE_DEVICE_EXISTS - device has already been constructed.
SCI_FAILURE_UNSUPPORTED_PROTOCOL - e.g. sas device attached to
sata-only controller instance.
SCI_FAILURE_INSUFFICIENT_RESOURCES - remote node contexts exhausted.

.. _`sci_remote_device_start`:

sci_remote_device_start
=======================

.. c:function:: enum sci_status sci_remote_device_start(struct isci_remote_device *idev, u32 timeout)

    This method will start the supplied remote device.  This method enables normal IO requests to flow through to the remote device.

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

    :param timeout:
        This parameter specifies the number of milliseconds in which the
        start operation should complete.
    :type timeout: u32

.. _`sci_remote_device_start.description`:

Description
-----------

An indication of whether the device was successfully started. SCI_SUCCESS
This value is returned if the device was successfully started.
SCI_FAILURE_INVALID_PHY This value is returned if the user attempts to start
the device when there have been no phys added to it.

.. _`isci_remote_device_alloc`:

isci_remote_device_alloc
========================

.. c:function:: struct isci_remote_device *isci_remote_device_alloc(struct isci_host *ihost, struct isci_port *iport)

    is received.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param iport:
        *undescribed*
    :type iport: struct isci_port \*

.. _`isci_remote_device_alloc.description`:

Description
-----------

pointer to new isci_remote_device.

.. _`isci_remote_device_stop`:

isci_remote_device_stop
=======================

.. c:function:: enum sci_status isci_remote_device_stop(struct isci_host *ihost, struct isci_remote_device *idev)

    This function is called internally to stop the remote device.

    :param ihost:
        *undescribed*
    :type ihost: struct isci_host \*

    :param idev:
        *undescribed*
    :type idev: struct isci_remote_device \*

.. _`isci_remote_device_stop.description`:

Description
-----------

The status of the ihost request to stop.

.. _`isci_remote_device_gone`:

isci_remote_device_gone
=======================

.. c:function:: void isci_remote_device_gone(struct domain_device *dev)

    This function is called by libsas when a domain device is removed.

    :param dev:
        *undescribed*
    :type dev: struct domain_device \*

.. _`isci_remote_device_found`:

isci_remote_device_found
========================

.. c:function:: int isci_remote_device_found(struct domain_device *dev)

    This function is called by libsas when a remote device is discovered. A remote device object is created and started. the function then sleeps until the sci core device started message is received.

    :param dev:
        *undescribed*
    :type dev: struct domain_device \*

.. _`isci_remote_device_found.description`:

Description
-----------

status, zero indicates success.

.. This file was automatic generated / don't edit.


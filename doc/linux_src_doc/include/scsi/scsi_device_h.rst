.. -*- coding: utf-8; mode: rst -*-

=============
scsi_device.h
=============


.. _`shost_for_each_device`:

shost_for_each_device
=====================

.. c:function:: shost_for_each_device ( sdev,  shost)

    iterate over all devices of a host

    :param sdev:
        the :c:type:`struct scsi_device <scsi_device>` to use as a cursor

    :param shost:
        the :c:type:`struct scsi_host <scsi_host>` to iterate over



.. _`shost_for_each_device.description`:

Description
-----------

Iterator that returns each device attached to ``shost``\ .  This loop
takes a reference on each device and releases it at the end.  If
you break out of the loop, you must call scsi_device_put(sdev).



.. _`__shost_for_each_device`:

__shost_for_each_device
=======================

.. c:function:: __shost_for_each_device ( sdev,  shost)

    iterate over all devices of a host (UNLOCKED)

    :param sdev:
        the :c:type:`struct scsi_device <scsi_device>` to use as a cursor

    :param shost:
        the :c:type:`struct scsi_host <scsi_host>` to iterate over



.. _`__shost_for_each_device.description`:

Description
-----------

Iterator that returns each device attached to ``shost``\ .  It does _not_
take a reference on the scsi_device, so the whole loop must be
protected by shost->host_lock.



.. _`__shost_for_each_device.note`:

Note
----

The only reason to use this is because you need to access the
device list in interrupt context.  Otherwise you really want to use
shost_for_each_device instead.



.. _`scsi_device_supports_vpd`:

scsi_device_supports_vpd
========================

.. c:function:: int scsi_device_supports_vpd (struct scsi_device *sdev)

    test if a device supports VPD pages

    :param struct scsi_device \*sdev:
        the :c:type:`struct scsi_device <scsi_device>` to test



.. _`scsi_device_supports_vpd.description`:

Description
-----------

If the 'try_vpd_pages' flag is set it takes precedence.
Otherwise we will assume VPD pages are supported if the
SCSI level is at least SPC-3 and 'skip_vpd_pages' is not set.


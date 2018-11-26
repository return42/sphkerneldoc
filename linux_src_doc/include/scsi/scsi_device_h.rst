.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/scsi_device.h

.. _`scsi_vpd`:

struct scsi_vpd
===============

.. c:type:: struct scsi_vpd

    SCSI Vital Product Data

.. _`scsi_vpd.definition`:

Definition
----------

.. code-block:: c

    struct scsi_vpd {
        struct rcu_head rcu;
        int len;
        unsigned char data[];
    }

.. _`scsi_vpd.members`:

Members
-------

rcu
    For \ :c:func:`kfree_rcu`\ .

len
    Length in bytes of \ ``data``\ .

data
    VPD data as defined in various T10 SCSI standard documents.

.. _`shost_for_each_device`:

shost_for_each_device
=====================

.. c:function::  shost_for_each_device( sdev,  shost)

    iterate over all devices of a host

    :param sdev:
        the \ :c:type:`struct scsi_device <scsi_device>`\  to use as a cursor
    :type sdev: 

    :param shost:
        the \ :c:type:`struct scsi_host <scsi_host>`\  to iterate over
    :type shost: 

.. _`shost_for_each_device.description`:

Description
-----------

Iterator that returns each device attached to \ ``shost``\ .  This loop
takes a reference on each device and releases it at the end.  If
you break out of the loop, you must call scsi_device_put(sdev).

.. _`__shost_for_each_device`:

__shost_for_each_device
=======================

.. c:function::  __shost_for_each_device( sdev,  shost)

    iterate over all devices of a host (UNLOCKED)

    :param sdev:
        the \ :c:type:`struct scsi_device <scsi_device>`\  to use as a cursor
    :type sdev: 

    :param shost:
        the \ :c:type:`struct scsi_host <scsi_host>`\  to iterate over
    :type shost: 

.. _`__shost_for_each_device.description`:

Description
-----------

Iterator that returns each device attached to \ ``shost``\ .  It does _not_
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

.. c:function:: int scsi_device_supports_vpd(struct scsi_device *sdev)

    test if a device supports VPD pages

    :param sdev:
        the \ :c:type:`struct scsi_device <scsi_device>`\  to test
    :type sdev: struct scsi_device \*

.. _`scsi_device_supports_vpd.description`:

Description
-----------

If the 'try_vpd_pages' flag is set it takes precedence.
Otherwise we will assume VPD pages are supported if the
SCSI level is at least SPC-3 and 'skip_vpd_pages' is not set.

.. This file was automatic generated / don't edit.


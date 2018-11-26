.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_ioctl.c

.. _`ioctl_probe`:

ioctl_probe
===========

.. c:function:: int ioctl_probe(struct Scsi_Host *host, void __user *buffer)

    -  return host identification

    :param host:
        host to identify
    :type host: struct Scsi_Host \*

    :param buffer:
        userspace buffer for identification
    :type buffer: void __user \*

.. _`ioctl_probe.description`:

Description
-----------

Return an identifying string at \ ``buffer``\ , if \ ``buffer``\  is non-NULL, filling
to the length stored at * (int *) \ ``buffer``\ .

.. _`scsi_ioctl`:

scsi_ioctl
==========

.. c:function:: int scsi_ioctl(struct scsi_device *sdev, int cmd, void __user *arg)

    Dispatch ioctl to scsi device

    :param sdev:
        scsi device receiving ioctl
    :type sdev: struct scsi_device \*

    :param cmd:
        which ioctl is it
    :type cmd: int

    :param arg:
        data associated with ioctl
    :type arg: void __user \*

.. _`scsi_ioctl.description`:

Description
-----------

The \ :c:func:`scsi_ioctl`\  function differs from most ioctls in that it
does not take a major/minor number as the dev field.  Rather, it takes
a pointer to a \ :c:type:`struct scsi_device <scsi_device>`\ .

.. This file was automatic generated / don't edit.


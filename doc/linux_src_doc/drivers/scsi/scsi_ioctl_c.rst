.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_ioctl.c

.. _`ioctl_probe`:

ioctl_probe
===========

.. c:function:: int ioctl_probe(struct Scsi_Host *host, void __user *buffer)

    -  return host identification

    :param struct Scsi_Host \*host:
        host to identify

    :param void __user \*buffer:
        userspace buffer for identification

.. _`ioctl_probe.description`:

Description
-----------

Return an identifying string at \ ``buffer``\ , if \ ``buffer``\  is non-NULL, filling
to the length stored at \* (int \*) \ ``buffer``\ .

.. _`scsi_ioctl`:

scsi_ioctl
==========

.. c:function:: int scsi_ioctl(struct scsi_device *sdev, int cmd, void __user *arg)

    Dispatch ioctl to scsi device

    :param struct scsi_device \*sdev:
        scsi device receiving ioctl

    :param int cmd:
        which ioctl is it

    :param void __user \*arg:
        data associated with ioctl

.. _`scsi_ioctl.description`:

Description
-----------

The \ :c:func:`scsi_ioctl`\  function differs from most ioctls in that it
does not take a major/minor number as the dev field.  Rather, it takes
a pointer to a \ :c:type:`struct scsi_device <scsi_device>`\ .

.. This file was automatic generated / don't edit.


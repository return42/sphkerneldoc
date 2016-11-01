.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tile-srom.c

.. _`srom_open`:

srom_open
=========

.. c:function:: int srom_open(struct inode *inode, struct file *filp)

    Device open routine.

    :param struct inode \*inode:
        Inode for this device.

    :param struct file \*filp:
        File for this specific open of the device.

.. _`srom_open.description`:

Description
-----------

Returns zero, or an error code.

.. _`srom_release`:

srom_release
============

.. c:function:: int srom_release(struct inode *inode, struct file *filp)

    Device release routine.

    :param struct inode \*inode:
        Inode for this device.

    :param struct file \*filp:
        File for this specific open of the device.

.. _`srom_release.description`:

Description
-----------

Returns zero, or an error code.

.. _`srom_read`:

srom_read
=========

.. c:function:: ssize_t srom_read(struct file *filp, char __user *buf, size_t count, loff_t *f_pos)

    Read data from the device.

    :param struct file \*filp:
        File for this specific open of the device.

    :param char __user \*buf:
        User's data buffer.

    :param size_t count:
        Number of bytes requested.

    :param loff_t \*f_pos:
        File position.

.. _`srom_read.description`:

Description
-----------

Returns number of bytes read, or an error code.

.. _`srom_write`:

srom_write
==========

.. c:function:: ssize_t srom_write(struct file *filp, const char __user *buf, size_t count, loff_t *f_pos)

    Write data to the device.

    :param struct file \*filp:
        File for this specific open of the device.

    :param const char __user \*buf:
        User's data buffer.

    :param size_t count:
        Number of bytes requested.

    :param loff_t \*f_pos:
        File position.

.. _`srom_write.description`:

Description
-----------

Returns number of bytes written, or an error code.

.. _`srom_setup_minor`:

srom_setup_minor
================

.. c:function:: int srom_setup_minor(struct srom_dev *srom, int devhdl)

    Initialize per-minor information.

    :param struct srom_dev \*srom:
        Per-device SROM state.

    :param int devhdl:
        Partition device handle.

.. This file was automatic generated / don't edit.


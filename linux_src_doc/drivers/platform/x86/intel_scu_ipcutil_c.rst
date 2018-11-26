.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/intel_scu_ipcutil.c

.. _`scu_reg_access`:

scu_reg_access
==============

.. c:function:: int scu_reg_access(u32 cmd, struct scu_ipc_data *data)

    implement register access ioctls

    :param cmd:
        command we are doing (read/write/update)
    :type cmd: u32

    :param data:
        kernel copy of ioctl data
    :type data: struct scu_ipc_data \*

.. _`scu_reg_access.description`:

Description
-----------

Allow the user to perform register accesses on the SCU via the
kernel interface

.. _`scu_ipc_ioctl`:

scu_ipc_ioctl
=============

.. c:function:: long scu_ipc_ioctl(struct file *fp, unsigned int cmd, unsigned long arg)

    control ioctls for the SCU

    :param fp:
        file handle of the SCU device
    :type fp: struct file \*

    :param cmd:
        ioctl coce
    :type cmd: unsigned int

    :param arg:
        pointer to user passed structure
    :type arg: unsigned long

.. _`scu_ipc_ioctl.description`:

Description
-----------

Support the I/O and firmware flashing interfaces of the SCU

.. This file was automatic generated / don't edit.


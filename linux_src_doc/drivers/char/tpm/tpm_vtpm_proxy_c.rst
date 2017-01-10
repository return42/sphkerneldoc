.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/tpm/tpm_vtpm_proxy.c

.. _`vtpm_proxy_fops_read`:

vtpm_proxy_fops_read
====================

.. c:function:: ssize_t vtpm_proxy_fops_read(struct file *filp, char __user *buf, size_t count, loff_t *off)

    Read TPM commands on 'server side'

    :param struct file \*filp:
        *undescribed*

    :param char __user \*buf:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*off:
        *undescribed*

.. _`vtpm_proxy_fops_read.return-value`:

Return value
------------

     Number of bytes read or negative error code

.. _`vtpm_proxy_fops_write`:

vtpm_proxy_fops_write
=====================

.. c:function:: ssize_t vtpm_proxy_fops_write(struct file *filp, const char __user *buf, size_t count, loff_t *off)

    Write TPM responses on 'server side'

    :param struct file \*filp:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t count:
        *undescribed*

    :param loff_t \*off:
        *undescribed*

.. _`vtpm_proxy_fops_write.return-value`:

Return value
------------

     Number of bytes read or negative error value

.. _`vtpm_proxy_fops_undo_open`:

vtpm_proxy_fops_undo_open
=========================

.. c:function:: void vtpm_proxy_fops_undo_open(struct proxy_dev *proxy_dev)

    counter-part to vtpm_fops_open

    :param struct proxy_dev \*proxy_dev:
        *undescribed*

.. _`vtpm_proxy_fops_undo_open.description`:

Description
-----------

Call to undo vtpm_proxy_fops_open

.. _`vtpmx_ioc_new_dev`:

vtpmx_ioc_new_dev
=================

.. c:function:: long vtpmx_ioc_new_dev(struct file *file, unsigned int ioctl, unsigned long arg)

    handler for the \ ``VTPM_PROXY_IOC_NEW_DEV``\  ioctl

    :param struct file \*file:
        /dev/vtpmx

    :param unsigned int ioctl:
        the ioctl number

    :param unsigned long arg:
        pointer to the struct vtpmx_proxy_new_dev

.. _`vtpmx_ioc_new_dev.description`:

Description
-----------

Creates an anonymous file that is used by the process acting as a TPM to
communicate with the client processes. The function will also add a new TPM
device through which data is proxied to this TPM acting process. The caller
will be provided with a file descriptor to communicate with the clients and
major and minor numbers for the TPM device.

.. This file was automatic generated / don't edit.


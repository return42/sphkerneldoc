.. -*- coding: utf-8; mode: rst -*-

==============
vmwgfx_ioctl.c
==============


.. _`vmw_fops_poll`:

vmw_fops_poll
=============

.. c:function:: unsigned int vmw_fops_poll (struct file *filp, struct poll_table_struct *wait)

    wrapper around the drm_poll function

    :param struct file \*filp:
        See the linux fops poll documentation.

    :param struct poll_table_struct \*wait:
        See the linux fops poll documentation.



.. _`vmw_fops_poll.description`:

Description
-----------

Wrapper around the drm_poll function that makes sure the device is
processing the fifo if drm_poll decides to wait.



.. _`vmw_fops_read`:

vmw_fops_read
=============

.. c:function:: ssize_t vmw_fops_read (struct file *filp, char __user *buffer, size_t count, loff_t *offset)

    wrapper around the drm_read function

    :param struct file \*filp:
        See the linux fops read documentation.

    :param char __user \*buffer:
        See the linux fops read documentation.

    :param size_t count:
        See the linux fops read documentation.

    :param loff_t \*offset:

        *undescribed*



.. _`vmw_fops_read.offset`:

offset
------

See the linux fops read documentation.

Wrapper around the drm_read function that makes sure the device is
processing the fifo if drm_read decides to wait.


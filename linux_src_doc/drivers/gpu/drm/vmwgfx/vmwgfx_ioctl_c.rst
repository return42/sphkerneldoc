.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_ioctl.c

.. _`vmw_fops_poll`:

vmw_fops_poll
=============

.. c:function:: __poll_t vmw_fops_poll(struct file *filp, struct poll_table_struct *wait)

    wrapper around the drm_poll function

    :param filp:
        See the linux fops poll documentation.
    :type filp: struct file \*

    :param wait:
        See the linux fops poll documentation.
    :type wait: struct poll_table_struct \*

.. _`vmw_fops_poll.description`:

Description
-----------

Wrapper around the drm_poll function that makes sure the device is
processing the fifo if drm_poll decides to wait.

.. _`vmw_fops_read`:

vmw_fops_read
=============

.. c:function:: ssize_t vmw_fops_read(struct file *filp, char __user *buffer, size_t count, loff_t *offset)

    wrapper around the drm_read function

    :param filp:
        See the linux fops read documentation.
    :type filp: struct file \*

    :param buffer:
        See the linux fops read documentation.
    :type buffer: char __user \*

    :param count:
        See the linux fops read documentation.
    :type count: size_t

    :param offset:
        *undescribed*
    :type offset: loff_t \*

.. _`vmw_fops_read.offset`:

offset
------

See the linux fops read documentation.

Wrapper around the drm_read function that makes sure the device is
processing the fifo if drm_read decides to wait.

.. This file was automatic generated / don't edit.


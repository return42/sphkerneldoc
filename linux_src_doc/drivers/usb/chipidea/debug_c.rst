.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/debug.c

.. _`ci_device_show`:

ci_device_show
==============

.. c:function:: int ci_device_show(struct seq_file *s, void *data)

    prints information about device capabilities and status

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`ci_port_test_show`:

ci_port_test_show
=================

.. c:function:: int ci_port_test_show(struct seq_file *s, void *data)

    reads port test mode

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`ci_port_test_write`:

ci_port_test_write
==================

.. c:function:: ssize_t ci_port_test_write(struct file *file, const char __user *ubuf, size_t count, loff_t *ppos)

    writes port test mode

    :param file:
        *undescribed*
    :type file: struct file \*

    :param ubuf:
        *undescribed*
    :type ubuf: const char __user \*

    :param count:
        *undescribed*
    :type count: size_t

    :param ppos:
        *undescribed*
    :type ppos: loff_t \*

.. _`ci_qheads_show`:

ci_qheads_show
==============

.. c:function:: int ci_qheads_show(struct seq_file *s, void *data)

    DMA contents of all queue heads

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`ci_requests_show`:

ci_requests_show
================

.. c:function:: int ci_requests_show(struct seq_file *s, void *data)

    DMA contents of all requests currently queued (all endpts)

    :param s:
        *undescribed*
    :type s: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`dbg_create_files`:

dbg_create_files
================

.. c:function:: void dbg_create_files(struct ci_hdrc *ci)

    initializes the attribute interface

    :param ci:
        device
    :type ci: struct ci_hdrc \*

.. _`dbg_create_files.description`:

Description
-----------

This function returns an error code

.. _`dbg_remove_files`:

dbg_remove_files
================

.. c:function:: void dbg_remove_files(struct ci_hdrc *ci)

    destroys the attribute interface

    :param ci:
        device
    :type ci: struct ci_hdrc \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

=======
debug.c
=======


.. _`ci_device_show`:

ci_device_show
==============

.. c:function:: int ci_device_show (struct seq_file *s, void *data)

    :param struct seq_file \*s:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`ci_port_test_show`:

ci_port_test_show
=================

.. c:function:: int ci_port_test_show (struct seq_file *s, void *data)

    :param struct seq_file \*s:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`ci_port_test_write`:

ci_port_test_write
==================

.. c:function:: ssize_t ci_port_test_write (struct file *file, const char __user *ubuf, size_t count, loff_t *ppos)

    :param struct file \*file:

        *undescribed*

    :param const char __user \*ubuf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*ppos:

        *undescribed*



.. _`ci_qheads_show`:

ci_qheads_show
==============

.. c:function:: int ci_qheads_show (struct seq_file *s, void *data)

    :param struct seq_file \*s:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`ci_requests_show`:

ci_requests_show
================

.. c:function:: int ci_requests_show (struct seq_file *s, void *data)

    :param struct seq_file \*s:

        *undescribed*

    :param void \*data:

        *undescribed*



.. _`dbg_create_files`:

dbg_create_files
================

.. c:function:: int dbg_create_files (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        device



.. _`dbg_create_files.description`:

Description
-----------

This function returns an error code



.. _`dbg_remove_files`:

dbg_remove_files
================

.. c:function:: void dbg_remove_files (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        device


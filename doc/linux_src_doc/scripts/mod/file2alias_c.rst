.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/mod/file2alias.c

.. _`device_id_check`:

device_id_check
===============

.. c:function:: void device_id_check(const char *modname, const char *device_id, unsigned long size, unsigned long id_size, void *symval)

    in .o file. If in-consistent then userspace and kernel does not agree on actual size which is a bug. Also verify that the final entry in the table is all zeros. Ignore both checks if build host differ from target host and size differs.

    :param const char \*modname:
        *undescribed*

    :param const char \*device_id:
        *undescribed*

    :param unsigned long size:
        *undescribed*

    :param unsigned long id_size:
        *undescribed*

    :param void \*symval:
        *undescribed*

.. This file was automatic generated / don't edit.


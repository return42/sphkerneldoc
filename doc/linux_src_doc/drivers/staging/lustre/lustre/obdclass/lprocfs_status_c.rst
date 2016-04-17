.. -*- coding: utf-8; mode: rst -*-

================
lprocfs_status.c
================


.. _`flag2str`:

flag2str
========

.. c:function:: flag2str ( flag,  first)

    :param flag:

        *undescribed*

    :param first:

        *undescribed*



.. _`lprocfs_find_named_value`:

lprocfs_find_named_value
========================

.. c:function:: char *lprocfs_find_named_value (const char *buffer, const char *name, size_t *count)

    :param const char \*buffer:

        *undescribed*

    :param const char \*name:

        *undescribed*

    :param size_t \*count:

        *undescribed*



.. _`lprocfs_find_named_value.description`:

Description
-----------

value immediately following \a name, reducing \a count appropriately.
If \a name is not found the original \a buffer is returned.


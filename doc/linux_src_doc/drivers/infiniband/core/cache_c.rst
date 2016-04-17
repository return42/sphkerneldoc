.. -*- coding: utf-8; mode: rst -*-

=======
cache.c
=======


.. _`ib_cache_gid_find_by_filter`:

ib_cache_gid_find_by_filter
===========================

.. c:function:: int ib_cache_gid_find_by_filter (struct ib_device *ib_dev, const union ib_gid *gid, u8 port, bool (*filter) (const union ib_gid *, const struct ib_gid_attr *, void *, void *context, u16 *index)

    Returns the GID table index where a specified GID value occurs

    :param struct ib_device \*ib_dev:

        *undescribed*

    :param const union ib_gid \*gid:
        The GID value to search for.

    :param u8 port:

        *undescribed*

    :param bool (\*filter) (const union ib_gid \*, const struct ib_gid_attr \*, void \*):
        The filter function is executed on any matching GID in the table.
        If the filter function returns true, the corresponding index is returned,
        otherwise, we continue searching the GID table. It's guaranteed that
        while filter is executed, ndev field is valid and the structure won't
        change. filter is executed in an atomic context. filter must not be NULL.

    :param void \*context:

        *undescribed*

    :param u16 \*index:
        The index into the cached GID table where the GID was found.  This
        parameter may be NULL.



.. _`ib_cache_gid_find_by_filter.description`:

Description
-----------

:c:func:`ib_cache_gid_find_by_filter` searches for the specified GID value
of which the filter function returns true in the port's GID table.
This function is only supported on RoCE ports.


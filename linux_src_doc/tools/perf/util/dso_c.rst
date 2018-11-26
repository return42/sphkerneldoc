.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/dso.c

.. _`open_dso`:

open_dso
========

.. c:function:: int open_dso(struct dso *dso, struct machine *machine)

    Open DSO data file

    :param dso:
        dso object
    :type dso: struct dso \*

    :param machine:
        *undescribed*
    :type machine: struct machine \*

.. _`open_dso.description`:

Description
-----------

Open \ ``dso``\ 's data file descriptor and updates
list/count of open DSO objects.

.. _`close_dso`:

close_dso
=========

.. c:function:: void close_dso(struct dso *dso)

    Close DSO data file

    :param dso:
        dso object
    :type dso: struct dso \*

.. _`close_dso.description`:

Description
-----------

Close \ ``dso``\ 's data file descriptor and updates
list/count of open DSO objects.

.. _`dso__data_close`:

dso__data_close
===============

.. c:function:: void dso__data_close(struct dso *dso)

    Close DSO data file

    :param dso:
        dso object
    :type dso: struct dso \*

.. _`dso__data_close.description`:

Description
-----------

External interface to close \ ``dso``\ 's data file descriptor.

.. _`dso__data_get_fd`:

dso__data_get_fd
================

.. c:function:: int dso__data_get_fd(struct dso *dso, struct machine *machine)

    Get dso's data file descriptor

    :param dso:
        dso object
    :type dso: struct dso \*

    :param machine:
        machine object
    :type machine: struct machine \*

.. _`dso__data_get_fd.description`:

Description
-----------

External interface to find dso's file, open it and
returns file descriptor.  It should be paired with
\ :c:func:`dso__data_put_fd`\  if it returns non-negative value.

.. _`dso__data_size`:

dso__data_size
==============

.. c:function:: off_t dso__data_size(struct dso *dso, struct machine *machine)

    Return dso data size

    :param dso:
        dso object
    :type dso: struct dso \*

    :param machine:
        machine object
    :type machine: struct machine \*

.. _`dso__data_size.return`:

Return
------

dso data size

.. _`dso__data_read_offset`:

dso__data_read_offset
=====================

.. c:function:: ssize_t dso__data_read_offset(struct dso *dso, struct machine *machine, u64 offset, u8 *data, ssize_t size)

    Read data from dso file offset

    :param dso:
        dso object
    :type dso: struct dso \*

    :param machine:
        machine object
    :type machine: struct machine \*

    :param offset:
        file offset
    :type offset: u64

    :param data:
        buffer to store data
    :type data: u8 \*

    :param size:
        size of the \ ``data``\  buffer
    :type size: ssize_t

.. _`dso__data_read_offset.description`:

Description
-----------

External interface to read data from dso file offset. Open
dso data file and use cached_read to get the data.

.. _`dso__data_read_addr`:

dso__data_read_addr
===================

.. c:function:: ssize_t dso__data_read_addr(struct dso *dso, struct map *map, struct machine *machine, u64 addr, u8 *data, ssize_t size)

    Read data from dso address

    :param dso:
        dso object
    :type dso: struct dso \*

    :param map:
        *undescribed*
    :type map: struct map \*

    :param machine:
        machine object
    :type machine: struct machine \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param data:
        buffer to store data
    :type data: u8 \*

    :param size:
        size of the \ ``data``\  buffer
    :type size: ssize_t

.. _`dso__data_read_addr.description`:

Description
-----------

External interface to read data from dso address.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/direct-io.c

.. _`dio_complete`:

dio_complete
============

.. c:function:: ssize_t dio_complete(struct dio *dio, ssize_t ret, bool is_async)

    called when all DIO BIO I/O has been completed

    :param struct dio \*dio:
        *undescribed*

    :param ssize_t ret:
        *undescribed*

    :param bool is_async:
        *undescribed*

.. _`dio_complete.description`:

Description
-----------

This drops i_dio_count, lets interested parties know that a DIO operation
has completed, and calculates the resulting return code for the operation.

It lets the filesystem know if it registered an interest earlier via
get_block.  Pass the private field of the map buffer_head so that
filesystems can use it to hold additional state between get_block calls and
dio_complete.

.. _`dio_end_io`:

dio_end_io
==========

.. c:function:: void dio_end_io(struct bio *bio, int error)

    handle the end io action for the given bio

    :param struct bio \*bio:
        The direct io bio thats being completed

    :param int error:
        Error if there was one

.. _`dio_end_io.description`:

Description
-----------

This is meant to be called by any filesystem that uses their own dio_submit_t
so that the DIO specific endio actions are dealt with after the filesystem
has done it's completion work.

.. This file was automatic generated / don't edit.


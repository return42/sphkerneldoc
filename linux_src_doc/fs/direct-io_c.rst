.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/direct-io.c

.. _`dio_complete`:

dio_complete
============

.. c:function:: ssize_t dio_complete(struct dio *dio, ssize_t ret, unsigned int flags)

    called when all DIO BIO I/O has been completed

    :param dio:
        *undescribed*
    :type dio: struct dio \*

    :param ret:
        *undescribed*
    :type ret: ssize_t

    :param flags:
        *undescribed*
    :type flags: unsigned int

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

.. c:function:: void dio_end_io(struct bio *bio)

    handle the end io action for the given bio

    :param bio:
        The direct io bio thats being completed
    :type bio: struct bio \*

.. _`dio_end_io.description`:

Description
-----------

This is meant to be called by any filesystem that uses their own dio_submit_t
so that the DIO specific endio actions are dealt with after the filesystem
has done it's completion work.

.. This file was automatic generated / don't edit.


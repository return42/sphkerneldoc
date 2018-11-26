.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/mpi/mpicoder.c

.. _`mpi_read_raw_data`:

mpi_read_raw_data
=================

.. c:function:: MPI mpi_read_raw_data(const void *xbuffer, size_t nbytes)

    Read a raw byte stream as a positive integer

    :param xbuffer:
        The data to read
    :type xbuffer: const void \*

    :param nbytes:
        The amount of data to read
    :type nbytes: size_t

.. _`mpi_read_buffer`:

mpi_read_buffer
===============

.. c:function:: int mpi_read_buffer(MPI a, uint8_t *buf, unsigned buf_len, unsigned *nbytes, int *sign)

    read MPI to a bufer provided by user (msb first)

    :param a:
        a multi precision integer
    :type a: MPI

    :param buf:
        bufer to which the output will be written to. Needs to be at
        leaset mpi_get_size(a) long.
    :type buf: uint8_t \*

    :param buf_len:
        size of the buf.
    :type buf_len: unsigned

    :param nbytes:
        receives the actual length of the data written on success and
        the data to-be-written on -EOVERFLOW in case buf_len was too
        small.
    :type nbytes: unsigned \*

    :param sign:
        if not NULL, it will be set to the sign of a.
    :type sign: int \*

.. _`mpi_read_buffer.return`:

Return
------

0 on success or error code in case of error

.. _`mpi_write_to_sgl`:

mpi_write_to_sgl
================

.. c:function:: int mpi_write_to_sgl(MPI a, struct scatterlist *sgl, unsigned nbytes, int *sign)

    Funnction exports MPI to an sgl (msb first)

    :param a:
        a multi precision integer
    :type a: MPI

    :param sgl:
        scatterlist to write to. Needs to be at least
        mpi_get_size(a) long.
    :type sgl: struct scatterlist \*

    :param nbytes:
        the number of bytes to write.  Leading bytes will be
        filled with zero.
    :type nbytes: unsigned

    :param sign:
        if not NULL, it will be set to the sign of a.
    :type sign: int \*

.. _`mpi_write_to_sgl.description`:

Description
-----------

This function works in the same way as the mpi_read_buffer, but it
takes an sgl instead of u8 \* buf.

.. _`mpi_write_to_sgl.return`:

Return
------

0 on success or error code in case of error

.. This file was automatic generated / don't edit.


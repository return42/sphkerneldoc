.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/i1480/dfu/phy.c

.. _`i1480_mpi_write`:

i1480_mpi_write
===============

.. c:function:: int i1480_mpi_write(struct i1480 *i1480, const void *data, size_t size)

    :param i1480:
        Device descriptor
    :type i1480: struct i1480 \*

    :param data:
        Data array to write
    :type data: const void \*

    :param size:
        Size of the data array
    :type size: size_t

.. _`i1480_mpi_write.the-data-array-is-organized-into-pairs`:

The data array is organized into pairs
--------------------------------------


ADDRESS VALUE

ADDRESS is BE 16 bit unsigned, VALUE 8 bit unsigned. Size thus has
to be a multiple of three.

.. _`i1480_mpi_read`:

i1480_mpi_read
==============

.. c:function:: int i1480_mpi_read(struct i1480 *i1480, u8 *data, u16 srcaddr, size_t size)

    :param i1480:
        Device descriptor
    :type i1480: struct i1480 \*

    :param data:
        where to place the read array
    :type data: u8 \*

    :param srcaddr:
        Where to read from
    :type srcaddr: u16

    :param size:
        Size of the data read array
    :type size: size_t

.. _`i1480_mpi_read.description`:

Description
-----------

The command data array is organized into pairs ADDR0 ADDR1..., and
the returned data in ADDR0 VALUE0 ADDR1 VALUE1...

We generate the command array to be a sequential read and then
rearrange the result.

We use the i1480->cmd_buf for the command, i1480->evt_buf for the reply.

As the reply has to fit in 512 bytes (i1480->evt_buffer), the max amount
of values we can read is (512 - sizeof(\*reply)) / 3

.. _`i1480_phy_fw_upload`:

i1480_phy_fw_upload
===================

.. c:function:: int i1480_phy_fw_upload(struct i1480 *i1480)

    :param i1480:
        Device instance
    :type i1480: struct i1480 \*

.. _`i1480_phy_fw_upload.description`:

Description
-----------

We assume the MAC fw is up and running. This means we can use the
MPI interface to write the PHY firmware. Once done, we issue an
MBOA Reset, which will force the MAC to reset and reinitialize the
PHY. If that works, we are ready to go.

Max packet size for the MPI write is 512, so the max buffer is 480
(which gives us 160 byte triads of MSB, LSB and VAL for the data).

.. This file was automatic generated / don't edit.


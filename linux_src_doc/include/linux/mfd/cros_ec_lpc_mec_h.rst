.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/cros_ec_lpc_mec.h

.. _`cros_ec_lpc_io_bytes_mec`:

cros_ec_lpc_io_bytes_mec
========================

.. c:function:: u8 cros_ec_lpc_io_bytes_mec(enum cros_ec_lpc_mec_io_type io_type, unsigned int offset, unsigned int length, u8 *buf)

    Read / write bytes to MEC EMI port

    :param enum cros_ec_lpc_mec_io_type io_type:
        MEC_IO_READ or MEC_IO_WRITE, depending on request

    :param unsigned int offset:
        Base read / write address

    :param unsigned int length:
        Number of bytes to read / write

    :param u8 \*buf:
        Destination / source buffer

.. _`cros_ec_lpc_io_bytes_mec.description`:

Description
-----------

\ ``return``\  8-bit checksum of all bytes read / written

.. This file was automatic generated / don't edit.


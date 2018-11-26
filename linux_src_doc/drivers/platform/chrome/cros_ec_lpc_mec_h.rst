.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/chrome/cros_ec_lpc_mec.h

.. _`cros_ec_lpc_io_bytes_mec`:

cros_ec_lpc_io_bytes_mec
========================

.. c:function:: u8 cros_ec_lpc_io_bytes_mec(enum cros_ec_lpc_mec_io_type io_type, unsigned int offset, unsigned int length, u8 *buf)

    Read / write bytes to MEC EMI port

    :param io_type:
        MEC_IO_READ or MEC_IO_WRITE, depending on request
    :type io_type: enum cros_ec_lpc_mec_io_type

    :param offset:
        Base read / write address
    :type offset: unsigned int

    :param length:
        Number of bytes to read / write
    :type length: unsigned int

    :param buf:
        Destination / source buffer
    :type buf: u8 \*

.. _`cros_ec_lpc_io_bytes_mec.description`:

Description
-----------

\ ``return``\  8-bit checksum of all bytes read / written

.. This file was automatic generated / don't edit.


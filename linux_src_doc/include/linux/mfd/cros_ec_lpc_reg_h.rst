.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/cros_ec_lpc_reg.h

.. _`cros_ec_lpc_read_bytes`:

cros_ec_lpc_read_bytes
======================

.. c:function:: u8 cros_ec_lpc_read_bytes(unsigned int offset, unsigned int length, u8 *dest)

    Read bytes from a given LPC-mapped address. Returns 8-bit checksum of all bytes read.

    :param unsigned int offset:
        Base read address

    :param unsigned int length:
        Number of bytes to read

    :param u8 \*dest:
        Destination buffer

.. _`cros_ec_lpc_write_bytes`:

cros_ec_lpc_write_bytes
=======================

.. c:function:: u8 cros_ec_lpc_write_bytes(unsigned int offset, unsigned int length, u8 *msg)

    Write bytes to a given LPC-mapped address. Returns 8-bit checksum of all bytes written.

    :param unsigned int offset:
        Base write address

    :param unsigned int length:
        Number of bytes to write

    :param u8 \*msg:
        Write data buffer

.. _`cros_ec_lpc_reg_init`:

cros_ec_lpc_reg_init
====================

.. c:function:: void cros_ec_lpc_reg_init( void)

    :param  void:
        no arguments

.. _`cros_ec_lpc_reg_init.description`:

Description
-----------

Initialize register I/O.

.. _`cros_ec_lpc_reg_destroy`:

cros_ec_lpc_reg_destroy
=======================

.. c:function:: void cros_ec_lpc_reg_destroy( void)

    :param  void:
        no arguments

.. _`cros_ec_lpc_reg_destroy.description`:

Description
-----------

Cleanup reg I/O.

.. This file was automatic generated / don't edit.


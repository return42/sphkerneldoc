.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/chrome/cros_ec_lpc_reg.h

.. _`cros_ec_lpc_read_bytes`:

cros_ec_lpc_read_bytes
======================

.. c:function:: u8 cros_ec_lpc_read_bytes(unsigned int offset, unsigned int length, u8 *dest)

    Read bytes from a given LPC-mapped address. Returns 8-bit checksum of all bytes read.

    :param offset:
        Base read address
    :type offset: unsigned int

    :param length:
        Number of bytes to read
    :type length: unsigned int

    :param dest:
        Destination buffer
    :type dest: u8 \*

.. _`cros_ec_lpc_write_bytes`:

cros_ec_lpc_write_bytes
=======================

.. c:function:: u8 cros_ec_lpc_write_bytes(unsigned int offset, unsigned int length, u8 *msg)

    Write bytes to a given LPC-mapped address. Returns 8-bit checksum of all bytes written.

    :param offset:
        Base write address
    :type offset: unsigned int

    :param length:
        Number of bytes to write
    :type length: unsigned int

    :param msg:
        Write data buffer
    :type msg: u8 \*

.. _`cros_ec_lpc_reg_init`:

cros_ec_lpc_reg_init
====================

.. c:function:: void cros_ec_lpc_reg_init( void)

    :param void:
        no arguments
    :type void: 

.. _`cros_ec_lpc_reg_init.description`:

Description
-----------

Initialize register I/O.

.. _`cros_ec_lpc_reg_destroy`:

cros_ec_lpc_reg_destroy
=======================

.. c:function:: void cros_ec_lpc_reg_destroy( void)

    :param void:
        no arguments
    :type void: 

.. _`cros_ec_lpc_reg_destroy.description`:

Description
-----------

Cleanup reg I/O.

.. This file was automatic generated / don't edit.


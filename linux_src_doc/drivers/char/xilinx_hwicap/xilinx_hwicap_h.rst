.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/char/xilinx_hwicap/xilinx_hwicap.h

.. _`hwicap_type_1_read`:

hwicap_type_1_read
==================

.. c:function:: u32 hwicap_type_1_read(u32 reg)

    Generates a Type 1 read packet header.

    :param u32 reg:
        is the address of the register to be read back.

.. _`hwicap_type_1_read.return`:

Return
------

Generates a Type 1 read packet header, which is used to indirectly
read registers in the configuration logic.  This packet must then
be sent through the icap device, and a return packet received with
the information.

.. _`hwicap_type_1_write`:

hwicap_type_1_write
===================

.. c:function:: u32 hwicap_type_1_write(u32 reg)

    Generates a Type 1 write packet header

    :param u32 reg:
        is the address of the register to be read back.

.. _`hwicap_type_1_write.return`:

Return
------

Type 1 write packet header

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/vf610_nfc.c

.. _`vf610_nfc_rd_from_sram`:

vf610_nfc_rd_from_sram
======================

.. c:function:: void vf610_nfc_rd_from_sram(void *dst, const void __iomem *src, size_t len, bool fix_endian)

    :param dst:
        destination address in regular memory
    :type dst: void \*

    :param src:
        source address in SRAM buffer
    :type src: const void __iomem \*

    :param len:
        bytes to copy
    :type len: size_t

    :param fix_endian:
        Fix endianness if required
    :type fix_endian: bool

.. _`vf610_nfc_rd_from_sram.description`:

Description
-----------

Use this accessor for the internal SRAM buffers. On the ARM
Freescale Vybrid SoC it's known that the driver can treat
the SRAM buffer as if it's memory. Other platform might need
to treat the buffers differently.

The controller stores bytes from the NAND chip internally in big
endianness. On little endian platforms such as Vybrid this leads
to reversed byte order.
For performance reason (and earlier probably due to unawareness)
the driver avoids correcting endianness where it has control over
write and read side (e.g. page wise data access).

.. _`vf610_nfc_wr_to_sram`:

vf610_nfc_wr_to_sram
====================

.. c:function:: void vf610_nfc_wr_to_sram(void __iomem *dst, const void *src, size_t len, bool fix_endian)

    :param dst:
        destination address in SRAM buffer
    :type dst: void __iomem \*

    :param src:
        source address in regular memory
    :type src: const void \*

    :param len:
        bytes to copy
    :type len: size_t

    :param fix_endian:
        Fix endianness if required
    :type fix_endian: bool

.. _`vf610_nfc_wr_to_sram.description`:

Description
-----------

Use this accessor for the internal SRAM buffers. On the ARM
Freescale Vybrid SoC it's known that the driver can treat
the SRAM buffer as if it's memory. Other platform might need
to treat the buffers differently.

The controller stores bytes from the NAND chip internally in big
endianness. On little endian platforms such as Vybrid this leads
to reversed byte order.
For performance reason (and earlier probably due to unawareness)
the driver avoids correcting endianness where it has control over
write and read side (e.g. page wise data access).

.. This file was automatic generated / don't edit.


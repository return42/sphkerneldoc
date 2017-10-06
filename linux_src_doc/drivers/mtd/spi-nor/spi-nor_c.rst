.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/spi-nor/spi-nor.c

.. _`macronix_quad_enable`:

macronix_quad_enable
====================

.. c:function:: int macronix_quad_enable(struct spi_nor *nor)

    set QE bit in Status Register.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

.. _`macronix_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Status Register.

bit 6 of the Status Register is the QE bit for Macronix like QSPI memories.

.. _`macronix_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_quad_enable`:

spansion_quad_enable
====================

.. c:function:: int spansion_quad_enable(struct spi_nor *nor)

    set QE bit in Configuraiton Register.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

.. _`spansion_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function is kept for legacy purpose because it has been used for a
long time without anybody complaining but it should be considered as
deprecated and maybe buggy.
First, this function doesn't care about the previous values of the Status
and Configuration Registers when it sets the QE bit (bit 1) in the

.. _`spansion_quad_enable.configuration-register`:

Configuration Register
----------------------

all other bits are cleared, which may have unwanted
side effects like removing some block protections.
Secondly, it uses the Read Configuration Register (35h) instruction though
some very old and few memories don't support this instruction. If a pull-up
resistor is present on the MISO/IO1 line, we might still be able to pass the
"read back" test because the QSPI memory doesn't recognize the command,
so leaves the MISO/IO1 line state unchanged, hence \ :c:func:`read_cr`\  returns 0xFF.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_no_read_cr_quad_enable`:

spansion_no_read_cr_quad_enable
===============================

.. c:function:: int spansion_no_read_cr_quad_enable(struct spi_nor *nor)

    set QE bit in Configuration Register.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

.. _`spansion_no_read_cr_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function should be used with QSPI memories not supporting the Read
Configuration Register (35h) instruction.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_no_read_cr_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_read_cr_quad_enable`:

spansion_read_cr_quad_enable
============================

.. c:function:: int spansion_read_cr_quad_enable(struct spi_nor *nor)

    set QE bit in Configuration Register.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

.. _`spansion_read_cr_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function should be used with QSPI memories supporting the Read
Configuration Register (35h) instruction.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_read_cr_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`sr2_bit7_quad_enable`:

sr2_bit7_quad_enable
====================

.. c:function:: int sr2_bit7_quad_enable(struct spi_nor *nor)

    set QE bit in Status Register 2.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

.. _`sr2_bit7_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Status Register 2.

This is one of the procedures to set the QE bit described in the SFDP
(JESD216 rev B) specification but no manufacturer using this procedure has
been identified yet, hence the name of the function.

.. _`sr2_bit7_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_read_sfdp`:

spi_nor_read_sfdp
=================

.. c:function:: int spi_nor_read_sfdp(struct spi_nor *nor, u32 addr, size_t len, void *buf)

    read Serial Flash Discoverable Parameters.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

    :param u32 addr:
        offset in the SFDP area to start reading data from

    :param size_t len:
        number of bytes to read

    :param void \*buf:
        buffer where the SFDP data are copied into (dma-safe memory)

.. _`spi_nor_read_sfdp.description`:

Description
-----------

Whatever the actual numbers of bytes for address and dummy cycles are
for (Fast) Read commands, the Read SFDP (5Ah) instruction is always
followed by a 3-byte address and 8 dummy clock cycles.

.. _`spi_nor_read_sfdp.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_read_sfdp_dma_unsafe`:

spi_nor_read_sfdp_dma_unsafe
============================

.. c:function:: int spi_nor_read_sfdp_dma_unsafe(struct spi_nor *nor, u32 addr, size_t len, void *buf)

    read Serial Flash Discoverable Parameters.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

    :param u32 addr:
        offset in the SFDP area to start reading data from

    :param size_t len:
        number of bytes to read

    :param void \*buf:
        buffer where the SFDP data are copied into

.. _`spi_nor_read_sfdp_dma_unsafe.description`:

Description
-----------

Wrap \ :c:func:`spi_nor_read_sfdp`\  using a kmalloc'ed bounce buffer as \ ``buf``\  is now not
guaranteed to be dma-safe.

.. _`spi_nor_read_sfdp_dma_unsafe.return`:

Return
------

-ENOMEM if \ :c:func:`kmalloc`\  fails, the return code of \ :c:func:`spi_nor_read_sfdp`\ 
otherwise.

.. _`spi_nor_parse_bfpt`:

spi_nor_parse_bfpt
==================

.. c:function:: int spi_nor_parse_bfpt(struct spi_nor *nor, const struct sfdp_parameter_header *bfpt_header, struct spi_nor_flash_parameter *params)

    read and parse the Basic Flash Parameter Table.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

    :param const struct sfdp_parameter_header \*bfpt_header:
        pointer to the 'struct sfdp_parameter_header' describing
        the Basic Flash Parameter Table length and version

    :param struct spi_nor_flash_parameter \*params:
        pointer to the 'struct spi_nor_flash_parameter' to be
        filled

.. _`spi_nor_parse_bfpt.description`:

Description
-----------

The Basic Flash Parameter Table is the main and only mandatory table as
defined by the SFDP (JESD216) specification.
It provides us with the total size (memory density) of the data array and
the number of address bytes for Fast Read, Page Program and Sector Erase
commands.
For Fast READ commands, it also gives the number of mode clock cycles and
wait states (regrouped in the number of dummy clock cycles) for each
supported instruction op code.
For Page Program, the page size is now available since JESD216 rev A, however
the supported instruction op codes are still not provided.
For Sector Erase commands, this table stores the supported instruction op
codes and the associated sector sizes.
Finally, the Quad Enable Requirements (QER) are also available since JESD216
rev A. The QER bits encode the manufacturer dependent procedure to be
executed to set the Quad Enable (QE) bit in some internal register of the
Quad SPI memory. Indeed the QE bit, when it exists, must be set before
sending any Quad SPI command to the memory. Actually, setting the QE bit
tells the memory to reassign its WP# and HOLD#/RESET# pins to functions IO2
and IO3 hence enabling 4 (Quad) I/O lines.

.. _`spi_nor_parse_bfpt.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_parse_sfdp`:

spi_nor_parse_sfdp
==================

.. c:function:: int spi_nor_parse_sfdp(struct spi_nor *nor, struct spi_nor_flash_parameter *params)

    parse the Serial Flash Discoverable Parameters.

    :param struct spi_nor \*nor:
        pointer to a 'struct spi_nor'

    :param struct spi_nor_flash_parameter \*params:
        pointer to the 'struct spi_nor_flash_parameter' to be
        filled

.. _`spi_nor_parse_sfdp.description`:

Description
-----------

The Serial Flash Discoverable Parameters are described by the JEDEC JESD216
specification. This is a standard which tends to supported by almost all
(Q)SPI memory manufacturers. Those hard-coded tables allow us to learn at
runtime the main parameters needed to perform basic SPI flash operations such
as Fast Read, Page Program or Sector Erase commands.

.. _`spi_nor_parse_sfdp.return`:

Return
------

0 on success, -errno otherwise.

.. This file was automatic generated / don't edit.


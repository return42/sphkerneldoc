.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_legacy.c

.. _`nand_read_byte`:

nand_read_byte
==============

.. c:function:: uint8_t nand_read_byte(struct nand_chip *chip)

    [DEFAULT] read one byte from the chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. _`nand_read_byte.description`:

Description
-----------

Default read function for 8bit buswidth

.. _`nand_read_byte16`:

nand_read_byte16
================

.. c:function:: uint8_t nand_read_byte16(struct nand_chip *chip)

    [DEFAULT] read one byte endianness aware from the chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. _`nand_read_byte16.description`:

Description
-----------

Default read function for 16bit buswidth with endianness conversion.

.. _`nand_select_chip`:

nand_select_chip
================

.. c:function:: void nand_select_chip(struct nand_chip *chip, int chipnr)

    [DEFAULT] control CE line

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param chipnr:
        chipnumber to select, -1 for deselect
    :type chipnr: int

.. _`nand_select_chip.description`:

Description
-----------

Default select function for 1 chip devices.

.. _`nand_write_byte`:

nand_write_byte
===============

.. c:function:: void nand_write_byte(struct nand_chip *chip, uint8_t byte)

    [DEFAULT] write single byte to chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param byte:
        value to write
    :type byte: uint8_t

.. _`nand_write_byte.description`:

Description
-----------

Default function to write a byte to I/O[7:0]

.. _`nand_write_byte16`:

nand_write_byte16
=================

.. c:function:: void nand_write_byte16(struct nand_chip *chip, uint8_t byte)

    [DEFAULT] write single byte to a chip with width 16

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param byte:
        value to write
    :type byte: uint8_t

.. _`nand_write_byte16.description`:

Description
-----------

Default function to write a byte to I/O[7:0] on a 16-bit wide chip.

.. _`nand_write_buf`:

nand_write_buf
==============

.. c:function:: void nand_write_buf(struct nand_chip *chip, const uint8_t *buf, int len)

    [DEFAULT] write buffer to chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param len:
        number of bytes to write
    :type len: int

.. _`nand_write_buf.description`:

Description
-----------

Default write function for 8bit buswidth.

.. _`nand_read_buf`:

nand_read_buf
=============

.. c:function:: void nand_read_buf(struct nand_chip *chip, uint8_t *buf, int len)

    [DEFAULT] read chip data into buffer

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: uint8_t \*

    :param len:
        number of bytes to read
    :type len: int

.. _`nand_read_buf.description`:

Description
-----------

Default read function for 8bit buswidth.

.. _`nand_write_buf16`:

nand_write_buf16
================

.. c:function:: void nand_write_buf16(struct nand_chip *chip, const uint8_t *buf, int len)

    [DEFAULT] write buffer to chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param len:
        number of bytes to write
    :type len: int

.. _`nand_write_buf16.description`:

Description
-----------

Default write function for 16bit buswidth.

.. _`nand_read_buf16`:

nand_read_buf16
===============

.. c:function:: void nand_read_buf16(struct nand_chip *chip, uint8_t *buf, int len)

    [DEFAULT] read chip data into buffer

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store date
    :type buf: uint8_t \*

    :param len:
        number of bytes to read
    :type len: int

.. _`nand_read_buf16.description`:

Description
-----------

Default read function for 16bit buswidth.

.. _`panic_nand_wait_ready`:

panic_nand_wait_ready
=====================

.. c:function:: void panic_nand_wait_ready(struct mtd_info *mtd, unsigned long timeo)

    [GENERIC] Wait for the ready pin after commands.

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param timeo:
        Timeout
    :type timeo: unsigned long

.. _`panic_nand_wait_ready.description`:

Description
-----------

Helper function for nand_wait_ready used when needing to wait in interrupt
context.

.. _`nand_wait_ready`:

nand_wait_ready
===============

.. c:function:: void nand_wait_ready(struct nand_chip *chip)

    [GENERIC] Wait for the ready pin after commands.

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. _`nand_wait_ready.description`:

Description
-----------

Wait for the ready pin after a command, and warn if a timeout occurs.

.. _`nand_wait_status_ready`:

nand_wait_status_ready
======================

.. c:function:: void nand_wait_status_ready(struct mtd_info *mtd, unsigned long timeo)

    [GENERIC] Wait for the ready status after commands.

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param timeo:
        Timeout in ms
    :type timeo: unsigned long

.. _`nand_wait_status_ready.description`:

Description
-----------

Wait for status ready (i.e. command done) or timeout.

.. _`nand_command`:

nand_command
============

.. c:function:: void nand_command(struct nand_chip *chip, unsigned int command, int column, int page_addr)

    [DEFAULT] Send command to NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param command:
        the command to be sent
    :type command: unsigned int

    :param column:
        the column address for this command, -1 if none
    :type column: int

    :param page_addr:
        the page address for this command, -1 if none
    :type page_addr: int

.. _`nand_command.description`:

Description
-----------

Send command to NAND device. This function is used for small page devices
(512 Bytes per page).

.. _`nand_command_lp`:

nand_command_lp
===============

.. c:function:: void nand_command_lp(struct nand_chip *chip, unsigned int command, int column, int page_addr)

    [DEFAULT] Send command to NAND large page device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param command:
        the command to be sent
    :type command: unsigned int

    :param column:
        the column address for this command, -1 if none
    :type column: int

    :param page_addr:
        the page address for this command, -1 if none
    :type page_addr: int

.. _`nand_command_lp.description`:

Description
-----------

Send command to NAND device. This is the version for the new large page
devices. We don't have the separate regions as we have in the small page
devices. We must emulate NAND_CMD_READOOB to keep the code compatible.

.. _`nand_get_set_features_notsupp`:

nand_get_set_features_notsupp
=============================

.. c:function:: int nand_get_set_features_notsupp(struct nand_chip *chip, int addr, u8 *subfeature_param)

    set/get features stub returning -ENOTSUPP

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param addr:
        feature address.
    :type addr: int

    :param subfeature_param:
        the subfeature parameters, a four bytes array.
    :type subfeature_param: u8 \*

.. _`nand_get_set_features_notsupp.description`:

Description
-----------

Should be used by NAND controller drivers that do not support the SET/GET
FEATURES operations.

.. _`nand_wait`:

nand_wait
=========

.. c:function:: int nand_wait(struct nand_chip *chip)

    [DEFAULT] wait until the command is done

    :param chip:
        NAND chip structure
    :type chip: struct nand_chip \*

.. _`nand_wait.description`:

Description
-----------

Wait for command done. This applies to erase and program only.

.. This file was automatic generated / don't edit.


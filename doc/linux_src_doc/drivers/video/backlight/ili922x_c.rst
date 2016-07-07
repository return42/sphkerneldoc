.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/ili922x.c

.. _`start_byte`:

START_BYTE
==========

.. c:function::  START_BYTE( id,  rs,  rw)

    :param  id:
        display's id as set by the manufacturer

    :param  rs:
        operation type bit, one of:
        - START_RS_INDEX      set the index register
        - START_RS_REG        write/read registers/GRAM

    :param  rw:
        read/write operation
        - START_RW_WRITE       write
        - START_RW_READ        read

.. _`start_byte.description`:

Description
-----------

Set the start byte according to the required operation.

.. _`start_byte.the-start-byte-is-defined-as`:

The start byte is defined as
----------------------------

----------------------------------
\| 0 \| 1 \| 1 \| 1 \| 0 \| ID \| RS \| RW \|
----------------------------------

.. _`check_freq_reg`:

CHECK_FREQ_REG
==============

.. c:function::  CHECK_FREQ_REG( s,  x)

    Check the frequency for the SPI transfer. According to the datasheet, the controller accept higher frequency for the GRAM transfer, but it requires lower frequency when the registers are read/written. The macro sets the frequency in the spi_transfer structure if the frequency exceeds the maximum value.

    :param  s:
        *undescribed*

    :param  x:
        *undescribed*

.. _`ili922x_read_status`:

ili922x_read_status
===================

.. c:function:: int ili922x_read_status(struct spi_device *spi, u16 *rs)

    read status register from display

    :param struct spi_device \*spi:
        spi device

    :param u16 \*rs:
        output value

.. _`ili922x_read`:

ili922x_read
============

.. c:function:: int ili922x_read(struct spi_device *spi, u8 reg, u16 *rx)

    read register from display

    :param struct spi_device \*spi:
        spi device

    :param u8 reg:
        offset of the register to be read

    :param u16 \*rx:
        output value

.. _`ili922x_write`:

ili922x_write
=============

.. c:function:: int ili922x_write(struct spi_device *spi, u8 reg, u16 value)

    write a controller register

    :param struct spi_device \*spi:
        struct spi_device \*

    :param u8 reg:
        offset of the register to be written

    :param u16 value:
        value to be written

.. _`ili922x_reg_dump`:

ili922x_reg_dump
================

.. c:function:: void ili922x_reg_dump(struct spi_device *spi)

    dump all registers

    :param struct spi_device \*spi:
        *undescribed*

.. _`set_write_to_gram_reg`:

set_write_to_gram_reg
=====================

.. c:function:: void set_write_to_gram_reg(struct spi_device *spi)

    initialize the display to write the GRAM

    :param struct spi_device \*spi:
        spi device

.. _`ili922x_poweron`:

ili922x_poweron
===============

.. c:function:: int ili922x_poweron(struct spi_device *spi)

    turn the display on

    :param struct spi_device \*spi:
        spi device

.. _`ili922x_poweron.description`:

Description
-----------

The sequence to turn on the display is taken from
the datasheet and/or the example code provided by the
manufacturer.

.. _`ili922x_poweroff`:

ili922x_poweroff
================

.. c:function:: int ili922x_poweroff(struct spi_device *spi)

    turn the display off

    :param struct spi_device \*spi:
        spi device

.. _`ili922x_display_init`:

ili922x_display_init
====================

.. c:function:: void ili922x_display_init(struct spi_device *spi)

    initialize the display by setting the configuration registers

    :param struct spi_device \*spi:
        spi device

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/backlight/ili922x.c

.. _`start_byte`:

START_BYTE
==========

.. c:function::  START_BYTE( id,  rs,  rw)

    :param id:
        display's id as set by the manufacturer
    :type id: 

    :param rs:
        operation type bit, one of:
        - START_RS_INDEX      set the index register
        - START_RS_REG        write/read registers/GRAM
    :type rs: 

    :param rw:
        read/write operation
        - START_RW_WRITE       write
        - START_RW_READ        read
    :type rw: 

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

    :param s:
        *undescribed*
    :type s: 

    :param x:
        *undescribed*
    :type x: 

.. _`ili922x_read_status`:

ili922x_read_status
===================

.. c:function:: int ili922x_read_status(struct spi_device *spi, u16 *rs)

    read status register from display

    :param spi:
        spi device
    :type spi: struct spi_device \*

    :param rs:
        output value
    :type rs: u16 \*

.. _`ili922x_read`:

ili922x_read
============

.. c:function:: int ili922x_read(struct spi_device *spi, u8 reg, u16 *rx)

    read register from display

    :param spi:
        spi device
    :type spi: struct spi_device \*

    :param reg:
        offset of the register to be read
    :type reg: u8

    :param rx:
        output value
    :type rx: u16 \*

.. _`ili922x_write`:

ili922x_write
=============

.. c:function:: int ili922x_write(struct spi_device *spi, u8 reg, u16 value)

    write a controller register

    :param spi:
        struct spi_device \*
    :type spi: struct spi_device \*

    :param reg:
        offset of the register to be written
    :type reg: u8

    :param value:
        value to be written
    :type value: u16

.. _`ili922x_reg_dump`:

ili922x_reg_dump
================

.. c:function:: void ili922x_reg_dump(struct spi_device *spi)

    dump all registers

    :param spi:
        *undescribed*
    :type spi: struct spi_device \*

.. _`set_write_to_gram_reg`:

set_write_to_gram_reg
=====================

.. c:function:: void set_write_to_gram_reg(struct spi_device *spi)

    initialize the display to write the GRAM

    :param spi:
        spi device
    :type spi: struct spi_device \*

.. _`ili922x_poweron`:

ili922x_poweron
===============

.. c:function:: int ili922x_poweron(struct spi_device *spi)

    turn the display on

    :param spi:
        spi device
    :type spi: struct spi_device \*

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

    :param spi:
        spi device
    :type spi: struct spi_device \*

.. _`ili922x_display_init`:

ili922x_display_init
====================

.. c:function:: void ili922x_display_init(struct spi_device *spi)

    initialize the display by setting the configuration registers

    :param spi:
        spi device
    :type spi: struct spi_device \*

.. This file was automatic generated / don't edit.


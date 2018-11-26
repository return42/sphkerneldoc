.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-ep93xx/core.c

.. _`ep93xx_chip_revision`:

ep93xx_chip_revision
====================

.. c:function:: unsigned int ep93xx_chip_revision( void)

    returns the EP93xx chip revision

    :param void:
        no arguments
    :type void: 

.. _`ep93xx_chip_revision.description`:

Description
-----------

See <mach/platform.h> for more information.

.. _`ep93xx_register_flash`:

ep93xx_register_flash
=====================

.. c:function:: void ep93xx_register_flash(unsigned int width, resource_size_t start, resource_size_t size)

    Register the external flash device.

    :param width:
        bank width in octets
    :type width: unsigned int

    :param start:
        resource start address
    :type start: resource_size_t

    :param size:
        resource size
    :type size: resource_size_t

.. _`ep93xx_register_eth`:

ep93xx_register_eth
===================

.. c:function:: void ep93xx_register_eth(struct ep93xx_eth_data *data, int copy_addr)

    Register the built-in ethernet platform device.

    :param data:
        platform specific ethernet configuration (__initdata)
    :type data: struct ep93xx_eth_data \*

    :param copy_addr:
        flag indicating that the MAC address should be copied
        from the IndAd registers (as programmed by the bootloader)
    :type copy_addr: int

.. _`ep93xx_register_i2c`:

ep93xx_register_i2c
===================

.. c:function:: void ep93xx_register_i2c(struct i2c_board_info *devices, int num)

    Register the i2c platform device.

    :param devices:
        platform specific i2c bus device information (__initdata)
    :type devices: struct i2c_board_info \*

    :param num:
        the number of devices on the i2c bus
    :type num: int

.. _`ep93xx_register_spi`:

ep93xx_register_spi
===================

.. c:function:: void ep93xx_register_spi(struct ep93xx_spi_info *info, struct spi_board_info *devices, int num)

    registers spi platform device

    :param info:
        ep93xx board specific spi master info (__initdata)
    :type info: struct ep93xx_spi_info \*

    :param devices:
        SPI devices to register (__initdata)
    :type devices: struct spi_board_info \*

    :param num:
        number of SPI devices to register
    :type num: int

.. _`ep93xx_register_spi.description`:

Description
-----------

This function registers platform device for the EP93xx SPI controller and
also makes sure that SPI pins are muxed so that I2S is not using those pins.

.. _`ep93xx_register_fb`:

ep93xx_register_fb
==================

.. c:function:: void ep93xx_register_fb(struct ep93xxfb_mach_info *data)

    Register the framebuffer platform device.

    :param data:
        platform specific framebuffer configuration (__initdata)
    :type data: struct ep93xxfb_mach_info \*

.. _`ep93xx_register_keypad`:

ep93xx_register_keypad
======================

.. c:function:: void ep93xx_register_keypad(struct ep93xx_keypad_platform_data *data)

    Register the keypad platform device.

    :param data:
        platform specific keypad configuration (__initdata)
    :type data: struct ep93xx_keypad_platform_data \*

.. This file was automatic generated / don't edit.


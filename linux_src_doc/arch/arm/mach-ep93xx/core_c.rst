.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-ep93xx/core.c

.. _`ep93xx_chip_revision`:

ep93xx_chip_revision
====================

.. c:function:: unsigned int ep93xx_chip_revision( void)

    returns the EP93xx chip revision

    :param  void:
        no arguments

.. _`ep93xx_chip_revision.description`:

Description
-----------

See <mach/platform.h> for more information.

.. _`ep93xx_register_flash`:

ep93xx_register_flash
=====================

.. c:function:: void ep93xx_register_flash(unsigned int width, resource_size_t start, resource_size_t size)

    Register the external flash device.

    :param unsigned int width:
        bank width in octets

    :param resource_size_t start:
        resource start address

    :param resource_size_t size:
        resource size

.. _`ep93xx_register_eth`:

ep93xx_register_eth
===================

.. c:function:: void ep93xx_register_eth(struct ep93xx_eth_data *data, int copy_addr)

    Register the built-in ethernet platform device.

    :param struct ep93xx_eth_data \*data:
        platform specific ethernet configuration (__initdata)

    :param int copy_addr:
        flag indicating that the MAC address should be copied
        from the IndAd registers (as programmed by the bootloader)

.. _`ep93xx_register_i2c`:

ep93xx_register_i2c
===================

.. c:function:: void ep93xx_register_i2c(struct i2c_board_info *devices, int num)

    Register the i2c platform device.

    :param struct i2c_board_info \*devices:
        platform specific i2c bus device information (__initdata)

    :param int num:
        the number of devices on the i2c bus

.. _`ep93xx_register_spi`:

ep93xx_register_spi
===================

.. c:function:: void ep93xx_register_spi(struct ep93xx_spi_info *info, struct spi_board_info *devices, int num)

    registers spi platform device

    :param struct ep93xx_spi_info \*info:
        ep93xx board specific spi master info (__initdata)

    :param struct spi_board_info \*devices:
        SPI devices to register (__initdata)

    :param int num:
        number of SPI devices to register

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

    :param struct ep93xxfb_mach_info \*data:
        platform specific framebuffer configuration (__initdata)

.. _`ep93xx_register_keypad`:

ep93xx_register_keypad
======================

.. c:function:: void ep93xx_register_keypad(struct ep93xx_keypad_platform_data *data)

    Register the keypad platform device.

    :param struct ep93xx_keypad_platform_data \*data:
        platform specific keypad configuration (__initdata)

.. This file was automatic generated / don't edit.


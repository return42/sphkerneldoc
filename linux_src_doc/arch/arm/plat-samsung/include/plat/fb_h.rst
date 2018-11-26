.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/fb.h

.. _`s3c_fb_set_platdata`:

s3c_fb_set_platdata
===================

.. c:function:: void s3c_fb_set_platdata(struct s3c_fb_platdata *pd)

    Setup the FB device with platform data.

    :param pd:
        The platform data to set. The data is copied from the passed structure
        so the machine data can mark the data \__initdata so that any unused
        machines will end up dumping their data at runtime.
    :type pd: struct s3c_fb_platdata \*

.. _`s3c64xx_fb_gpio_setup_24bpp`:

s3c64xx_fb_gpio_setup_24bpp
===========================

.. c:function:: void s3c64xx_fb_gpio_setup_24bpp( void)

    S3C64XX setup function for 24bpp LCD

    :param void:
        no arguments
    :type void: 

.. _`s3c64xx_fb_gpio_setup_24bpp.description`:

Description
-----------

Initialise the GPIO for an 24bpp LCD display on the RGB interface.

.. This file was automatic generated / don't edit.


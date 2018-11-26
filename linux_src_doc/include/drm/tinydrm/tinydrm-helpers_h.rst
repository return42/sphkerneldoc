.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/tinydrm/tinydrm-helpers.h

.. _`tinydrm_machine_little_endian`:

tinydrm_machine_little_endian
=============================

.. c:function:: bool tinydrm_machine_little_endian( void)

    Machine is little endian

    :param void:
        no arguments
    :type void: 

.. _`tinydrm_machine_little_endian.return`:

Return
------

true if *defined(__LITTLE_ENDIAN)*, false otherwise

.. _`tinydrm_dbg_spi_message`:

tinydrm_dbg_spi_message
=======================

.. c:function:: void tinydrm_dbg_spi_message(struct spi_device *spi, struct spi_message *m)

    Dump SPI message

    :param spi:
        SPI device
    :type spi: struct spi_device \*

    :param m:
        SPI message
    :type m: struct spi_message \*

.. _`tinydrm_dbg_spi_message.description`:

Description
-----------

Dumps info about the transfers in a SPI message including buffer content.
DEBUG has to be defined for this function to be enabled alongside setting
the DRM_UT_DRIVER bit of \ :c:type:`struct drm_debug <drm_debug>`\ .

.. This file was automatic generated / don't edit.


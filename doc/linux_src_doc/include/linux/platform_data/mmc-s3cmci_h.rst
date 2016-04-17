.. -*- coding: utf-8; mode: rst -*-

============
mmc-s3cmci.h
============


.. _`s3c24xx_mci_pdata`:

struct s3c24xx_mci_pdata
========================

.. c:type:: s3c24xx_mci_pdata

    sd/mmc controller platform data


.. _`s3c24xx_mci_pdata.definition`:

Definition
----------

.. code-block:: c

  struct s3c24xx_mci_pdata {
    unsigned int no_wprotect:1;
    unsigned int no_detect:1;
    unsigned int wprotect_invert:1;
    unsigned int detect_invert:1;
    unsigned int use_dma:1;
    unsigned int gpio_detect;
    unsigned int gpio_wprotect;
    unsigned long ocr_avail;
    void (* set_power) (unsigned char power_mode,unsigned short vdd);
  };


.. _`s3c24xx_mci_pdata.members`:

Members
-------

:``no_wprotect``:
    Set this to indicate there is no write-protect switch.

:``no_detect``:
    Set this if there is no detect switch.

:``wprotect_invert``:
    Invert the default sense of the write protect switch.

:``detect_invert``:
    Invert the default sense of the write protect switch.

:``use_dma``:
    Set to allow the use of DMA.

:``gpio_detect``:
    GPIO number for the card detect line.

:``gpio_wprotect``:
    GPIO number for the write protect line.

:``ocr_avail``:
    The mask of the available power states, non-zero to use.

:``set_power``:
    Callback to control the power mode.




.. _`s3c24xx_mci_pdata.description`:

Description
-----------

The ``gpio_detect`` is used for card detection when ``no_wprotect`` is unset,
and the default sense is that 0 returned from :c:func:`gpio_get_value` means
that a card is inserted. If ``detect_invert`` is set, then the value from
:c:func:`gpio_get_value` is inverted, which makes 1 mean card inserted.

The driver will use ``gpio_wprotect`` to signal whether the card is write
protected if ``no_wprotect`` is not set. A 0 returned from :c:func:`gpio_get_value`
means the card is read/write, and 1 means read-only. The ``wprotect_invert``
will invert the value returned from :c:func:`gpio_get_value`.

Card power is set by ``ocr_availa``\ , using MCC_VDD_ constants if it is set
to a non-zero value, otherwise the default of 3.2-3.4V is used.



.. _`s3c24xx_mci_set_platdata`:

s3c24xx_mci_set_platdata
========================

.. c:function:: void s3c24xx_mci_set_platdata (struct s3c24xx_mci_pdata *pdata)

    set platform data for mmc/sdi device

    :param struct s3c24xx_mci_pdata \*pdata:
        The platform data



.. _`s3c24xx_mci_set_platdata.description`:

Description
-----------

Copy the platform data supplied by ``pdata`` so that this can be marked
__initdata.


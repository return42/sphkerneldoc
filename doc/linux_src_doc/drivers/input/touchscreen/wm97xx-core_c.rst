.. -*- coding: utf-8; mode: rst -*-

=============
wm97xx-core.c
=============


.. _`wm97xx_read_aux_adc`:

wm97xx_read_aux_adc
===================

.. c:function:: int wm97xx_read_aux_adc (struct wm97xx *wm, u16 adcsel)

    Read the aux adc.

    :param struct wm97xx \*wm:
        wm97xx device.

    :param u16 adcsel:
        codec ADC to be read



.. _`wm97xx_read_aux_adc.description`:

Description
-----------

Reads the selected AUX ADC.



.. _`wm97xx_get_gpio`:

wm97xx_get_gpio
===============

.. c:function:: enum wm97xx_gpio_status wm97xx_get_gpio (struct wm97xx *wm, u32 gpio)

    Get the status of a codec GPIO.

    :param struct wm97xx \*wm:
        wm97xx device.

    :param u32 gpio:
        gpio



.. _`wm97xx_get_gpio.description`:

Description
-----------

Get the status of a codec GPIO pin



.. _`wm97xx_set_gpio`:

wm97xx_set_gpio
===============

.. c:function:: void wm97xx_set_gpio (struct wm97xx *wm, u32 gpio, enum wm97xx_gpio_status status)

    Set the status of a codec GPIO.

    :param struct wm97xx \*wm:
        wm97xx device.

    :param u32 gpio:
        gpio

    :param enum wm97xx_gpio_status status:

        *undescribed*



.. _`wm97xx_set_gpio.description`:

Description
-----------


Set the status of a codec GPIO pin



.. _`wm97xx_ts_input_open`:

wm97xx_ts_input_open
====================

.. c:function:: int wm97xx_ts_input_open (struct input_dev *idev)

    Open the touch screen input device.

    :param struct input_dev \*idev:
        Input device to be opened.



.. _`wm97xx_ts_input_open.description`:

Description
-----------

Called by the input sub system to open a wm97xx touchscreen device.
Starts the touchscreen thread and touch digitiser.



.. _`wm97xx_ts_input_close`:

wm97xx_ts_input_close
=====================

.. c:function:: void wm97xx_ts_input_close (struct input_dev *idev)

    Close the touch screen input device.

    :param struct input_dev \*idev:
        Input device to be closed.



.. _`wm97xx_ts_input_close.description`:

Description
-----------

Called by the input sub system to close a wm97xx touchscreen
device.  Kills the touchscreen thread and stops the touch
digitiser.


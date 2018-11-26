.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/wm97xx-core.c

.. _`wm97xx_read_aux_adc`:

wm97xx_read_aux_adc
===================

.. c:function:: int wm97xx_read_aux_adc(struct wm97xx *wm, u16 adcsel)

    Read the aux adc.

    :param wm:
        wm97xx device.
    :type wm: struct wm97xx \*

    :param adcsel:
        codec ADC to be read
    :type adcsel: u16

.. _`wm97xx_read_aux_adc.description`:

Description
-----------

Reads the selected AUX ADC.

.. _`wm97xx_get_gpio`:

wm97xx_get_gpio
===============

.. c:function:: enum wm97xx_gpio_status wm97xx_get_gpio(struct wm97xx *wm, u32 gpio)

    Get the status of a codec GPIO.

    :param wm:
        wm97xx device.
    :type wm: struct wm97xx \*

    :param gpio:
        gpio
    :type gpio: u32

.. _`wm97xx_get_gpio.description`:

Description
-----------

Get the status of a codec GPIO pin

.. _`wm97xx_set_gpio`:

wm97xx_set_gpio
===============

.. c:function:: void wm97xx_set_gpio(struct wm97xx *wm, u32 gpio, enum wm97xx_gpio_status status)

    Set the status of a codec GPIO.

    :param wm:
        wm97xx device.
    :type wm: struct wm97xx \*

    :param gpio:
        gpio
    :type gpio: u32

    :param status:
        *undescribed*
    :type status: enum wm97xx_gpio_status

.. _`wm97xx_set_gpio.description`:

Description
-----------


Set the status of a codec GPIO pin

.. _`wm97xx_ts_input_open`:

wm97xx_ts_input_open
====================

.. c:function:: int wm97xx_ts_input_open(struct input_dev *idev)

    Open the touch screen input device.

    :param idev:
        Input device to be opened.
    :type idev: struct input_dev \*

.. _`wm97xx_ts_input_open.description`:

Description
-----------

Called by the input sub system to open a wm97xx touchscreen device.
Starts the touchscreen thread and touch digitiser.

.. _`wm97xx_ts_input_close`:

wm97xx_ts_input_close
=====================

.. c:function:: void wm97xx_ts_input_close(struct input_dev *idev)

    Close the touch screen input device.

    :param idev:
        Input device to be closed.
    :type idev: struct input_dev \*

.. _`wm97xx_ts_input_close.description`:

Description
-----------

Called by the input sub system to close a wm97xx touchscreen
device.  Kills the touchscreen thread and stops the touch
digitiser.

.. This file was automatic generated / don't edit.


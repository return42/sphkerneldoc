.. -*- coding: utf-8; mode: rst -*-

=======
sht15.h
=======


.. _`sht15_platform_data`:

struct sht15_platform_data
==========================

.. c:type:: sht15_platform_data

    sht15 connectivity info


.. _`sht15_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct sht15_platform_data {
    int gpio_data;
    int gpio_sck;
    int supply_mv;
    bool checksum;
    bool no_otp_reload;
    bool low_resolution;
  };


.. _`sht15_platform_data.members`:

Members
-------

:``gpio_data``:
    no. of gpio to which bidirectional data line is
    connected.

:``gpio_sck``:
    no. of gpio to which the data clock is connected.

:``supply_mv``:
    supply voltage in mv. Overridden by regulator if
    available.

:``checksum``:
    flag to indicate the checksum should be validated.

:``no_otp_reload``:
    flag to indicate no reload from OTP.

:``low_resolution``:
    flag to indicate the temp/humidity resolution to use.



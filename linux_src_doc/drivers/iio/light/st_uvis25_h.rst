.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/light/st_uvis25.h

.. _`st_uvis25_hw`:

struct st_uvis25_hw
===================

.. c:type:: struct st_uvis25_hw

    ST UVIS25 sensor instance

.. _`st_uvis25_hw.definition`:

Definition
----------

.. code-block:: c

    struct st_uvis25_hw {
        struct regmap *regmap;
        struct iio_trigger *trig;
        bool enabled;
        int irq;
    }

.. _`st_uvis25_hw.members`:

Members
-------

regmap
    Register map of the device.

trig
    The trigger in use by the driver.

enabled
    Status of the sensor (false->off, true->on).

irq
    Device interrupt line (I2C or SPI).

.. This file was automatic generated / don't edit.


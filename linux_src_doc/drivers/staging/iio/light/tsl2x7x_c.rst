.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/light/tsl2x7x.c

.. _`tsl2x7x_get_lux`:

tsl2x7x_get_lux
===============

.. c:function:: int tsl2x7x_get_lux(struct iio_dev *indio_dev)

    Reads and calculates current lux value.

    :param struct iio_dev \*indio_dev:
        pointer to IIO device

.. _`tsl2x7x_get_lux.description`:

Description
-----------

The raw ch0 and ch1 values of the ambient light sensed in the last
integration cycle are read from the device.
Time scale factor array values are adjusted based on the integration time.
The raw values are multiplied by a scale factor, and device gain is obtained
using gain index. Limit checks are done next, then the ratio of a multiple
of ch1 value, to the ch0 value, is calculated. Array tsl2x7x_device_lux[]
is then scanned to find the first ratio value that is just above the ratio
we just calculated. The ch0 and ch1 multiplier constants in the array are
then used along with the time scale factor array values, to calculate the
lux.

.. _`tsl2x7x_get_prox`:

tsl2x7x_get_prox
================

.. c:function:: int tsl2x7x_get_prox(struct iio_dev *indio_dev)

    Reads proximity data registers and updates chip->prox_data.

    :param struct iio_dev \*indio_dev:
        pointer to IIO device

.. _`tsl2x7x_defaults`:

tsl2x7x_defaults
================

.. c:function:: void tsl2x7x_defaults(struct tsl2X7X_chip *chip)

    Populates the device nominal operating parameters with those provided by a 'platform' data struct or with prefined defaults.

    :param struct tsl2X7X_chip \*chip:
        pointer to device structure.

.. _`tsl2x7x_als_calibrate`:

tsl2x7x_als_calibrate
=====================

.. c:function:: int tsl2x7x_als_calibrate(struct iio_dev *indio_dev)

    Obtain single reading and calculate the als_gain_trim.

    :param struct iio_dev \*indio_dev:
        pointer to IIO device

.. _`tsl2x7x_invoke_change`:

tsl2x7x_invoke_change
=====================

.. c:function:: int tsl2x7x_invoke_change(struct iio_dev *indio_dev)

    :param struct iio_dev \*indio_dev:
        pointer to IIO device

.. _`tsl2x7x_invoke_change.description`:

Description
-----------

Obtain and lock both ALS and PROX resources,
determine and save device state (On/Off),
cycle device to implement updated parameter,
put device back into proper state, and unlock
resource.

.. _`tsl2x7x_prox_cal`:

tsl2x7x_prox_cal
================

.. c:function:: void tsl2x7x_prox_cal(struct iio_dev *indio_dev)

    Calculates std. and sets thresholds.

    :param struct iio_dev \*indio_dev:
        pointer to IIO device

.. _`tsl2x7x_prox_cal.description`:

Description
-----------

Calculates a standard deviation based on the samples,
and sets the threshold accordingly.

.. This file was automatic generated / don't edit.


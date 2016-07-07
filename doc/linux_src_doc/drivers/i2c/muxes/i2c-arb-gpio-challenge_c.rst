.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/muxes/i2c-arb-gpio-challenge.c

.. _`i2c_arbitrator_data`:

struct i2c_arbitrator_data
==========================

.. c:type:: struct i2c_arbitrator_data

    Driver data for I2C arbitrator

.. _`i2c_arbitrator_data.definition`:

Definition
----------

.. code-block:: c

    struct i2c_arbitrator_data {
        int our_gpio;
        int our_gpio_release;
        int their_gpio;
        int their_gpio_release;
        unsigned int slew_delay_us;
        unsigned int wait_retry_us;
        unsigned int wait_free_us;
    }

.. _`i2c_arbitrator_data.members`:

Members
-------

our_gpio
    GPIO we'll use to claim.

our_gpio_release
    0 if active high; 1 if active low; AKA if the GPIO ==
    this then consider it released.

their_gpio
    GPIO that the other side will use to claim.

their_gpio_release
    0 if active high; 1 if active low; AKA if the GPIO ==
    this then consider it released.

slew_delay_us
    microseconds to wait for a GPIO to go high.

wait_retry_us
    we'll attempt another claim after this many microseconds.

wait_free_us
    we'll give up after this many microseconds.

.. _`i2c_arbitrator_select`:

i2c_arbitrator_select
=====================

.. c:function:: int i2c_arbitrator_select(struct i2c_mux_core *muxc, u32 chan)

    claim the I2C bus

    :param struct i2c_mux_core \*muxc:
        *undescribed*

    :param u32 chan:
        *undescribed*

.. _`i2c_arbitrator_select.description`:

Description
-----------

Use the GPIO-based signalling protocol; return -EBUSY if we fail.

.. _`i2c_arbitrator_deselect`:

i2c_arbitrator_deselect
=======================

.. c:function:: int i2c_arbitrator_deselect(struct i2c_mux_core *muxc, u32 chan)

    release the I2C bus

    :param struct i2c_mux_core \*muxc:
        *undescribed*

    :param u32 chan:
        *undescribed*

.. _`i2c_arbitrator_deselect.description`:

Description
-----------

Release the I2C bus using the GPIO-based signalling protocol.

.. This file was automatic generated / don't edit.


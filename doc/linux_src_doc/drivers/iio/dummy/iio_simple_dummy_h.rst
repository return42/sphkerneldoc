.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_simple_dummy.h

.. _`iio_dummy_state`:

struct iio_dummy_state
======================

.. c:type:: struct iio_dummy_state

    device instance specific state.

.. _`iio_dummy_state.definition`:

Definition
----------

.. code-block:: c

    struct iio_dummy_state {
        int dac_val;
        int single_ended_adc_val;
        int differential_adc_val[2];
        int accel_val;
        int accel_calibbias;
        int activity_running;
        int activity_walking;
        const struct iio_dummy_accel_calibscale *accel_calibscale;
        struct mutex lock;
        struct iio_dummy_regs *regs;
        int steps_enabled;
        int steps;
        int height;
        #ifdef CONFIG_IIO_SIMPLE_DUMMY_EVENTS
        int event_irq;
        int event_val;
        bool event_en;
        s64 event_timestamp;
        #endif
    }

.. _`iio_dummy_state.members`:

Members
-------

dac_val
    cache for dac value

single_ended_adc_val
    cache for single ended adc value

differential_adc_val
    cache for differential adc value

accel_val
    cache for acceleration value

accel_calibbias
    cache for acceleration calibbias

activity_running
    *undescribed*

activity_walking
    *undescribed*

accel_calibscale
    cache for acceleration calibscale

lock
    lock to ensure state is consistent

regs
    *undescribed*

steps_enabled
    *undescribed*

steps
    *undescribed*

height
    *undescribed*

event_irq
    irq number for event line (faked)

event_val
    cache for event threshold value

event_en
    cache of whether event is enabled

event_timestamp
    *undescribed*

.. _`iio_simple_dummy_scan_elements`:

enum iio_simple_dummy_scan_elements
===================================

.. c:type:: enum iio_simple_dummy_scan_elements

    scan index enum

.. _`iio_simple_dummy_scan_elements.definition`:

Definition
----------

.. code-block:: c

    enum iio_simple_dummy_scan_elements {
        DUMMY_INDEX_VOLTAGE_0,
        DUMMY_INDEX_DIFFVOLTAGE_1M2,
        DUMMY_INDEX_DIFFVOLTAGE_3M4,
        DUMMY_INDEX_ACCELX
    };

.. _`iio_simple_dummy_scan_elements.constants`:

Constants
---------

DUMMY_INDEX_VOLTAGE_0
    the single ended voltage channel

DUMMY_INDEX_DIFFVOLTAGE_1M2
    first differential channel

DUMMY_INDEX_DIFFVOLTAGE_3M4
    second differential channel

DUMMY_INDEX_ACCELX
    acceleration channel

.. _`iio_simple_dummy_scan_elements.description`:

Description
-----------

Enum provides convenient numbering for the scan index.

.. This file was automatic generated / don't edit.


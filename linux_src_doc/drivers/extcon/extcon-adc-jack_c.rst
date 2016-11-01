.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon-adc-jack.c

.. _`adc_jack_data`:

struct adc_jack_data
====================

.. c:type:: struct adc_jack_data

    internal data for adc_jack device driver

.. _`adc_jack_data.definition`:

Definition
----------

.. code-block:: c

    struct adc_jack_data {
        struct device *dev;
        struct extcon_dev *edev;
        const unsigned int **cable_names;
        struct adc_jack_cond *adc_conditions;
        int num_conditions;
        int irq;
        unsigned long handling_delay;
        struct delayed_work handler;
        struct iio_channel *chan;
        bool wakeup_source;
    }

.. _`adc_jack_data.members`:

Members
-------

dev
    *undescribed*

edev
    extcon device.

cable_names
    list of supported cables.

adc_conditions
    list of adc value conditions.

num_conditions
    size of adc_conditions.

irq
    irq number of attach/detach event (0 if not exist).

handling_delay
    interrupt handler will schedule extcon event
    handling at handling_delay jiffies.

handler
    extcon event handler called by interrupt handler.

chan
    iio channel being queried.

wakeup_source
    *undescribed*

.. This file was automatic generated / don't edit.


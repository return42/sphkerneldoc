.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/ad799x.c

.. _`ad799x_chip_config`:

struct ad799x_chip_config
=========================

.. c:type:: struct ad799x_chip_config

    chip specific information

.. _`ad799x_chip_config.definition`:

Definition
----------

.. code-block:: c

    struct ad799x_chip_config {
        const struct iio_chan_spec channel;
        u16 default_config;
        const struct iio_info *info;
    }

.. _`ad799x_chip_config.members`:

Members
-------

channel
    channel specification

default_config
    device default configuration

info
    pointer to iio_info struct

.. _`ad799x_chip_info`:

struct ad799x_chip_info
=======================

.. c:type:: struct ad799x_chip_info

    chip specific information

.. _`ad799x_chip_info.definition`:

Definition
----------

.. code-block:: c

    struct ad799x_chip_info {
        int num_channels;
        const struct ad799x_chip_config noirq_config;
        const struct ad799x_chip_config irq_config;
    }

.. _`ad799x_chip_info.members`:

Members
-------

num_channels
    number of channels

noirq_config
    device configuration w/o IRQ

irq_config
    device configuration w/IRQ

.. _`ad799x_trigger_handler`:

ad799x_trigger_handler
======================

.. c:function:: irqreturn_t ad799x_trigger_handler(int irq, void *p)

    :param int irq:
        *undescribed*

    :param void \*p:
        *undescribed*

.. _`ad799x_trigger_handler.description`:

Description
-----------

Currently there is no option in this driver to disable the saving of
timestamps within the ring.

.. This file was automatic generated / don't edit.


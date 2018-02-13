.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/intel/pinctrl-intel.c

.. _`intel_pinctrl`:

struct intel_pinctrl
====================

.. c:type:: struct intel_pinctrl

    Intel pinctrl private structure

.. _`intel_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct intel_pinctrl {
        struct device *dev;
        raw_spinlock_t lock;
        struct pinctrl_desc pctldesc;
        struct pinctrl_dev *pctldev;
        struct gpio_chip chip;
        const struct intel_pinctrl_soc_data *soc;
        struct intel_community *communities;
        size_t ncommunities;
        struct intel_pinctrl_context context;
        int irq;
    }

.. _`intel_pinctrl.members`:

Members
-------

dev
    Pointer to the device structure

lock
    Lock to serialize register access

pctldesc
    Pin controller description

pctldev
    Pointer to the pin controller device

chip
    GPIO chip in this pin controller

soc
    SoC/PCH specific pin configuration data

communities
    All communities in this pin controller

ncommunities
    Number of communities in this pin controller

context
    Configuration saved over system sleep

irq
    pinctrl/GPIO chip irq number

.. _`intel_gpio_to_pin`:

intel_gpio_to_pin
=================

.. c:function:: int intel_gpio_to_pin(struct intel_pinctrl *pctrl, unsigned offset, const struct intel_community **community, const struct intel_padgroup **padgrp)

    Translate from GPIO offset to pin number

    :param struct intel_pinctrl \*pctrl:
        Pinctrl structure

    :param unsigned offset:
        GPIO offset from gpiolib

    :param const struct intel_community \*\*community:
        *undescribed*

    :param const struct intel_padgroup \*\*padgrp:
        Pad group is filled here if not \ ``NULL``\ 

.. _`intel_gpio_to_pin.description`:

Description
-----------

When coming through gpiolib irqchip, the GPIO offset is not
automatically translated to pinctrl pin number. This function can be
used to find out the corresponding pinctrl pin.

.. This file was automatic generated / don't edit.


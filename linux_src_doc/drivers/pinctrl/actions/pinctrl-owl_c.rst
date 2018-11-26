.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/actions/pinctrl-owl.c

.. _`owl_pinctrl`:

struct owl_pinctrl
==================

.. c:type:: struct owl_pinctrl

    pinctrl state of the device

.. _`owl_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct owl_pinctrl {
        struct device *dev;
        struct pinctrl_dev *pctrldev;
        struct gpio_chip chip;
        raw_spinlock_t lock;
        struct clk *clk;
        const struct owl_pinctrl_soc_data *soc;
        void __iomem *base;
        struct irq_chip irq_chip;
        unsigned int num_irq;
        unsigned int *irq;
    }

.. _`owl_pinctrl.members`:

Members
-------

dev
    device handle

pctrldev
    pinctrl handle

chip
    gpio chip

lock
    spinlock to protect registers

clk
    *undescribed*

soc
    reference to soc_data

base
    pinctrl register base address

irq_chip
    *undescribed*

num_irq
    *undescribed*

irq
    *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/qcom/pinctrl-msm.c

.. _`msm_pinctrl`:

struct msm_pinctrl
==================

.. c:type:: struct msm_pinctrl

    state for a pinctrl-msm device

.. _`msm_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct msm_pinctrl {
        struct device *dev;
        struct pinctrl_dev *pctrl;
        struct gpio_chip chip;
        struct notifier_block restart_nb;
        int irq;
        spinlock_t lock;
        unsigned long dual_edge_irqs[BITS_TO_LONGS(MAX_NR_GPIO)];
        unsigned long enabled_irqs[BITS_TO_LONGS(MAX_NR_GPIO)];
        const struct msm_pinctrl_soc_data *soc;
        void __iomem *regs;
    }

.. _`msm_pinctrl.members`:

Members
-------

dev
    device handle.

pctrl
    pinctrl handle.

chip
    gpiochip handle.

restart_nb
    restart notifier block.

irq
    parent irq for the TLMM irq_chip.

lock
    Spinlock to protect register resources as well
    as msm_pinctrl data structures.

dual_edge_irqs
    Bitmap of irqs that need sw emulated dual edge
    detection.
    \ ``soc``\ ;            Reference to soc_data of platform specific data.

enabled_irqs
    Bitmap of currently enabled irqs.

soc
    *undescribed*

regs
    Base address for the TLMM register map.

.. This file was automatic generated / don't edit.


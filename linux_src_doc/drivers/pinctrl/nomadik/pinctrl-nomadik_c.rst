.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/nomadik/pinctrl-nomadik.c

.. _`nmk_pinctrl`:

struct nmk_pinctrl
==================

.. c:type:: struct nmk_pinctrl

    state container for the Nomadik pin controller

.. _`nmk_pinctrl.definition`:

Definition
----------

.. code-block:: c

    struct nmk_pinctrl {
        struct device *dev;
        struct pinctrl_dev *pctl;
        const struct nmk_pinctrl_soc_data *soc;
        void __iomem *prcm_base;
    }

.. _`nmk_pinctrl.members`:

Members
-------

dev
    containing device pointer

pctl
    corresponding pin controller device

soc
    SoC data for this specific chip

prcm_base
    PRCM register range virtual base

.. This file was automatic generated / don't edit.


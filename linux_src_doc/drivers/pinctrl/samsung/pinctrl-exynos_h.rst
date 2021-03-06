.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-exynos.h

.. _`exynos_weint_data`:

struct exynos_weint_data
========================

.. c:type:: struct exynos_weint_data

    irq specific data for all the wakeup interrupts generated by the external wakeup interrupt controller.

.. _`exynos_weint_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos_weint_data {
        unsigned int irq;
        struct samsung_pin_bank *bank;
    }

.. _`exynos_weint_data.members`:

Members
-------

irq
    interrupt number within the domain.

bank
    bank responsible for this interrupt

.. _`exynos_muxed_weint_data`:

struct exynos_muxed_weint_data
==============================

.. c:type:: struct exynos_muxed_weint_data

    irq specific data for muxed wakeup interrupts generated by the external wakeup interrupt controller.

.. _`exynos_muxed_weint_data.definition`:

Definition
----------

.. code-block:: c

    struct exynos_muxed_weint_data {
        unsigned int nr_banks;
        struct samsung_pin_bank *banks[];
    }

.. _`exynos_muxed_weint_data.members`:

Members
-------

nr_banks
    count of banks being part of the mux

banks
    array of banks being part of the mux

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-s3c64xx.c

.. _`s3c64xx_eint0_data`:

struct s3c64xx_eint0_data
=========================

.. c:type:: struct s3c64xx_eint0_data

    EINT0 common data

.. _`s3c64xx_eint0_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_eint0_data {
        struct samsung_pinctrl_drv_data *drvdata;
        struct irq_domain *domains[NUM_EINT0];
        u8 pins[NUM_EINT0];
    }

.. _`s3c64xx_eint0_data.members`:

Members
-------

drvdata
    pin controller driver data

domains
    IRQ domains of particular EINT0 interrupts

pins
    pin offsets inside of banks of particular EINT0 interrupts

.. _`s3c64xx_eint0_domain_data`:

struct s3c64xx_eint0_domain_data
================================

.. c:type:: struct s3c64xx_eint0_domain_data

    EINT0 per-domain data

.. _`s3c64xx_eint0_domain_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_eint0_domain_data {
        struct samsung_pin_bank *bank;
        u8 eints[];
    }

.. _`s3c64xx_eint0_domain_data.members`:

Members
-------

bank
    pin bank related to the domain

eints
    EINT0 interrupts related to the domain

.. _`s3c64xx_eint_gpio_data`:

struct s3c64xx_eint_gpio_data
=============================

.. c:type:: struct s3c64xx_eint_gpio_data

    GPIO EINT data

.. _`s3c64xx_eint_gpio_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c64xx_eint_gpio_data {
        struct samsung_pinctrl_drv_data *drvdata;
        struct irq_domain *domains[];
    }

.. _`s3c64xx_eint_gpio_data.members`:

Members
-------

drvdata
    pin controller driver data

domains
    array of domains related to EINT interrupt groups

.. _`s3c64xx_eint_gpio_init`:

s3c64xx_eint_gpio_init
======================

.. c:function:: int s3c64xx_eint_gpio_init(struct samsung_pinctrl_drv_data *d)

    setup handling of external gpio interrupts.

    :param struct samsung_pinctrl_drv_data \*d:
        driver data of samsung pinctrl driver.

.. _`s3c64xx_eint_eint0_init`:

s3c64xx_eint_eint0_init
=======================

.. c:function:: int s3c64xx_eint_eint0_init(struct samsung_pinctrl_drv_data *d)

    setup handling of external wakeup interrupts.

    :param struct samsung_pinctrl_drv_data \*d:
        driver data of samsung pinctrl driver.

.. This file was automatic generated / don't edit.


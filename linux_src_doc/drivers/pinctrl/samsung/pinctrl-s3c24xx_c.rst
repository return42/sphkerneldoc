.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-s3c24xx.c

.. _`s3c24xx_eint_data`:

struct s3c24xx_eint_data
========================

.. c:type:: struct s3c24xx_eint_data

    EINT common data

.. _`s3c24xx_eint_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c24xx_eint_data {
        struct samsung_pinctrl_drv_data *drvdata;
        struct irq_domain *domains[NUM_EINT];
        int parents[NUM_EINT_IRQ];
    }

.. _`s3c24xx_eint_data.members`:

Members
-------

drvdata
    pin controller driver data

domains
    IRQ domains of particular EINT interrupts

parents
    mapped parent irqs in the main interrupt controller

.. _`s3c24xx_eint_domain_data`:

struct s3c24xx_eint_domain_data
===============================

.. c:type:: struct s3c24xx_eint_domain_data

    per irq-domain data

.. _`s3c24xx_eint_domain_data.definition`:

Definition
----------

.. code-block:: c

    struct s3c24xx_eint_domain_data {
        struct samsung_pin_bank *bank;
        struct s3c24xx_eint_data *eint_data;
        bool eint0_3_parent_only;
    }

.. _`s3c24xx_eint_domain_data.members`:

Members
-------

bank
    pin bank related to the domain

eint_data
    common data

eint0_3_parent_only
    *undescribed*

.. _`s3c24xx_eint_domain_data.eint0_3_parent_only`:

eint0_3_parent_only
-------------------

live eints 0-3 only in the main intc

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/misc/palmas-pwrbutton.c

.. _`palmas_pwron`:

struct palmas_pwron
===================

.. c:type:: struct palmas_pwron

    Palmas power on data

.. _`palmas_pwron.definition`:

Definition
----------

.. code-block:: c

    struct palmas_pwron {
        struct palmas *palmas;
        struct input_dev *input_dev;
        struct delayed_work input_work;
        int irq;
    }

.. _`palmas_pwron.members`:

Members
-------

palmas
    pointer to palmas device

input_dev
    pointer to input device

input_work
    work for detecting release of key

irq
    irq that we are hooked on to

.. _`palmas_pwron_config`:

struct palmas_pwron_config
==========================

.. c:type:: struct palmas_pwron_config

    configuration of palmas power on

.. _`palmas_pwron_config.definition`:

Definition
----------

.. code-block:: c

    struct palmas_pwron_config {
        u8 long_press_time_val;
        u8 pwron_debounce_val;
    }

.. _`palmas_pwron_config.members`:

Members
-------

long_press_time_val
    value for long press h/w shutdown event

pwron_debounce_val
    value for debounce of power button

.. _`palmas_power_button_work`:

palmas_power_button_work
========================

.. c:function:: void palmas_power_button_work(struct work_struct *work)

    Detects the button release event

    :param work:
        work item to detect button release
    :type work: struct work_struct \*

.. _`pwron_irq`:

pwron_irq
=========

.. c:function:: irqreturn_t pwron_irq(int irq, void *palmas_pwron)

    button press isr

    :param irq:
        irq
    :type irq: int

    :param palmas_pwron:
        pwron struct
    :type palmas_pwron: void \*

.. _`pwron_irq.return`:

Return
------

IRQ_HANDLED

.. _`palmas_pwron_params_ofinit`:

palmas_pwron_params_ofinit
==========================

.. c:function:: void palmas_pwron_params_ofinit(struct device *dev, struct palmas_pwron_config *config)

    device tree parameter parser

    :param dev:
        palmas button device
    :type dev: struct device \*

    :param config:
        configuration params that this fills up
    :type config: struct palmas_pwron_config \*

.. _`palmas_pwron_probe`:

palmas_pwron_probe
==================

.. c:function:: int palmas_pwron_probe(struct platform_device *pdev)

    probe

    :param pdev:
        platform device for the button
    :type pdev: struct platform_device \*

.. _`palmas_pwron_probe.return`:

Return
------

0 for successful probe else appropriate error

.. _`palmas_pwron_remove`:

palmas_pwron_remove
===================

.. c:function:: int palmas_pwron_remove(struct platform_device *pdev)

    Cleanup on removal

    :param pdev:
        platform device for the button
    :type pdev: struct platform_device \*

.. _`palmas_pwron_remove.return`:

Return
------

0

.. _`palmas_pwron_suspend`:

palmas_pwron_suspend
====================

.. c:function:: int __maybe_unused palmas_pwron_suspend(struct device *dev)

    suspend handler

    :param dev:
        power button device
    :type dev: struct device \*

.. _`palmas_pwron_suspend.description`:

Description
-----------

Cancel all pending work items for the power button, setup irq for wakeup

.. _`palmas_pwron_suspend.return`:

Return
------

0

.. _`palmas_pwron_resume`:

palmas_pwron_resume
===================

.. c:function:: int __maybe_unused palmas_pwron_resume(struct device *dev)

    resume handler

    :param dev:
        power button device
    :type dev: struct device \*

.. _`palmas_pwron_resume.description`:

Description
-----------

Just disable the wakeup capability of irq here.

.. _`palmas_pwron_resume.return`:

Return
------

0

.. This file was automatic generated / don't edit.


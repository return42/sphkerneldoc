.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/pm.c

.. _`suspend_device_irqs`:

suspend_device_irqs
===================

.. c:function:: void suspend_device_irqs( void)

    disable all currently enabled interrupt lines

    :param  void:
        no arguments

.. _`suspend_device_irqs.description`:

Description
-----------

During system-wide suspend or hibernation device drivers need to be
prevented from receiving interrupts and this function is provided
for this purpose.

So we disable all interrupts and mark them IRQS_SUSPENDED except
for those which are unused, those which are marked as not
suspendable via an interrupt request with the flag IRQF_NO_SUSPEND
set and those which are marked as active wakeup sources.

The active wakeup sources are handled by the flow handler entry
code which checks for the IRQD_WAKEUP_ARMED flag, suspends the
interrupt and notifies the pm core about the wakeup.

.. _`irq_pm_syscore_resume`:

irq_pm_syscore_resume
=====================

.. c:function:: void irq_pm_syscore_resume( void)

    enable interrupt lines early

    :param  void:
        no arguments

.. _`irq_pm_syscore_resume.description`:

Description
-----------

Enable all interrupt lines with \ ``IRQF_EARLY_RESUME``\  set.

.. _`resume_device_irqs`:

resume_device_irqs
==================

.. c:function:: void resume_device_irqs( void)

    enable interrupt lines disabled by \ :c:func:`suspend_device_irqs`\ 

    :param  void:
        no arguments

.. _`resume_device_irqs.description`:

Description
-----------

Enable all non-\ ``IRQF_EARLY_RESUME``\  interrupt lines previously
disabled by \ :c:func:`suspend_device_irqs`\  that have the IRQS_SUSPENDED flag
set as well as those with \ ``IRQF_FORCE_RESUME``\ .

.. This file was automatic generated / don't edit.


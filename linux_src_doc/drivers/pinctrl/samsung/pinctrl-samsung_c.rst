.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-samsung.c

.. _`samsung_pinctrl_suspend`:

samsung_pinctrl_suspend
=======================

.. c:function:: int __maybe_unused samsung_pinctrl_suspend(struct device *dev)

    save pinctrl state for suspend

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`samsung_pinctrl_suspend.description`:

Description
-----------

Save data for all banks handled by this device.

.. _`samsung_pinctrl_resume`:

samsung_pinctrl_resume
======================

.. c:function:: int __maybe_unused samsung_pinctrl_resume(struct device *dev)

    restore pinctrl state from suspend

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`samsung_pinctrl_resume.description`:

Description
-----------

Restore one of the banks that was saved during suspend.

We don't bother doing anything complicated to avoid glitching lines since
we're called before pad retention is turned off.

.. This file was automatic generated / don't edit.


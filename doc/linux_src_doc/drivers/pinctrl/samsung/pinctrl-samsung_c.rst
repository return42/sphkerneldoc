.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/samsung/pinctrl-samsung.c

.. _`samsung_pinctrl_suspend_dev`:

samsung_pinctrl_suspend_dev
===========================

.. c:function:: void samsung_pinctrl_suspend_dev(struct samsung_pinctrl_drv_data *drvdata)

    save pinctrl state for suspend for a device

    :param struct samsung_pinctrl_drv_data \*drvdata:
        *undescribed*

.. _`samsung_pinctrl_suspend_dev.description`:

Description
-----------

Save data for all banks handled by this device.

.. _`samsung_pinctrl_resume_dev`:

samsung_pinctrl_resume_dev
==========================

.. c:function:: void samsung_pinctrl_resume_dev(struct samsung_pinctrl_drv_data *drvdata)

    restore pinctrl state from suspend for a device

    :param struct samsung_pinctrl_drv_data \*drvdata:
        *undescribed*

.. _`samsung_pinctrl_resume_dev.description`:

Description
-----------

Restore one of the banks that was saved during suspend.

We don't bother doing anything complicated to avoid glitching lines since
we're called before pad retention is turned off.

.. _`samsung_pinctrl_suspend`:

samsung_pinctrl_suspend
=======================

.. c:function:: int samsung_pinctrl_suspend( void)

    save pinctrl state for suspend

    :param  void:
        no arguments

.. _`samsung_pinctrl_suspend.description`:

Description
-----------

Save data for all banks across all devices.

.. _`samsung_pinctrl_resume`:

samsung_pinctrl_resume
======================

.. c:function:: void samsung_pinctrl_resume( void)

    restore pinctrl state for suspend

    :param  void:
        no arguments

.. _`samsung_pinctrl_resume.description`:

Description
-----------

Restore data for all banks across all devices.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/generic_ops.c

.. _`pm_generic_runtime_suspend`:

pm_generic_runtime_suspend
==========================

.. c:function:: int pm_generic_runtime_suspend(struct device *dev)

    Generic runtime suspend callback for subsystems.

    :param struct device \*dev:
        Device to suspend.

.. _`pm_generic_runtime_suspend.description`:

Description
-----------

If PM operations are defined for the \ ``dev``\ 's driver and they include
->runtime_suspend(), execute it and return its error code.  Otherwise,
return 0.

.. _`pm_generic_runtime_resume`:

pm_generic_runtime_resume
=========================

.. c:function:: int pm_generic_runtime_resume(struct device *dev)

    Generic runtime resume callback for subsystems.

    :param struct device \*dev:
        Device to resume.

.. _`pm_generic_runtime_resume.description`:

Description
-----------

If PM operations are defined for the \ ``dev``\ 's driver and they include
->runtime_resume(), execute it and return its error code.  Otherwise,
return 0.

.. _`pm_generic_prepare`:

pm_generic_prepare
==================

.. c:function:: int pm_generic_prepare(struct device *dev)

    Generic routine preparing a device for power transition.

    :param struct device \*dev:
        Device to prepare.

.. _`pm_generic_prepare.description`:

Description
-----------

Prepare a device for a system-wide power transition.

.. _`pm_generic_suspend_noirq`:

pm_generic_suspend_noirq
========================

.. c:function:: int pm_generic_suspend_noirq(struct device *dev)

    Generic suspend_noirq callback for subsystems.

    :param struct device \*dev:
        Device to suspend.

.. _`pm_generic_suspend_late`:

pm_generic_suspend_late
=======================

.. c:function:: int pm_generic_suspend_late(struct device *dev)

    Generic suspend_late callback for subsystems.

    :param struct device \*dev:
        Device to suspend.

.. _`pm_generic_suspend`:

pm_generic_suspend
==================

.. c:function:: int pm_generic_suspend(struct device *dev)

    Generic suspend callback for subsystems.

    :param struct device \*dev:
        Device to suspend.

.. _`pm_generic_freeze_noirq`:

pm_generic_freeze_noirq
=======================

.. c:function:: int pm_generic_freeze_noirq(struct device *dev)

    Generic freeze_noirq callback for subsystems.

    :param struct device \*dev:
        Device to freeze.

.. _`pm_generic_freeze_late`:

pm_generic_freeze_late
======================

.. c:function:: int pm_generic_freeze_late(struct device *dev)

    Generic freeze_late callback for subsystems.

    :param struct device \*dev:
        Device to freeze.

.. _`pm_generic_freeze`:

pm_generic_freeze
=================

.. c:function:: int pm_generic_freeze(struct device *dev)

    Generic freeze callback for subsystems.

    :param struct device \*dev:
        Device to freeze.

.. _`pm_generic_poweroff_noirq`:

pm_generic_poweroff_noirq
=========================

.. c:function:: int pm_generic_poweroff_noirq(struct device *dev)

    Generic poweroff_noirq callback for subsystems.

    :param struct device \*dev:
        Device to handle.

.. _`pm_generic_poweroff_late`:

pm_generic_poweroff_late
========================

.. c:function:: int pm_generic_poweroff_late(struct device *dev)

    Generic poweroff_late callback for subsystems.

    :param struct device \*dev:
        Device to handle.

.. _`pm_generic_poweroff`:

pm_generic_poweroff
===================

.. c:function:: int pm_generic_poweroff(struct device *dev)

    Generic poweroff callback for subsystems.

    :param struct device \*dev:
        Device to handle.

.. _`pm_generic_thaw_noirq`:

pm_generic_thaw_noirq
=====================

.. c:function:: int pm_generic_thaw_noirq(struct device *dev)

    Generic thaw_noirq callback for subsystems.

    :param struct device \*dev:
        Device to thaw.

.. _`pm_generic_thaw_early`:

pm_generic_thaw_early
=====================

.. c:function:: int pm_generic_thaw_early(struct device *dev)

    Generic thaw_early callback for subsystems.

    :param struct device \*dev:
        Device to thaw.

.. _`pm_generic_thaw`:

pm_generic_thaw
===============

.. c:function:: int pm_generic_thaw(struct device *dev)

    Generic thaw callback for subsystems.

    :param struct device \*dev:
        Device to thaw.

.. _`pm_generic_resume_noirq`:

pm_generic_resume_noirq
=======================

.. c:function:: int pm_generic_resume_noirq(struct device *dev)

    Generic resume_noirq callback for subsystems.

    :param struct device \*dev:
        Device to resume.

.. _`pm_generic_resume_early`:

pm_generic_resume_early
=======================

.. c:function:: int pm_generic_resume_early(struct device *dev)

    Generic resume_early callback for subsystems.

    :param struct device \*dev:
        Device to resume.

.. _`pm_generic_resume`:

pm_generic_resume
=================

.. c:function:: int pm_generic_resume(struct device *dev)

    Generic resume callback for subsystems.

    :param struct device \*dev:
        Device to resume.

.. _`pm_generic_restore_noirq`:

pm_generic_restore_noirq
========================

.. c:function:: int pm_generic_restore_noirq(struct device *dev)

    Generic restore_noirq callback for subsystems.

    :param struct device \*dev:
        Device to restore.

.. _`pm_generic_restore_early`:

pm_generic_restore_early
========================

.. c:function:: int pm_generic_restore_early(struct device *dev)

    Generic restore_early callback for subsystems.

    :param struct device \*dev:
        Device to resume.

.. _`pm_generic_restore`:

pm_generic_restore
==================

.. c:function:: int pm_generic_restore(struct device *dev)

    Generic restore callback for subsystems.

    :param struct device \*dev:
        Device to restore.

.. _`pm_generic_complete`:

pm_generic_complete
===================

.. c:function:: void pm_generic_complete(struct device *dev)

    Generic routine completing a device power transition.

    :param struct device \*dev:
        Device to handle.

.. _`pm_generic_complete.description`:

Description
-----------

Complete a device power transition during a system-wide power transition.

.. _`pm_complete_with_resume_check`:

pm_complete_with_resume_check
=============================

.. c:function:: void pm_complete_with_resume_check(struct device *dev)

    Complete a device power transition.

    :param struct device \*dev:
        Device to handle.

.. _`pm_complete_with_resume_check.description`:

Description
-----------

Complete a device power transition during a system-wide power transition and
optionally schedule a runtime resume of the device if the system resume in
progress has been initated by the platform firmware and the device had its
power.direct_complete flag set.

.. This file was automatic generated / don't edit.


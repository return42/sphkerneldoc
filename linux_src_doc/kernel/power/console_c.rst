.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/console.c

.. _`pm_vt_switch_required`:

pm_vt_switch_required
=====================

.. c:function:: void pm_vt_switch_required(struct device *dev, bool required)

    indicate VT switch at suspend requirements

    :param dev:
        device
    :type dev: struct device \*

    :param required:
        if true, caller needs VT switch at suspend/resume time
    :type required: bool

.. _`pm_vt_switch_required.description`:

Description
-----------

The different console drivers may or may not require VT switches across
suspend/resume, depending on how they handle restoring video state and
what may be running.

Drivers can indicate support for switchless suspend/resume, which can
save time and flicker, by using this routine and passing 'false' as
the argument.  If any loaded driver needs VT switching, or the
no_console_suspend argument has been passed on the command line, VT
switches will occur.

.. _`pm_vt_switch_unregister`:

pm_vt_switch_unregister
=======================

.. c:function:: void pm_vt_switch_unregister(struct device *dev)

    stop tracking a device's VT switching needs

    :param dev:
        device
    :type dev: struct device \*

.. _`pm_vt_switch_unregister.description`:

Description
-----------

Remove \ ``dev``\  from the vt switch list.

.. This file was automatic generated / don't edit.


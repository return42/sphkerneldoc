.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/of_xilinx_wdt.c

.. _`xwdt_suspend`:

xwdt_suspend
============

.. c:function:: int __maybe_unused xwdt_suspend(struct device *dev)

    Suspend the device.

    :param struct device \*dev:
        handle to the device structure.

.. _`xwdt_suspend.return`:

Return
------

0 always.

.. _`xwdt_resume`:

xwdt_resume
===========

.. c:function:: int __maybe_unused xwdt_resume(struct device *dev)

    Resume the device.

    :param struct device \*dev:
        handle to the device structure.

.. _`xwdt_resume.return`:

Return
------

0 on success, errno otherwise.

.. This file was automatic generated / don't edit.


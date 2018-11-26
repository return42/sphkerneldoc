.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/uartlite.c

.. _`ulite_suspend`:

ulite_suspend
=============

.. c:function:: int __maybe_unused ulite_suspend(struct device *dev)

    Stop the device.

    :param dev:
        handle to the device structure.
    :type dev: struct device \*

.. _`ulite_suspend.return`:

Return
------

0 always.

.. _`ulite_resume`:

ulite_resume
============

.. c:function:: int __maybe_unused ulite_resume(struct device *dev)

    Resume the device.

    :param dev:
        handle to the device structure.
    :type dev: struct device \*

.. _`ulite_resume.return`:

Return
------

0 on success, errno otherwise.

.. This file was automatic generated / don't edit.


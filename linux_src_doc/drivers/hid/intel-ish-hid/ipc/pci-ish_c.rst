.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ipc/pci-ish.c

.. _`ish_event_tracer`:

ish_event_tracer
================

.. c:function:: void ish_event_tracer(struct ishtp_device *dev, char *format,  ...)

    Callback function to dump trace messages

    :param struct ishtp_device \*dev:
        ishtp device

    :param char \*format:
        printf style format

    :param ... :
        variable arguments

.. _`ish_event_tracer.description`:

Description
-----------

Callback to direct log messages to Linux trace buffers

.. _`ish_init`:

ish_init
========

.. c:function:: int ish_init(struct ishtp_device *dev)

    Init function

    :param struct ishtp_device \*dev:
        ishtp device

.. _`ish_init.description`:

Description
-----------

This function initialize wait queues for suspend/resume and call
calls hadware initialization function. This will initiate
startup sequence

.. _`ish_init.return`:

Return
------

0 for success or error code for failure

.. _`ish_probe`:

ish_probe
=========

.. c:function:: int ish_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    PCI driver probe callback

    :param struct pci_dev \*pdev:
        pci device

    :param const struct pci_device_id \*ent:
        pci device id

.. _`ish_probe.description`:

Description
-----------

Initialize PCI function, setup interrupt and call for ISH initialization

.. _`ish_probe.return`:

Return
------

0 for success or error code for failure

.. _`ish_remove`:

ish_remove
==========

.. c:function:: void ish_remove(struct pci_dev *pdev)

    PCI driver remove callback

    :param struct pci_dev \*pdev:
        pci device

.. _`ish_remove.description`:

Description
-----------

This function does cleanup of ISH on pci remove callback

.. _`ish_resume_handler`:

ish_resume_handler
==================

.. c:function:: void ish_resume_handler(struct work_struct *work)

    Work function to complete resume

    :param struct work_struct \*work:
        work struct

.. _`ish_resume_handler.description`:

Description
-----------

The resume work function to complete resume function asynchronously.
There are two types of platforms, one where ISH is not powered off,
in that case a simple resume message is enough, others we need
a reset sequence.

.. _`ish_suspend`:

ish_suspend
===========

.. c:function:: int ish_suspend(struct device *device)

    ISH suspend callback

    :param struct device \*device:
        device pointer

.. _`ish_suspend.description`:

Description
-----------

ISH suspend callback

.. _`ish_suspend.return`:

Return
------

0 to the pm core

.. _`ish_resume`:

ish_resume
==========

.. c:function:: int ish_resume(struct device *device)

    ISH resume callback

    :param struct device \*device:
        device pointer

.. _`ish_resume.description`:

Description
-----------

ISH resume callback

.. _`ish_resume.return`:

Return
------

0 to the pm core

.. This file was automatic generated / don't edit.

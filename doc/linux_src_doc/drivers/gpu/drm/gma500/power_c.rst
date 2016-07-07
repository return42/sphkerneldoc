.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/power.c

.. _`gma_power_init`:

gma_power_init
==============

.. c:function:: void gma_power_init(struct drm_device *dev)

    initialise power manager

    :param struct drm_device \*dev:
        our device

.. _`gma_power_init.description`:

Description
-----------

Set up for power management tracking of our hardware.

.. _`gma_power_uninit`:

gma_power_uninit
================

.. c:function:: void gma_power_uninit(struct drm_device *dev)

    end power manager

    :param struct drm_device \*dev:
        device to end for

.. _`gma_power_uninit.description`:

Description
-----------

Undo the effects of gma_power_init

.. _`gma_suspend_display`:

gma_suspend_display
===================

.. c:function:: void gma_suspend_display(struct drm_device *dev)

    suspend the display logic

    :param struct drm_device \*dev:
        our DRM device

.. _`gma_suspend_display.description`:

Description
-----------

Suspend the display logic of the graphics interface

.. _`gma_resume_display`:

gma_resume_display
==================

.. c:function:: void gma_resume_display(struct pci_dev *pdev)

    resume display side logic

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`gma_resume_display.description`:

Description
-----------

Resume the display hardware restoring state and enabling
as necessary.

.. _`gma_suspend_pci`:

gma_suspend_pci
===============

.. c:function:: void gma_suspend_pci(struct pci_dev *pdev)

    suspend PCI side

    :param struct pci_dev \*pdev:
        PCI device

.. _`gma_suspend_pci.description`:

Description
-----------

Perform the suspend processing on our PCI device state

.. _`gma_resume_pci`:

gma_resume_pci
==============

.. c:function:: bool gma_resume_pci(struct pci_dev *pdev)

    resume helper

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`gma_resume_pci.description`:

Description
-----------

Perform the resume processing on our PCI device state - rewrite
register state and re-enable the PCI device

.. _`gma_power_suspend`:

gma_power_suspend
=================

.. c:function:: int gma_power_suspend(struct device *_dev)

    bus callback for suspend

    :param struct device \*_dev:
        *undescribed*

.. _`gma_power_suspend.description`:

Description
-----------

Called back by the PCI layer during a suspend of the system. We
perform the necessary shut down steps and save enough state that
we can undo this when resume is called.

.. _`gma_power_resume`:

gma_power_resume
================

.. c:function:: int gma_power_resume(struct device *_dev)

    resume power

    :param struct device \*_dev:
        *undescribed*

.. _`gma_power_resume.description`:

Description
-----------

Resume the PCI side of the graphics and then the displays

.. _`gma_power_is_on`:

gma_power_is_on
===============

.. c:function:: bool gma_power_is_on(struct drm_device *dev)

    returne true if power is on

    :param struct drm_device \*dev:
        our DRM device

.. _`gma_power_is_on.description`:

Description
-----------

Returns true if the display island power is on at this moment

.. _`gma_power_begin`:

gma_power_begin
===============

.. c:function:: bool gma_power_begin(struct drm_device *dev, bool force_on)

    begin requiring power

    :param struct drm_device \*dev:
        our DRM device

    :param bool force_on:
        true to force power on

.. _`gma_power_begin.description`:

Description
-----------

Begin an action that requires the display power island is enabled.
We refcount the islands.

.. _`gma_power_end`:

gma_power_end
=============

.. c:function:: void gma_power_end(struct drm_device *dev)

    end use of power

    :param struct drm_device \*dev:
        Our DRM device

.. _`gma_power_end.description`:

Description
-----------

Indicate that one of our \ :c:func:`gma_power_begin`\  requested periods when
the diplay island power is needed has completed.

.. This file was automatic generated / don't edit.


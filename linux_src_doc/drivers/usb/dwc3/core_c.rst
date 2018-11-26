.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/core.c

.. _`dwc3_default_autosuspend_delay`:

DWC3_DEFAULT_AUTOSUSPEND_DELAY
==============================

.. c:function::  DWC3_DEFAULT_AUTOSUSPEND_DELAY()

    DesignWare USB3 DRD Controller Core file

.. _`dwc3_default_autosuspend_delay.description`:

Description
-----------

Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com

Authors: Felipe Balbi <balbi@ti.com>,
         Sebastian Andrzej Siewior <bigeasy@linutronix.de>

.. _`dwc3_get_dr_mode`:

dwc3_get_dr_mode
================

.. c:function:: int dwc3_get_dr_mode(struct dwc3 *dwc)

    Validates and sets dr_mode

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_core_soft_reset`:

dwc3_core_soft_reset
====================

.. c:function:: int dwc3_core_soft_reset(struct dwc3 *dwc)

    Issues core soft reset and PHY reset

    :param dwc:
        pointer to our context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_free_one_event_buffer`:

dwc3_free_one_event_buffer
==========================

.. c:function:: void dwc3_free_one_event_buffer(struct dwc3 *dwc, struct dwc3_event_buffer *evt)

    Frees one event buffer

    :param dwc:
        Pointer to our controller context structure
    :type dwc: struct dwc3 \*

    :param evt:
        Pointer to event buffer to be freed
    :type evt: struct dwc3_event_buffer \*

.. _`dwc3_alloc_one_event_buffer`:

dwc3_alloc_one_event_buffer
===========================

.. c:function:: struct dwc3_event_buffer *dwc3_alloc_one_event_buffer(struct dwc3 *dwc, unsigned length)

    Allocates one event buffer structure

    :param dwc:
        Pointer to our controller context structure
    :type dwc: struct dwc3 \*

    :param length:
        size of the event buffer
    :type length: unsigned

.. _`dwc3_alloc_one_event_buffer.description`:

Description
-----------

Returns a pointer to the allocated event buffer structure on success
otherwise ERR_PTR(errno).

.. _`dwc3_free_event_buffers`:

dwc3_free_event_buffers
=======================

.. c:function:: void dwc3_free_event_buffers(struct dwc3 *dwc)

    frees all allocated event buffers

    :param dwc:
        Pointer to our controller context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_alloc_event_buffers`:

dwc3_alloc_event_buffers
========================

.. c:function:: int dwc3_alloc_event_buffers(struct dwc3 *dwc, unsigned length)

    Allocates \ ``num``\  event buffers of size \ ``length``\ 

    :param dwc:
        pointer to our controller context structure
    :type dwc: struct dwc3 \*

    :param length:
        size of event buffer
    :type length: unsigned

.. _`dwc3_alloc_event_buffers.description`:

Description
-----------

Returns 0 on success otherwise negative errno. In the error case, dwc
may contain some buffers allocated but not all which were requested.

.. _`dwc3_event_buffers_setup`:

dwc3_event_buffers_setup
========================

.. c:function:: int dwc3_event_buffers_setup(struct dwc3 *dwc)

    setup our allocated event buffers

    :param dwc:
        pointer to our controller context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_event_buffers_setup.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. _`dwc3_phy_setup`:

dwc3_phy_setup
==============

.. c:function:: int dwc3_phy_setup(struct dwc3 *dwc)

    Configure USB PHY Interface of DWC3 Core

    :param dwc:
        Pointer to our controller context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_phy_setup.description`:

Description
-----------

Returns 0 on success. The USB PHY interfaces are configured but not
initialized. The PHY interfaces and the PHYs get initialized together with
the core in dwc3_core_init.

.. _`dwc3_core_init`:

dwc3_core_init
==============

.. c:function:: int dwc3_core_init(struct dwc3 *dwc)

    Low-level initialization of DWC3 Core

    :param dwc:
        Pointer to our controller context structure
    :type dwc: struct dwc3 \*

.. _`dwc3_core_init.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. This file was automatic generated / don't edit.


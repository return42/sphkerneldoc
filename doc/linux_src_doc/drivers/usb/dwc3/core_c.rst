.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/core.c

.. _`dwc3_set_mode`:

dwc3_set_mode
=============

.. c:function:: void dwc3_set_mode(struct dwc3 *dwc, u32 mode)

    DesignWare USB3 DRD Controller Core file

    :param struct dwc3 \*dwc:
        *undescribed*

    :param u32 mode:
        *undescribed*

.. _`dwc3_set_mode.description`:

Description
-----------

Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com

.. _`dwc3_set_mode.authors`:

Authors
-------

Felipe Balbi <balbi\ ``ti``\ .com>,
Sebastian Andrzej Siewior <bigeasy\ ``linutronix``\ .de>

.. _`dwc3_set_mode.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _`dwc3_core_soft_reset`:

dwc3_core_soft_reset
====================

.. c:function:: int dwc3_core_soft_reset(struct dwc3 *dwc)

    Issues core soft reset and PHY reset

    :param struct dwc3 \*dwc:
        pointer to our context structure

.. _`dwc3_soft_reset`:

dwc3_soft_reset
===============

.. c:function:: int dwc3_soft_reset(struct dwc3 *dwc)

    Issue soft reset

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

.. _`dwc3_free_one_event_buffer`:

dwc3_free_one_event_buffer
==========================

.. c:function:: void dwc3_free_one_event_buffer(struct dwc3 *dwc, struct dwc3_event_buffer *evt)

    Frees one event buffer

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

    :param struct dwc3_event_buffer \*evt:
        Pointer to event buffer to be freed

.. _`dwc3_alloc_one_event_buffer`:

dwc3_alloc_one_event_buffer
===========================

.. c:function:: struct dwc3_event_buffer *dwc3_alloc_one_event_buffer(struct dwc3 *dwc, unsigned length)

    Allocates one event buffer structure

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

    :param unsigned length:
        size of the event buffer

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

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

.. _`dwc3_alloc_event_buffers`:

dwc3_alloc_event_buffers
========================

.. c:function:: int dwc3_alloc_event_buffers(struct dwc3 *dwc, unsigned length)

    Allocates \ ``num``\  event buffers of size \ ``length``\ 

    :param struct dwc3 \*dwc:
        pointer to our controller context structure

    :param unsigned length:
        size of event buffer

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

    :param struct dwc3 \*dwc:
        pointer to our controller context structure

.. _`dwc3_event_buffers_setup.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. _`dwc3_phy_setup`:

dwc3_phy_setup
==============

.. c:function:: int dwc3_phy_setup(struct dwc3 *dwc)

    Configure USB PHY Interface of DWC3 Core

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

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

    :param struct dwc3 \*dwc:
        Pointer to our controller context structure

.. _`dwc3_core_init.description`:

Description
-----------

Returns 0 on success otherwise negative errno.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

=======
debug.h
=======


.. _`__dwc3_debug_h`:

__DWC3_DEBUG_H
==============

.. c:function:: __DWC3_DEBUG_H ()

    DesignWare USB3 DRD Controller Debug Header



.. _`__dwc3_debug_h.description`:

Description
-----------


Copyright (C) 2010-2011 Texas Instruments Incorporated - http://www.ti.com



.. _`__dwc3_debug_h.authors`:

Authors
-------

Felipe Balbi <balbi\ ``ti``\ .com>,
Sebastian Andrzej Siewior <bigeasy\ ``linutronix``\ .de>



.. _`__dwc3_debug_h.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.



.. _`dwc3_gadget_ep_cmd_string`:

dwc3_gadget_ep_cmd_string
=========================

.. c:function:: const char *dwc3_gadget_ep_cmd_string (u8 cmd)

    returns endpoint command string

    :param u8 cmd:
        command code



.. _`dwc3_gadget_generic_cmd_string`:

dwc3_gadget_generic_cmd_string
==============================

.. c:function:: const char *dwc3_gadget_generic_cmd_string (u8 cmd)

    returns generic command string

    :param u8 cmd:
        command code



.. _`dwc3_gadget_link_string`:

dwc3_gadget_link_string
=======================

.. c:function:: const char *dwc3_gadget_link_string (enum dwc3_link_state link_state)

    returns link name

    :param enum dwc3_link_state link_state:
        link state code



.. _`dwc3_gadget_event_string`:

dwc3_gadget_event_string
========================

.. c:function:: const char *dwc3_gadget_event_string (u8 event)

    returns event name

    :param u8 event:
        the event code



.. _`dwc3_ep_event_string`:

dwc3_ep_event_string
====================

.. c:function:: const char *dwc3_ep_event_string (u8 event)

    returns event name

    :param u8 event:
        then event code



.. _`dwc3_gadget_event_type_string`:

dwc3_gadget_event_type_string
=============================

.. c:function:: const char *dwc3_gadget_event_type_string (u8 event)

    return event name

    :param u8 event:
        the event code


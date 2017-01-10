.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/debug.h

.. _`dwc3_gadget_ep_cmd_string`:

dwc3_gadget_ep_cmd_string
=========================

.. c:function:: const char *dwc3_gadget_ep_cmd_string(u8 cmd)

    returns endpoint command string

    :param u8 cmd:
        command code

.. _`dwc3_gadget_generic_cmd_string`:

dwc3_gadget_generic_cmd_string
==============================

.. c:function:: const char *dwc3_gadget_generic_cmd_string(u8 cmd)

    returns generic command string

    :param u8 cmd:
        command code

.. _`dwc3_gadget_link_string`:

dwc3_gadget_link_string
=======================

.. c:function:: const char *dwc3_gadget_link_string(enum dwc3_link_state link_state)

    returns link name

    :param enum dwc3_link_state link_state:
        link state code

.. _`dwc3_gadget_event_string`:

dwc3_gadget_event_string
========================

.. c:function:: const char *dwc3_gadget_event_string(const struct dwc3_event_devt *event)

    returns event name

    :param const struct dwc3_event_devt \*event:
        the event code

.. _`dwc3_ep_event_string`:

dwc3_ep_event_string
====================

.. c:function:: const char *dwc3_ep_event_string(const struct dwc3_event_depevt *event, u32 ep0state)

    returns event name

    :param const struct dwc3_event_depevt \*event:
        then event code

    :param u32 ep0state:
        *undescribed*

.. _`dwc3_gadget_event_type_string`:

dwc3_gadget_event_type_string
=============================

.. c:function:: const char *dwc3_gadget_event_type_string(u8 event)

    return event name

    :param u8 event:
        the event code

.. This file was automatic generated / don't edit.


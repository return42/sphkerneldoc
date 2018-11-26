.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc3/debug.h

.. _`dwc3_gadget_ep_cmd_string`:

dwc3_gadget_ep_cmd_string
=========================

.. c:function:: const char *dwc3_gadget_ep_cmd_string(u8 cmd)

    returns endpoint command string

    :param cmd:
        command code
    :type cmd: u8

.. _`dwc3_gadget_generic_cmd_string`:

dwc3_gadget_generic_cmd_string
==============================

.. c:function:: const char *dwc3_gadget_generic_cmd_string(u8 cmd)

    returns generic command string

    :param cmd:
        command code
    :type cmd: u8

.. _`dwc3_gadget_link_string`:

dwc3_gadget_link_string
=======================

.. c:function:: const char *dwc3_gadget_link_string(enum dwc3_link_state link_state)

    returns link name

    :param link_state:
        link state code
    :type link_state: enum dwc3_link_state

.. _`dwc3_trb_type_string`:

dwc3_trb_type_string
====================

.. c:function:: const char *dwc3_trb_type_string(unsigned int type)

    returns TRB type as a string

    :param type:
        the type of the TRB
    :type type: unsigned int

.. _`dwc3_gadget_event_string`:

dwc3_gadget_event_string
========================

.. c:function:: const char *dwc3_gadget_event_string(char *str, const struct dwc3_event_devt *event)

    returns event name

    :param str:
        *undescribed*
    :type str: char \*

    :param event:
        the event code
    :type event: const struct dwc3_event_devt \*

.. _`dwc3_decode_ctrl`:

dwc3_decode_ctrl
================

.. c:function:: const char *dwc3_decode_ctrl(char *str, __u8 bRequestType, __u8 bRequest, __u16 wValue, __u16 wIndex, __u16 wLength)

    returns a string represetion of ctrl request

    :param str:
        *undescribed*
    :type str: char \*

    :param bRequestType:
        *undescribed*
    :type bRequestType: __u8

    :param bRequest:
        *undescribed*
    :type bRequest: __u8

    :param wValue:
        *undescribed*
    :type wValue: __u16

    :param wIndex:
        *undescribed*
    :type wIndex: __u16

    :param wLength:
        *undescribed*
    :type wLength: __u16

.. _`dwc3_ep_event_string`:

dwc3_ep_event_string
====================

.. c:function:: const char *dwc3_ep_event_string(char *str, const struct dwc3_event_depevt *event, u32 ep0state)

    returns event name

    :param str:
        *undescribed*
    :type str: char \*

    :param event:
        then event code
    :type event: const struct dwc3_event_depevt \*

    :param ep0state:
        *undescribed*
    :type ep0state: u32

.. _`dwc3_gadget_event_type_string`:

dwc3_gadget_event_type_string
=============================

.. c:function:: const char *dwc3_gadget_event_type_string(u8 event)

    return event name

    :param event:
        the event code
    :type event: u8

.. This file was automatic generated / don't edit.


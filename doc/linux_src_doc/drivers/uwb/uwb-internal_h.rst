.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/uwb-internal.h

.. _`uwb_event_type`:

enum uwb_event_type
===================

.. c:type:: enum uwb_event_type

    types of UWB management daemon events

.. _`uwb_event_type.definition`:

Definition
----------

.. code-block:: c

    enum uwb_event_type {
        UWB_EVT_TYPE_NOTIF,
        UWB_EVT_TYPE_MSG
    };

.. _`uwb_event_type.constants`:

Constants
---------

UWB_EVT_TYPE_NOTIF
    *undescribed*

UWB_EVT_TYPE_MSG
    *undescribed*

.. _`uwb_event_type.description`:

Description
-----------

The UWB management daemon (uwbd) can receive two types of events:
UWB_EVT_TYPE_NOTIF - notification from the radio controller.
UWB_EVT_TYPE_MSG   - a simple message.

.. _`uwb_event_notif`:

struct uwb_event_notif
======================

.. c:type:: struct uwb_event_notif

    an event for a radio controller notification

.. _`uwb_event_notif.definition`:

Definition
----------

.. code-block:: c

    struct uwb_event_notif {
        size_t size;
        struct uwb_rceb *rceb;
    }

.. _`uwb_event_notif.members`:

Members
-------

size
    Size of the buffer (ie: Guaranteed to contain at least
    a full 'struct uwb_rceb')

rceb
    Pointer to a \ :c:func:`kmalloced`\  event payload

.. _`uwb_event_message`:

enum uwb_event_message
======================

.. c:type:: enum uwb_event_message

    an event for a message for asynchronous processing

.. _`uwb_event_message.definition`:

Definition
----------

.. code-block:: c

    enum uwb_event_message {
        UWB_EVT_MSG_RESET
    };

.. _`uwb_event_message.constants`:

Constants
---------

UWB_EVT_MSG_RESET
    *undescribed*

.. _`uwb_event_message.description`:

Description
-----------

UWB_EVT_MSG_RESET - reset the radio controller and all PAL hardware.

.. This file was automatic generated / don't edit.


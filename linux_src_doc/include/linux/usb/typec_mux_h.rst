.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/typec_mux.h

.. _`typec_switch`:

struct typec_switch
===================

.. c:type:: struct typec_switch

    USB Type-C cable orientation switch

.. _`typec_switch.definition`:

Definition
----------

.. code-block:: c

    struct typec_switch {
        struct device *dev;
        struct list_head entry;
        int (*set)(struct typec_switch *sw, enum typec_orientation orientation);
    }

.. _`typec_switch.members`:

Members
-------

dev
    Switch device

entry
    List entry

set
    Callback to the driver for setting the orientation

.. _`typec_switch.description`:

Description
-----------

USB Type-C pin flipper switch routing the correct data pairs from the
connector to the USB controller depending on the orientation of the cable
plug.

.. _`typec_mux`:

struct typec_mux
================

.. c:type:: struct typec_mux

    USB Type-C connector pin mux

.. _`typec_mux.definition`:

Definition
----------

.. code-block:: c

    struct typec_mux {
        struct device *dev;
        struct list_head entry;
        int (*set)(struct typec_mux *mux, int state);
    }

.. _`typec_mux.members`:

Members
-------

dev
    Mux device

entry
    List entry

set
    Callback to the driver for setting the state of the mux

.. _`typec_mux.description`:

Description
-----------

Pin Multiplexer/DeMultiplexer switch routing the USB Type-C connector pins to
different components depending on the requested mode of operation. Used with
Accessory/Alternate modes.

.. This file was automatic generated / don't edit.


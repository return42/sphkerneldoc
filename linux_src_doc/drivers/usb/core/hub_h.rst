.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/core/hub.h

.. _`usb_port`:

struct usb_port
===============

.. c:type:: struct usb_port

    kernel's representation of a usb port

.. _`usb_port.definition`:

Definition
----------

.. code-block:: c

    struct usb_port {
        struct usb_device *child;
        struct device dev;
        struct usb_dev_state *port_owner;
        struct usb_port *peer;
        struct dev_pm_qos_request *req;
        enum usb_port_connect_type connect_type;
        usb_port_location_t location;
        struct mutex status_lock;
        u32 over_current_count;
        u8 portnum;
        u32 quirks;
        unsigned int is_superspeed:1;
        unsigned int usb3_lpm_u1_permit:1;
        unsigned int usb3_lpm_u2_permit:1;
    }

.. _`usb_port.members`:

Members
-------

child
    usb device attached to the port

dev
    generic device interface

port_owner
    port's owner

peer
    related usb2 and usb3 ports (share the same connector)

req
    default pm qos request for hubs without port power control

connect_type
    port's connect type

location
    opaque representation of platform connector location

status_lock
    synchronize \ :c:func:`port_event`\  vs usb_port_{suspend\|resume}

over_current_count
    *undescribed*

portnum
    port index num based one
    \ ``is_superspeed``\  cache super-speed status

quirks
    *undescribed*

is_superspeed
    *undescribed*

usb3_lpm_u1_permit
    whether USB3 U1 LPM is permitted.

usb3_lpm_u2_permit
    whether USB3 U2 LPM is permitted.

.. This file was automatic generated / don't edit.


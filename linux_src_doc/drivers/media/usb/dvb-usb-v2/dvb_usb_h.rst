.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/usb/dvb-usb-v2/dvb_usb.h

.. _`dvb_usb_driver_info`:

struct dvb_usb_driver_info
==========================

.. c:type:: struct dvb_usb_driver_info

    dvb usb routines

.. _`dvb_usb_driver_info.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_driver_info {
        const char *name;
        const char *rc_map;
        const struct dvb_usb_device_properties *props;
    }

.. _`dvb_usb_driver_info.members`:

Members
-------

name
    device name

rc_map
    name of rc codes table

props
    structure containing all device properties

.. _`dvb_usb_rc`:

struct dvb_usb_rc
=================

.. c:type:: struct dvb_usb_rc


.. _`dvb_usb_rc.definition`:

Definition
----------

.. code-block:: c

    struct dvb_usb_rc {
        const char *map_name;
        u64 allowed_protos;
        int (*change_protocol)(struct rc_dev *dev, u64 *rc_proto);
        int (*query) (struct dvb_usb_device *d);
        unsigned int interval;
        enum rc_driver_type driver_type;
        bool bulk_mode;
    }

.. _`dvb_usb_rc.members`:

Members
-------

map_name
    name of rc codes table

allowed_protos
    protocol(s) supported by the driver

change_protocol
    callback to change protocol

query
    called to query an event from the device

interval
    time in ms between two queries

driver_type
    used to point if a device supports raw mode

bulk_mode
    device supports bulk mode for rc (disable polling mode)

.. _`max_no_of_fe_per_adap`:

MAX_NO_OF_FE_PER_ADAP
=====================

.. c:function::  MAX_NO_OF_FE_PER_ADAP()

.. _`max_no_urbs_for_data_stream`:

MAX_NO_URBS_FOR_DATA_STREAM
===========================

.. c:function::  MAX_NO_URBS_FOR_DATA_STREAM()

.. This file was automatic generated / don't edit.


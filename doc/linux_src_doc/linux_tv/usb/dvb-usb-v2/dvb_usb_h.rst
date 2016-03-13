.. -*- coding: utf-8; mode: rst -*-

=========
dvb_usb.h
=========



.. _xref_struct_dvb_usb_driver_info:

struct dvb_usb_driver_info
==========================

.. c:type:: struct dvb_usb_driver_info

    



Definition
----------

.. code-block:: c

  struct dvb_usb_driver_info {
    const char * name;
    const char * rc_map;
    const struct dvb_usb_device_properties * props;
  };



Members
-------

:``const char * name``:
    device name

:``const char * rc_map``:
    name of rc codes table

:``const struct dvb_usb_device_properties * props``:
    structure containing all device properties




Description
-----------

dvb usb routines




.. _xref_struct_dvb_usb_rc:

struct dvb_usb_rc
=================

.. c:type:: struct dvb_usb_rc

    



Definition
----------

.. code-block:: c

  struct dvb_usb_rc {
    const char * map_name;
    u64 allowed_protos;
    int (* change_protocol) (struct rc_dev *dev, u64 *rc_type);
    int (* query) (struct dvb_usb_device *d);
    unsigned int interval;
    enum rc_driver_type driver_type;
    bool bulk_mode;
  };



Members
-------

:``const char * map_name``:
    name of rc codes table

:``u64 allowed_protos``:
    protocol(s) supported by the driver

:``int (*)(struct rc_dev *dev, u64 *rc_type) change_protocol``:
    callback to change protocol

:``int (*) (struct dvb_usb_device *d) query``:
    called to query an event from the device

:``unsigned int interval``:
    time in ms between two queries

:``enum rc_driver_type driver_type``:
    used to point if a device supports raw mode

:``bool bulk_mode``:
    device supports bulk mode for rc (disable polling mode)





.. _xref_MAX_NO_OF_FE_PER_ADAP:

MAX_NO_OF_FE_PER_ADAP
=====================

.. c:function:: MAX_NO_OF_FE_PER_ADAP ()

    




.. _xref_MAX_NO_URBS_FOR_DATA_STREAM:

MAX_NO_URBS_FOR_DATA_STREAM
===========================

.. c:function:: MAX_NO_URBS_FOR_DATA_STREAM ()

    



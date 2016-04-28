.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-ep:

=============
struct usb_ep
=============

*man struct usb_ep(9)*

*4.6.0-rc5*

device side representation of USB endpoint


Synopsis
========

.. code-block:: c

    struct usb_ep {
      void * driver_data;
      const char * name;
      const struct usb_ep_ops * ops;
      struct list_head ep_list;
      struct usb_ep_caps caps;
      unsigned maxpacket:16;
      unsigned maxpacket_limit:16;
      unsigned max_streams:16;
      unsigned mult:2;
      unsigned maxburst:5;
      u8 address;
      const struct usb_endpoint_descriptor * desc;
      const struct usb_ss_ep_comp_descriptor * comp_desc;
    };


Members
=======

driver_data
    for use by the gadget driver.

name
    identifier for the endpoint, such as “ep-a” or “ep9in-bulk”

ops
    Function pointers used to access hardware-specific operations.

ep_list
    the gadget's ep_list holds all of its endpoints

caps
    The structure describing types and directions supported by endoint.

maxpacket
    The maximum packet size used on this endpoint. The initial value can
    sometimes be reduced (hardware allowing), according to the endpoint
    descriptor used to configure the endpoint.

maxpacket_limit
    The maximum packet size value which can be handled by this endpoint.
    It's set once by UDC driver when endpoint is initialized, and should
    not be changed. Should not be confused with maxpacket.

max_streams
    The maximum number of streams supported by this EP (0 - 16, actual
    number is 2^n)

mult
    multiplier, 'mult' value for SS Isoc EPs

maxburst
    the maximum number of bursts supported by this EP (for usb3)

address
    used to identify the endpoint when finding descriptor that matches
    connection speed

desc
    endpoint descriptor. This pointer is set before the endpoint is
    enabled and remains valid until the endpoint is disabled.

comp_desc
    In case of SuperSpeed support, this is the endpoint companion
    descriptor that is used to configure the endpoint


Description
===========

the bus controller driver lists all the general purpose endpoints in
gadget->ep_list. the control endpoint (gadget->ep0) is not in that
list, and is accessed only in response to a driver ``setup`` callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

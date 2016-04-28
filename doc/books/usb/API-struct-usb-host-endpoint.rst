.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-host-endpoint:

========================
struct usb_host_endpoint
========================

*man struct usb_host_endpoint(9)*

*4.6.0-rc5*

host-side endpoint descriptor and queue


Synopsis
========

.. code-block:: c

    struct usb_host_endpoint {
      struct usb_endpoint_descriptor desc;
      struct usb_ss_ep_comp_descriptor ss_ep_comp;
      struct usb_ssp_isoc_ep_comp_descriptor ssp_isoc_ep_comp;
      struct list_head urb_list;
      void * hcpriv;
      struct ep_device * ep_dev;
      unsigned char * extra;
      int extralen;
      int enabled;
      int streams;
    };


Members
=======

desc
    descriptor for this endpoint, wMaxPacketSize in native byteorder

ss_ep_comp
    SuperSpeed companion descriptor for this endpoint

ssp_isoc_ep_comp
    SuperSpeedPlus isoc companion descriptor for this endpoint

urb_list
    urbs queued to this endpoint; maintained by usbcore

hcpriv
    for use by HCD; typically holds hardware dma queue head (QH) with
    one or more transfer descriptors (TDs) per urb

ep_dev
    ep_device for sysfs info

extra
    descriptors following this endpoint in the configuration

extralen
    how many bytes of “extra” are valid

enabled
    URBs may be submitted to this endpoint

streams
    number of USB-3 streams allocated on the endpoint


Description
===========

USB requests are always queued to a given endpoint, identified by a
descriptor within an active interface in a given USB configuration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

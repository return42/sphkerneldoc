
.. _API-struct-usb-composite-dev:

========================
struct usb_composite_dev
========================

*man struct usb_composite_dev(9)*

*4.6.0-rc1*

represents one composite usb gadget


Synopsis
========

.. code-block:: c

    struct usb_composite_dev {
      struct usb_gadget * gadget;
      struct usb_request * req;
      struct usb_request * os_desc_req;
      struct usb_configuration * config;
      u8 qw_sign[OS_STRING_QW_SIGN_LEN];
      u8 b_vendor_code;
      struct usb_configuration * os_desc_config;
      unsigned int use_os_string:1;
    };


Members
=======

gadget
    read-only, abstracts the gadget's usb peripheral controller

req
    used for control responses; buffer is pre-allocated

os_desc_req
    used for OS descriptors responses; buffer is pre-allocated

config
    the currently active configuration

qw_sign[OS_STRING_QW_SIGN_LEN]
    qwSignature part of the OS string

b_vendor_code
    bMS_VendorCode part of the OS string

os_desc_config
    the configuration to be used with OS descriptors

use_os_string
    false by default, interested gadgets set it


Description
===========

One of these devices is allocated and initialized before the associated device driver's ``bind`` is called.


OPEN ISSUE
==========

it appears that some WUSB devices will need to be built by combining a normal (wired) gadget with a wireless one. This revision of the gadget framework should probably try to make
sure doing that won't hurt too much.


One notion for how to handle Wireless USB devices involves
==========================================================

(a) a second gadget here, discovery mechanism TBD, but likely needing separate “register/unregister WUSB gadget” calls; (b) updates to usb_gadget to include flags “is it
wireless”, “is it wired”, plus (presumably in a wrapper structure) bandgroup and PHY info; (c) presumably a wireless_ep wrapping a usb_ep, and reporting wireless-specific
parameters like maxburst and maxsequence; (d) configurations that are specific to wireless links; (e) function drivers that understand wireless configs and will support wireless
for (additional) function instances; (f) a function to support association setup (like CBAF), not necessarily requiring a wireless adapter; (g) composite device setup that can
create one or more wireless configs, including appropriate association setup support; (h) more, TBD.

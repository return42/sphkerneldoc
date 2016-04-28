.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-device:

=================
struct usb_device
=================

*man struct usb_device(9)*

*4.6.0-rc5*

kernel's representation of a USB device


Synopsis
========

.. code-block:: c

    struct usb_device {
      int devnum;
      char devpath[16];
      u32 route;
      enum usb_device_state state;
      enum usb_device_speed speed;
      struct usb_tt * tt;
      int ttport;
      unsigned int toggle[2];
      struct usb_device * parent;
      struct usb_bus * bus;
      struct usb_host_endpoint ep0;
      struct device dev;
      struct usb_device_descriptor descriptor;
      struct usb_host_bos * bos;
      struct usb_host_config * config;
      struct usb_host_config * actconfig;
      struct usb_host_endpoint * ep_in[16];
      struct usb_host_endpoint * ep_out[16];
      char ** rawdescriptors;
      unsigned short bus_mA;
      u8 portnum;
      u8 level;
      unsigned can_submit:1;
      unsigned persist_enabled:1;
      unsigned have_langid:1;
      unsigned authorized:1;
      unsigned authenticated:1;
      unsigned wusb:1;
      unsigned lpm_capable:1;
      unsigned usb2_hw_lpm_capable:1;
      unsigned usb2_hw_lpm_besl_capable:1;
      unsigned usb2_hw_lpm_enabled:1;
      unsigned usb2_hw_lpm_allowed:1;
      unsigned usb3_lpm_u1_enabled:1;
      unsigned usb3_lpm_u2_enabled:1;
      int string_langid;
      char * product;
      char * manufacturer;
      char * serial;
      struct list_head filelist;
      int maxchild;
      u32 quirks;
      atomic_t urbnum;
      unsigned long active_duration;
    #ifdef CONFIG_PM
      unsigned long connect_time;
      unsigned do_remote_wakeup:1;
      unsigned reset_resume:1;
      unsigned port_is_suspended:1;
    #endif
      struct wusb_dev * wusb_dev;
      int slot_id;
      enum usb_device_removable removable;
      struct usb2_lpm_parameters l1_params;
      struct usb3_lpm_parameters u1_params;
      struct usb3_lpm_parameters u2_params;
      unsigned lpm_disable_count;
    };


Members
=======

devnum
    device number; address on a USB bus

devpath[16]
    device ID string for use in messages (e.g., /port/...)

route
    tree topology hex string for use with xHCI

state
    device state: configured, not attached, etc.

speed
    device speed: high/full/low (or error)

tt
    Transaction Translator info; used with low/full speed dev, highspeed
    hub

ttport
    device port on that tt hub

toggle[2]
    one bit for each endpoint, with ([0] = IN, [1] = OUT) endpoints

parent
    our hub, unless we're the root

bus
    bus we're part of

ep0
    endpoint 0 data (default control pipe)

dev
    generic device interface

descriptor
    USB device descriptor

bos
    USB device BOS descriptor set

config
    all of the device's configs

actconfig
    the active configuration

ep_in[16]
    array of IN endpoints

ep_out[16]
    array of OUT endpoints

rawdescriptors
    raw descriptors for each config

bus_mA
    Current available from the bus

portnum
    parent port number (origin 1)

level
    number of USB hub ancestors

can_submit
    URBs may be submitted

persist_enabled
    USB_PERSIST enabled for this device

have_langid
    whether string_langid is valid

authorized
    policy has said we can use it; (user space) policy determines if we
    authorize this device to be used or not. By default, wired USB
    devices are authorized. WUSB devices are not, until we authorize
    them from user space. FIXME -- complete doc

authenticated
    Crypto authentication passed

wusb
    device is Wireless USB

lpm_capable
    device supports LPM

usb2_hw_lpm_capable
    device can perform USB2 hardware LPM

usb2_hw_lpm_besl_capable
    device can perform USB2 hardware BESL LPM

usb2_hw_lpm_enabled
    USB2 hardware LPM is enabled

usb2_hw_lpm_allowed
    Userspace allows USB 2.0 LPM to be enabled

usb3_lpm_u1_enabled
    USB3 hardware U1 LPM enabled

usb3_lpm_u2_enabled
    USB3 hardware U2 LPM enabled

string_langid
    language ID for strings

product
    iProduct string, if present (static)

manufacturer
    iManufacturer string, if present (static)

serial
    iSerialNumber string, if present (static)

filelist
    usbfs files that are open to this device

maxchild
    number of ports if hub

quirks
    quirks of the whole device

urbnum
    number of URBs submitted for the whole device

active_duration
    total time device is not suspended

connect_time
    time device was first connected

do_remote_wakeup
    remote wakeup should be enabled

reset_resume
    needs reset instead of resume

port_is_suspended
    the upstream port is suspended (L2 or U3)

wusb_dev
    if this is a Wireless USB device, link to the WUSB specific data for
    the device.

slot_id
    Slot ID assigned by xHCI

removable
    Device can be physically removed from this port

l1_params
    best effor service latency for USB2 L1 LPM state, and L1 timeout.

u1_params
    exit latencies for USB3 U1 LPM state, and hub-initiated timeout.

u2_params
    exit latencies for USB3 U2 LPM state, and hub-initiated timeout.

lpm_disable_count
    Ref count used by ``usb_disable_lpm`` and ``usb_enable_lpm`` to keep
    track of the number of functions that require USB 3.0 Link Power
    Management to be disabled for this usb_device. This count should
    only be manipulated by those functions, with the bandwidth_mutex is
    held.


Notes
=====

Usbcore drivers should not set usbdev->state directly. Instead use
``usb_set_device_state``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

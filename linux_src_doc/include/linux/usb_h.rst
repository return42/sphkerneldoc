.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb.h

.. _`usb_host_endpoint`:

struct usb_host_endpoint
========================

.. c:type:: struct usb_host_endpoint

    host-side endpoint descriptor and queue

.. _`usb_host_endpoint.definition`:

Definition
----------

.. code-block:: c

    struct usb_host_endpoint {
        struct usb_endpoint_descriptor desc;
        struct usb_ss_ep_comp_descriptor ss_ep_comp;
        struct usb_ssp_isoc_ep_comp_descriptor ssp_isoc_ep_comp;
        struct list_head urb_list;
        void *hcpriv;
        struct ep_device *ep_dev;
        unsigned char *extra;
        int extralen;
        int enabled;
        int streams;
    }

.. _`usb_host_endpoint.members`:

Members
-------

desc
    descriptor for this endpoint, wMaxPacketSize in native byteorder

ss_ep_comp
    SuperSpeed companion descriptor for this endpoint

ssp_isoc_ep_comp
    SuperSpeedPlus isoc companion descriptor for this endpoint

urb_list
    urbs queued to this endpoint; maintained by usbcore

hcpriv
    for use by HCD; typically holds hardware dma queue head (QH)
    with one or more transfer descriptors (TDs) per urb

ep_dev
    ep_device for sysfs info

extra
    descriptors following this endpoint in the configuration

extralen
    how many bytes of "extra" are valid

enabled
    URBs may be submitted to this endpoint

streams
    number of USB-3 streams allocated on the endpoint

.. _`usb_host_endpoint.description`:

Description
-----------

USB requests are always queued to a given endpoint, identified by a
descriptor within an active interface in a given USB configuration.

.. _`usb_interface`:

struct usb_interface
====================

.. c:type:: struct usb_interface

    what usb device drivers talk to

.. _`usb_interface.definition`:

Definition
----------

.. code-block:: c

    struct usb_interface {
        struct usb_host_interface *altsetting;
        struct usb_host_interface *cur_altsetting;
        unsigned num_altsetting;
        struct usb_interface_assoc_descriptor *intf_assoc;
        int minor;
        enum usb_interface_condition condition;
        unsigned sysfs_files_created:1;
        unsigned ep_devs_created:1;
        unsigned unregistering:1;
        unsigned needs_remote_wakeup:1;
        unsigned needs_altsetting0:1;
        unsigned needs_binding:1;
        unsigned resetting_device:1;
        unsigned authorized:1;
        struct device dev;
        struct device *usb_dev;
        atomic_t pm_usage_cnt;
        struct work_struct reset_ws;
    }

.. _`usb_interface.members`:

Members
-------

altsetting
    array of interface structures, one for each alternate
    setting that may be selected.  Each one includes a set of
    endpoint configurations.  They will be in no particular order.

cur_altsetting
    the current altsetting.

num_altsetting
    number of altsettings defined.

intf_assoc
    interface association descriptor

minor
    the minor number assigned to this interface, if this
    interface is bound to a driver that uses the USB major number.
    If this interface does not use the USB major, this field should
    be unused.  The driver should set this value in the \ :c:func:`probe`\ 
    function of the driver, after it has been assigned a minor
    number from the USB core by calling \ :c:func:`usb_register_dev`\ .

condition
    binding state of the interface: not bound, binding
    (in \ :c:func:`probe`\ ), bound to a driver, or unbinding (in \ :c:func:`disconnect`\ )

sysfs_files_created
    sysfs attributes exist

ep_devs_created
    endpoint child pseudo-devices exist

unregistering
    flag set when the interface is being unregistered

needs_remote_wakeup
    flag set when the driver requires remote-wakeup
    capability during autosuspend.

needs_altsetting0
    flag set when a set-interface request for altsetting 0
    has been deferred.

needs_binding
    flag set when the driver should be re-probed or unbound
    following a reset or suspend operation it doesn't support.

resetting_device
    USB core reset the device, so use alt setting 0 as
    current; needs bandwidth alloc after reset.

authorized
    This allows to (de)authorize individual interfaces instead
    a whole device in contrast to the device authorization.

dev
    driver model's view of this device

usb_dev
    if an interface is bound to the USB major, this will point
    to the sysfs representation for that device.

pm_usage_cnt
    PM usage counter for this interface

reset_ws
    Used for scheduling resets from atomic context.

.. _`usb_interface.description`:

Description
-----------

USB device drivers attach to interfaces on a physical device.  Each
interface encapsulates a single high level function, such as feeding
an audio stream to a speaker or reporting a change in a volume control.
Many USB devices only have one interface.  The protocol used to talk to
an interface's endpoints can be defined in a usb "class" specification,
or by a product's vendor.  The (default) control endpoint is part of
every interface, but is never listed among the interface's descriptors.

The driver that is bound to the interface can use standard driver model
calls such as \ :c:func:`dev_get_drvdata`\  on the dev member of this structure.

Each interface may have alternate settings.  The initial configuration
of a device sets altsetting 0, but the device driver can change
that setting using \ :c:func:`usb_set_interface`\ .  Alternate settings are often
used to control the use of periodic endpoints, such as by having
different endpoints use different amounts of reserved USB bandwidth.
All standards-conformant USB devices that use isochronous endpoints
will use them in non-default settings.

The USB specification says that alternate setting numbers must run from
0 to one less than the total number of alternate settings.  But some
devices manage to mess this up, and the structures aren't necessarily
stored in numerical order anyhow.  Use \ :c:func:`usb_altnum_to_altsetting`\  to
look up an alternate setting in the altsetting array based on its number.

.. _`usb_interface_cache`:

struct usb_interface_cache
==========================

.. c:type:: struct usb_interface_cache

    long-term representation of a device interface

.. _`usb_interface_cache.definition`:

Definition
----------

.. code-block:: c

    struct usb_interface_cache {
        unsigned num_altsetting;
        struct kref ref;
        struct usb_host_interface altsetting[0];
    }

.. _`usb_interface_cache.members`:

Members
-------

num_altsetting
    number of altsettings defined.

ref
    reference counter.

altsetting
    variable-length array of interface structures, one for
    each alternate setting that may be selected.  Each one includes a
    set of endpoint configurations.  They will be in no particular order.

.. _`usb_interface_cache.description`:

Description
-----------

These structures persist for the lifetime of a usb_device, unlike
struct usb_interface (which persists only as long as its configuration
is installed).  The altsetting arrays can be accessed through these
structures at any time, permitting comparison of configurations and
providing support for the /sys/kernel/debug/usb/devices pseudo-file.

.. _`usb_host_config`:

struct usb_host_config
======================

.. c:type:: struct usb_host_config

    representation of a device's configuration

.. _`usb_host_config.definition`:

Definition
----------

.. code-block:: c

    struct usb_host_config {
        struct usb_config_descriptor desc;
        char *string;
        struct usb_interface_assoc_descriptor *intf_assoc[USB_MAXIADS];
        struct usb_interface *interface[USB_MAXINTERFACES];
        struct usb_interface_cache *intf_cache[USB_MAXINTERFACES];
        unsigned char *extra;
        int extralen;
    }

.. _`usb_host_config.members`:

Members
-------

desc
    the device's configuration descriptor.

string
    pointer to the cached version of the iConfiguration string, if
    present for this configuration.

intf_assoc
    list of any interface association descriptors in this config

interface
    array of pointers to usb_interface structures, one for each
    interface in the configuration.  The number of interfaces is stored
    in desc.bNumInterfaces.  These pointers are valid only while the
    the configuration is active.

intf_cache
    array of pointers to usb_interface_cache structures, one
    for each interface in the configuration.  These structures exist
    for the entire life of the device.

extra
    pointer to buffer containing all extra descriptors associated
    with this configuration (those preceding the first interface
    descriptor).

extralen
    length of the extra descriptors buffer.

.. _`usb_host_config.description`:

Description
-----------

USB devices may have multiple configurations, but only one can be active
at any time.  Each encapsulates a different operational environment;
for example, a dual-speed device would have separate configurations for
full-speed and high-speed operation.  The number of configurations
available is stored in the device descriptor as bNumConfigurations.

A configuration can contain multiple interfaces.  Each corresponds to
a different function of the USB device, and all are available whenever
the configuration is active.  The USB standard says that interfaces
are supposed to be numbered from 0 to desc.bNumInterfaces-1, but a lot
of devices get this wrong.  In addition, the interface array is not
guaranteed to be sorted in numerical order.  Use \ :c:func:`usb_ifnum_to_if`\  to
look up an interface entry based on its number.

Device drivers should not attempt to activate configurations.  The choice
of which configuration to install is a policy decision based on such
considerations as available power, functionality provided, and the user's
desires (expressed through userspace tools).  However, drivers can call
\ :c:func:`usb_reset_configuration`\  to reinitialize the current configuration and
all its interfaces.

.. _`usb_device`:

struct usb_device
=================

.. c:type:: struct usb_device

    kernel's representation of a USB device

.. _`usb_device.definition`:

Definition
----------

.. code-block:: c

    struct usb_device {
        int devnum;
        char devpath[16];
        u32 route;
        enum usb_device_state state;
        enum usb_device_speed speed;
        struct usb_tt *tt;
        int ttport;
        unsigned int toggle[2];
        struct usb_device *parent;
        struct usb_bus *bus;
        struct usb_host_endpoint ep0;
        struct device dev;
        struct usb_device_descriptor descriptor;
        struct usb_host_bos *bos;
        struct usb_host_config *config;
        struct usb_host_config *actconfig;
        struct usb_host_endpoint *ep_in[16];
        struct usb_host_endpoint *ep_out[16];
        char **rawdescriptors;
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
        char *product;
        char *manufacturer;
        char *serial;
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
        struct wusb_dev *wusb_dev;
        int slot_id;
        enum usb_device_removable removable;
        struct usb2_lpm_parameters l1_params;
        struct usb3_lpm_parameters u1_params;
        struct usb3_lpm_parameters u2_params;
        unsigned lpm_disable_count;
    }

.. _`usb_device.members`:

Members
-------

devnum
    device number; address on a USB bus

devpath
    device ID string for use in messages (e.g., /port/...)

route
    tree topology hex string for use with xHCI

state
    device state: configured, not attached, etc.

speed
    device speed: high/full/low (or error)

tt
    Transaction Translator info; used with low/full speed dev, highspeed hub

ttport
    device port on that tt hub

toggle
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

ep_in
    array of IN endpoints

ep_out
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
    policy has said we can use it;
    (user space) policy determines if we authorize this device to be
    used or not. By default, wired USB devices are authorized.
    WUSB devices are not, until we authorize them from user space.
    FIXME -- complete doc

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
    if this is a Wireless USB device, link to the WUSB
    specific data for the device.

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
    Ref count used by \ :c:func:`usb_disable_lpm`\  and \ :c:func:`usb_enable_lpm`\ 
    to keep track of the number of functions that require USB 3.0 Link Power
    Management to be disabled for this usb_device.  This count should only
    be manipulated by those functions, with the bandwidth_mutex is held.

.. _`usb_device.notes`:

Notes
-----

Usbcore drivers should not set usbdev->state directly.  Instead use
\ :c:func:`usb_set_device_state`\ .

.. _`usb_hub_for_each_child`:

usb_hub_for_each_child
======================

.. c:function::  usb_hub_for_each_child( hdev,  port1,  child)

    iterate over all child devices on the hub

    :param  hdev:
        USB device belonging to the usb hub

    :param  port1:
        portnum associated with child device

    :param  child:
        child device pointer

.. _`usb_interface_claimed`:

usb_interface_claimed
=====================

.. c:function:: int usb_interface_claimed(struct usb_interface *iface)

    returns true iff an interface is claimed

    :param struct usb_interface \*iface:
        the interface being checked

.. _`usb_interface_claimed.return`:

Return
------

%true (nonzero) iff the interface is claimed, else \ ``false``\ 
(zero).

.. _`usb_interface_claimed.note`:

Note
----

Callers must own the driver model's usb bus readlock.  So driver
\ :c:func:`probe`\  entries don't need extra locking, but other call contexts
may need to explicitly claim that lock.

.. _`usb_make_path`:

usb_make_path
=============

.. c:function:: int usb_make_path(struct usb_device *dev, char *buf, size_t size)

    returns stable device path in the usb tree

    :param struct usb_device \*dev:
        the device whose path is being constructed

    :param char \*buf:
        where to put the string

    :param size_t size:
        how big is "buf"?

.. _`usb_make_path.return`:

Return
------

Length of the string (> 0) or negative if size was too small.

.. _`usb_make_path.note`:

Note
----

This identifier is intended to be "stable", reflecting physical paths in
hardware such as physical bus addresses for host controllers or ports on
USB hubs.  That makes it stay the same until systems are physically
reconfigured, by re-cabling a tree of USB devices or by moving USB host
controllers.  Adding and removing devices, including virtual root hubs
in host controller driver modules, does not change these path identifiers;
neither does rebooting or re-enumerating.  These are more useful identifiers
than changeable ("unstable") ones like bus numbers or device addresses.

With a partial exception for devices connected to USB 2.0 root hubs, these
identifiers are also predictable.  So long as the device tree isn't changed,
plugging any USB device into a given hub port always gives it the same path.
Because of the use of "companion" controllers, devices connected to ports on
USB 2.0 root hubs (EHCI host controllers) will get one path ID if they are
high speed, and a different one if they are full or low speed.

.. _`usb_device`:

USB_DEVICE
==========

.. c:function::  USB_DEVICE( vend,  prod)

    macro used to describe a specific usb device

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

.. _`usb_device.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific device.

.. _`usb_device_ver`:

USB_DEVICE_VER
==============

.. c:function::  USB_DEVICE_VER( vend,  prod,  lo,  hi)

    describe a specific usb device with a version range

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

    :param  lo:
        the bcdDevice_lo value

    :param  hi:
        the bcdDevice_hi value

.. _`usb_device_ver.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific device, with a version range.

.. _`usb_device_interface_class`:

USB_DEVICE_INTERFACE_CLASS
==========================

.. c:function::  USB_DEVICE_INTERFACE_CLASS( vend,  prod,  cl)

    describe a usb device with a specific interface class

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

    :param  cl:
        bInterfaceClass value

.. _`usb_device_interface_class.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific interface class of devices.

.. _`usb_device_interface_protocol`:

USB_DEVICE_INTERFACE_PROTOCOL
=============================

.. c:function::  USB_DEVICE_INTERFACE_PROTOCOL( vend,  prod,  pr)

    describe a usb device with a specific interface protocol

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

    :param  pr:
        bInterfaceProtocol value

.. _`usb_device_interface_protocol.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific interface protocol of devices.

.. _`usb_device_interface_number`:

USB_DEVICE_INTERFACE_NUMBER
===========================

.. c:function::  USB_DEVICE_INTERFACE_NUMBER( vend,  prod,  num)

    describe a usb device with a specific interface number

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

    :param  num:
        bInterfaceNumber value

.. _`usb_device_interface_number.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific interface number of devices.

.. _`usb_device_info`:

USB_DEVICE_INFO
===============

.. c:function::  USB_DEVICE_INFO( cl,  sc,  pr)

    macro used to describe a class of usb devices

    :param  cl:
        bDeviceClass value

    :param  sc:
        bDeviceSubClass value

    :param  pr:
        bDeviceProtocol value

.. _`usb_device_info.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific class of devices.

.. _`usb_interface_info`:

USB_INTERFACE_INFO
==================

.. c:function::  USB_INTERFACE_INFO( cl,  sc,  pr)

    macro used to describe a class of usb interfaces

    :param  cl:
        bInterfaceClass value

    :param  sc:
        bInterfaceSubClass value

    :param  pr:
        bInterfaceProtocol value

.. _`usb_interface_info.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific class of interfaces.

.. _`usb_device_and_interface_info`:

USB_DEVICE_AND_INTERFACE_INFO
=============================

.. c:function::  USB_DEVICE_AND_INTERFACE_INFO( vend,  prod,  cl,  sc,  pr)

    describe a specific usb device with a class of usb interfaces

    :param  vend:
        the 16 bit USB Vendor ID

    :param  prod:
        the 16 bit USB Product ID

    :param  cl:
        bInterfaceClass value

    :param  sc:
        bInterfaceSubClass value

    :param  pr:
        bInterfaceProtocol value

.. _`usb_device_and_interface_info.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific device with a specific class of interfaces.

This is especially useful when explicitly matching devices that have
vendor specific bDeviceClass values, but standards-compliant interfaces.

.. _`usb_vendor_and_interface_info`:

USB_VENDOR_AND_INTERFACE_INFO
=============================

.. c:function::  USB_VENDOR_AND_INTERFACE_INFO( vend,  cl,  sc,  pr)

    describe a specific usb vendor with a class of usb interfaces

    :param  vend:
        the 16 bit USB Vendor ID

    :param  cl:
        bInterfaceClass value

    :param  sc:
        bInterfaceSubClass value

    :param  pr:
        bInterfaceProtocol value

.. _`usb_vendor_and_interface_info.description`:

Description
-----------

This macro is used to create a struct usb_device_id that matches a
specific vendor with a specific class of interfaces.

This is especially useful when explicitly matching devices that have
vendor specific bDeviceClass values, but standards-compliant interfaces.

.. _`usbdrv_wrap`:

struct usbdrv_wrap
==================

.. c:type:: struct usbdrv_wrap

    wrapper for driver-model structure

.. _`usbdrv_wrap.definition`:

Definition
----------

.. code-block:: c

    struct usbdrv_wrap {
        struct device_driver driver;
        int for_devices;
    }

.. _`usbdrv_wrap.members`:

Members
-------

driver
    The driver-model core driver structure.

for_devices
    Non-zero for device drivers, 0 for interface drivers.

.. _`usb_driver`:

struct usb_driver
=================

.. c:type:: struct usb_driver

    identifies USB interface driver to usbcore

.. _`usb_driver.definition`:

Definition
----------

.. code-block:: c

    struct usb_driver {
        const char *name;
        int (*probe) (struct usb_interface *intf, const struct usb_device_id *id);
        void (*disconnect) (struct usb_interface *intf);
        int (*unlocked_ioctl) (struct usb_interface *intf, unsigned int code, void *buf);
        int (*suspend) (struct usb_interface *intf, pm_message_t message);
        int (*resume) (struct usb_interface *intf);
        int (*reset_resume)(struct usb_interface *intf);
        int (*pre_reset)(struct usb_interface *intf);
        int (*post_reset)(struct usb_interface *intf);
        const struct usb_device_id *id_table;
        struct usb_dynids dynids;
        struct usbdrv_wrap drvwrap;
        unsigned int no_dynamic_id:1;
        unsigned int supports_autosuspend:1;
        unsigned int disable_hub_initiated_lpm:1;
        unsigned int soft_unbind:1;
    }

.. _`usb_driver.members`:

Members
-------

name
    The driver name should be unique among USB drivers,
    and should normally be the same as the module name.

probe
    Called to see if the driver is willing to manage a particular
    interface on a device.  If it is, probe returns zero and uses
    \ :c:func:`usb_set_intfdata`\  to associate driver-specific data with the
    interface.  It may also use \ :c:func:`usb_set_interface`\  to specify the
    appropriate altsetting.  If unwilling to manage the interface,
    return -ENODEV, if genuine IO errors occurred, an appropriate
    negative errno value.

disconnect
    Called when the interface is no longer accessible, usually
    because its device has been (or is being) disconnected or the
    driver module is being unloaded.

unlocked_ioctl
    Used for drivers that want to talk to userspace through
    the "usbfs" filesystem.  This lets devices provide ways to
    expose information to user space regardless of where they
    do (or don't) show up otherwise in the filesystem.

suspend
    Called when the device is going to be suspended by the
    system either from system sleep or runtime suspend context. The
    return value will be ignored in system sleep context, so do NOT
    try to continue using the device if suspend fails in this case.
    Instead, let the resume or reset-resume routine recover from
    the failure.

resume
    Called when the device is being resumed by the system.

reset_resume
    Called when the suspended device has been reset instead
    of being resumed.

pre_reset
    Called by \ :c:func:`usb_reset_device`\  when the device is about to be
    reset.  This routine must not return until the driver has no active
    URBs for the device, and no more URBs may be submitted until the
    post_reset method is called.

post_reset
    Called by \ :c:func:`usb_reset_device`\  after the device
    has been reset

id_table
    USB drivers use ID table to support hotplugging.
    Export this with MODULE_DEVICE_TABLE(usb,...).  This must be set
    or your driver's probe function will never get called.

dynids
    used internally to hold the list of dynamically added device
    ids for this driver.

drvwrap
    Driver-model core structure wrapper.

no_dynamic_id
    if set to 1, the USB core will not allow dynamic ids to be
    added to this driver by preventing the sysfs file from being created.

supports_autosuspend
    if set to 0, the USB core will not allow autosuspend
    for interfaces bound to this driver.

disable_hub_initiated_lpm
    if set to 1, the USB core will not allow hubs
    to initiate lower power link state transitions when an idle timeout
    occurs.  Device-initiated USB 3.0 link PM will still be allowed.

soft_unbind
    if set to 1, the USB core will not kill URBs and disable
    endpoints before calling the driver's disconnect method.

.. _`usb_driver.description`:

Description
-----------

USB interface drivers must provide a name, \ :c:func:`probe`\  and \ :c:func:`disconnect`\ 
methods, and an id_table.  Other driver fields are optional.

The id_table is used in hotplugging.  It holds a set of descriptors,
and specialized data may be associated with each entry.  That table
is used by both user and kernel mode hotplugging support.

The \ :c:func:`probe`\  and \ :c:func:`disconnect`\  methods are called in a context where
they can sleep, but they should avoid abusing the privilege.  Most
work to connect to a device should be done when the device is opened,
and undone at the last close.  The disconnect code needs to address
concurrency issues with respect to \ :c:func:`open`\  and \ :c:func:`close`\  methods, as
well as forcing all pending I/O requests to complete (by unlinking
them as necessary, and blocking until the unlinks complete).

.. _`usb_device_driver`:

struct usb_device_driver
========================

.. c:type:: struct usb_device_driver

    identifies USB device driver to usbcore

.. _`usb_device_driver.definition`:

Definition
----------

.. code-block:: c

    struct usb_device_driver {
        const char *name;
        int (*probe) (struct usb_device *udev);
        void (*disconnect) (struct usb_device *udev);
        int (*suspend) (struct usb_device *udev, pm_message_t message);
        int (*resume) (struct usb_device *udev, pm_message_t message);
        struct usbdrv_wrap drvwrap;
        unsigned int supports_autosuspend:1;
    }

.. _`usb_device_driver.members`:

Members
-------

name
    The driver name should be unique among USB drivers,
    and should normally be the same as the module name.

probe
    Called to see if the driver is willing to manage a particular
    device.  If it is, probe returns zero and uses \ :c:func:`dev_set_drvdata`\ 
    to associate driver-specific data with the device.  If unwilling
    to manage the device, return a negative errno value.

disconnect
    Called when the device is no longer accessible, usually
    because it has been (or is being) disconnected or the driver's
    module is being unloaded.

suspend
    Called when the device is going to be suspended by the system.

resume
    Called when the device is being resumed by the system.

drvwrap
    Driver-model core structure wrapper.

supports_autosuspend
    if set to 0, the USB core will not allow autosuspend
    for devices bound to this driver.

.. _`usb_device_driver.description`:

Description
-----------

USB drivers must provide all the fields listed above except drvwrap.

.. _`usb_class_driver`:

struct usb_class_driver
=======================

.. c:type:: struct usb_class_driver

    identifies a USB driver that wants to use the USB major number

.. _`usb_class_driver.definition`:

Definition
----------

.. code-block:: c

    struct usb_class_driver {
        char *name;
        char *(*devnode)(struct device *dev, umode_t *mode);
        const struct file_operations *fops;
        int minor_base;
    }

.. _`usb_class_driver.members`:

Members
-------

name
    the usb class device name for this driver.  Will show up in sysfs.

devnode
    Callback to provide a naming hint for a possible
    device node to create.

fops
    pointer to the struct file_operations of this driver.

minor_base
    the start of the minor range for this driver.

.. _`usb_class_driver.description`:

Description
-----------

This structure is used for the \ :c:func:`usb_register_dev`\  and
\ :c:func:`usb_deregister_dev`\  functions, to consolidate a number of the
parameters used for them.

.. _`module_usb_driver`:

module_usb_driver
=================

.. c:function::  module_usb_driver( __usb_driver)

    Helper macro for registering a USB driver

    :param  __usb_driver:
        usb_driver struct

.. _`module_usb_driver.description`:

Description
-----------

Helper macro for USB drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ 

.. _`urb`:

struct urb
==========

.. c:type:: struct urb

    USB Request Block

.. _`urb.definition`:

Definition
----------

.. code-block:: c

    struct urb {
        struct kref kref;
        void *hcpriv;
        atomic_t use_count;
        atomic_t reject;
        int unlinked;
        struct list_head urb_list;
        struct list_head anchor_list;
        struct usb_anchor *anchor;
        struct usb_device *dev;
        struct usb_host_endpoint *ep;
        unsigned int pipe;
        unsigned int stream_id;
        int status;
        unsigned int transfer_flags;
        void *transfer_buffer;
        dma_addr_t transfer_dma;
        struct scatterlist *sg;
        int num_mapped_sgs;
        int num_sgs;
        u32 transfer_buffer_length;
        u32 actual_length;
        unsigned char *setup_packet;
        dma_addr_t setup_dma;
        int start_frame;
        int number_of_packets;
        int interval;
        int error_count;
        void *context;
        usb_complete_t complete;
        struct usb_iso_packet_descriptor iso_frame_desc[0];
    }

.. _`urb.members`:

Members
-------

kref
    *undescribed*

hcpriv
    *undescribed*

use_count
    *undescribed*

reject
    *undescribed*

unlinked
    *undescribed*

urb_list
    For use by current owner of the URB.

anchor_list
    membership in the list of an anchor

anchor
    to anchor URBs to a common mooring

dev
    Identifies the USB device to perform the request.

ep
    Points to the endpoint's data structure.  Will eventually
    replace \ ``pipe``\ .

pipe
    Holds endpoint number, direction, type, and more.
    Create these values with the eight macros available;
    usb_{snd,rcv}TYPEpipe(dev,endpoint), where the TYPE is "ctrl"
    (control), "bulk", "int" (interrupt), or "iso" (isochronous).
    For example \ :c:func:`usb_sndbulkpipe`\  or \ :c:func:`usb_rcvintpipe`\ .  Endpoint
    numbers range from zero to fifteen.  Note that "in" endpoint two
    is a different endpoint (and pipe) from "out" endpoint two.
    The current configuration controls the existence, type, and
    maximum packet size of any given endpoint.

stream_id
    the endpoint's stream ID for bulk streams

status
    This is read in non-iso completion functions to get the
    status of the particular request.  ISO requests only use it
    to tell whether the URB was unlinked; detailed status for
    each frame is in the fields of the iso_frame-desc.

transfer_flags
    A variety of flags may be used to affect how URB
    submission, unlinking, or operation are handled.  Different
    kinds of URB can use different flags.

transfer_buffer
    This identifies the buffer to (or from) which the I/O
    request will be performed unless URB_NO_TRANSFER_DMA_MAP is set
    (however, do not leave garbage in transfer_buffer even then).
    This buffer must be suitable for DMA; allocate it with
    \ :c:func:`kmalloc`\  or equivalent.  For transfers to "in" endpoints, contents
    of this buffer will be modified.  This buffer is used for the data
    stage of control transfers.

transfer_dma
    When transfer_flags includes URB_NO_TRANSFER_DMA_MAP,
    the device driver is saying that it provided this DMA address,
    which the host controller driver should use in preference to the
    transfer_buffer.

sg
    scatter gather buffer list, the buffer size of each element in
    the list (except the last) must be divisible by the endpoint's
    max packet size if no_sg_constraint isn't set in 'struct usb_bus'

num_mapped_sgs
    (internal) number of mapped sg entries

num_sgs
    number of entries in the sg list

transfer_buffer_length
    How big is transfer_buffer.  The transfer may
    be broken up into chunks according to the current maximum packet
    size for the endpoint, which is a function of the configuration
    and is encoded in the pipe.  When the length is zero, neither
    transfer_buffer nor transfer_dma is used.

actual_length
    This is read in non-iso completion functions, and
    it tells how many bytes (out of transfer_buffer_length) were
    transferred.  It will normally be the same as requested, unless
    either an error was reported or a short read was performed.
    The URB_SHORT_NOT_OK transfer flag may be used to make such
    short reads be reported as errors.

setup_packet
    Only used for control transfers, this points to eight bytes
    of setup data.  Control transfers always start by sending this data
    to the device.  Then transfer_buffer is read or written, if needed.

setup_dma
    DMA pointer for the setup packet.  The caller must not use
    this field; setup_packet must point to a valid buffer.

start_frame
    Returns the initial frame for isochronous transfers.

number_of_packets
    Lists the number of ISO transfer buffers.

interval
    Specifies the polling interval for interrupt or isochronous
    transfers.  The units are frames (milliseconds) for full and low
    speed devices, and microframes (1/8 millisecond) for highspeed
    and SuperSpeed devices.

error_count
    Returns the number of ISO transfers that reported errors.

context
    For use in completion functions.  This normally points to
    request-specific driver context.

complete
    Completion handler. This URB is passed as the parameter to the
    completion function.  The completion function may then do what
    it likes with the URB, including resubmitting or freeing it.

iso_frame_desc
    Used to provide arrays of ISO transfer buffers and to
    collect the transfer status for each buffer.

.. _`urb.description`:

Description
-----------

This structure identifies USB transfer requests.  URBs must be allocated by
calling \ :c:func:`usb_alloc_urb`\  and freed with a call to \ :c:func:`usb_free_urb`\ .
Initialization may be done using various usb_fill_*_urb() functions.  URBs
are submitted using \ :c:func:`usb_submit_urb`\ , and pending requests may be canceled
using \ :c:func:`usb_unlink_urb`\  or \ :c:func:`usb_kill_urb`\ .

.. _`urb.data-transfer-buffers`:

Data Transfer Buffers
---------------------


Normally drivers provide I/O buffers allocated with \ :c:func:`kmalloc`\  or otherwise
taken from the general page pool.  That is provided by transfer_buffer
(control requests also use setup_packet), and host controller drivers
perform a dma mapping (and unmapping) for each buffer transferred.  Those
mapping operations can be expensive on some platforms (perhaps using a dma
bounce buffer or talking to an IOMMU),
although they're cheap on commodity x86 and ppc hardware.

Alternatively, drivers may pass the URB_NO_TRANSFER_DMA_MAP transfer flag,
which tells the host controller driver that no such mapping is needed for
the transfer_buffer since
the device driver is DMA-aware.  For example, a device driver might
allocate a DMA buffer with \ :c:func:`usb_alloc_coherent`\  or call \ :c:func:`usb_buffer_map`\ .
When this transfer flag is provided, host controller drivers will
attempt to use the dma address found in the transfer_dma
field rather than determining a dma address themselves.

Note that transfer_buffer must still be set if the controller
does not support DMA (as indicated by bus.uses_dma) and when talking
to root hub. If you have to trasfer between highmem zone and the device
on such controller, create a bounce buffer or bail out with an error.
If transfer_buffer cannot be set (is in highmem) and the controller is DMA
capable, assign NULL to it, so that usbmon knows not to use the value.
The setup_packet must always be set, so it cannot be located in highmem.

.. _`urb.initialization`:

Initialization
--------------


All URBs submitted must initialize the dev, pipe, transfer_flags (may be
zero), and complete fields.  All URBs must also initialize
transfer_buffer and transfer_buffer_length.  They may provide the
URB_SHORT_NOT_OK transfer flag, indicating that short reads are
to be treated as errors; that flag is invalid for write requests.

Bulk URBs may
use the URB_ZERO_PACKET transfer flag, indicating that bulk OUT transfers
should always terminate with a short packet, even if it means adding an
extra zero length packet.

Control URBs must provide a valid pointer in the setup_packet field.
Unlike the transfer_buffer, the setup_packet may not be mapped for DMA
beforehand.

Interrupt URBs must provide an interval, saying how often (in milliseconds
or, for highspeed devices, 125 microsecond units)
to poll for transfers.  After the URB has been submitted, the interval
field reflects how the transfer was actually scheduled.
The polling interval may be more frequent than requested.
For example, some controllers have a maximum interval of 32 milliseconds,
while others support intervals of up to 1024 milliseconds.
Isochronous URBs also have transfer intervals.  (Note that for isochronous
endpoints, as well as high speed interrupt endpoints, the encoding of
the transfer interval in the endpoint descriptor is logarithmic.
Device drivers must convert that value to linear units themselves.)

If an isochronous endpoint queue isn't already running, the host
controller will schedule a new URB to start as soon as bandwidth
utilization allows.  If the queue is running then a new URB will be
scheduled to start in the first transfer slot following the end of the
preceding URB, if that slot has not already expired.  If the slot has
expired (which can happen when IRQ delivery is delayed for a long time),
the scheduling behavior depends on the URB_ISO_ASAP flag.  If the flag
is clear then the URB will be scheduled to start in the expired slot,
implying that some of its packets will not be transferred; if the flag
is set then the URB will be scheduled in the first unexpired slot,
breaking the queue's synchronization.  Upon URB completion, the
start_frame field will be set to the (micro)frame number in which the
transfer was scheduled.  Ranges for frame counter values are HC-specific
and can go from as low as 256 to as high as 65536 frames.

Isochronous URBs have a different data transfer model, in part because
the quality of service is only "best effort".  Callers provide specially
allocated URBs, with number_of_packets worth of iso_frame_desc structures
at the end.  Each such packet is an individual ISO transfer.  Isochronous
URBs are normally queued, submitted by drivers to arrange that
transfers are at least double buffered, and then explicitly resubmitted
in completion handlers, so
that data (such as audio or video) streams at as constant a rate as the
host controller scheduler can support.

.. _`urb.completion-callbacks`:

Completion Callbacks
--------------------


The completion callback is made \ :c:func:`in_interrupt`\ , and one of the first
things that a completion handler should do is check the status field.
The status field is provided for all URBs.  It is used to report
unlinked URBs, and status for all non-ISO transfers.  It should not
be examined before the URB is returned to the completion handler.

The context field is normally used to link URBs back to the relevant
driver or request state.

When the completion callback is invoked for non-isochronous URBs, the
actual_length field tells how many bytes were transferred.  This field
is updated even when the URB terminated with an error or was unlinked.

ISO transfer status is reported in the status and actual_length fields
of the iso_frame_desc array, and the number of errors is reported in
error_count.  Completion callbacks for ISO transfers will normally
(re)submit URBs to ensure a constant transfer rate.

Note that even fields marked "public" should not be touched by the driver
when the urb is owned by the hcd, that is, since the call to
\ :c:func:`usb_submit_urb`\  till the entry into the completion routine.

.. _`usb_fill_control_urb`:

usb_fill_control_urb
====================

.. c:function:: void usb_fill_control_urb(struct urb *urb, struct usb_device *dev, unsigned int pipe, unsigned char *setup_packet, void *transfer_buffer, int buffer_length, usb_complete_t complete_fn, void *context)

    initializes a control urb

    :param struct urb \*urb:
        pointer to the urb to initialize.

    :param struct usb_device \*dev:
        pointer to the struct usb_device for this urb.

    :param unsigned int pipe:
        the endpoint pipe

    :param unsigned char \*setup_packet:
        pointer to the setup_packet buffer

    :param void \*transfer_buffer:
        pointer to the transfer buffer

    :param int buffer_length:
        length of the transfer buffer

    :param usb_complete_t complete_fn:
        pointer to the usb_complete_t function

    :param void \*context:
        what to set the urb context to.

.. _`usb_fill_control_urb.description`:

Description
-----------

Initializes a control urb with the proper information needed to submit
it to a device.

.. _`usb_fill_bulk_urb`:

usb_fill_bulk_urb
=================

.. c:function:: void usb_fill_bulk_urb(struct urb *urb, struct usb_device *dev, unsigned int pipe, void *transfer_buffer, int buffer_length, usb_complete_t complete_fn, void *context)

    macro to help initialize a bulk urb

    :param struct urb \*urb:
        pointer to the urb to initialize.

    :param struct usb_device \*dev:
        pointer to the struct usb_device for this urb.

    :param unsigned int pipe:
        the endpoint pipe

    :param void \*transfer_buffer:
        pointer to the transfer buffer

    :param int buffer_length:
        length of the transfer buffer

    :param usb_complete_t complete_fn:
        pointer to the usb_complete_t function

    :param void \*context:
        what to set the urb context to.

.. _`usb_fill_bulk_urb.description`:

Description
-----------

Initializes a bulk urb with the proper information needed to submit it
to a device.

.. _`usb_fill_int_urb`:

usb_fill_int_urb
================

.. c:function:: void usb_fill_int_urb(struct urb *urb, struct usb_device *dev, unsigned int pipe, void *transfer_buffer, int buffer_length, usb_complete_t complete_fn, void *context, int interval)

    macro to help initialize a interrupt urb

    :param struct urb \*urb:
        pointer to the urb to initialize.

    :param struct usb_device \*dev:
        pointer to the struct usb_device for this urb.

    :param unsigned int pipe:
        the endpoint pipe

    :param void \*transfer_buffer:
        pointer to the transfer buffer

    :param int buffer_length:
        length of the transfer buffer

    :param usb_complete_t complete_fn:
        pointer to the usb_complete_t function

    :param void \*context:
        what to set the urb context to.

    :param int interval:
        what to set the urb interval to, encoded like
        the endpoint descriptor's bInterval value.

.. _`usb_fill_int_urb.description`:

Description
-----------

Initializes a interrupt urb with the proper information needed to submit
it to a device.

Note that High Speed and SuperSpeed(+) interrupt endpoints use a logarithmic
encoding of the endpoint interval, and express polling intervals in
microframes (eight per millisecond) rather than in frames (one per
millisecond).

Wireless USB also uses the logarithmic encoding, but specifies it in units of
128us instead of 125us.  For Wireless USB devices, the interval is passed
through to the host controller, rather than being translated into microframe
units.

.. _`usb_urb_dir_in`:

usb_urb_dir_in
==============

.. c:function:: int usb_urb_dir_in(struct urb *urb)

    check if an URB describes an IN transfer

    :param struct urb \*urb:
        URB to be checked

.. _`usb_urb_dir_in.return`:

Return
------

1 if \ ``urb``\  describes an IN transfer (device-to-host),
otherwise 0.

.. _`usb_urb_dir_out`:

usb_urb_dir_out
===============

.. c:function:: int usb_urb_dir_out(struct urb *urb)

    check if an URB describes an OUT transfer

    :param struct urb \*urb:
        URB to be checked

.. _`usb_urb_dir_out.return`:

Return
------

1 if \ ``urb``\  describes an OUT transfer (host-to-device),
otherwise 0.

.. _`usb_sg_request`:

struct usb_sg_request
=====================

.. c:type:: struct usb_sg_request

    support for scatter/gather I/O

.. _`usb_sg_request.definition`:

Definition
----------

.. code-block:: c

    struct usb_sg_request {
        int status;
        size_t bytes;
        spinlock_t lock;
        struct usb_device *dev;
        int pipe;
        int entries;
        struct urb **urbs;
        int count;
        struct completion complete;
    }

.. _`usb_sg_request.members`:

Members
-------

status
    zero indicates success, else negative errno

bytes
    counts bytes transferred.

lock
    *undescribed*

dev
    *undescribed*

pipe
    *undescribed*

entries
    *undescribed*

urbs
    *undescribed*

count
    *undescribed*

complete
    *undescribed*

.. _`usb_sg_request.description`:

Description
-----------

These requests are initialized using \ :c:func:`usb_sg_init`\ , and then are used
as request handles passed to \ :c:func:`usb_sg_wait`\  or \ :c:func:`usb_sg_cancel`\ .  Most
members of the request object aren't for driver access.

The status and bytecount values are valid only after \ :c:func:`usb_sg_wait`\ 
returns.  If the status is zero, then the bytecount matches the total
from the request.

After an error completion, drivers may need to clear a halt condition
on the endpoint.

.. This file was automatic generated / don't edit.



.. _API-struct-usb-interface:

====================
struct usb_interface
====================

*man struct usb_interface(9)*

*4.6.0-rc1*

what usb device drivers talk to


Synopsis
========

.. code-block:: c

    struct usb_interface {
      struct usb_host_interface * altsetting;
      struct usb_host_interface * cur_altsetting;
      unsigned num_altsetting;
      struct usb_interface_assoc_descriptor * intf_assoc;
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
      struct device * usb_dev;
      atomic_t pm_usage_cnt;
      struct work_struct reset_ws;
    };


Members
=======

altsetting
    array of interface structures, one for each alternate setting that may be selected. Each one includes a set of endpoint configurations. They will be in no particular order.

cur_altsetting
    the current altsetting.

num_altsetting
    number of altsettings defined.

intf_assoc
    interface association descriptor

minor
    the minor number assigned to this interface, if this interface is bound to a driver that uses the USB major number. If this interface does not use the USB major, this field
    should be unused. The driver should set this value in the ``probe`` function of the driver, after it has been assigned a minor number from the USB core by calling
    ``usb_register_dev``.

condition
    binding state of the interface: not bound, binding (in ``probe``), bound to a driver, or unbinding (in ``disconnect``)

sysfs_files_created
    sysfs attributes exist

ep_devs_created
    endpoint child pseudo-devices exist

unregistering
    flag set when the interface is being unregistered

needs_remote_wakeup
    flag set when the driver requires remote-wakeup capability during autosuspend.

needs_altsetting0
    flag set when a set-interface request for altsetting 0 has been deferred.

needs_binding
    flag set when the driver should be re-probed or unbound following a reset or suspend operation it doesn't support.

resetting_device
    USB core reset the device, so use alt setting 0 as current; needs bandwidth alloc after reset.

authorized
    This allows to (de)authorize individual interfaces instead a whole device in contrast to the device authorization.

dev
    driver model's view of this device

usb_dev
    if an interface is bound to the USB major, this will point to the sysfs representation for that device.

pm_usage_cnt
    PM usage counter for this interface

reset_ws
    Used for scheduling resets from atomic context.


Description
===========

USB device drivers attach to interfaces on a physical device. Each interface encapsulates a single high level function, such as feeding an audio stream to a speaker or reporting a
change in a volume control. Many USB devices only have one interface. The protocol used to talk to an interface's endpoints can be defined in a usb “class” specification, or by a
product's vendor. The (default) control endpoint is part of every interface, but is never listed among the interface's descriptors.

The driver that is bound to the interface can use standard driver model calls such as ``dev_get_drvdata`` on the dev member of this structure.

Each interface may have alternate settings. The initial configuration of a device sets altsetting 0, but the device driver can change that setting using ``usb_set_interface``.
Alternate settings are often used to control the use of periodic endpoints, such as by having different endpoints use different amounts of reserved USB bandwidth. All
standards-conformant USB devices that use isochronous endpoints will use them in non-default settings.

The USB specification says that alternate setting numbers must run from 0 to one less than the total number of alternate settings. But some devices manage to mess this up, and the
structures aren't necessarily stored in numerical order anyhow. Use ``usb_altnum_to_altsetting`` to look up an alternate setting in the altsetting array based on its number.

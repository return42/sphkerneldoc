.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/include/visorbus.h

.. _`visor_driver`:

struct visor_driver
===================

.. c:type:: struct visor_driver

    Information provided by each visor driver when it registers with the visorbus driver.

.. _`visor_driver.definition`:

Definition
----------

.. code-block:: c

    struct visor_driver {
        const char *name;
        struct module *owner;
        struct visor_channeltype_descriptor *channel_types;
        int (*probe)(struct visor_device *dev);
        void (*remove)(struct visor_device *dev);
        void (*channel_interrupt)(struct visor_device *dev);
        int (*pause)(struct visor_device *dev, visorbus_state_complete_func complete_func);
        int (*resume)(struct visor_device *dev, visorbus_state_complete_func complete_func);
        struct device_driver driver;
    }

.. _`visor_driver.members`:

Members
-------

name
    Name of the visor driver.

owner
    The module owner.

channel_types
    Types of channels handled by this driver, ending with
    a zero GUID. Our specialized BUS.match() method knows
    about this list, and uses it to determine whether this
    driver will in fact handle a new device that it has
    detected.

probe
    Called when a new device comes online, by our \ :c:func:`probe`\ 
    function specified by driver.probe() (triggered
    ultimately by some call to \ :c:func:`driver_register`\ ,
    \ :c:func:`bus_add_driver`\ , or \ :c:func:`driver_attach`\ ).

remove
    Called when a new device is removed, by our \ :c:func:`remove`\ 
    function specified by driver.remove() (triggered
    ultimately by some call to \ :c:func:`device_release_driver`\ ).

channel_interrupt
    Called periodically, whenever there is a possiblity
    that "something interesting" may have happened to the
    channel.

pause
    Called to initiate a change of the device's state.  If
    the return valu\`e is < 0, there was an error and the
    state transition will NOT occur.  If the return value
    is >= 0, then the state transition was INITIATED
    successfully, and \ :c:func:`complete_func`\  will be called (or
    was just called) with the final status when either the
    state transition fails or completes successfully.

resume
    Behaves similar to pause.

driver
    Private reference to the device driver. For use by bus
    driver only.

.. _`visor_device`:

struct visor_device
===================

.. c:type:: struct visor_device

    A device type for things "plugged" into the visorbus bus

.. _`visor_device.definition`:

Definition
----------

.. code-block:: c

    struct visor_device {
        struct visorchannel *visorchannel;
        guid_t channel_type_guid;
        struct device device;
        struct list_head list_all;
        struct timer_list timer;
        bool timer_active;
        bool being_removed;
        struct mutex visordriver_callback_lock;
        bool pausing;
        bool resuming;
        u32 chipset_bus_no;
        u32 chipset_dev_no;
        struct visorchipset_state state;
        guid_t inst;
        u8 *name;
        struct controlvm_message_header *pending_msg_hdr;
        void *vbus_hdr_info;
        guid_t partition_guid;
        struct dentry *debugfs_dir;
        struct dentry *debugfs_client_bus_info;
    }

.. _`visor_device.members`:

Members
-------

visorchannel
    Points to the channel that the device is
    associated with.

channel_type_guid
    Identifies the channel type to the bus driver.

device
    Device struct meant for use by the bus driver
    only.

list_all
    Used by the bus driver to enumerate devices.

timer
    Timer fired periodically to do interrupt-type
    activity.

timer_active
    *undescribed*

being_removed
    Indicates that the device is being removed from
    the bus. Private bus driver use only.

visordriver_callback_lock
    Used by the bus driver to lock when adding and
    removing devices.

pausing
    Indicates that a change towards a paused state.
    is in progress. Only modified by the bus driver.

resuming
    Indicates that a change towards a running state
    is in progress. Only modified by the bus driver.

chipset_bus_no
    Private field used by the bus driver.

chipset_dev_no
    Private field used the bus driver.

state
    Used to indicate the current state of the
    device.

inst
    Unique GUID for this instance of the device.

name
    Name of the device.

pending_msg_hdr
    For private use by bus driver to respond to
    hypervisor requests.

vbus_hdr_info
    A pointer to header info. Private use by bus
    driver.

partition_guid
    Indicates client partion id. This should be the
    same across all visor_devices in the current
    guest. Private use by bus driver only.

debugfs_dir
    *undescribed*

debugfs_client_bus_info
    *undescribed*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/wimax.h

.. _`wimax_dev`:

struct wimax_dev
================

.. c:type:: struct wimax_dev

    Generic WiMAX device

.. _`wimax_dev.definition`:

Definition
----------

.. code-block:: c

    struct wimax_dev {
        struct net_device *net_dev;
        struct list_head id_table_node;
        struct mutex mutex;
        struct mutex mutex_reset;
        enum wimax_st state;
        int (* op_msg_from_user) (struct wimax_dev *wimax_dev,const char *,const void *, size_t,const struct genl_info *info);
        int (* op_rfkill_sw_toggle) (struct wimax_dev *wimax_dev,enum wimax_rf_state);
        int (* op_reset) (struct wimax_dev *wimax_dev);
        struct rfkill *rfkill;
        unsigned int rf_hw;
        unsigned int rf_sw;
        char name[32];
        struct dentry *debugfs_dentry;
    }

.. _`wimax_dev.members`:

Members
-------

net_dev
    [fill] Pointer to the \ :c:type:`struct net_device <net_device>`\  this WiMAX
    device implements.

id_table_node
    [private] link to the list of wimax devices kept by
    id-table.c. Protected by it's own spinlock.

mutex
    [private] Serializes all concurrent access and execution of
    operations.

mutex_reset
    [private] Serializes reset operations. Needs to be a
    different mutex because as part of the reset operation, the
    driver has to call back into the stack to do things such as
    state change, that require wimax_dev->mutex.

state
    [private] Current state of the WiMAX device.

op_msg_from_user
    [fill] Driver-specific operation to
    handle a raw message from user space to the driver. The
    driver can send messages to user space using with
    \ :c:func:`wimax_msg_to_user`\ .

op_rfkill_sw_toggle
    [fill] Driver-specific operation to act on
    userspace (or any other agent) requesting the WiMAX device to
    change the RF Kill software switch (WIMAX_RF_ON or
    WIMAX_RF_OFF).
    If such hardware support is not present, it is assumed the
    radio cannot be switched off and it is always on (and the stack
    will error out when trying to switch it off). In such case,
    this function pointer can be left as NULL.

op_reset
    [fill] Driver specific operation to reset the
    device.
    This operation should always attempt first a warm reset that
    does not disconnect the device from the bus and return 0.
    If that fails, it should resort to some sort of cold or bus
    reset (even if it implies a bus disconnection and device
    disappearance). In that case, -ENODEV should be returned to
    indicate the device is gone.
    This operation has to be synchronous, and return only when the
    reset is complete. In case of having had to resort to bus/cold
    reset implying a device disconnection, the call is allowed to
    return immediately.

rfkill
    [private] integration into the RF-Kill infrastructure.

rf_hw
    [private] State of the hardware radio switch (OFF/ON)

rf_sw
    [private] State of the software radio switch (OFF/ON)

name
    [fill] A way to identify this device. We need to register a
    name with many subsystems (rfkill, workqueue creation, etc).
    We can't use the network device name as that
    might change and in some instances we don't know it yet (until
    we don't call \ :c:func:`register_netdev`\ ). So we generate an unique one
    using the driver name and device bus id, place it here and use
    it across the board. Recommended naming:
    DRIVERNAME-BUSNAME:BUSID (dev->bus->name, dev->bus_id).

debugfs_dentry
    [private] Used to hook up a debugfs entry. This
    shows up in the debugfs root as wimax\:DEVICENAME.

.. _`wimax_dev.note`:

NOTE
----

wimax_dev->mutex is NOT locked when this op is being
called; however, wimax_dev->mutex_reset IS locked to ensure
serialization of calls to \ :c:func:`wimax_reset`\ .
See \ :c:func:`wimax_reset`\ 's documentation.

.. _`wimax_dev.description`:

Description
-----------

This structure defines a common interface to access all WiMAX
devices from different vendors and provides a common API as well as
a free-form device-specific messaging channel.

.. _`wimax_dev.usage`:

Usage
-----

1. Embed a \ :c:type:`struct wimax_dev <wimax_dev>`\  at \*the beginning\* the network
device structure so that \ :c:func:`netdev_priv`\  points to it.

2. \ :c:func:`memset`\  it to zero

3. Initialize with \ :c:func:`wimax_dev_init`\ . This will leave the WiMAX
device in the \ ``__WIMAX_ST_NULL``\  state.

4. Fill all the fields marked with [fill]; once called
\ :c:func:`wimax_dev_add`\ , those fields CANNOT be modified.

5. Call \ :c:func:`wimax_dev_add`\  \*after\* registering the network
device. This will leave the WiMAX device in the \ ``WIMAX_ST_DOWN``\ 
state.
Protect the driver's net_device->\ :c:func:`open`\  against succeeding if
the wimax device state is lower than \ ``WIMAX_ST_DOWN``\ .

6. Select when the device is going to be turned on/initialized;
for example, it could be initialized on 'ifconfig up' (when the
netdev op '\ :c:func:`open`\ ' is called on the driver).

When the device is initialized (at \`ifconfig up\` time, or right
after calling \ :c:func:`wimax_dev_add`\  from \\ :c:func:`_probe`\ , make sure the
following steps are taken

a. Move the device to \ ``WIMAX_ST_UNINITIALIZED``\ . This is needed so
some API calls that shouldn't work until the device is ready
can be blocked.

b. Initialize the device. Make sure to turn the SW radio switch
off and move the device to state \ ``WIMAX_ST_RADIO_OFF``\  when
done. When just initialized, a device should be left in RADIO
OFF state until user space devices to turn it on.

c. Query the device for the state of the hardware rfkill switch
and call \ :c:func:`wimax_rfkill_report_hw`\  and \ :c:func:`wimax_rfkill_report_sw`\ 
as needed. See below.

\ :c:func:`wimax_dev_rm`\  undoes before unregistering the network device. Once
\ :c:func:`wimax_dev_add`\  is called, the driver can get called on the
wimax_dev->op\_\* function pointers

.. _`wimax_dev.concurrency`:

CONCURRENCY
-----------


The stack provides a mutex for each device that will disallow API
calls happening concurrently; thus, op calls into the driver
through the wimax_dev->op\*() function pointers will always be
serialized and \*never\* concurrent.

For locking, take wimax_dev->mutex is taken; (most) operations in
the API have to check for \ :c:func:`wimax_dev_is_ready`\  to return 0 before
continuing (this is done internally).

.. _`wimax_dev.reference-counting`:

REFERENCE COUNTING
------------------


The WiMAX device is reference counted by the associated network
device. The only operation that can be used to reference the device
is \ :c:func:`wimax_dev_get_by_genl_info`\ , and the reference it acquires has
to be released with dev_put(wimax_dev->net_dev).

.. _`wimax_dev.rfkill`:

RFKILL
------


At startup, both HW and SW radio switchess are assumed to be off.

At initialization time [after calling \ :c:func:`wimax_dev_add`\ ], have the
driver query the device for the status of the software and hardware
RF kill switches and call \ :c:func:`wimax_report_rfkill_hw`\  and
\ :c:func:`wimax_rfkill_report_sw`\  to indicate their state. If any is
missing, just call it to indicate it is ON (radio always on).

Whenever the driver detects a change in the state of the RF kill
switches, it should call \ :c:func:`wimax_report_rfkill_hw`\  or
\ :c:func:`wimax_report_rfkill_sw`\  to report it to the stack.

.. This file was automatic generated / don't edit.


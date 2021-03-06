.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/cros_ec.h

.. _`cros_ec_command`:

struct cros_ec_command
======================

.. c:type:: struct cros_ec_command

    Information about a ChromeOS EC command.

.. _`cros_ec_command.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_command {
        uint32_t version;
        uint32_t command;
        uint32_t outsize;
        uint32_t insize;
        uint32_t result;
        uint8_t data[0];
    }

.. _`cros_ec_command.members`:

Members
-------

version
    Command version number (often 0).

command
    Command to send (EC_CMD_...).

outsize
    Outgoing length in bytes.

insize
    Max number of bytes to accept from the EC.

result
    EC's response to the command (separate from communication failure).

data
    Where to put the incoming data from EC and outgoing data to EC.

.. _`cros_ec_device`:

struct cros_ec_device
=====================

.. c:type:: struct cros_ec_device

    Information about a ChromeOS EC device.

.. _`cros_ec_device.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_device {
        const char *phys_name;
        struct device *dev;
        bool was_wake_device;
        struct class *cros_class;
        int (*cmd_readmem)(struct cros_ec_device *ec, unsigned int offset, unsigned int bytes, void *dest);
        u16 max_request;
        u16 max_response;
        u16 max_passthru;
        u16 proto_version;
        void *priv;
        int irq;
        u8 *din;
        u8 *dout;
        int din_size;
        int dout_size;
        bool wake_enabled;
        bool suspended;
        int (*cmd_xfer)(struct cros_ec_device *ec, struct cros_ec_command *msg);
        int (*pkt_xfer)(struct cros_ec_device *ec, struct cros_ec_command *msg);
        struct mutex lock;
        bool mkbp_event_supported;
        struct blocking_notifier_head event_notifier;
        struct ec_response_get_next_event_v1 event_data;
        int event_size;
        u32 host_event_wake_mask;
    }

.. _`cros_ec_device.members`:

Members
-------

phys_name
    Name of physical comms layer (e.g. 'i2c-4').

dev
    Device pointer for physical comms device

was_wake_device
    True if this device was set to wake the system from
    sleep at the last suspend.

cros_class
    The class structure for this device.

cmd_readmem
    Direct read of the EC memory-mapped region, if supported.

max_request
    Max size of message requested.

max_response
    Max size of message response.

max_passthru
    Max sice of passthru message.

proto_version
    The protocol version used for this device.

priv
    Private data.

irq
    Interrupt to use.

din
    Input buffer (for data from EC). This buffer will always be
    dword-aligned and include enough space for up to 7 word-alignment
    bytes also, so we can ensure that the body of the message is always
    dword-aligned (64-bit). We use this alignment to keep ARM and x86
    happy. Probably word alignment would be OK, there might be a small
    performance advantage to using dword.

dout
    Output buffer (for data to EC). This buffer will always be
    dword-aligned and include enough space for up to 7 word-alignment
    bytes also, so we can ensure that the body of the message is always
    dword-aligned (64-bit). We use this alignment to keep ARM and x86
    happy. Probably word alignment would be OK, there might be a small
    performance advantage to using dword.

din_size
    Size of din buffer to allocate (zero to use static din).

dout_size
    Size of dout buffer to allocate (zero to use static dout).

wake_enabled
    True if this device can wake the system from sleep.

suspended
    True if this device had been suspended.

cmd_xfer
    Send command to EC and get response.
    Returns the number of bytes received if the communication
    succeeded, but that doesn't mean the EC was happy with the
    command. The caller should check msg.result for the EC's result
    code.

pkt_xfer
    Send packet to EC and get response.

lock
    One transaction at a time.

mkbp_event_supported
    True if this EC supports the MKBP event protocol.

event_notifier
    Interrupt event notifier for transport devices.

event_data
    Raw payload transferred with the MKBP event.

event_size
    Size in bytes of the event data.

host_event_wake_mask
    Mask of host events that cause wake from suspend.

.. _`cros_ec_sensor_platform`:

struct cros_ec_sensor_platform
==============================

.. c:type:: struct cros_ec_sensor_platform

    ChromeOS EC sensor platform information.

.. _`cros_ec_sensor_platform.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_sensor_platform {
        u8 sensor_num;
    }

.. _`cros_ec_sensor_platform.members`:

Members
-------

sensor_num
    Id of the sensor, as reported by the EC.

.. _`cros_ec_platform`:

struct cros_ec_platform
=======================

.. c:type:: struct cros_ec_platform

    ChromeOS EC platform information.

.. _`cros_ec_platform.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_platform {
        const char *ec_name;
        u16 cmd_offset;
    }

.. _`cros_ec_platform.members`:

Members
-------

ec_name
    Name of EC device (e.g. 'cros-ec', 'cros-pd', ...)
    used in /dev/ and sysfs.

cmd_offset
    Offset to apply for each command. Set when
    registering a device behind another one.

.. _`cros_ec_dev`:

struct cros_ec_dev
==================

.. c:type:: struct cros_ec_dev

    ChromeOS EC device entry point.

.. _`cros_ec_dev.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_dev {
        struct device class_dev;
        struct cdev cdev;
        struct cros_ec_device *ec_dev;
        struct device *dev;
        struct cros_ec_debugfs *debug_info;
        bool has_kb_wake_angle;
        u16 cmd_offset;
        u32 features[2];
    }

.. _`cros_ec_dev.members`:

Members
-------

class_dev
    Device structure used in sysfs.

cdev
    Character device structure in /dev.

ec_dev
    cros_ec_device structure to talk to the physical device.

dev
    Pointer to the platform device.

debug_info
    cros_ec_debugfs structure for debugging information.

has_kb_wake_angle
    True if at least 2 accelerometer are connected to the EC.

cmd_offset
    Offset to apply for each command.

features
    Features supported by the EC.

.. _`cros_ec_suspend`:

cros_ec_suspend
===============

.. c:function:: int cros_ec_suspend(struct cros_ec_device *ec_dev)

    Handle a suspend operation for the ChromeOS EC device.

    :param ec_dev:
        Device to suspend.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_suspend.description`:

Description
-----------

This can be called by drivers to handle a suspend event.

.. _`cros_ec_suspend.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_resume`:

cros_ec_resume
==============

.. c:function:: int cros_ec_resume(struct cros_ec_device *ec_dev)

    Handle a resume operation for the ChromeOS EC device.

    :param ec_dev:
        Device to resume.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_resume.description`:

Description
-----------

This can be called by drivers to handle a resume event.

.. _`cros_ec_resume.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_prepare_tx`:

cros_ec_prepare_tx
==================

.. c:function:: int cros_ec_prepare_tx(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Prepare an outgoing message in the output buffer.

    :param ec_dev:
        Device to register.
    :type ec_dev: struct cros_ec_device \*

    :param msg:
        Message to write.
    :type msg: struct cros_ec_command \*

.. _`cros_ec_prepare_tx.description`:

Description
-----------

This is intended to be used by all ChromeOS EC drivers, but at present
only SPI uses it. Once LPC uses the same protocol it can start using it.
I2C could use it now, with a refactor of the existing code.

.. _`cros_ec_prepare_tx.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_check_result`:

cros_ec_check_result
====================

.. c:function:: int cros_ec_check_result(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Check ec_msg->result.

    :param ec_dev:
        EC device.
    :type ec_dev: struct cros_ec_device \*

    :param msg:
        Message to check.
    :type msg: struct cros_ec_command \*

.. _`cros_ec_check_result.description`:

Description
-----------

This is used by ChromeOS EC drivers to check the ec_msg->result for
errors and to warn about them.

.. _`cros_ec_check_result.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_cmd_xfer`:

cros_ec_cmd_xfer
================

.. c:function:: int cros_ec_cmd_xfer(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Send a command to the ChromeOS EC.

    :param ec_dev:
        EC device.
    :type ec_dev: struct cros_ec_device \*

    :param msg:
        Message to write.
    :type msg: struct cros_ec_command \*

.. _`cros_ec_cmd_xfer.description`:

Description
-----------

Call this to send a command to the ChromeOS EC.  This should be used
instead of calling the EC's \ :c:func:`cmd_xfer`\  callback directly.

.. _`cros_ec_cmd_xfer.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_cmd_xfer_status`:

cros_ec_cmd_xfer_status
=======================

.. c:function:: int cros_ec_cmd_xfer_status(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Send a command to the ChromeOS EC.

    :param ec_dev:
        EC device.
    :type ec_dev: struct cros_ec_device \*

    :param msg:
        Message to write.
    :type msg: struct cros_ec_command \*

.. _`cros_ec_cmd_xfer_status.description`:

Description
-----------

This function is identical to cros_ec_cmd_xfer, except it returns success
status only if both the command was transmitted successfully and the EC
replied with success status. It's not necessary to check msg->result when
using this function.

.. _`cros_ec_cmd_xfer_status.return`:

Return
------

The number of bytes transferred on success or negative error code.

.. _`cros_ec_remove`:

cros_ec_remove
==============

.. c:function:: int cros_ec_remove(struct cros_ec_device *ec_dev)

    Remove a ChromeOS EC.

    :param ec_dev:
        Device to register.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_remove.description`:

Description
-----------

Call this to deregister a ChromeOS EC, then clean up any private data.

.. _`cros_ec_remove.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_register`:

cros_ec_register
================

.. c:function:: int cros_ec_register(struct cros_ec_device *ec_dev)

    Register a new ChromeOS EC, using the provided info.

    :param ec_dev:
        Device to register.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_register.description`:

Description
-----------

Before calling this, allocate a pointer to a new device and then fill
in all the fields up to the --private-- marker.

.. _`cros_ec_register.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_query_all`:

cros_ec_query_all
=================

.. c:function:: int cros_ec_query_all(struct cros_ec_device *ec_dev)

    Query the protocol version supported by the ChromeOS EC.

    :param ec_dev:
        Device to register.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_query_all.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_get_next_event`:

cros_ec_get_next_event
======================

.. c:function:: int cros_ec_get_next_event(struct cros_ec_device *ec_dev, bool *wake_event)

    Fetch next event from the ChromeOS EC.

    :param ec_dev:
        Device to fetch event from.
    :type ec_dev: struct cros_ec_device \*

    :param wake_event:
        Pointer to a bool set to true upon return if the event might be
        treated as a wake event. Ignored if null.
    :type wake_event: bool \*

.. _`cros_ec_get_next_event.return`:

Return
------

0 on success or negative error code.

.. _`cros_ec_get_host_event`:

cros_ec_get_host_event
======================

.. c:function:: u32 cros_ec_get_host_event(struct cros_ec_device *ec_dev)

    Return a mask of event set by the ChromeOS EC.

    :param ec_dev:
        Device to fetch event from.
    :type ec_dev: struct cros_ec_device \*

.. _`cros_ec_get_host_event.description`:

Description
-----------

When MKBP is supported, when the EC raises an interrupt, we collect the
events raised and call the functions in the ec notifier. This function
is a helper to know which events are raised.

.. _`cros_ec_get_host_event.return`:

Return
------

0 on success or negative error code.

.. This file was automatic generated / don't edit.


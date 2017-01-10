.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/cros_ec.h

.. _`cros_ec_device`:

struct cros_ec_device
=====================

.. c:type:: struct cros_ec_device

    Information about a ChromeOS EC device

.. _`cros_ec_device.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_device {
        const char *phys_name;
        struct device *dev;
        bool was_wake_device;
        struct class *cros_class;
        int (*cmd_readmem)(struct cros_ec_device *ec, unsigned int offset,unsigned int bytes, void *dest);
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
        int (*cmd_xfer)(struct cros_ec_device *ec,struct cros_ec_command *msg);
        int (*pkt_xfer)(struct cros_ec_device *ec,struct cros_ec_command *msg);
        struct mutex lock;
        bool mkbp_event_supported;
        struct blocking_notifier_head event_notifier;
        struct ec_response_get_next_event event_data;
        int event_size;
    }

.. _`cros_ec_device.members`:

Members
-------

phys_name
    name of physical comms layer (e.g. 'i2c-4')

dev
    Device pointer for physical comms device

was_wake_device
    true if this device was set to wake the system from
    sleep at the last suspend

cros_class
    *undescribed*

cmd_readmem
    direct read of the EC memory-mapped region, if supported
    \ ``offset``\  is within EC_LPC_ADDR_MEMMAP region.

max_request
    *undescribed*

max_response
    *undescribed*

max_passthru
    *undescribed*

proto_version
    *undescribed*

priv
    Private data

irq
    Interrupt to use

din
    input buffer (for data from EC)

dout
    output buffer (for data to EC)
    \note
    These two buffers will always be dword-aligned and include enough
    space for up to 7 word-alignment bytes also, so we can ensure that
    the body of the message is always dword-aligned (64-bit).
    We use this alignment to keep ARM and x86 happy. Probably word
    alignment would be OK, there might be a small performance advantage
    to using dword.

din_size
    size of din buffer to allocate (zero to use static din)

dout_size
    size of dout buffer to allocate (zero to use static dout)

wake_enabled
    true if this device can wake the system from sleep

cmd_xfer
    send command to EC and get response
    Returns the number of bytes received if the communication succeeded, but
    that doesn't mean the EC was happy with the command. The caller
    should check msg.result for the EC's result code.

pkt_xfer
    send packet to EC and get response

lock
    one transaction at a time

mkbp_event_supported
    true if this EC supports the MKBP event protocol.

event_notifier
    interrupt event notifier for transport devices.

event_data
    raw payload transferred with the MKBP event.

event_size
    size in bytes of the event data.

.. _`cros_ec_sensor_platform`:

struct cros_ec_sensor_platform
==============================

.. c:type:: struct cros_ec_sensor_platform

    ChromeOS EC sensor platform information

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

.. _`cros_ec_suspend`:

cros_ec_suspend
===============

.. c:function:: int cros_ec_suspend(struct cros_ec_device *ec_dev)

    Handle a suspend operation for the ChromeOS EC device

    :param struct cros_ec_device \*ec_dev:
        *undescribed*

.. _`cros_ec_suspend.description`:

Description
-----------

This can be called by drivers to handle a suspend event.

.. _`cros_ec_suspend.ec_dev`:

ec_dev
------

Device to suspend
\ ``return``\  0 if ok, -ve on error

.. _`cros_ec_resume`:

cros_ec_resume
==============

.. c:function:: int cros_ec_resume(struct cros_ec_device *ec_dev)

    Handle a resume operation for the ChromeOS EC device

    :param struct cros_ec_device \*ec_dev:
        Device to resume
        \ ``return``\  0 if ok, -ve on error

.. _`cros_ec_resume.description`:

Description
-----------

This can be called by drivers to handle a resume event.

.. _`cros_ec_prepare_tx`:

cros_ec_prepare_tx
==================

.. c:function:: int cros_ec_prepare_tx(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Prepare an outgoing message in the output buffer

    :param struct cros_ec_device \*ec_dev:
        Device to register

    :param struct cros_ec_command \*msg:
        Message to write

.. _`cros_ec_prepare_tx.description`:

Description
-----------

This is intended to be used by all ChromeOS EC drivers, but at present
only SPI uses it. Once LPC uses the same protocol it can start using it.
I2C could use it now, with a refactor of the existing code.

.. _`cros_ec_check_result`:

cros_ec_check_result
====================

.. c:function:: int cros_ec_check_result(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Check ec_msg->result

    :param struct cros_ec_device \*ec_dev:
        EC device

    :param struct cros_ec_command \*msg:
        Message to check

.. _`cros_ec_check_result.description`:

Description
-----------

This is used by ChromeOS EC drivers to check the ec_msg->result for
errors and to warn about them.

.. _`cros_ec_cmd_xfer`:

cros_ec_cmd_xfer
================

.. c:function:: int cros_ec_cmd_xfer(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Send a command to the ChromeOS EC

    :param struct cros_ec_device \*ec_dev:
        EC device

    :param struct cros_ec_command \*msg:
        Message to write

.. _`cros_ec_cmd_xfer.description`:

Description
-----------

Call this to send a command to the ChromeOS EC.  This should be used
instead of calling the EC's \ :c:func:`cmd_xfer`\  callback directly.

.. _`cros_ec_cmd_xfer_status`:

cros_ec_cmd_xfer_status
=======================

.. c:function:: int cros_ec_cmd_xfer_status(struct cros_ec_device *ec_dev, struct cros_ec_command *msg)

    Send a command to the ChromeOS EC

    :param struct cros_ec_device \*ec_dev:
        EC device

    :param struct cros_ec_command \*msg:
        Message to write

.. _`cros_ec_cmd_xfer_status.description`:

Description
-----------

This function is identical to cros_ec_cmd_xfer, except it returns success
status only if both the command was transmitted successfully and the EC
replied with success status. It's not necessary to check msg->result when
using this function.

.. _`cros_ec_remove`:

cros_ec_remove
==============

.. c:function:: int cros_ec_remove(struct cros_ec_device *ec_dev)

    Remove a ChromeOS EC

    :param struct cros_ec_device \*ec_dev:
        Device to register
        \ ``return``\  0 if ok, -ve on error

.. _`cros_ec_remove.description`:

Description
-----------

Call this to deregister a ChromeOS EC, then clean up any private data.

.. _`cros_ec_register`:

cros_ec_register
================

.. c:function:: int cros_ec_register(struct cros_ec_device *ec_dev)

    Register a new ChromeOS EC, using the provided info

    :param struct cros_ec_device \*ec_dev:
        Device to register
        \ ``return``\  0 if ok, -ve on error

.. _`cros_ec_register.description`:

Description
-----------

Before calling this, allocate a pointer to a new device and then fill
in all the fields up to the --private-- marker.

.. _`cros_ec_query_all`:

cros_ec_query_all
=================

.. c:function:: int cros_ec_query_all(struct cros_ec_device *ec_dev)

    Query the protocol version supported by the ChromeOS EC

    :param struct cros_ec_device \*ec_dev:
        Device to register
        \ ``return``\  0 if ok, -ve on error

.. _`cros_ec_get_next_event`:

cros_ec_get_next_event
======================

.. c:function:: int cros_ec_get_next_event(struct cros_ec_device *ec_dev)

    Fetch next event from the ChromeOS EC

    :param struct cros_ec_device \*ec_dev:
        Device to fetch event from

.. _`cros_ec_get_next_event.return`:

Return
------

0 on success, Linux error number on failure

.. This file was automatic generated / don't edit.


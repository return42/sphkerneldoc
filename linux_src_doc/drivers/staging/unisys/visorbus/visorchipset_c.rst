.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/visorchipset.c

.. _`initialize_controlvm_payload_info`:

initialize_controlvm_payload_info
=================================

.. c:function:: int initialize_controlvm_payload_info(u64 phys_addr, u64 offset, u32 bytes, struct visor_controlvm_payload_info *info)

    init controlvm_payload_info struct

    :param u64 phys_addr:
        the physical address of controlvm channel

    :param u64 offset:
        the offset to payload

    :param u32 bytes:
        the size of the payload in bytes

    :param struct visor_controlvm_payload_info \*info:
        the returning valid struct

.. _`initialize_controlvm_payload_info.description`:

Description
-----------

When provided with the physical address of the controlvm channel
(phys_addr), the offset to the payload area we need to manage
(offset), and the size of this payload area (bytes), fills in the
controlvm_payload_info struct.

.. _`initialize_controlvm_payload_info.return`:

Return
------

CONTROLVM_RESP_SUCCESS for success or a negative for failure

.. _`parahotplug_next_id`:

parahotplug_next_id
===================

.. c:function:: int parahotplug_next_id( void)

    generate unique int to match an outstanding CONTROLVM message with a udev script /proc response

    :param  void:
        no arguments

.. _`parahotplug_next_id.return`:

Return
------

a unique integer value

.. _`parahotplug_next_expiration`:

parahotplug_next_expiration
===========================

.. c:function:: unsigned long parahotplug_next_expiration( void)

    returns the time (in jiffies) when a CONTROLVM message on the list should expire -- PARAHOTPLUG_TIMEOUT_MS in the future

    :param  void:
        no arguments

.. _`parahotplug_next_expiration.return`:

Return
------

expected expiration time (in jiffies)

.. _`parahotplug_request_create`:

parahotplug_request_create
==========================

.. c:function:: struct parahotplug_request *parahotplug_request_create(struct controlvm_message *msg)

    create a parahotplug_request, which is basically a wrapper for a CONTROLVM_MESSAGE that we can stick on a list

    :param struct controlvm_message \*msg:
        the message to insert in the request

.. _`parahotplug_request_create.return`:

Return
------

the request containing the provided message

.. _`parahotplug_request_destroy`:

parahotplug_request_destroy
===========================

.. c:function:: void parahotplug_request_destroy(struct parahotplug_request *req)

    free a parahotplug_request

    :param struct parahotplug_request \*req:
        the request to deallocate

.. _`parahotplug_request_complete`:

parahotplug_request_complete
============================

.. c:function:: int parahotplug_request_complete(int id, u16 active)

    mark request as complete

    :param int id:
        the id of the request

    :param u16 active:
        indicates whether the request is assigned to active partition

.. _`parahotplug_request_complete.description`:

Description
-----------

Called from the /proc handler, which means the user script has
finished the enable/disable. Find the matching identifier, and
respond to the CONTROLVM message with success.

.. _`parahotplug_request_complete.return`:

Return
------

0 on success or -EINVAL on failure

.. _`devicedisabled_store`:

devicedisabled_store
====================

.. c:function:: ssize_t devicedisabled_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    disables the hotplug device

    :param struct device \*dev:
        sysfs interface variable not utilized in this function

    :param struct device_attribute \*attr:
        sysfs interface variable not utilized in this function

    :param const char \*buf:
        buffer containing the device id

    :param size_t count:
        the size of the buffer

.. _`devicedisabled_store.description`:

Description
-----------

The parahotplug/devicedisabled interface gets called by our support script
when an SR-IOV device has been shut down. The ID is passed to the script
and then passed back when the device has been removed.

.. _`devicedisabled_store.return`:

Return
------

the size of the buffer for success or negative for error

.. _`deviceenabled_store`:

deviceenabled_store
===================

.. c:function:: ssize_t deviceenabled_store(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)

    enables the hotplug device

    :param struct device \*dev:
        sysfs interface variable not utilized in this function

    :param struct device_attribute \*attr:
        sysfs interface variable not utilized in this function

    :param const char \*buf:
        buffer containing the device id

    :param size_t count:
        the size of the buffer

.. _`deviceenabled_store.description`:

Description
-----------

The parahotplug/deviceenabled interface gets called by our support script
when an SR-IOV device has been recovered. The ID is passed to the script
and then passed back when the device has been brought back up.

.. _`deviceenabled_store.return`:

Return
------

the size of the buffer for success or negative for error

.. _`parahotplug_request_kickoff`:

parahotplug_request_kickoff
===========================

.. c:function:: void parahotplug_request_kickoff(struct parahotplug_request *req)

    initiate parahotplug request

    :param struct parahotplug_request \*req:
        the request to initiate

.. _`parahotplug_request_kickoff.description`:

Description
-----------

Cause uevent to run the user level script to do the disable/enable specified
in the parahotplug_request.

.. _`parahotplug_process_message`:

parahotplug_process_message
===========================

.. c:function:: void parahotplug_process_message(struct controlvm_message *inmsg)

    enables or disables a PCI device by kicking off a udev script

    :param struct controlvm_message \*inmsg:
        the message indicating whether to enable or disable

.. _`visorchipset_chipset_ready`:

visorchipset_chipset_ready
==========================

.. c:function:: int visorchipset_chipset_ready( void)

    sends chipset_ready action

    :param  void:
        no arguments

.. _`visorchipset_chipset_ready.description`:

Description
-----------

Send ACTION=online for DEVPATH=/sys/devices/platform/visorchipset.

.. _`visorchipset_chipset_ready.return`:

Return
------

CONTROLVM_RESP_SUCCESS

.. _`visorchipset_chipset_notready`:

visorchipset_chipset_notready
=============================

.. c:function:: int visorchipset_chipset_notready( void)

    sends chipset_notready action

    :param  void:
        no arguments

.. _`visorchipset_chipset_notready.description`:

Description
-----------

Send ACTION=offline for DEVPATH=/sys/devices/platform/visorchipset.

.. _`visorchipset_chipset_notready.return`:

Return
------

CONTROLVM_RESP_SUCCESS

.. _`handle_command`:

handle_command
==============

.. c:function:: bool handle_command(struct controlvm_message inmsg, u64 channel_addr)

    process a controlvm message

    :param struct controlvm_message inmsg:
        the message to process

    :param u64 channel_addr:
        address of the controlvm channel

.. _`handle_command.return`:

Return
------

false - this function will return false only in the case where the
controlvm message was NOT processed, but processing must be
retried before reading the next controlvm message; a
scenario where this can occur is when we need to throttle
the allocation of memory in which to copy out controlvm
payload data
true  - processing of the controlvm message completed,
either successfully or with an error

.. _`read_controlvm_event`:

read_controlvm_event
====================

.. c:function:: bool read_controlvm_event(struct controlvm_message *msg)

    retreives the next message from the CONTROLVM_QUEUE_EVENT queue in the controlvm channel

    :param struct controlvm_message \*msg:
        pointer to the retrieved message

.. _`read_controlvm_event.return`:

Return
------

true if a valid message was retrieved or false otherwise

.. _`parahotplug_process_list`:

parahotplug_process_list
========================

.. c:function:: void parahotplug_process_list( void)

    remove any request from the list that's been on there too long and respond with an error

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


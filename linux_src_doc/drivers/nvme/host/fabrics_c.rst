.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvme/host/fabrics.c

.. _`nvmf_get_address`:

nvmf_get_address
================

.. c:function:: int nvmf_get_address(struct nvme_ctrl *ctrl, char *buf, int size)

    Get address/port

    :param struct nvme_ctrl \*ctrl:
        Host NVMe controller instance which we got the address

    :param char \*buf:
        OUTPUT parameter that will contain the address/port

    :param int size:
        buffer size

.. _`nvmf_get_subsysnqn`:

nvmf_get_subsysnqn
==================

.. c:function:: const char *nvmf_get_subsysnqn(struct nvme_ctrl *ctrl)

    Get subsystem NQN

    :param struct nvme_ctrl \*ctrl:
        Host NVMe controller instance which we got the NQN

.. _`nvmf_reg_read32`:

nvmf_reg_read32
===============

.. c:function:: int nvmf_reg_read32(struct nvme_ctrl *ctrl, u32 off, u32 *val)

    NVMe Fabrics "Property Get" API function.

    :param struct nvme_ctrl \*ctrl:
        Host NVMe controller instance maintaining the admin
        queue used to submit the property read command to
        the allocated NVMe controller resource on the target system.

    :param u32 off:
        Starting offset value of the targeted property
        register (see the fabrics section of the NVMe standard).

    :param u32 \*val:
        OUTPUT parameter that will contain the value of
        the property after a successful read.

.. _`nvmf_reg_read32.description`:

Description
-----------

Used by the host system to retrieve a 32-bit capsule property value
from an NVMe controller on the target system.

("Capsule property" is an "PCIe register concept" applied to the
NVMe fabrics space.)

.. _`nvmf_reg_read32.return`:

Return
------

0: successful read
> 0: NVMe error status code
< 0: Linux errno error code

.. _`nvmf_reg_read64`:

nvmf_reg_read64
===============

.. c:function:: int nvmf_reg_read64(struct nvme_ctrl *ctrl, u32 off, u64 *val)

    NVMe Fabrics "Property Get" API function.

    :param struct nvme_ctrl \*ctrl:
        Host NVMe controller instance maintaining the admin
        queue used to submit the property read command to
        the allocated controller resource on the target system.

    :param u32 off:
        Starting offset value of the targeted property
        register (see the fabrics section of the NVMe standard).

    :param u64 \*val:
        OUTPUT parameter that will contain the value of
        the property after a successful read.

.. _`nvmf_reg_read64.description`:

Description
-----------

Used by the host system to retrieve a 64-bit capsule property value
from an NVMe controller on the target system.

("Capsule property" is an "PCIe register concept" applied to the
NVMe fabrics space.)

.. _`nvmf_reg_read64.return`:

Return
------

0: successful read
> 0: NVMe error status code
< 0: Linux errno error code

.. _`nvmf_reg_write32`:

nvmf_reg_write32
================

.. c:function:: int nvmf_reg_write32(struct nvme_ctrl *ctrl, u32 off, u32 val)

    NVMe Fabrics "Property Write" API function.

    :param struct nvme_ctrl \*ctrl:
        Host NVMe controller instance maintaining the admin
        queue used to submit the property read command to
        the allocated NVMe controller resource on the target system.

    :param u32 off:
        Starting offset value of the targeted property
        register (see the fabrics section of the NVMe standard).

    :param u32 val:
        Input parameter that contains the value to be
        written to the property.

.. _`nvmf_reg_write32.description`:

Description
-----------

Used by the NVMe host system to write a 32-bit capsule property value
to an NVMe controller on the target system.

("Capsule property" is an "PCIe register concept" applied to the
NVMe fabrics space.)

.. _`nvmf_reg_write32.return`:

Return
------

0: successful write
> 0: NVMe error status code
< 0: Linux errno error code

.. _`nvmf_log_connect_error`:

nvmf_log_connect_error
======================

.. c:function:: void nvmf_log_connect_error(struct nvme_ctrl *ctrl, int errval, int offset, struct nvme_command *cmd, struct nvmf_connect_data *data)

    Error-parsing-diagnostic print out function for \ :c:func:`connect`\  errors.

    :param struct nvme_ctrl \*ctrl:
        the specific /dev/nvmeX device that had the error.

    :param int errval:
        Error code to be decoded in a more human-friendly
        printout.

    :param int offset:
        For use with the NVMe error code NVME_SC_CONNECT_INVALID_PARAM.

    :param struct nvme_command \*cmd:
        This is the SQE portion of a submission capsule.

    :param struct nvmf_connect_data \*data:
        This is the "Data" portion of a submission capsule.

.. _`nvmf_connect_admin_queue`:

nvmf_connect_admin_queue
========================

.. c:function:: int nvmf_connect_admin_queue(struct nvme_ctrl *ctrl)

    NVMe Fabrics Admin Queue "Connect" API function.

    :param struct nvme_ctrl \*ctrl:
        Host nvme controller instance used to request
        a new NVMe controller allocation on the target
        system and  establish an NVMe Admin connection to
        that controller.

.. _`nvmf_connect_admin_queue.description`:

Description
-----------

This function enables an NVMe host device to request a new allocation of
an NVMe controller resource on a target system as well establish a
fabrics-protocol connection of the NVMe Admin queue between the
host system device and the allocated NVMe controller on the
target system via a NVMe Fabrics "Connect" command.

.. _`nvmf_connect_admin_queue.return`:

Return
------

0: success
> 0: NVMe error status code
< 0: Linux errno error code

.. _`nvmf_connect_io_queue`:

nvmf_connect_io_queue
=====================

.. c:function:: int nvmf_connect_io_queue(struct nvme_ctrl *ctrl, u16 qid)

    NVMe Fabrics I/O Queue "Connect" API function.

    :param struct nvme_ctrl \*ctrl:
        Host nvme controller instance used to establish an
        NVMe I/O queue connection to the already allocated NVMe
        controller on the target system.

    :param u16 qid:
        NVMe I/O queue number for the new I/O connection between
        host and target (note qid == 0 is illegal as this is
        the Admin queue, per NVMe standard).

.. _`nvmf_connect_io_queue.description`:

Description
-----------

This function issues a fabrics-protocol connection
of a NVMe I/O queue (via NVMe Fabrics "Connect" command)
between the host system device and the allocated NVMe controller
on the target system.

.. _`nvmf_connect_io_queue.return`:

Return
------

0: success
> 0: NVMe error status code
< 0: Linux errno error code

.. _`nvmf_register_transport`:

nvmf_register_transport
=======================

.. c:function:: void nvmf_register_transport(struct nvmf_transport_ops *ops)

    NVMe Fabrics Library registration function.

    :param struct nvmf_transport_ops \*ops:
        Transport ops instance to be registered to the
        common fabrics library.

.. _`nvmf_register_transport.description`:

Description
-----------

API function that registers the type of specific transport fabric
being implemented to the common NVMe fabrics library. Part of
the overall init sequence of starting up a fabrics driver.

.. _`nvmf_unregister_transport`:

nvmf_unregister_transport
=========================

.. c:function:: void nvmf_unregister_transport(struct nvmf_transport_ops *ops)

    NVMe Fabrics Library unregistration function.

    :param struct nvmf_transport_ops \*ops:
        Transport ops instance to be unregistered from the
        common fabrics library.

.. _`nvmf_unregister_transport.description`:

Description
-----------

Fabrics API function that unregisters the type of specific transport
fabric being implemented from the common NVMe fabrics library.
Part of the overall exit sequence of unloading the implemented driver.

.. This file was automatic generated / don't edit.


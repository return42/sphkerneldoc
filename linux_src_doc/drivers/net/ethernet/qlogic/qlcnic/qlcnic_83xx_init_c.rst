.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qlogic/qlcnic/qlcnic_83xx_init.c

.. _`qlcnic_83xx_idc_check_reset_ack_reg`:

qlcnic_83xx_idc_check_reset_ack_reg
===================================

.. c:function:: int qlcnic_83xx_idc_check_reset_ack_reg(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_check_reset_ack_reg.description`:

Description
-----------

Check ACK wait limit and clear the functions which failed to ACK

Return 0 if all functions have acknowledged the reset request.

.. _`qlcnic_83xx_idc_tx_soft_reset`:

qlcnic_83xx_idc_tx_soft_reset
=============================

.. c:function:: int qlcnic_83xx_idc_tx_soft_reset(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_tx_soft_reset.description`:

Description
-----------

Handle context deletion and recreation request from transmit routine

Returns -EBUSY  or Success (0)

.. _`qlcnic_83xx_idc_detach_driver`:

qlcnic_83xx_idc_detach_driver
=============================

.. c:function:: void qlcnic_83xx_idc_detach_driver(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
        Detach net interface, stop TX and cleanup resources before the HW reset.
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_detach_driver.return`:

Return
------

None

.. _`qlcnic_83xx_idc_attach_driver`:

qlcnic_83xx_idc_attach_driver
=============================

.. c:function:: void qlcnic_83xx_idc_attach_driver(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_attach_driver.description`:

Description
-----------

Re-attach and re-enable net interface

.. _`qlcnic_83xx_idc_attach_driver.return`:

Return
------

None

.. _`qlcnic_83xx_idc_find_reset_owner_id`:

qlcnic_83xx_idc_find_reset_owner_id
===================================

.. c:function:: int qlcnic_83xx_idc_find_reset_owner_id(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_find_reset_owner_id.description`:

Description
-----------

NIC gets precedence over ISCSI and ISCSI has precedence over FCOE.
Within the same class, function with lowest PCI ID assumes ownership

.. _`qlcnic_83xx_idc_find_reset_owner_id.return`:

Return
------

reset owner id or failure indication (-EIO)

.. _`qlcnic_83xx_idc_ready_state_entry`:

qlcnic_83xx_idc_ready_state_entry
=================================

.. c:function:: int qlcnic_83xx_idc_ready_state_entry(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_ready_state_entry.description`:

Description
-----------

Perform ready state initialization, this routine will get invoked only
once from READY state.

.. _`qlcnic_83xx_idc_ready_state_entry.return`:

Return
------

Error code or Success(0)

.. _`qlcnic_83xx_idc_vnic_pf_entry`:

qlcnic_83xx_idc_vnic_pf_entry
=============================

.. c:function:: int qlcnic_83xx_idc_vnic_pf_entry(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_vnic_pf_entry.description`:

Description
-----------

Ensure vNIC mode privileged function starts only after vNIC mode is
enabled by management function.
If vNIC mode is ready, start initialization.

.. _`qlcnic_83xx_idc_vnic_pf_entry.return`:

Return
------

-EIO or 0

.. _`qlcnic_83xx_idc_cold_state_handler`:

qlcnic_83xx_idc_cold_state_handler
==================================

.. c:function:: int qlcnic_83xx_idc_cold_state_handler(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_cold_state_handler.description`:

Description
-----------

If HW is up and running device will enter READY state.
If firmware image from host needs to be loaded, device is
forced to start with the file firmware image.

.. _`qlcnic_83xx_idc_cold_state_handler.return`:

Return
------

Error code or Success(0)

.. _`qlcnic_83xx_idc_init_state`:

qlcnic_83xx_idc_init_state
==========================

.. c:function:: int qlcnic_83xx_idc_init_state(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_init_state.description`:

Description
-----------

Reset owner will restart the device from this state.
Device will enter failed state if it remains
in this state for more than DEV_INIT time limit.

.. _`qlcnic_83xx_idc_init_state.return`:

Return
------

Error code or Success(0)

.. _`qlcnic_83xx_idc_ready_state`:

qlcnic_83xx_idc_ready_state
===========================

.. c:function:: int qlcnic_83xx_idc_ready_state(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_ready_state.description`:

Description
-----------

Perform IDC protocol specicifed actions after monitoring device state and
events.

.. _`qlcnic_83xx_idc_ready_state.return`:

Return
------

Error code or Success(0)

.. _`qlcnic_83xx_idc_need_reset_state`:

qlcnic_83xx_idc_need_reset_state
================================

.. c:function:: int qlcnic_83xx_idc_need_reset_state(struct qlcnic_adapter *adapter)

    :param adapter:
        adapter structure
    :type adapter: struct qlcnic_adapter \*

.. _`qlcnic_83xx_idc_need_reset_state.device-will-remain-in-this-state-until`:

Device will remain in this state until
--------------------------------------

Reset request ACK's are received from all the functions
Wait time exceeds max time limit

.. _`qlcnic_83xx_idc_need_reset_state.return`:

Return
------

Error code or Success(0)

.. _`qlcnic_83xx_idc_poll_dev_state`:

qlcnic_83xx_idc_poll_dev_state
==============================

.. c:function:: void qlcnic_83xx_idc_poll_dev_state(struct work_struct *work)

    :param work:
        kernel work queue structure used to schedule the function
    :type work: struct work_struct \*

.. _`qlcnic_83xx_idc_poll_dev_state.description`:

Description
-----------

Poll device state periodically and perform state specific
actions defined by Inter Driver Communication (IDC) protocol.

.. _`qlcnic_83xx_idc_poll_dev_state.return`:

Return
------

None

.. _`qlcnic_83xx_exec_template_cmd`:

qlcnic_83xx_exec_template_cmd
=============================

.. c:function:: void qlcnic_83xx_exec_template_cmd(struct qlcnic_adapter *p_dev, char *p_buff)

    :param p_dev:
        adapter structure
    :type p_dev: struct qlcnic_adapter \*

    :param p_buff:
        Poiter to instruction template
    :type p_buff: char \*

.. _`qlcnic_83xx_exec_template_cmd.description`:

Description
-----------

Template provides instructions to stop, restart and initalize firmware.
These instructions are abstracted as a series of read, write and
poll operations on hardware registers. Register information and operation
specifics are not exposed to the driver. Driver reads the template from
flash and executes the instructions located at pre-defined offsets.

.. _`qlcnic_83xx_exec_template_cmd.return`:

Return
------

None

.. This file was automatic generated / don't edit.


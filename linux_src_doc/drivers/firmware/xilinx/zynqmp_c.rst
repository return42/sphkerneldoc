.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/firmware/xilinx/zynqmp.c

.. _`zynqmp_pm_ret_code`:

zynqmp_pm_ret_code
==================

.. c:function:: int zynqmp_pm_ret_code(u32 ret_status)

    Convert PMU-FW error codes to Linux error codes

    :param ret_status:
        PMUFW return code
    :type ret_status: u32

.. _`zynqmp_pm_ret_code.return`:

Return
------

corresponding Linux error code

.. _`do_fw_call_smc`:

do_fw_call_smc
==============

.. c:function:: int do_fw_call_smc(u64 arg0, u64 arg1, u64 arg2, u32 *ret_payload)

    Call system-level platform management layer (SMC)

    :param arg0:
        Argument 0 to SMC call
    :type arg0: u64

    :param arg1:
        Argument 1 to SMC call
    :type arg1: u64

    :param arg2:
        Argument 2 to SMC call
    :type arg2: u64

    :param ret_payload:
        Returned value array
    :type ret_payload: u32 \*

.. _`do_fw_call_smc.description`:

Description
-----------

Invoke platform management function via SMC call (no hypervisor present).

.. _`do_fw_call_smc.return`:

Return
------

Returns status, either success or error+reason

.. _`do_fw_call_hvc`:

do_fw_call_hvc
==============

.. c:function:: int do_fw_call_hvc(u64 arg0, u64 arg1, u64 arg2, u32 *ret_payload)

    Call system-level platform management layer (HVC)

    :param arg0:
        Argument 0 to HVC call
    :type arg0: u64

    :param arg1:
        Argument 1 to HVC call
    :type arg1: u64

    :param arg2:
        Argument 2 to HVC call
    :type arg2: u64

    :param ret_payload:
        Returned value array
    :type ret_payload: u32 \*

.. _`do_fw_call_hvc.description`:

Description
-----------

Invoke platform management function via HVC
HVC-based for communication through hypervisor
(no direct communication with ATF).

.. _`do_fw_call_hvc.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_invoke_fn`:

zynqmp_pm_invoke_fn
===================

.. c:function:: int zynqmp_pm_invoke_fn(u32 pm_api_id, u32 arg0, u32 arg1, u32 arg2, u32 arg3, u32 *ret_payload)

    Invoke the system-level platform management layer caller function depending on the configuration

    :param pm_api_id:
        Requested PM-API call
    :type pm_api_id: u32

    :param arg0:
        Argument 0 to requested PM-API call
    :type arg0: u32

    :param arg1:
        Argument 1 to requested PM-API call
    :type arg1: u32

    :param arg2:
        Argument 2 to requested PM-API call
    :type arg2: u32

    :param arg3:
        Argument 3 to requested PM-API call
    :type arg3: u32

    :param ret_payload:
        Returned value array
    :type ret_payload: u32 \*

.. _`zynqmp_pm_invoke_fn.description`:

Description
-----------

Invoke platform management function for SMC or HVC call, depending on
configuration.
Following SMC Calling Convention (SMCCC) for SMC64:
Pm Function Identifier,
PM_SIP_SVC + PM_API_ID =
((SMC_TYPE_FAST << FUNCID_TYPE_SHIFT)
((SMC_64) << FUNCID_CC_SHIFT)
((SIP_START) << FUNCID_OEN_SHIFT)
((PM_API_ID) & FUNCID_NUM_MASK))

PM_SIP_SVC   - Registered ZynqMP SIP Service Call.
PM_API_ID    - Platform Management API ID.

.. _`zynqmp_pm_invoke_fn.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_get_api_version`:

zynqmp_pm_get_api_version
=========================

.. c:function:: int zynqmp_pm_get_api_version(u32 *version)

    Get version number of PMU PM firmware

    :param version:
        Returned version value
    :type version: u32 \*

.. _`zynqmp_pm_get_api_version.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_get_trustzone_version`:

zynqmp_pm_get_trustzone_version
===============================

.. c:function:: int zynqmp_pm_get_trustzone_version(u32 *version)

    Get secure trustzone firmware version

    :param version:
        Returned version value
    :type version: u32 \*

.. _`zynqmp_pm_get_trustzone_version.return`:

Return
------

Returns status, either success or error+reason

.. _`get_set_conduit_method`:

get_set_conduit_method
======================

.. c:function:: int get_set_conduit_method(struct device_node *np)

    Choose SMC or HVC based communication

    :param np:
        Pointer to the device_node structure
    :type np: struct device_node \*

.. _`get_set_conduit_method.description`:

Description
-----------

Use SMC or HVC-based functions to communicate with EL2/EL3.

.. _`get_set_conduit_method.return`:

Return
------

Returns 0 on success or error code

.. _`zynqmp_pm_query_data`:

zynqmp_pm_query_data
====================

.. c:function:: int zynqmp_pm_query_data(struct zynqmp_pm_query_data qdata, u32 *out)

    Get query data from firmware

    :param qdata:
        Variable to the zynqmp_pm_query_data structure
    :type qdata: struct zynqmp_pm_query_data

    :param out:
        Returned output value
    :type out: u32 \*

.. _`zynqmp_pm_query_data.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_enable`:

zynqmp_pm_clock_enable
======================

.. c:function:: int zynqmp_pm_clock_enable(u32 clock_id)

    Enable the clock for given id

    :param clock_id:
        ID of the clock to be enabled
    :type clock_id: u32

.. _`zynqmp_pm_clock_enable.description`:

Description
-----------

This function is used by master to enable the clock
including peripherals and PLL clocks.

.. _`zynqmp_pm_clock_enable.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_disable`:

zynqmp_pm_clock_disable
=======================

.. c:function:: int zynqmp_pm_clock_disable(u32 clock_id)

    Disable the clock for given id

    :param clock_id:
        ID of the clock to be disable
    :type clock_id: u32

.. _`zynqmp_pm_clock_disable.description`:

Description
-----------

This function is used by master to disable the clock
including peripherals and PLL clocks.

.. _`zynqmp_pm_clock_disable.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_getstate`:

zynqmp_pm_clock_getstate
========================

.. c:function:: int zynqmp_pm_clock_getstate(u32 clock_id, u32 *state)

    Get the clock state for given id

    :param clock_id:
        ID of the clock to be queried
    :type clock_id: u32

    :param state:
        1/0 (Enabled/Disabled)
    :type state: u32 \*

.. _`zynqmp_pm_clock_getstate.description`:

Description
-----------

This function is used by master to get the state of clock
including peripherals and PLL clocks.

.. _`zynqmp_pm_clock_getstate.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_setdivider`:

zynqmp_pm_clock_setdivider
==========================

.. c:function:: int zynqmp_pm_clock_setdivider(u32 clock_id, u32 divider)

    Set the clock divider for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param divider:
        divider value
    :type divider: u32

.. _`zynqmp_pm_clock_setdivider.description`:

Description
-----------

This function is used by master to set divider for any clock
to achieve desired rate.

.. _`zynqmp_pm_clock_setdivider.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_getdivider`:

zynqmp_pm_clock_getdivider
==========================

.. c:function:: int zynqmp_pm_clock_getdivider(u32 clock_id, u32 *divider)

    Get the clock divider for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param divider:
        divider value
    :type divider: u32 \*

.. _`zynqmp_pm_clock_getdivider.description`:

Description
-----------

This function is used by master to get divider values
for any clock.

.. _`zynqmp_pm_clock_getdivider.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_setrate`:

zynqmp_pm_clock_setrate
=======================

.. c:function:: int zynqmp_pm_clock_setrate(u32 clock_id, u64 rate)

    Set the clock rate for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param rate:
        rate value in hz
    :type rate: u64

.. _`zynqmp_pm_clock_setrate.description`:

Description
-----------

This function is used by master to set rate for any clock.

.. _`zynqmp_pm_clock_setrate.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_getrate`:

zynqmp_pm_clock_getrate
=======================

.. c:function:: int zynqmp_pm_clock_getrate(u32 clock_id, u64 *rate)

    Get the clock rate for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param rate:
        rate value in hz
    :type rate: u64 \*

.. _`zynqmp_pm_clock_getrate.description`:

Description
-----------

This function is used by master to get rate
for any clock.

.. _`zynqmp_pm_clock_getrate.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_setparent`:

zynqmp_pm_clock_setparent
=========================

.. c:function:: int zynqmp_pm_clock_setparent(u32 clock_id, u32 parent_id)

    Set the clock parent for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param parent_id:
        parent id
    :type parent_id: u32

.. _`zynqmp_pm_clock_setparent.description`:

Description
-----------

This function is used by master to set parent for any clock.

.. _`zynqmp_pm_clock_setparent.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_clock_getparent`:

zynqmp_pm_clock_getparent
=========================

.. c:function:: int zynqmp_pm_clock_getparent(u32 clock_id, u32 *parent_id)

    Get the clock parent for given id

    :param clock_id:
        ID of the clock
    :type clock_id: u32

    :param parent_id:
        parent id
    :type parent_id: u32 \*

.. _`zynqmp_pm_clock_getparent.description`:

Description
-----------

This function is used by master to get parent index
for any clock.

.. _`zynqmp_pm_clock_getparent.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_is_valid_ioctl`:

zynqmp_is_valid_ioctl
=====================

.. c:function:: int zynqmp_is_valid_ioctl(u32 ioctl_id)

    Check whether IOCTL ID is valid or not

    :param ioctl_id:
        IOCTL ID
    :type ioctl_id: u32

.. _`zynqmp_is_valid_ioctl.return`:

Return
------

1 if IOCTL is valid else 0

.. _`zynqmp_pm_ioctl`:

zynqmp_pm_ioctl
===============

.. c:function:: int zynqmp_pm_ioctl(u32 node_id, u32 ioctl_id, u32 arg1, u32 arg2, u32 *out)

    PM IOCTL API for device control and configs

    :param node_id:
        Node ID of the device
    :type node_id: u32

    :param ioctl_id:
        ID of the requested IOCTL
    :type ioctl_id: u32

    :param arg1:
        Argument 1 to requested IOCTL call
    :type arg1: u32

    :param arg2:
        Argument 2 to requested IOCTL call
    :type arg2: u32

    :param out:
        Returned output value
    :type out: u32 \*

.. _`zynqmp_pm_ioctl.description`:

Description
-----------

This function calls IOCTL to firmware for device control and configuration.

.. _`zynqmp_pm_ioctl.return`:

Return
------

Returns status, either success or error+reason

.. _`zynqmp_pm_get_eemi_ops`:

zynqmp_pm_get_eemi_ops
======================

.. c:function:: const struct zynqmp_eemi_ops *zynqmp_pm_get_eemi_ops( void)

    Get eemi ops functions

    :param void:
        no arguments
    :type void: 

.. _`zynqmp_pm_get_eemi_ops.return`:

Return
------

Pointer of eemi_ops structure

.. This file was automatic generated / don't edit.


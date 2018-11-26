.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/iavf/iavf_common.c

.. _`iavf_set_mac_type`:

iavf_set_mac_type
=================

.. c:function:: iavf_status iavf_set_mac_type(struct iavf_hw *hw)

    Sets MAC type

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

.. _`iavf_set_mac_type.description`:

Description
-----------

This function sets the mac type of the adapter based on the
vendor ID and device ID stored in the hw structure.

.. _`iavf_aq_str`:

iavf_aq_str
===========

.. c:function:: const char *iavf_aq_str(struct iavf_hw *hw, enum i40e_admin_queue_err aq_err)

    convert AQ err code to a string

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param aq_err:
        the AQ error code to convert
    :type aq_err: enum i40e_admin_queue_err

.. _`iavf_stat_str`:

iavf_stat_str
=============

.. c:function:: const char *iavf_stat_str(struct iavf_hw *hw, iavf_status stat_err)

    convert status err code to a string

    :param hw:
        pointer to the HW structure
    :type hw: struct iavf_hw \*

    :param stat_err:
        the status error code to convert
    :type stat_err: iavf_status

.. _`iavf_debug_aq`:

iavf_debug_aq
=============

.. c:function:: void iavf_debug_aq(struct iavf_hw *hw, enum iavf_debug_mask mask, void *desc, void *buffer, u16 buf_len)

    :param hw:
        debug mask related to admin queue
    :type hw: struct iavf_hw \*

    :param mask:
        debug mask
    :type mask: enum iavf_debug_mask

    :param desc:
        pointer to admin queue descriptor
    :type desc: void \*

    :param buffer:
        pointer to command buffer
    :type buffer: void \*

    :param buf_len:
        max length of buffer
    :type buf_len: u16

.. _`iavf_debug_aq.description`:

Description
-----------

Dumps debug log about adminq command with descriptor contents.

.. _`iavf_check_asq_alive`:

iavf_check_asq_alive
====================

.. c:function:: bool iavf_check_asq_alive(struct iavf_hw *hw)

    :param hw:
        pointer to the hw struct
    :type hw: struct iavf_hw \*

.. _`iavf_check_asq_alive.description`:

Description
-----------

Returns true if Queue is enabled else false.

.. _`iavf_aq_queue_shutdown`:

iavf_aq_queue_shutdown
======================

.. c:function:: iavf_status iavf_aq_queue_shutdown(struct iavf_hw *hw, bool unloading)

    :param hw:
        pointer to the hw struct
    :type hw: struct iavf_hw \*

    :param unloading:
        is the driver unloading itself
    :type unloading: bool

.. _`iavf_aq_queue_shutdown.description`:

Description
-----------

Tell the Firmware that we're shutting down the AdminQ and whether
or not the driver is unloading as well.

.. _`iavf_aq_get_set_rss_lut`:

iavf_aq_get_set_rss_lut
=======================

.. c:function:: iavf_status iavf_aq_get_set_rss_lut(struct iavf_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size, bool set)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

    :param set:
        set true to set the table, false to get the table
    :type set: bool

.. _`iavf_aq_get_set_rss_lut.description`:

Description
-----------

Internal function to get or set RSS look up table

.. _`iavf_aq_get_rss_lut`:

iavf_aq_get_rss_lut
===================

.. c:function:: iavf_status iavf_aq_get_rss_lut(struct iavf_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

.. _`iavf_aq_get_rss_lut.description`:

Description
-----------

get the RSS lookup table, PF or VSI type

.. _`iavf_aq_set_rss_lut`:

iavf_aq_set_rss_lut
===================

.. c:function:: iavf_status iavf_aq_set_rss_lut(struct iavf_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param pf_lut:
        for PF table set true, for VSI table set false
    :type pf_lut: bool

    :param lut:
        pointer to the lut buffer provided by the caller
    :type lut: u8 \*

    :param lut_size:
        size of the lut buffer
    :type lut_size: u16

.. _`iavf_aq_set_rss_lut.description`:

Description
-----------

set the RSS lookup table, PF or VSI type

.. _`iavf_aq_get_set_rss_key`:

iavf_aq_get_set_rss_key
=======================

.. c:function:: iavf_status iavf_aq_get_set_rss_key(struct iavf_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key, bool set)

    :param hw:
        pointer to the hw struct
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

    :param set:
        set true to set the key, false to get the key
    :type set: bool

.. _`iavf_aq_get_set_rss_key.description`:

Description
-----------

get the RSS key per VSI

.. _`iavf_aq_get_rss_key`:

iavf_aq_get_rss_key
===================

.. c:function:: iavf_status iavf_aq_get_rss_key(struct iavf_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param hw:
        pointer to the hw struct
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

.. _`iavf_aq_set_rss_key`:

iavf_aq_set_rss_key
===================

.. c:function:: iavf_status iavf_aq_set_rss_key(struct iavf_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param hw:
        pointer to the hw struct
    :type hw: struct iavf_hw \*

    :param vsi_id:
        vsi fw index
    :type vsi_id: u16

    :param key:
        pointer to key info struct
    :type key: struct i40e_aqc_get_set_rss_key_data \*

.. _`iavf_aq_set_rss_key.description`:

Description
-----------

set the RSS key per VSI

.. _`iavf_aq_send_msg_to_pf`:

iavf_aq_send_msg_to_pf
======================

.. c:function:: iavf_status iavf_aq_send_msg_to_pf(struct iavf_hw *hw, enum virtchnl_ops v_opcode, iavf_status v_retval, u8 *msg, u16 msglen, struct i40e_asq_cmd_details *cmd_details)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

    :param v_opcode:
        opcodes for VF-PF communication
    :type v_opcode: enum virtchnl_ops

    :param v_retval:
        return error code
    :type v_retval: iavf_status

    :param msg:
        pointer to the msg buffer
    :type msg: u8 \*

    :param msglen:
        msg length
    :type msglen: u16

    :param cmd_details:
        pointer to command details
    :type cmd_details: struct i40e_asq_cmd_details \*

.. _`iavf_aq_send_msg_to_pf.description`:

Description
-----------

Send message to PF driver using admin queue. By default, this message
is sent asynchronously, i.e. \ :c:func:`iavf_asq_send_command`\  does not wait for
completion before returning.

.. _`iavf_vf_parse_hw_config`:

iavf_vf_parse_hw_config
=======================

.. c:function:: void iavf_vf_parse_hw_config(struct iavf_hw *hw, struct virtchnl_vf_resource *msg)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

    :param msg:
        pointer to the virtual channel VF resource structure
    :type msg: struct virtchnl_vf_resource \*

.. _`iavf_vf_parse_hw_config.description`:

Description
-----------

Given a VF resource message from the PF, populate the hw struct
with appropriate information.

.. _`iavf_vf_reset`:

iavf_vf_reset
=============

.. c:function:: iavf_status iavf_vf_reset(struct iavf_hw *hw)

    :param hw:
        pointer to the hardware structure
    :type hw: struct iavf_hw \*

.. _`iavf_vf_reset.description`:

Description
-----------

Send a VF_RESET message to the PF. Does not wait for response from PF
as none will be forthcoming. Immediately after calling this function,
the admin queue should be shut down and (optionally) reinitialized.

.. This file was automatic generated / don't edit.


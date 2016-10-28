.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/i40evf/i40e_common.c

.. _`i40e_set_mac_type`:

i40e_set_mac_type
=================

.. c:function:: i40e_status i40e_set_mac_type(struct i40e_hw *hw)

    Sets MAC type

    :param struct i40e_hw \*hw:
        pointer to the HW structure

.. _`i40e_set_mac_type.description`:

Description
-----------

This function sets the mac type of the adapter based on the
vendor ID and device ID stored in the hw structure.

.. _`i40evf_aq_str`:

i40evf_aq_str
=============

.. c:function:: const char *i40evf_aq_str(struct i40e_hw *hw, enum i40e_admin_queue_err aq_err)

    convert AQ err code to a string

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param enum i40e_admin_queue_err aq_err:
        the AQ error code to convert

.. _`i40evf_stat_str`:

i40evf_stat_str
===============

.. c:function:: const char *i40evf_stat_str(struct i40e_hw *hw, i40e_status stat_err)

    convert status err code to a string

    :param struct i40e_hw \*hw:
        pointer to the HW structure

    :param i40e_status stat_err:
        the status error code to convert

.. _`i40evf_debug_aq`:

i40evf_debug_aq
===============

.. c:function:: void i40evf_debug_aq(struct i40e_hw *hw, enum i40e_debug_mask mask, void *desc, void *buffer, u16 buf_len)

    :param struct i40e_hw \*hw:
        debug mask related to admin queue

    :param enum i40e_debug_mask mask:
        debug mask

    :param void \*desc:
        pointer to admin queue descriptor

    :param void \*buffer:
        pointer to command buffer

    :param u16 buf_len:
        max length of buffer

.. _`i40evf_debug_aq.description`:

Description
-----------

Dumps debug log about adminq command with descriptor contents.

.. _`i40evf_check_asq_alive`:

i40evf_check_asq_alive
======================

.. c:function:: bool i40evf_check_asq_alive(struct i40e_hw *hw)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

.. _`i40evf_check_asq_alive.description`:

Description
-----------

Returns true if Queue is enabled else false.

.. _`i40evf_aq_queue_shutdown`:

i40evf_aq_queue_shutdown
========================

.. c:function:: i40e_status i40evf_aq_queue_shutdown(struct i40e_hw *hw, bool unloading)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param bool unloading:
        is the driver unloading itself

.. _`i40evf_aq_queue_shutdown.description`:

Description
-----------

Tell the Firmware that we're shutting down the AdminQ and whether
or not the driver is unloading as well.

.. _`i40e_aq_get_set_rss_lut`:

i40e_aq_get_set_rss_lut
=======================

.. c:function:: i40e_status i40e_aq_get_set_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size, bool set)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        vsi fw index

    :param bool pf_lut:
        for PF table set true, for VSI table set false

    :param u8 \*lut:
        pointer to the lut buffer provided by the caller

    :param u16 lut_size:
        size of the lut buffer

    :param bool set:
        set true to set the table, false to get the table

.. _`i40e_aq_get_set_rss_lut.description`:

Description
-----------

Internal function to get or set RSS look up table

.. _`i40evf_aq_get_rss_lut`:

i40evf_aq_get_rss_lut
=====================

.. c:function:: i40e_status i40evf_aq_get_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        vsi fw index

    :param bool pf_lut:
        for PF table set true, for VSI table set false

    :param u8 \*lut:
        pointer to the lut buffer provided by the caller

    :param u16 lut_size:
        size of the lut buffer

.. _`i40evf_aq_get_rss_lut.description`:

Description
-----------

get the RSS lookup table, PF or VSI type

.. _`i40evf_aq_set_rss_lut`:

i40evf_aq_set_rss_lut
=====================

.. c:function:: i40e_status i40evf_aq_set_rss_lut(struct i40e_hw *hw, u16 vsi_id, bool pf_lut, u8 *lut, u16 lut_size)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param u16 vsi_id:
        vsi fw index

    :param bool pf_lut:
        for PF table set true, for VSI table set false

    :param u8 \*lut:
        pointer to the lut buffer provided by the caller

    :param u16 lut_size:
        size of the lut buffer

.. _`i40evf_aq_set_rss_lut.description`:

Description
-----------

set the RSS lookup table, PF or VSI type

.. _`i40e_aq_get_set_rss_key`:

i40e_aq_get_set_rss_key
=======================

.. c:function:: i40e_status i40e_aq_get_set_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key, bool set)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        vsi fw index

    :param struct i40e_aqc_get_set_rss_key_data \*key:
        pointer to key info struct

    :param bool set:
        set true to set the key, false to get the key

.. _`i40e_aq_get_set_rss_key.description`:

Description
-----------

get the RSS key per VSI

.. _`i40evf_aq_get_rss_key`:

i40evf_aq_get_rss_key
=====================

.. c:function:: i40e_status i40evf_aq_get_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        vsi fw index

    :param struct i40e_aqc_get_set_rss_key_data \*key:
        pointer to key info struct

.. _`i40evf_aq_set_rss_key`:

i40evf_aq_set_rss_key
=====================

.. c:function:: i40e_status i40evf_aq_set_rss_key(struct i40e_hw *hw, u16 vsi_id, struct i40e_aqc_get_set_rss_key_data *key)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u16 vsi_id:
        vsi fw index

    :param struct i40e_aqc_get_set_rss_key_data \*key:
        pointer to key info struct

.. _`i40evf_aq_set_rss_key.description`:

Description
-----------

set the RSS key per VSI

.. _`i40evf_aq_rx_ctl_read_register`:

i40evf_aq_rx_ctl_read_register
==============================

.. c:function:: i40e_status i40evf_aq_rx_ctl_read_register(struct i40e_hw *hw, u32 reg_addr, u32 *reg_val, struct i40e_asq_cmd_details *cmd_details)

    use FW to read from an Rx control register

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u32 reg_addr:
        register address

    :param u32 \*reg_val:
        ptr to register value

    :param struct i40e_asq_cmd_details \*cmd_details:
        pointer to command details structure or NULL

.. _`i40evf_aq_rx_ctl_read_register.description`:

Description
-----------

Use the firmware to read the Rx control register,
especially useful if the Rx unit is under heavy pressure

.. _`i40evf_read_rx_ctl`:

i40evf_read_rx_ctl
==================

.. c:function:: u32 i40evf_read_rx_ctl(struct i40e_hw *hw, u32 reg_addr)

    read from an Rx control register

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u32 reg_addr:
        register address

.. _`i40evf_aq_rx_ctl_write_register`:

i40evf_aq_rx_ctl_write_register
===============================

.. c:function:: i40e_status i40evf_aq_rx_ctl_write_register(struct i40e_hw *hw, u32 reg_addr, u32 reg_val, struct i40e_asq_cmd_details *cmd_details)

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u32 reg_addr:
        register address

    :param u32 reg_val:
        register value

    :param struct i40e_asq_cmd_details \*cmd_details:
        pointer to command details structure or NULL

.. _`i40evf_aq_rx_ctl_write_register.description`:

Description
-----------

Use the firmware to write to an Rx control register,
especially useful if the Rx unit is under heavy pressure

.. _`i40evf_write_rx_ctl`:

i40evf_write_rx_ctl
===================

.. c:function:: void i40evf_write_rx_ctl(struct i40e_hw *hw, u32 reg_addr, u32 reg_val)

    write to an Rx control register

    :param struct i40e_hw \*hw:
        pointer to the hw struct

    :param u32 reg_addr:
        register address

    :param u32 reg_val:
        register value

.. _`i40e_aq_send_msg_to_pf`:

i40e_aq_send_msg_to_pf
======================

.. c:function:: i40e_status i40e_aq_send_msg_to_pf(struct i40e_hw *hw, enum i40e_virtchnl_ops v_opcode, i40e_status v_retval, u8 *msg, u16 msglen, struct i40e_asq_cmd_details *cmd_details)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param enum i40e_virtchnl_ops v_opcode:
        opcodes for VF-PF communication

    :param i40e_status v_retval:
        return error code

    :param u8 \*msg:
        pointer to the msg buffer

    :param u16 msglen:
        msg length

    :param struct i40e_asq_cmd_details \*cmd_details:
        pointer to command details

.. _`i40e_aq_send_msg_to_pf.description`:

Description
-----------

Send message to PF driver using admin queue. By default, this message
is sent asynchronously, i.e. \ :c:func:`i40evf_asq_send_command`\  does not wait for
completion before returning.

.. _`i40e_vf_parse_hw_config`:

i40e_vf_parse_hw_config
=======================

.. c:function:: void i40e_vf_parse_hw_config(struct i40e_hw *hw, struct i40e_virtchnl_vf_resource *msg)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

    :param struct i40e_virtchnl_vf_resource \*msg:
        pointer to the virtual channel VF resource structure

.. _`i40e_vf_parse_hw_config.description`:

Description
-----------

Given a VF resource message from the PF, populate the hw struct
with appropriate information.

.. _`i40e_vf_reset`:

i40e_vf_reset
=============

.. c:function:: i40e_status i40e_vf_reset(struct i40e_hw *hw)

    :param struct i40e_hw \*hw:
        pointer to the hardware structure

.. _`i40e_vf_reset.description`:

Description
-----------

Send a VF_RESET message to the PF. Does not wait for response from PF
as none will be forthcoming. Immediately after calling this function,
the admin queue should be shut down and (optionally) reinitialized.

.. This file was automatic generated / don't edit.


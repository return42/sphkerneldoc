.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/marvell/libertas/cmd.c

.. _`lbs_cmd_copyback`:

lbs_cmd_copyback
================

.. c:function:: int lbs_cmd_copyback(struct lbs_private *priv, unsigned long extra, struct cmd_header *resp)

    Simple callback that copies response back into command

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param unsigned long extra:
        A pointer to the original command structure for which
        'resp' is a response

    :param struct cmd_header \*resp:
        A pointer to the command response

.. _`lbs_cmd_copyback.return`:

Return
------

0 on success, error on failure

.. _`lbs_cmd_async_callback`:

lbs_cmd_async_callback
======================

.. c:function:: int lbs_cmd_async_callback(struct lbs_private *priv, unsigned long extra, struct cmd_header *resp)

    Simple callback that ignores the result. Use this if you just want to send a command to the hardware, but don't care for the result.

    :param struct lbs_private \*priv:
        ignored

    :param unsigned long extra:
        ignored

    :param struct cmd_header \*resp:
        ignored

.. _`lbs_cmd_async_callback.return`:

Return
------

0 for success

.. _`is_command_allowed_in_ps`:

is_command_allowed_in_ps
========================

.. c:function:: u8 is_command_allowed_in_ps(u16 cmd)

    tests if a command is allowed in Power Save mode

    :param u16 cmd:
        the command ID

.. _`is_command_allowed_in_ps.return`:

Return
------

1 if allowed, 0 if not allowed

.. _`lbs_update_hw_spec`:

lbs_update_hw_spec
==================

.. c:function:: int lbs_update_hw_spec(struct lbs_private *priv)

    Updates the hardware details like MAC address and regulatory region

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_update_hw_spec.return`:

Return
------

0 on success, error on failure

.. _`lbs_set_ps_mode`:

lbs_set_ps_mode
===============

.. c:function:: int lbs_set_ps_mode(struct lbs_private *priv, u16 cmd_action, bool block)

    Sets the Power Save mode

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param u16 cmd_action:
        The Power Save operation (PS_MODE_ACTION_ENTER_PS or
        PS_MODE_ACTION_EXIT_PS)

    :param bool block:
        Whether to block on a response or not

.. _`lbs_set_ps_mode.return`:

Return
------

0 on success, error on failure

.. _`lbs_set_snmp_mib`:

lbs_set_snmp_mib
================

.. c:function:: int lbs_set_snmp_mib(struct lbs_private *priv, u32 oid, u16 val)

    Set an SNMP MIB value

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param u32 oid:
        The OID to set in the firmware

    :param u16 val:
        Value to set the OID to

.. _`lbs_set_snmp_mib.return`:

Return
------

0 on success, error on failure

.. _`lbs_get_snmp_mib`:

lbs_get_snmp_mib
================

.. c:function:: int lbs_get_snmp_mib(struct lbs_private *priv, u32 oid, u16 *out_val)

    Get an SNMP MIB value

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param u32 oid:
        The OID to retrieve from the firmware

    :param u16 \*out_val:
        Location for the returned value

.. _`lbs_get_snmp_mib.return`:

Return
------

0 on success, error on failure

.. _`lbs_get_tx_power`:

lbs_get_tx_power
================

.. c:function:: int lbs_get_tx_power(struct lbs_private *priv, s16 *curlevel, s16 *minlevel, s16 *maxlevel)

    Get the min, max, and current TX power

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param s16 \*curlevel:
        Current power level in dBm

    :param s16 \*minlevel:
        Minimum supported power level in dBm (optional)

    :param s16 \*maxlevel:
        Maximum supported power level in dBm (optional)

.. _`lbs_get_tx_power.return`:

Return
------

0 on success, error on failure

.. _`lbs_set_tx_power`:

lbs_set_tx_power
================

.. c:function:: int lbs_set_tx_power(struct lbs_private *priv, s16 dbm)

    Set the TX power

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param s16 dbm:
        The desired power level in dBm

.. _`lbs_set_tx_power.return`:

Return
------

0 on success, error on failure

.. _`lbs_set_monitor_mode`:

lbs_set_monitor_mode
====================

.. c:function:: int lbs_set_monitor_mode(struct lbs_private *priv, int enable)

    Enable or disable monitor mode (only implemented on OLPC usb8388 FW)

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param int enable:
        1 to enable monitor mode, 0 to disable

.. _`lbs_set_monitor_mode.return`:

Return
------

0 on success, error on failure

.. _`lbs_get_channel`:

lbs_get_channel
===============

.. c:function:: int lbs_get_channel(struct lbs_private *priv)

    Get the radio channel

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_get_channel.return`:

Return
------

The channel on success, error on failure

.. _`lbs_set_channel`:

lbs_set_channel
===============

.. c:function:: int lbs_set_channel(struct lbs_private *priv, u8 channel)

    Set the radio channel

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param u8 channel:
        The desired channel, or 0 to clear a locked channel

.. _`lbs_set_channel.return`:

Return
------

0 on success, error on failure

.. _`lbs_get_rssi`:

lbs_get_rssi
============

.. c:function:: int lbs_get_rssi(struct lbs_private *priv, s8 *rssi, s8 *nf)

    Get current RSSI and noise floor

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param s8 \*rssi:
        On successful return, signal level in mBm

    :param s8 \*nf:
        On successful return, Noise floor

.. _`lbs_get_rssi.return`:

Return
------

The channel on success, error on failure

.. _`lbs_set_11d_domain_info`:

lbs_set_11d_domain_info
=======================

.. c:function:: int lbs_set_11d_domain_info(struct lbs_private *priv)

    Send regulatory and 802.11d domain information to the firmware

    :param struct lbs_private \*priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

.. _`lbs_set_11d_domain_info.return`:

Return
------

0 on success, error code on failure

.. _`lbs_get_reg`:

lbs_get_reg
===========

.. c:function:: int lbs_get_reg(struct lbs_private *priv, u16 reg, u16 offset, u32 *value)

    Read a MAC, Baseband, or RF register

    :param struct lbs_private \*priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

    :param u16 reg:
        register command, one of CMD_MAC_REG_ACCESS,
        CMD_BBP_REG_ACCESS, or CMD_RF_REG_ACCESS

    :param u16 offset:
        byte offset of the register to get

    :param u32 \*value:
        on success, the value of the register at 'offset'

.. _`lbs_get_reg.return`:

Return
------

0 on success, error code on failure

.. _`lbs_set_reg`:

lbs_set_reg
===========

.. c:function:: int lbs_set_reg(struct lbs_private *priv, u16 reg, u16 offset, u32 value)

    Write a MAC, Baseband, or RF register

    :param struct lbs_private \*priv:
        pointer to \ :c:type:`struct lbs_private <lbs_private>`\ 

    :param u16 reg:
        register command, one of CMD_MAC_REG_ACCESS,
        CMD_BBP_REG_ACCESS, or CMD_RF_REG_ACCESS

    :param u16 offset:
        byte offset of the register to set

    :param u32 value:
        the value to write to the register at 'offset'

.. _`lbs_set_reg.return`:

Return
------

0 on success, error code on failure

.. _`lbs_allocate_cmd_buffer`:

lbs_allocate_cmd_buffer
=======================

.. c:function:: int lbs_allocate_cmd_buffer(struct lbs_private *priv)

    allocates the command buffer and links it to command free queue

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_allocate_cmd_buffer.return`:

Return
------

0 for success or -1 on error

.. _`lbs_free_cmd_buffer`:

lbs_free_cmd_buffer
===================

.. c:function:: int lbs_free_cmd_buffer(struct lbs_private *priv)

    free the command buffer

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_free_cmd_buffer.return`:

Return
------

0 for success

.. _`lbs_get_free_cmd_node`:

lbs_get_free_cmd_node
=====================

.. c:function:: struct cmd_ctrl_node *lbs_get_free_cmd_node(struct lbs_private *priv)

    gets a free command node if available in command free queue

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_get_free_cmd_node.return`:

Return
------

A pointer to \ :c:type:`struct cmd_ctrl_node <cmd_ctrl_node>`\  structure on success
or \ ``NULL``\  on error

.. _`lbs_execute_next_command`:

lbs_execute_next_command
========================

.. c:function:: int lbs_execute_next_command(struct lbs_private *priv)

    execute next command in command pending queue. Will put firmware back to PS mode if applicable.

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_execute_next_command.return`:

Return
------

0 on success or -1 on error

.. _`lbs_ps_confirm_sleep`:

lbs_ps_confirm_sleep
====================

.. c:function:: void lbs_ps_confirm_sleep(struct lbs_private *priv)

    checks condition and prepares to send sleep confirm command to firmware if ok

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

.. _`lbs_ps_confirm_sleep.return`:

Return
------

n/a

.. _`lbs_set_tpc_cfg`:

lbs_set_tpc_cfg
===============

.. c:function:: int lbs_set_tpc_cfg(struct lbs_private *priv, int enable, int8_t p0, int8_t p1, int8_t p2, int usesnr)

    Configures the transmission power control functionality

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param int enable:
        Transmission power control enable

    :param int8_t p0:
        Power level when link quality is good (dBm).

    :param int8_t p1:
        Power level when link quality is fair (dBm).

    :param int8_t p2:
        Power level when link quality is poor (dBm).

    :param int usesnr:
        Use Signal to Noise Ratio in TPC

.. _`lbs_set_tpc_cfg.return`:

Return
------

0 on success

.. _`lbs_set_power_adapt_cfg`:

lbs_set_power_adapt_cfg
=======================

.. c:function:: int lbs_set_power_adapt_cfg(struct lbs_private *priv, int enable, int8_t p0, int8_t p1, int8_t p2)

    Configures the power adaptation settings

    :param struct lbs_private \*priv:
        A pointer to \ :c:type:`struct lbs_private <lbs_private>`\  structure

    :param int enable:
        Power adaptation enable

    :param int8_t p0:
        Power level for 1, 2, 5.5 and 11 Mbps (dBm).

    :param int8_t p1:
        Power level for 6, 9, 12, 18, 22, 24 and 36 Mbps (dBm).

    :param int8_t p2:
        Power level for 48 and 54 Mbps (dBm).

.. _`lbs_set_power_adapt_cfg.return`:

Return
------

0 on Success

.. This file was automatic generated / don't edit.


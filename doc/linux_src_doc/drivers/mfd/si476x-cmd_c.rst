.. -*- coding: utf-8; mode: rst -*-

============
si476x-cmd.c
============


.. _`si476x_core_send_command`:

si476x_core_send_command
========================

.. c:function:: int si476x_core_send_command (struct si476x_core *core, const u8 command, const u8 args[], const int argn, u8 resp[], const int respn, const int usecs)

    sends a command to si476x and waits its response

    :param struct si476x_core \*core:
        si476x_device structure for the device we are
        communicating with

    :param const u8 command:
        command id

    :param const u8 args:
        command arguments we are sending

    :param const int argn:
        actual size of ``args``

    :param u8 resp:

        *undescribed*

    :param const int respn:
        actual size of ``response``

    :param const int usecs:
        amount of time to wait before reading the response (in
        usecs)



.. _`si476x_core_send_command.description`:

Description
-----------

Function returns 0 on succsess and negative error code on
failure



.. _`si476x_core_cmd_func_info`:

si476x_core_cmd_func_info
=========================

.. c:function:: int si476x_core_cmd_func_info (struct si476x_core *core, struct si476x_func_info *info)

    send 'FUNC_INFO' command to the device

    :param struct si476x_core \*core:
        device to send the command to

    :param struct si476x_func_info \*info:
        struct si476x_func_info to fill all the information
        returned by the command



.. _`si476x_core_cmd_func_info.description`:

Description
-----------

The command requests the firmware and patch version for currently
loaded firmware (dependent on the function of the device FM/AM/WB)

Function returns 0 on succsess and negative error code on
failure



.. _`si476x_core_cmd_set_property`:

si476x_core_cmd_set_property
============================

.. c:function:: int si476x_core_cmd_set_property (struct si476x_core *core, u16 property, u16 value)

    send 'SET_PROPERTY' command to the device

    :param struct si476x_core \*core:
        device to send the command to

    :param u16 property:
        property address

    :param u16 value:
        property value



.. _`si476x_core_cmd_set_property.description`:

Description
-----------

Function returns 0 on succsess and negative error code on
failure



.. _`si476x_core_cmd_get_property`:

si476x_core_cmd_get_property
============================

.. c:function:: int si476x_core_cmd_get_property (struct si476x_core *core, u16 property)

    send 'GET_PROPERTY' command to the device

    :param struct si476x_core \*core:
        device to send the command to

    :param u16 property:
        property address



.. _`si476x_core_cmd_get_property.description`:

Description
-----------

Function return the value of property as u16 on success or a
negative error on failure



.. _`si476x_core_cmd_dig_audio_pin_cfg`:

si476x_core_cmd_dig_audio_pin_cfg
=================================

.. c:function:: int si476x_core_cmd_dig_audio_pin_cfg (struct si476x_core *core, enum si476x_dclk_config dclk, enum si476x_dfs_config dfs, enum si476x_dout_config dout, enum si476x_xout_config xout)

    send 'DIG_AUDIO_PIN_CFG' command to the device

    :param struct si476x_core \*core:
        device to send the command to

    :param enum si476x_dclk_config dclk:
        DCLK pin function configuration::

                   #SI476X_DCLK_NOOP     - do not modify the behaviour
                #SI476X_DCLK_TRISTATE - put the pin in tristate condition,
                                        enable 1MOhm pulldown
                #SI476X_DCLK_DAUDIO   - set the pin to be a part of digital
                                        audio interface

    :param enum si476x_dfs_config dfs:
        DFS pin function configuration::

                #SI476X_DFS_NOOP      - do not modify the behaviour
                #SI476X_DFS_TRISTATE  - put the pin in tristate condition,
                                    enable 1MOhm pulldown
             SI476X_DFS_DAUDIO    - set the pin to be a part of digital
                                    audio interface

        ``dout`` - DOUT pin function configuration::

             SI476X_DOUT_NOOP       - do not modify the behaviour
             SI476X_DOUT_TRISTATE   - put the pin in tristate condition,
                                      enable 1MOhm pulldown
             SI476X_DOUT_I2S_OUTPUT - set this pin to be digital out on I2S
                                      port 1
             SI476X_DOUT_I2S_INPUT  - set this pin to be digital in on I2S
                                      port 1

        ``xout`` - XOUT pin function configuration::

                SI476X_XOUT_NOOP        - do not modify the behaviour
             SI476X_XOUT_TRISTATE    - put the pin in tristate condition,
                                       enable 1MOhm pulldown
             SI476X_XOUT_I2S_INPUT   - set this pin to be digital in on I2S
                                       port 1
             SI476X_XOUT_MODE_SELECT - set this pin to be the input that
                                       selects the mode of the I2S audio
                                       combiner (analog or HD)
                                       [SI4761/63/65/67 Only]

    :param enum si476x_dout_config dout:

        *undescribed*

    :param enum si476x_xout_config xout:

        *undescribed*



.. _`si476x_core_cmd_dig_audio_pin_cfg.description`:

Description
-----------

Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_zif_pin_cfg`:

si476x_core_cmd_zif_pin_cfg
===========================

.. c:function:: int si476x_core_cmd_zif_pin_cfg (struct si476x_core *core, enum si476x_iqclk_config iqclk, enum si476x_iqfs_config iqfs, enum si476x_iout_config iout, enum si476x_qout_config qout)

    send 'ZIF_PIN_CFG_COMMAND' @core - device to send the command to @iqclk - IQCL pin function configuration: SI476X_IQCLK_NOOP - do not modify the behaviour SI476X_IQCLK_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_IQCLK_IQ - set pin to be a part of I/Q interace in master mode @iqfs - IQFS pin function configuration: SI476X_IQFS_NOOP - do not modify the behaviour SI476X_IQFS_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_IQFS_IQ - set pin to be a part of I/Q interace in master mode @iout - IOUT pin function configuration: SI476X_IOUT_NOOP - do not modify the behaviour SI476X_IOUT_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_IOUT_OUTPUT - set pin to be I out @qout - QOUT pin function configuration: SI476X_QOUT_NOOP - do not modify the behaviour SI476X_QOUT_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_QOUT_OUTPUT - set pin to be Q out

    :param struct si476x_core \*core:

        *undescribed*

    :param enum si476x_iqclk_config iqclk:

        *undescribed*

    :param enum si476x_iqfs_config iqfs:

        *undescribed*

    :param enum si476x_iout_config iout:

        *undescribed*

    :param enum si476x_qout_config qout:

        *undescribed*



.. _`si476x_core_cmd_zif_pin_cfg.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_ic_link_gpo_ctl_pin_cfg`:

si476x_core_cmd_ic_link_gpo_ctl_pin_cfg
=======================================

.. c:function:: int si476x_core_cmd_ic_link_gpo_ctl_pin_cfg (struct si476x_core *core, enum si476x_icin_config icin, enum si476x_icip_config icip, enum si476x_icon_config icon, enum si476x_icop_config icop)

    send 'IC_LINK_GPIO_CTL_PIN_CFG' comand to the device @core - device to send the command to @icin - ICIN pin function configuration: SI476X_ICIN_NOOP - do not modify the behaviour SI476X_ICIN_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_ICIN_GPO1_HIGH - set pin to be an output, drive it high SI476X_ICIN_GPO1_LOW - set pin to be an output, drive it low SI476X_ICIN_IC_LINK - set the pin to be a part of Inter-Chip link @icip - ICIP pin function configuration: SI476X_ICIP_NOOP - do not modify the behaviour SI476X_ICIP_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_ICIP_GPO1_HIGH - set pin to be an output, drive it high SI476X_ICIP_GPO1_LOW - set pin to be an output, drive it low SI476X_ICIP_IC_LINK - set the pin to be a part of Inter-Chip link @icon - ICON pin function configuration: SI476X_ICON_NOOP - do not modify the behaviour SI476X_ICON_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_ICON_I2S - set the pin to be a part of audio interface in slave mode (DCLK) SI476X_ICON_IC_LINK - set the pin to be a part of Inter-Chip link @icop - ICOP pin function configuration: SI476X_ICOP_NOOP - do not modify the behaviour SI476X_ICOP_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_ICOP_I2S - set the pin to be a part of audio interface in slave mode (DOUT) [Si4761/63/65/67 Only] SI476X_ICOP_IC_LINK - set the pin to be a part of Inter-Chip link

    :param struct si476x_core \*core:

        *undescribed*

    :param enum si476x_icin_config icin:

        *undescribed*

    :param enum si476x_icip_config icip:

        *undescribed*

    :param enum si476x_icon_config icon:

        *undescribed*

    :param enum si476x_icop_config icop:

        *undescribed*



.. _`si476x_core_cmd_ic_link_gpo_ctl_pin_cfg.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_ana_audio_pin_cfg`:

si476x_core_cmd_ana_audio_pin_cfg
=================================

.. c:function:: int si476x_core_cmd_ana_audio_pin_cfg (struct si476x_core *core, enum si476x_lrout_config lrout)

    send 'ANA_AUDIO_PIN_CFG' to the device @core - device to send the command to @lrout - LROUT pin function configuration: SI476X_LROUT_NOOP - do not modify the behaviour SI476X_LROUT_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_LROUT_AUDIO - set pin to be audio output SI476X_LROUT_MPX - set pin to be MPX output

    :param struct si476x_core \*core:

        *undescribed*

    :param enum si476x_lrout_config lrout:

        *undescribed*



.. _`si476x_core_cmd_ana_audio_pin_cfg.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_intb_pin_cfg_a10`:

si476x_core_cmd_intb_pin_cfg_a10
================================

.. c:function:: int si476x_core_cmd_intb_pin_cfg_a10 (struct si476x_core *core, enum si476x_intb_config intb, enum si476x_a1_config a1)

    send 'INTB_PIN_CFG' command to the device @core - device to send the command to @intb - INTB pin function configuration: SI476X_INTB_NOOP - do not modify the behaviour SI476X_INTB_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_INTB_DAUDIO - set pin to be a part of digital audio interface in slave mode SI476X_INTB_IRQ - set pin to be an interrupt request line @a1 - A1 pin function configuration: SI476X_A1_NOOP - do not modify the behaviour SI476X_A1_TRISTATE - put the pin in tristate condition, enable 1MOhm pulldown SI476X_A1_IRQ - set pin to be an interrupt request line

    :param struct si476x_core \*core:

        *undescribed*

    :param enum si476x_intb_config intb:

        *undescribed*

    :param enum si476x_a1_config a1:

        *undescribed*



.. _`si476x_core_cmd_intb_pin_cfg_a10.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_am_rsq_status`:

si476x_core_cmd_am_rsq_status
=============================

.. c:function:: int si476x_core_cmd_am_rsq_status (struct si476x_core *core, struct si476x_rsq_status_args *rsqargs, struct si476x_rsq_status_report *report)

    send 'AM_RSQ_STATUS' command to the device @core - device to send the command to @rsqack - if set command clears RSQINT, SNRINT, SNRLINT, RSSIHINT, RSSSILINT, BLENDINT, MULTHINT and MULTLINT @attune - when set the values in the status report are the values that were calculated at tune @cancel - abort ongoing seek/tune opertation @stcack - clear the STCINT bin in status register @report - all signal quality information retured by the command (if NULL then the output of the command is ignored)

    :param struct si476x_core \*core:

        *undescribed*

    :param struct si476x_rsq_status_args \*rsqargs:

        *undescribed*

    :param struct si476x_rsq_status_report \*report:

        *undescribed*



.. _`si476x_core_cmd_am_rsq_status.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_fm_seek_start`:

si476x_core_cmd_fm_seek_start
=============================

.. c:function:: int si476x_core_cmd_fm_seek_start (struct si476x_core *core, bool seekup, bool wrap)

    send 'FM_SEEK_START' command to the device @core - device to send the command to @seekup - if set the direction of the search is 'up' @wrap - if set seek wraps when hitting band limit

    :param struct si476x_core \*core:

        *undescribed*

    :param bool seekup:

        *undescribed*

    :param bool wrap:

        *undescribed*



.. _`si476x_core_cmd_fm_seek_start.description`:

Description
-----------


This function begins search for a valid station. The station is
considered valid when 'FM_VALID_SNR_THRESHOLD' and
'FM_VALID_RSSI_THRESHOLD' and 'FM_VALID_MAX_TUNE_ERROR' criteria
are met.

Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_fm_rds_status`:

si476x_core_cmd_fm_rds_status
=============================

.. c:function:: int si476x_core_cmd_fm_rds_status (struct si476x_core *core, bool status_only, bool mtfifo, bool intack, struct si476x_rds_status_report *report)

    send 'FM_RDS_STATUS' command to the device @core - device to send the command to @status_only - if set the data is not removed from RDSFIFO, RDSFIFOUSED is not decremented and data in all the rest RDS data contains the last valid info received @mtfifo if set the command clears RDS receive FIFO @intack if set the command clards the RDSINT bit.

    :param struct si476x_core \*core:

        *undescribed*

    :param bool status_only:

        *undescribed*

    :param bool mtfifo:

        *undescribed*

    :param bool intack:

        *undescribed*

    :param struct si476x_rds_status_report \*report:

        *undescribed*



.. _`si476x_core_cmd_fm_rds_status.description`:

Description
-----------


Function returns 0 on success and negative error code on failure



.. _`si476x_core_cmd_fm_phase_div_status`:

si476x_core_cmd_fm_phase_div_status
===================================

.. c:function:: int si476x_core_cmd_fm_phase_div_status (struct si476x_core *core)

    get the phase diversity status

    :param struct si476x_core \*core:
        si476x device



.. _`si476x_core_cmd_fm_phase_div_status.description`:

Description
-----------

NOTE caller must hold core lock

Function returns the value of the status bit in case of success and
negative error code in case of failre.



.. _`si476x_core_cmd_am_seek_start`:

si476x_core_cmd_am_seek_start
=============================

.. c:function:: int si476x_core_cmd_am_seek_start (struct si476x_core *core, bool seekup, bool wrap)

    send 'FM_SEEK_START' command to the device @core - device to send the command to @seekup - if set the direction of the search is 'up' @wrap - if set seek wraps when hitting band limit

    :param struct si476x_core \*core:

        *undescribed*

    :param bool seekup:

        *undescribed*

    :param bool wrap:

        *undescribed*



.. _`si476x_core_cmd_am_seek_start.description`:

Description
-----------


This function begins search for a valid station. The station is
considered valid when 'FM_VALID_SNR_THRESHOLD' and
'FM_VALID_RSSI_THRESHOLD' and 'FM_VALID_MAX_TUNE_ERROR' criteria
are met.

Function returns 0 on success and negative error code on failure


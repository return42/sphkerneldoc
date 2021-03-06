.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/intel/atom/sst-atom-controls.c

.. _`sst_fill_and_send_cmd`:

sst_fill_and_send_cmd
=====================

.. c:function:: int sst_fill_and_send_cmd(struct sst_data *drv, u8 ipc_msg, u8 block, u8 task_id, u8 pipe_id, void *cmd_data, u16 len)

    generate the IPC message and send it to the FW

    :param drv:
        *undescribed*
    :type drv: struct sst_data \*

    :param ipc_msg:
        type of IPC (CMD, SET_PARAMS, GET_PARAMS)
    :type ipc_msg: u8

    :param block:
        *undescribed*
    :type block: u8

    :param task_id:
        *undescribed*
    :type task_id: u8

    :param pipe_id:
        *undescribed*
    :type pipe_id: u8

    :param cmd_data:
        the IPC payload
    :type cmd_data: void \*

    :param len:
        *undescribed*
    :type len: u16

.. _`sst_send_slot_map`:

sst_send_slot_map
=================

.. c:function:: int sst_send_slot_map(struct sst_data *drv)

    this is invoked with lock held

    :param drv:
        *undescribed*
    :type drv: struct sst_data \*

.. _`sst_slot_get`:

sst_slot_get
============

.. c:function:: int sst_slot_get(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    get the status of the interleaver/deinterleaver control

    :param kcontrol:
        *undescribed*
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        *undescribed*
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`sst_slot_get.description`:

Description
-----------

Searches the map where the control status is stored, and gets the
channel/slot which is currently set for this enumerated control. Since it is
an enumerated control, there is only one possible value.

.. _`sst_slot_put`:

sst_slot_put
============

.. c:function:: int sst_slot_put(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    set the status of interleaver/deinterleaver control

    :param kcontrol:
        *undescribed*
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        *undescribed*
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`sst_slot_put.description`:

Description
-----------

(de)interleaver controls are defined in opposite sense to be user-friendly

Instead of the enum value being the value written to the register, it is the
register address; and the kcontrol number (register num) is the value written
to the register. This is so that there can be only one value for each
slot/channel since there is only one control for each slot/channel.

This means that whenever an enum is set, we need to clear the bit
for that kcontrol_no for all the interleaver OR deinterleaver registers

.. _`sst_find_and_send_pipe_algo`:

sst_find_and_send_pipe_algo
===========================

.. c:function:: int sst_find_and_send_pipe_algo(struct sst_data *drv, const char *pipe, struct sst_ids *ids)

    send all the algo parameters for a pipe

    :param drv:
        *undescribed*
    :type drv: struct sst_data \*

    :param pipe:
        *undescribed*
    :type pipe: const char \*

    :param ids:
        *undescribed*
    :type ids: struct sst_ids \*

.. _`sst_find_and_send_pipe_algo.description`:

Description
-----------

The algos which are in each pipeline are sent to the firmware one by one

Called with lock held

.. _`sst_send_gain_cmd`:

sst_send_gain_cmd
=================

.. c:function:: int sst_send_gain_cmd(struct sst_data *drv, struct sst_gain_value *gv, u16 task_id, u16 loc_id, u16 module_id, int mute)

    send the gain algorithm IPC to the FW

    :param drv:
        *undescribed*
    :type drv: struct sst_data \*

    :param gv:
        the stored value of gain (also contains rampduration)
    :type gv: struct sst_gain_value \*

    :param task_id:
        *undescribed*
    :type task_id: u16

    :param loc_id:
        *undescribed*
    :type loc_id: u16

    :param module_id:
        *undescribed*
    :type module_id: u16

    :param mute:
        flag that indicates whether this was called from the
        digital_mute callback or directly. If called from the
        digital_mute callback, module will be muted/unmuted based on this
        flag. The flag is always 0 if called directly.
    :type mute: int

.. _`sst_send_gain_cmd.description`:

Description
-----------

Called with sst_data.lock held

The user-set gain value is sent only if the user-controllable 'mute' control
is OFF (indicated by gv->mute). Otherwise, the mute value (MIN value) is
sent.

.. _`fill_swm_input`:

fill_swm_input
==============

.. c:function:: int fill_swm_input(struct snd_soc_component *cmpnt, struct swm_input_ids *swm_input, unsigned int reg)

    fill in the SWM input ids given the register

    :param cmpnt:
        *undescribed*
    :type cmpnt: struct snd_soc_component \*

    :param swm_input:
        *undescribed*
    :type swm_input: struct swm_input_ids \*

    :param reg:
        *undescribed*
    :type reg: unsigned int

.. _`fill_swm_input.description`:

Description
-----------

The register value is a bit-field inicated which mixer inputs are ON. Use the
lookup table to get the input-id and fill it in the structure.

.. _`sst_set_pipe_gain`:

sst_set_pipe_gain
=================

.. c:function:: int sst_set_pipe_gain(struct sst_ids *ids, struct sst_data *drv, int mute)

    :param ids:
        *undescribed*
    :type ids: struct sst_ids \*

    :param drv:
        *undescribed*
    :type drv: struct sst_data \*

    :param mute:
        *undescribed*
    :type mute: int

.. _`sst_send_pipe_gains`:

sst_send_pipe_gains
===================

.. c:function:: int sst_send_pipe_gains(struct snd_soc_dai *dai, int stream, int mute)

    send gains for the front-end DAIs

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param stream:
        *undescribed*
    :type stream: int

    :param mute:
        *undescribed*
    :type mute: int

.. _`sst_send_pipe_gains.description`:

Description
-----------

The gains in the pipes connected to the front-ends are muted/unmuted
automatically via the \ :c:func:`digital_mute`\  DAPM callback. This function sends the
gains for the front-end pipes.

.. _`sst_fill_module_list`:

sst_fill_module_list
====================

.. c:function:: int sst_fill_module_list(struct snd_kcontrol *kctl, struct snd_soc_dapm_widget *w, int type)

    populate the list of modules/gains for a pipe

    :param kctl:
        *undescribed*
    :type kctl: struct snd_kcontrol \*

    :param w:
        *undescribed*
    :type w: struct snd_soc_dapm_widget \*

    :param type:
        *undescribed*
    :type type: int

.. _`sst_fill_module_list.description`:

Description
-----------


Fills the widget pointer in the kcontrol private data, and also fills the
kcontrol pointer in the widget private data.

Widget pointer is used to send the algo/gain in the .put() handler if the
widget is powerd on.

Kcontrol pointer is used to send the algo/gain in the widget power ON/OFF
event handler. Each widget (pipe) has multiple algos stored in the algo_list.

.. _`sst_fill_widget_module_info`:

sst_fill_widget_module_info
===========================

.. c:function:: int sst_fill_widget_module_info(struct snd_soc_dapm_widget *w, struct snd_soc_component *component)

    fill list of gains/algos for the pipe

    :param w:
        *undescribed*
    :type w: struct snd_soc_dapm_widget \*

    :param component:
        *undescribed*
    :type component: struct snd_soc_component \*

.. _`sst_fill_widget_module_info.description`:

Description
-----------

Fill the list of gains/algos for the widget by looking at all the card
controls and comparing the name of the widget with the first part of control
name. First part of control name contains the pipe name (widget name).

.. _`sst_fill_linked_widgets`:

sst_fill_linked_widgets
=======================

.. c:function:: void sst_fill_linked_widgets(struct snd_soc_component *component, struct sst_ids *ids)

    fill the parent pointer for the linked widget

    :param component:
        *undescribed*
    :type component: struct snd_soc_component \*

    :param ids:
        *undescribed*
    :type ids: struct sst_ids \*

.. _`sst_map_modules_to_pipe`:

sst_map_modules_to_pipe
=======================

.. c:function:: int sst_map_modules_to_pipe(struct snd_soc_component *component)

    fill algo/gains list for all pipes

    :param component:
        *undescribed*
    :type component: struct snd_soc_component \*

.. This file was automatic generated / don't edit.


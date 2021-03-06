.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_generic.c

.. _`snd_hda_gen_spec_init`:

snd_hda_gen_spec_init
=====================

.. c:function:: int snd_hda_gen_spec_init(struct hda_gen_spec *spec)

    initialize hda_gen_spec struct

    :param spec:
        hda_gen_spec object to initialize
    :type spec: struct hda_gen_spec \*

.. _`snd_hda_gen_spec_init.description`:

Description
-----------

Initialize the given hda_gen_spec object.

.. _`snd_hda_gen_add_kctl`:

snd_hda_gen_add_kctl
====================

.. c:function:: struct snd_kcontrol_new *snd_hda_gen_add_kctl(struct hda_gen_spec *spec, const char *name, const struct snd_kcontrol_new *temp)

    Add a new kctl_new struct from the template

    :param spec:
        hda_gen_spec object
    :type spec: struct hda_gen_spec \*

    :param name:
        name string to override the template, NULL if unchanged
    :type name: const char \*

    :param temp:
        template for the new kctl
    :type temp: const struct snd_kcontrol_new \*

.. _`snd_hda_gen_add_kctl.description`:

Description
-----------

Add a new kctl (actually snd_kcontrol_new to be instantiated later)
element based on the given snd_kcontrol_new template \ ``temp``\  and the
name string \ ``name``\  to the list in \ ``spec``\ .
Returns the newly created object or NULL as error.

.. _`snd_hda_get_path_idx`:

snd_hda_get_path_idx
====================

.. c:function:: int snd_hda_get_path_idx(struct hda_codec *codec, struct nid_path *path)

    get the index number corresponding to the path instance

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param path:
        nid_path object
    :type path: struct nid_path \*

.. _`snd_hda_get_path_idx.description`:

Description
-----------

The returned index starts from 1, i.e. the actual array index with offset 1,
and zero is handled as an invalid path

.. _`snd_hda_get_path_from_idx`:

snd_hda_get_path_from_idx
=========================

.. c:function:: struct nid_path *snd_hda_get_path_from_idx(struct hda_codec *codec, int idx)

    get the path instance corresponding to the given index number

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param idx:
        the path index
    :type idx: int

.. _`snd_hda_add_new_path`:

snd_hda_add_new_path
====================

.. c:function:: struct nid_path *snd_hda_add_new_path(struct hda_codec *codec, hda_nid_t from_nid, hda_nid_t to_nid, int anchor_nid)

    parse the path between the given NIDs and add to the path list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param from_nid:
        the NID where the path start from
    :type from_nid: hda_nid_t

    :param to_nid:
        the NID where the path ends at
    :type to_nid: hda_nid_t

    :param anchor_nid:
        the anchor indication, see \ :c:func:`snd_hda_parse_nid_path`\ 
    :type anchor_nid: int

.. _`snd_hda_add_new_path.description`:

Description
-----------

If no valid path is found, returns NULL.

.. _`snd_hda_activate_path`:

snd_hda_activate_path
=====================

.. c:function:: void snd_hda_activate_path(struct hda_codec *codec, struct nid_path *path, bool enable, bool add_aamix)

    activate or deactivate the given path

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param path:
        the path to activate/deactivate
    :type path: struct nid_path \*

    :param enable:
        flag to activate or not
    :type enable: bool

    :param add_aamix:
        enable the input from aamix NID
    :type add_aamix: bool

.. _`snd_hda_activate_path.description`:

Description
-----------

If \ ``add_aamix``\  is set, enable the input from aa-mix NID as well (if any).

.. _`snd_hda_gen_add_micmute_led`:

snd_hda_gen_add_micmute_led
===========================

.. c:function:: int snd_hda_gen_add_micmute_led(struct hda_codec *codec, void (*hook)(struct hda_codec *))

    helper for setting up mic mute LED hook

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param void (\*hook)(struct hda_codec \*):
        the callback for updating LED

.. _`snd_hda_gen_add_micmute_led.description`:

Description
-----------

Called from the codec drivers for offering the mic mute LED controls.
When established, it sets up cap_sync_hook and triggers the callback at
each time when the capture mixer switch changes.  The callback is supposed
to update the LED accordingly.

Returns 0 if the hook is established or a negative error code.

.. _`snd_hda_gen_fix_pin_power`:

snd_hda_gen_fix_pin_power
=========================

.. c:function:: int snd_hda_gen_fix_pin_power(struct hda_codec *codec, hda_nid_t pin)

    Fix the power of the given pin widget to D0

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param pin:
        NID of pin to fix
    :type pin: hda_nid_t

.. _`snd_hda_gen_update_outputs`:

snd_hda_gen_update_outputs
==========================

.. c:function:: void snd_hda_gen_update_outputs(struct hda_codec *codec)

    Toggle outputs muting

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_gen_update_outputs.description`:

Description
-----------

Update the mute status of all outputs based on the current jack states.

.. _`snd_hda_gen_hp_automute`:

snd_hda_gen_hp_automute
=======================

.. c:function:: void snd_hda_gen_hp_automute(struct hda_codec *codec, struct hda_jack_callback *jack)

    standard HP-automute helper

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param jack:
        jack object, NULL for the whole
    :type jack: struct hda_jack_callback \*

.. _`snd_hda_gen_line_automute`:

snd_hda_gen_line_automute
=========================

.. c:function:: void snd_hda_gen_line_automute(struct hda_codec *codec, struct hda_jack_callback *jack)

    standard line-out-automute helper

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param jack:
        jack object, NULL for the whole
    :type jack: struct hda_jack_callback \*

.. _`snd_hda_gen_mic_autoswitch`:

snd_hda_gen_mic_autoswitch
==========================

.. c:function:: void snd_hda_gen_mic_autoswitch(struct hda_codec *codec, struct hda_jack_callback *jack)

    standard mic auto-switch helper

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param jack:
        jack object, NULL for the whole
    :type jack: struct hda_jack_callback \*

.. _`snd_hda_gen_path_power_filter`:

snd_hda_gen_path_power_filter
=============================

.. c:function:: unsigned int snd_hda_gen_path_power_filter(struct hda_codec *codec, hda_nid_t nid, unsigned int power_state)

    power_filter hook to make inactive widgets into power down

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to evalute
    :type nid: hda_nid_t

    :param power_state:
        target power state
    :type power_state: unsigned int

.. _`snd_hda_gen_stream_pm`:

snd_hda_gen_stream_pm
=====================

.. c:function:: void snd_hda_gen_stream_pm(struct hda_codec *codec, hda_nid_t nid, bool on)

    Stream power management callback

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        audio widget
    :type nid: hda_nid_t

    :param on:
        power on/off flag
    :type on: bool

.. _`snd_hda_gen_stream_pm.description`:

Description
-----------

Set this in patch_ops.stream_pm.  Only valid with power_save_node flag.

.. _`snd_hda_gen_parse_auto_config`:

snd_hda_gen_parse_auto_config
=============================

.. c:function:: int snd_hda_gen_parse_auto_config(struct hda_codec *codec, struct auto_pin_cfg *cfg)

    Parse the given BIOS configuration and set up the hda_gen_spec

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param cfg:
        Parsed pin configuration
    :type cfg: struct auto_pin_cfg \*

.. _`snd_hda_gen_parse_auto_config.description`:

Description
-----------

return 1 if successful, 0 if the proper config is not found,
or a negative error code

.. _`snd_hda_gen_build_controls`:

snd_hda_gen_build_controls
==========================

.. c:function:: int snd_hda_gen_build_controls(struct hda_codec *codec)

    Build controls from the parsed results

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_gen_build_controls.description`:

Description
-----------

Pass this to build_controls patch_ops.

.. _`snd_hda_gen_build_pcms`:

snd_hda_gen_build_pcms
======================

.. c:function:: int snd_hda_gen_build_pcms(struct hda_codec *codec)

    build PCM streams based on the parsed results

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_gen_build_pcms.description`:

Description
-----------

Pass this to build_pcms patch_ops.

.. _`snd_hda_gen_init`:

snd_hda_gen_init
================

.. c:function:: int snd_hda_gen_init(struct hda_codec *codec)

    initialize the generic spec

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_gen_init.description`:

Description
-----------

This can be put as patch_ops init function.

.. _`snd_hda_gen_free`:

snd_hda_gen_free
================

.. c:function:: void snd_hda_gen_free(struct hda_codec *codec)

    free the generic spec

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_gen_free.description`:

Description
-----------

This can be put as patch_ops free function.

.. _`snd_hda_gen_check_power_status`:

snd_hda_gen_check_power_status
==============================

.. c:function:: int snd_hda_gen_check_power_status(struct hda_codec *codec, hda_nid_t nid)

    check the loopback power save state

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to inspect
    :type nid: hda_nid_t

.. _`snd_hda_gen_check_power_status.description`:

Description
-----------

This can be put as patch_ops check_power_status function.

.. This file was automatic generated / don't edit.


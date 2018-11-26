.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_auto_parser.c

.. _`snd_hda_get_input_pin_attr`:

snd_hda_get_input_pin_attr
==========================

.. c:function:: int snd_hda_get_input_pin_attr(unsigned int def_conf)

    Get the input pin attribute from pin config

    :param def_conf:
        pin configuration value
    :type def_conf: unsigned int

.. _`snd_hda_get_input_pin_attr.description`:

Description
-----------

Guess the input pin attribute (INPUT_PIN_ATTR_XXX) from the given
default pin configuration value.

.. _`hda_get_input_pin_label`:

hda_get_input_pin_label
=======================

.. c:function:: const char *hda_get_input_pin_label(struct hda_codec *codec, const struct auto_pin_cfg_item *item, hda_nid_t pin, bool check_location)

    Give a label for the given input pin

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param item:
        ping config item to refer
    :type item: const struct auto_pin_cfg_item \*

    :param pin:
        the pin NID
    :type pin: hda_nid_t

    :param check_location:
        flag to add the jack location prefix
    :type check_location: bool

.. _`hda_get_input_pin_label.description`:

Description
-----------

When \ ``check_location``\  is true, the function checks the pin location
for mic and line-in pins, and set an appropriate prefix like "Front",
"Rear", "Internal".

.. _`hda_get_autocfg_input_label`:

hda_get_autocfg_input_label
===========================

.. c:function:: const char *hda_get_autocfg_input_label(struct hda_codec *codec, const struct auto_pin_cfg *cfg, int input)

    Get a label for the given input

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param cfg:
        the parsed pin configuration
    :type cfg: const struct auto_pin_cfg \*

    :param input:
        the input index number
    :type input: int

.. _`hda_get_autocfg_input_label.description`:

Description
-----------

Get a label for the given input pin defined by the autocfg item.
Unlike \ :c:func:`hda_get_input_pin_label`\ , this function checks all inputs
defined in autocfg and avoids the redundant mic/line prefix as much as
possible.

.. _`snd_hda_get_pin_label`:

snd_hda_get_pin_label
=====================

.. c:function:: int snd_hda_get_pin_label(struct hda_codec *codec, hda_nid_t nid, const struct auto_pin_cfg *cfg, char *label, int maxlen, int *indexp)

    Get a label for the given I/O pin

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        pin NID
    :type nid: hda_nid_t

    :param cfg:
        the parsed pin configuration
    :type cfg: const struct auto_pin_cfg \*

    :param label:
        the string buffer to store
    :type label: char \*

    :param maxlen:
        the max length of string buffer (including termination)
    :type maxlen: int

    :param indexp:
        the pointer to return the index number (for multiple ctls)
    :type indexp: int \*

.. _`snd_hda_get_pin_label.description`:

Description
-----------

Get a label for the given pin.  This function works for both input and
output pins.  When \ ``cfg``\  is given as non-NULL, the function tries to get
an optimized label using \ :c:func:`hda_get_autocfg_input_label`\ .

This function tries to give a unique label string for the pin as much as
possible.  For example, when the multiple line-outs are present, it adds
the channel suffix like "Front", "Surround", etc (only when \ ``cfg``\  is given).
If no unique name with a suffix is available and \ ``indexp``\  is non-NULL, the
index number is stored in the pointer.

.. _`snd_hda_add_verbs`:

snd_hda_add_verbs
=================

.. c:function:: int snd_hda_add_verbs(struct hda_codec *codec, const struct hda_verb *list)

    Add verbs to the init list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param list:
        zero-terminated verb list to add
    :type list: const struct hda_verb \*

.. _`snd_hda_add_verbs.description`:

Description
-----------

Append the given verb list to the execution list.  The verbs will be
performed at init and resume time via \ :c:func:`snd_hda_apply_verbs`\ .

.. _`snd_hda_apply_verbs`:

snd_hda_apply_verbs
===================

.. c:function:: void snd_hda_apply_verbs(struct hda_codec *codec)

    Execute the init verb lists

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_apply_pincfgs`:

snd_hda_apply_pincfgs
=====================

.. c:function:: void snd_hda_apply_pincfgs(struct hda_codec *codec, const struct hda_pintbl *cfg)

    Set each pin config in the given list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param cfg:
        NULL-terminated pin config table
    :type cfg: const struct hda_pintbl \*

.. _`snd_hda_apply_fixup`:

snd_hda_apply_fixup
===================

.. c:function:: void snd_hda_apply_fixup(struct hda_codec *codec, int action)

    Apply the fixup chain with the given action

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param action:
        fixup action (HDA_FIXUP_ACT_XXX)
    :type action: int

.. _`snd_hda_pick_pin_fixup`:

snd_hda_pick_pin_fixup
======================

.. c:function:: void snd_hda_pick_pin_fixup(struct hda_codec *codec, const struct snd_hda_pin_quirk *pin_quirk, const struct hda_fixup *fixlist)

    Pick up a fixup matching with the pin quirk list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param pin_quirk:
        zero-terminated pin quirk list
    :type pin_quirk: const struct snd_hda_pin_quirk \*

    :param fixlist:
        the fixup list
    :type fixlist: const struct hda_fixup \*

.. _`snd_hda_pick_fixup`:

snd_hda_pick_fixup
==================

.. c:function:: void snd_hda_pick_fixup(struct hda_codec *codec, const struct hda_model_fixup *models, const struct snd_pci_quirk *quirk, const struct hda_fixup *fixlist)

    Pick up a fixup matching with PCI/codec SSID or model string

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param models:
        NULL-terminated model string list
    :type models: const struct hda_model_fixup \*

    :param quirk:
        zero-terminated PCI/codec SSID quirk list
    :type quirk: const struct snd_pci_quirk \*

    :param fixlist:
        the fixup list
    :type fixlist: const struct hda_fixup \*

.. _`snd_hda_pick_fixup.description`:

Description
-----------

Pick up a fixup entry matching with the given model string or SSID.
If a fixup was already set beforehand, the function doesn't do anything.
When a special model string "nofixup" is given, also no fixup is applied.

The function tries to find the matching model name at first, if given.
If nothing matched, try to look up the PCI SSID.
If still nothing matched, try to look up the codec SSID.

.. This file was automatic generated / don't edit.


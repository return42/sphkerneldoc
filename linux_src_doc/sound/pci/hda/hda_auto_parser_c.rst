.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_auto_parser.c

.. _`snd_hda_get_input_pin_attr`:

snd_hda_get_input_pin_attr
==========================

.. c:function:: int snd_hda_get_input_pin_attr(unsigned int def_conf)

    Get the input pin attribute from pin config

    :param unsigned int def_conf:
        pin configuration value

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

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct auto_pin_cfg_item \*item:
        ping config item to refer

    :param hda_nid_t pin:
        the pin NID

    :param bool check_location:
        flag to add the jack location prefix

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

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct auto_pin_cfg \*cfg:
        the parsed pin configuration

    :param int input:
        the input index number

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

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID

    :param const struct auto_pin_cfg \*cfg:
        the parsed pin configuration

    :param char \*label:
        the string buffer to store

    :param int maxlen:
        the max length of string buffer (including termination)

    :param int \*indexp:
        the pointer to return the index number (for multiple ctls)

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

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct hda_verb \*list:
        zero-terminated verb list to add

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

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_apply_pincfgs`:

snd_hda_apply_pincfgs
=====================

.. c:function:: void snd_hda_apply_pincfgs(struct hda_codec *codec, const struct hda_pintbl *cfg)

    Set each pin config in the given list

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct hda_pintbl \*cfg:
        NULL-terminated pin config table

.. _`snd_hda_apply_fixup`:

snd_hda_apply_fixup
===================

.. c:function:: void snd_hda_apply_fixup(struct hda_codec *codec, int action)

    Apply the fixup chain with the given action

    :param struct hda_codec \*codec:
        the HDA codec

    :param int action:
        fixup action (HDA_FIXUP_ACT_XXX)

.. _`snd_hda_pick_pin_fixup`:

snd_hda_pick_pin_fixup
======================

.. c:function:: void snd_hda_pick_pin_fixup(struct hda_codec *codec, const struct snd_hda_pin_quirk *pin_quirk, const struct hda_fixup *fixlist)

    Pick up a fixup matching with the pin quirk list

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct snd_hda_pin_quirk \*pin_quirk:
        zero-terminated pin quirk list

    :param const struct hda_fixup \*fixlist:
        the fixup list

.. _`snd_hda_pick_fixup`:

snd_hda_pick_fixup
==================

.. c:function:: void snd_hda_pick_fixup(struct hda_codec *codec, const struct hda_model_fixup *models, const struct snd_pci_quirk *quirk, const struct hda_fixup *fixlist)

    Pick up a fixup matching with PCI/codec SSID or model string

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct hda_model_fixup \*models:
        NULL-terminated model string list

    :param const struct snd_pci_quirk \*quirk:
        zero-terminated PCI/codec SSID quirk list

    :param const struct hda_fixup \*fixlist:
        the fixup list

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


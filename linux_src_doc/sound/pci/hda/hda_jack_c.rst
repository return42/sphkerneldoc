.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_jack.c

.. _`is_jack_detectable`:

is_jack_detectable
==================

.. c:function:: bool is_jack_detectable(struct hda_codec *codec, hda_nid_t nid)

    Check whether the given pin is jack-detectable

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID

.. _`is_jack_detectable.description`:

Description
-----------

Check whether the given pin is capable to report the jack detection.
The jack detection might not work by various reasons, e.g. the jack
detection is prohibited in the codec level, the pin config has
AC_DEFCFG_MISC_NO_PRESENCE bit, no unsol support, etc.

.. _`snd_hda_jack_tbl_get`:

snd_hda_jack_tbl_get
====================

.. c:function:: struct hda_jack_tbl *snd_hda_jack_tbl_get(struct hda_codec *codec, hda_nid_t nid)

    query the jack-table entry for the given NID

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID to refer to

.. _`snd_hda_jack_tbl_get_from_tag`:

snd_hda_jack_tbl_get_from_tag
=============================

.. c:function:: struct hda_jack_tbl *snd_hda_jack_tbl_get_from_tag(struct hda_codec *codec, unsigned char tag)

    query the jack-table entry for the given tag

    :param struct hda_codec \*codec:
        the HDA codec

    :param unsigned char tag:
        tag value to refer to

.. _`snd_hda_jack_tbl_new`:

snd_hda_jack_tbl_new
====================

.. c:function:: struct hda_jack_tbl *snd_hda_jack_tbl_new(struct hda_codec *codec, hda_nid_t nid)

    create a jack-table entry for the given NID

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID to assign

.. _`snd_hda_jack_set_dirty_all`:

snd_hda_jack_set_dirty_all
==========================

.. c:function:: void snd_hda_jack_set_dirty_all(struct hda_codec *codec)

    Mark all the cached as dirty

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_jack_set_dirty_all.description`:

Description
-----------

This function sets the dirty flag to all entries of jack table.
It's called from the resume path in hda_codec.c.

.. _`snd_hda_pin_sense`:

snd_hda_pin_sense
=================

.. c:function:: u32 snd_hda_pin_sense(struct hda_codec *codec, hda_nid_t nid)

    execute pin sense measurement

    :param struct hda_codec \*codec:
        the CODEC to sense

    :param hda_nid_t nid:
        the pin NID to sense

.. _`snd_hda_pin_sense.description`:

Description
-----------

Execute necessary pin sense measurement and return its Presence Detect,
Impedance, ELD Valid etc. status bits.

.. _`snd_hda_jack_detect_state`:

snd_hda_jack_detect_state
=========================

.. c:function:: int snd_hda_jack_detect_state(struct hda_codec *codec, hda_nid_t nid)

    query pin Presence Detect status

    :param struct hda_codec \*codec:
        the CODEC to sense

    :param hda_nid_t nid:
        the pin NID to sense

.. _`snd_hda_jack_detect_state.description`:

Description
-----------

Query and return the pin's Presence Detect status, as either
HDA_JACK_NOT_PRESENT, HDA_JACK_PRESENT or HDA_JACK_PHANTOM.

.. _`snd_hda_jack_detect_enable_callback`:

snd_hda_jack_detect_enable_callback
===================================

.. c:function:: struct hda_jack_callback *snd_hda_jack_detect_enable_callback(struct hda_codec *codec, hda_nid_t nid, hda_jack_callback_fn func)

    enable the jack-detection

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID to enable

    :param hda_jack_callback_fn func:
        callback function to register

.. _`snd_hda_jack_detect_enable_callback.description`:

Description
-----------

In the case of error, the return value will be a pointer embedded with
errno.  Check and handle the return value appropriately with standard
macros such as @\ :c:func:`IS_ERR`\  and @\ :c:func:`PTR_ERR`\ .

.. _`snd_hda_jack_detect_enable`:

snd_hda_jack_detect_enable
==========================

.. c:function:: int snd_hda_jack_detect_enable(struct hda_codec *codec, hda_nid_t nid)

    Enable the jack detection on the given pin

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID to enable jack detection

.. _`snd_hda_jack_detect_enable.description`:

Description
-----------

Enable the jack detection with the default callback.  Returns zero if
successful or a negative error code.

.. _`snd_hda_jack_set_gating_jack`:

snd_hda_jack_set_gating_jack
============================

.. c:function:: int snd_hda_jack_set_gating_jack(struct hda_codec *codec, hda_nid_t gated_nid, hda_nid_t gating_nid)

    Set gating jack.

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t gated_nid:
        gated pin NID

    :param hda_nid_t gating_nid:
        gating pin NID

.. _`snd_hda_jack_set_gating_jack.description`:

Description
-----------

Indicates the gated jack is only valid when the gating jack is plugged.

.. _`snd_hda_jack_report_sync`:

snd_hda_jack_report_sync
========================

.. c:function:: void snd_hda_jack_report_sync(struct hda_codec *codec)

    sync the states of all jacks and report if changed

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_jack_add_kctl`:

snd_hda_jack_add_kctl
=====================

.. c:function:: int snd_hda_jack_add_kctl(struct hda_codec *codec, hda_nid_t nid, const char *name, bool phantom_jack)

    Add a kctl for the given pin

    :param struct hda_codec \*codec:
        the HDA codec

    :param hda_nid_t nid:
        pin NID to assign

    :param const char \*name:
        string name for the jack

    :param bool phantom_jack:
        flag to deal as a phantom jack

.. _`snd_hda_jack_add_kctl.description`:

Description
-----------

This assigns a jack-detection kctl to the given pin.  The kcontrol
will have the given name and index.

.. _`snd_hda_jack_add_kctls`:

snd_hda_jack_add_kctls
======================

.. c:function:: int snd_hda_jack_add_kctls(struct hda_codec *codec, const struct auto_pin_cfg *cfg)

    Add kctls for all pins included in the given pincfg

    :param struct hda_codec \*codec:
        the HDA codec

    :param const struct auto_pin_cfg \*cfg:
        pin config table to parse

.. _`snd_hda_jack_unsol_event`:

snd_hda_jack_unsol_event
========================

.. c:function:: void snd_hda_jack_unsol_event(struct hda_codec *codec, unsigned int res)

    Handle an unsolicited event

    :param struct hda_codec \*codec:
        the HDA codec

    :param unsigned int res:
        the unsolicited event data

.. _`snd_hda_jack_poll_all`:

snd_hda_jack_poll_all
=====================

.. c:function:: void snd_hda_jack_poll_all(struct hda_codec *codec)

    Poll all jacks

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_jack_poll_all.description`:

Description
-----------

Poll all detectable jacks with dirty flag, update the status, call
callbacks and call \ :c:func:`snd_hda_jack_report_sync`\  if any changes are found.

.. This file was automatic generated / don't edit.


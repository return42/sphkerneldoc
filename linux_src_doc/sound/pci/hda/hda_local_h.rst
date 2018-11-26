.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_local.h

.. _`snd_hda_set_pin_ctl`:

snd_hda_set_pin_ctl
===================

.. c:function:: int snd_hda_set_pin_ctl(struct hda_codec *codec, hda_nid_t pin, unsigned int val)

    Set a pin-control value safely

    :param codec:
        the codec instance
    :type codec: struct hda_codec \*

    :param pin:
        the pin NID to set the control
    :type pin: hda_nid_t

    :param val:
        the pin-control value (AC_PINCTL\_\* bits)
    :type val: unsigned int

.. _`snd_hda_set_pin_ctl.description`:

Description
-----------

This function sets the pin-control value to the given pin, but
filters out the invalid pin-control bits when the pin has no such
capabilities.  For example, when PIN_HP is passed but the pin has no
HP-drive capability, the HP bit is omitted.

The function doesn't check the input VREF capability bits, though.
Use \ :c:func:`snd_hda_get_default_vref`\  to guess the right value.
Also, this function is only for analog pins, not for HDMI pins.

.. _`snd_hda_set_pin_ctl_cache`:

snd_hda_set_pin_ctl_cache
=========================

.. c:function:: int snd_hda_set_pin_ctl_cache(struct hda_codec *codec, hda_nid_t pin, unsigned int val)

    Set a pin-control value safely

    :param codec:
        the codec instance
    :type codec: struct hda_codec \*

    :param pin:
        the pin NID to set the control
    :type pin: hda_nid_t

    :param val:
        the pin-control value (AC_PINCTL\_\* bits)
    :type val: unsigned int

.. _`snd_hda_set_pin_ctl_cache.description`:

Description
-----------

Just like \ :c:func:`snd_hda_set_pin_ctl`\  but write to cache as well.

.. _`snd_hda_query_pin_caps`:

snd_hda_query_pin_caps
======================

.. c:function:: u32 snd_hda_query_pin_caps(struct hda_codec *codec, hda_nid_t nid)

    Query PIN capabilities

    :param codec:
        the HD-auio codec
    :type codec: struct hda_codec \*

    :param nid:
        the NID to query
    :type nid: hda_nid_t

.. _`snd_hda_query_pin_caps.description`:

Description
-----------

Query PIN capabilities for the given widget.
Returns the obtained capability bits.

When cap bits have been already read, this doesn't read again but
returns the cached value.

.. _`snd_hda_override_pin_caps`:

snd_hda_override_pin_caps
=========================

.. c:function:: int snd_hda_override_pin_caps(struct hda_codec *codec, hda_nid_t nid, unsigned int caps)

    Override the pin capabilities

    :param codec:
        the CODEC
    :type codec: struct hda_codec \*

    :param nid:
        the NID to override
    :type nid: hda_nid_t

    :param caps:
        the capability bits to set
    :type caps: unsigned int

.. _`snd_hda_override_pin_caps.description`:

Description
-----------

Override the cached PIN capabilitiy bits value by the given one.

Returns zero if successful or a negative error code.

.. This file was automatic generated / don't edit.


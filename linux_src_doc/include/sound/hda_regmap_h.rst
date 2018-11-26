.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/hda_regmap.h

.. _`snd_hdac_regmap_encode_verb`:

snd_hdac_regmap_encode_verb
===========================

.. c:function::  snd_hdac_regmap_encode_verb( nid,  verb)

    encode the verb to a pseudo register

    :param nid:
        widget NID
    :type nid: 

    :param verb:
        codec verb
    :type verb: 

.. _`snd_hdac_regmap_encode_verb.description`:

Description
-----------

Returns an encoded pseudo register.

.. _`snd_hdac_regmap_encode_amp`:

snd_hdac_regmap_encode_amp
==========================

.. c:function::  snd_hdac_regmap_encode_amp( nid,  ch,  dir,  idx)

    encode the AMP verb to a pseudo register

    :param nid:
        widget NID
    :type nid: 

    :param ch:
        channel (left = 0, right = 1)
    :type ch: 

    :param dir:
        direction (#HDA_INPUT, #HDA_OUTPUT)
    :type dir: 

    :param idx:
        input index value
    :type idx: 

.. _`snd_hdac_regmap_encode_amp.description`:

Description
-----------

Returns an encoded pseudo register.

.. _`snd_hdac_regmap_encode_amp_stereo`:

snd_hdac_regmap_encode_amp_stereo
=================================

.. c:function::  snd_hdac_regmap_encode_amp_stereo( nid,  dir,  idx)

    encode a pseudo register for stereo AMPs

    :param nid:
        widget NID
    :type nid: 

    :param dir:
        direction (#HDA_INPUT, #HDA_OUTPUT)
    :type dir: 

    :param idx:
        input index value
    :type idx: 

.. _`snd_hdac_regmap_encode_amp_stereo.description`:

Description
-----------

Returns an encoded pseudo register.

.. _`snd_hdac_regmap_write`:

snd_hdac_regmap_write
=====================

.. c:function:: int snd_hdac_regmap_write(struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int val)

    Write a verb with caching

    :param codec:
        *undescribed*
    :type codec: struct hdac_device \*

    :param nid:
        codec NID
    :type nid: hda_nid_t

    :param verb:
        *undescribed*
    :type verb: unsigned int

    :param val:
        value to write
    :type val: unsigned int

.. _`snd_hdac_regmap_write.description`:

Description
-----------

For writing an amp value, use \ :c:func:`snd_hdac_regmap_update_amp`\ .

.. _`snd_hdac_regmap_update`:

snd_hdac_regmap_update
======================

.. c:function:: int snd_hdac_regmap_update(struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int mask, unsigned int val)

    Update a verb value with caching

    :param codec:
        *undescribed*
    :type codec: struct hdac_device \*

    :param nid:
        codec NID
    :type nid: hda_nid_t

    :param verb:
        verb to update
    :type verb: unsigned int

    :param mask:
        bit mask to update
    :type mask: unsigned int

    :param val:
        value to update
    :type val: unsigned int

.. _`snd_hdac_regmap_update.description`:

Description
-----------

For updating an amp value, use \ :c:func:`snd_hdac_regmap_update_amp`\ .

.. _`snd_hdac_regmap_read`:

snd_hdac_regmap_read
====================

.. c:function:: int snd_hdac_regmap_read(struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int *val)

    Read a verb with caching

    :param codec:
        *undescribed*
    :type codec: struct hdac_device \*

    :param nid:
        codec NID
    :type nid: hda_nid_t

    :param verb:
        verb to read
    :type verb: unsigned int

    :param val:
        pointer to store the value
    :type val: unsigned int \*

.. _`snd_hdac_regmap_read.description`:

Description
-----------

For reading an amp value, use \ :c:func:`snd_hda_regmap_get_amp`\ .

.. _`snd_hdac_regmap_get_amp`:

snd_hdac_regmap_get_amp
=======================

.. c:function:: int snd_hdac_regmap_get_amp(struct hdac_device *codec, hda_nid_t nid, int ch, int dir, int idx)

    Read AMP value

    :param codec:
        HD-audio codec
    :type codec: struct hdac_device \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param ch:
        channel (left=0 or right=1)
    :type ch: int

    :param dir:
        *undescribed*
    :type dir: int

    :param idx:
        *undescribed*
    :type idx: int

.. _`snd_hdac_regmap_get_amp.description`:

Description
-----------

Read AMP value.  The volume is between 0 to 0x7f, 0x80 = mute bit.
Returns the value or a negative error.

.. _`snd_hdac_regmap_update_amp`:

snd_hdac_regmap_update_amp
==========================

.. c:function:: int snd_hdac_regmap_update_amp(struct hdac_device *codec, hda_nid_t nid, int ch, int dir, int idx, int mask, int val)

    update the AMP value

    :param codec:
        HD-audio codec
    :type codec: struct hdac_device \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param ch:
        channel (left=0 or right=1)
    :type ch: int

    :param dir:
        *undescribed*
    :type dir: int

    :param idx:
        the index value (only for input direction)
    :type idx: int

    :param mask:
        bit mask to set
    :type mask: int

    :param val:
        the bits value to set
    :type val: int

.. _`snd_hdac_regmap_update_amp.description`:

Description
-----------

Update the AMP value with a bit mask.
Returns 0 if the value is unchanged, 1 if changed, or a negative error.

.. _`snd_hdac_regmap_get_amp_stereo`:

snd_hdac_regmap_get_amp_stereo
==============================

.. c:function:: int snd_hdac_regmap_get_amp_stereo(struct hdac_device *codec, hda_nid_t nid, int dir, int idx)

    Read stereo AMP values

    :param codec:
        HD-audio codec
    :type codec: struct hdac_device \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param dir:
        *undescribed*
    :type dir: int

    :param idx:
        *undescribed*
    :type idx: int

.. _`snd_hdac_regmap_get_amp_stereo.description`:

Description
-----------

Read stereo AMP values.  The lower byte is left, the upper byte is right.
Returns the value or a negative error.

.. _`snd_hdac_regmap_update_amp_stereo`:

snd_hdac_regmap_update_amp_stereo
=================================

.. c:function:: int snd_hdac_regmap_update_amp_stereo(struct hdac_device *codec, hda_nid_t nid, int dir, int idx, int mask, int val)

    update the stereo AMP value

    :param codec:
        HD-audio codec
    :type codec: struct hdac_device \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param dir:
        *undescribed*
    :type dir: int

    :param idx:
        the index value (only for input direction)
    :type idx: int

    :param mask:
        bit mask to set
    :type mask: int

    :param val:
        the bits value to set
    :type val: int

.. _`snd_hdac_regmap_update_amp_stereo.description`:

Description
-----------

Update the stereo AMP value with a bit mask.
The lower byte is left, the upper byte is right.
Returns 0 if the value is unchanged, 1 if changed, or a negative error.

.. _`snd_hdac_regmap_sync_node`:

snd_hdac_regmap_sync_node
=========================

.. c:function:: void snd_hdac_regmap_sync_node(struct hdac_device *codec, hda_nid_t nid)

    sync the widget node attributes

    :param codec:
        HD-audio codec
    :type codec: struct hdac_device \*

    :param nid:
        NID to sync
    :type nid: hda_nid_t

.. This file was automatic generated / don't edit.


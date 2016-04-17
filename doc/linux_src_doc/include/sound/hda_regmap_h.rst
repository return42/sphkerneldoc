.. -*- coding: utf-8; mode: rst -*-

============
hda_regmap.h
============


.. _`snd_hdac_regmap_encode_verb`:

snd_hdac_regmap_encode_verb
===========================

.. c:function:: snd_hdac_regmap_encode_verb ( nid,  verb)

    encode the verb to a pseudo register

    :param nid:
        widget NID

    :param verb:
        codec verb



.. _`snd_hdac_regmap_encode_verb.description`:

Description
-----------

Returns an encoded pseudo register.



.. _`snd_hdac_regmap_encode_amp`:

snd_hdac_regmap_encode_amp
==========================

.. c:function:: snd_hdac_regmap_encode_amp ( nid,  ch,  dir,  idx)

    encode the AMP verb to a pseudo register

    :param nid:
        widget NID

    :param ch:
        channel (left = 0, right = 1)

    :param dir:
        direction (#HDA_INPUT, #HDA_OUTPUT)

    :param idx:
        input index value



.. _`snd_hdac_regmap_encode_amp.description`:

Description
-----------

Returns an encoded pseudo register.



.. _`snd_hdac_regmap_encode_amp_stereo`:

snd_hdac_regmap_encode_amp_stereo
=================================

.. c:function:: snd_hdac_regmap_encode_amp_stereo ( nid,  dir,  idx)

    encode a pseudo register for stereo AMPs

    :param nid:
        widget NID

    :param dir:
        direction (#HDA_INPUT, #HDA_OUTPUT)

    :param idx:
        input index value



.. _`snd_hdac_regmap_encode_amp_stereo.description`:

Description
-----------

Returns an encoded pseudo register.



.. _`snd_hdac_regmap_write`:

snd_hdac_regmap_write
=====================

.. c:function:: int snd_hdac_regmap_write (struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int val)

    Write a verb with caching

    :param struct hdac_device \*codec:

        *undescribed*

    :param hda_nid_t nid:
        codec NID

    :param unsigned int verb:

        *undescribed*

    :param unsigned int val:
        value to write



.. _`snd_hdac_regmap_write.description`:

Description
-----------

For writing an amp value, use :c:func:`snd_hdac_regmap_update_amp`.



.. _`snd_hdac_regmap_update`:

snd_hdac_regmap_update
======================

.. c:function:: int snd_hdac_regmap_update (struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int mask, unsigned int val)

    Update a verb value with caching

    :param struct hdac_device \*codec:

        *undescribed*

    :param hda_nid_t nid:
        codec NID

    :param unsigned int verb:
        verb to update

    :param unsigned int mask:
        bit mask to update

    :param unsigned int val:
        value to update



.. _`snd_hdac_regmap_update.description`:

Description
-----------

For updating an amp value, use :c:func:`snd_hdac_regmap_update_amp`.



.. _`snd_hdac_regmap_read`:

snd_hdac_regmap_read
====================

.. c:function:: int snd_hdac_regmap_read (struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int *val)

    Read a verb with caching

    :param struct hdac_device \*codec:

        *undescribed*

    :param hda_nid_t nid:
        codec NID

    :param unsigned int verb:
        verb to read

    :param unsigned int \*val:
        pointer to store the value



.. _`snd_hdac_regmap_read.description`:

Description
-----------

For reading an amp value, use :c:func:`snd_hda_regmap_get_amp`.



.. _`snd_hdac_regmap_get_amp`:

snd_hdac_regmap_get_amp
=======================

.. c:function:: int snd_hdac_regmap_get_amp (struct hdac_device *codec, hda_nid_t nid, int ch, int dir, int idx)

    Read AMP value

    :param struct hdac_device \*codec:
        HD-audio codec

    :param hda_nid_t nid:
        NID to read the AMP value

    :param int ch:
        channel (left=0 or right=1)

    :param int dir:

        *undescribed*

    :param int idx:

        *undescribed*



.. _`snd_hdac_regmap_get_amp.description`:

Description
-----------

Read AMP value.  The volume is between 0 to 0x7f, 0x80 = mute bit.
Returns the value or a negative error.



.. _`snd_hdac_regmap_update_amp`:

snd_hdac_regmap_update_amp
==========================

.. c:function:: int snd_hdac_regmap_update_amp (struct hdac_device *codec, hda_nid_t nid, int ch, int dir, int idx, int mask, int val)

    update the AMP value

    :param struct hdac_device \*codec:
        HD-audio codec

    :param hda_nid_t nid:
        NID to read the AMP value

    :param int ch:
        channel (left=0 or right=1)

    :param int dir:

        *undescribed*

    :param int idx:
        the index value (only for input direction)

    :param int mask:
        bit mask to set

    :param int val:
        the bits value to set



.. _`snd_hdac_regmap_update_amp.description`:

Description
-----------

Update the AMP value with a bit mask.
Returns 0 if the value is unchanged, 1 if changed, or a negative error.



.. _`snd_hdac_regmap_get_amp_stereo`:

snd_hdac_regmap_get_amp_stereo
==============================

.. c:function:: int snd_hdac_regmap_get_amp_stereo (struct hdac_device *codec, hda_nid_t nid, int dir, int idx)

    Read stereo AMP values

    :param struct hdac_device \*codec:
        HD-audio codec

    :param hda_nid_t nid:
        NID to read the AMP value

    :param int dir:

        *undescribed*

    :param int idx:

        *undescribed*



.. _`snd_hdac_regmap_get_amp_stereo.description`:

Description
-----------

Read stereo AMP values.  The lower byte is left, the upper byte is right.
Returns the value or a negative error.



.. _`snd_hdac_regmap_update_amp_stereo`:

snd_hdac_regmap_update_amp_stereo
=================================

.. c:function:: int snd_hdac_regmap_update_amp_stereo (struct hdac_device *codec, hda_nid_t nid, int dir, int idx, int mask, int val)

    update the stereo AMP value

    :param struct hdac_device \*codec:
        HD-audio codec

    :param hda_nid_t nid:
        NID to read the AMP value

    :param int dir:

        *undescribed*

    :param int idx:
        the index value (only for input direction)

    :param int mask:
        bit mask to set

    :param int val:
        the bits value to set



.. _`snd_hdac_regmap_update_amp_stereo.description`:

Description
-----------

Update the stereo AMP value with a bit mask.
The lower byte is left, the upper byte is right.
Returns 0 if the value is unchanged, 1 if changed, or a negative error.



.. _`snd_hdac_regmap_sync_node`:

snd_hdac_regmap_sync_node
=========================

.. c:function:: void snd_hdac_regmap_sync_node (struct hdac_device *codec, hda_nid_t nid)

    sync the widget node attributes

    :param struct hdac_device \*codec:
        HD-audio codec

    :param hda_nid_t nid:
        NID to sync


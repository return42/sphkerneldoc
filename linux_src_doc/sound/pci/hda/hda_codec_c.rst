.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_codec.c

.. _`snd_hda_sequence_write`:

snd_hda_sequence_write
======================

.. c:function:: void snd_hda_sequence_write(struct hda_codec *codec, const struct hda_verb *seq)

    sequence writes

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param seq:
        VERB array to send
    :type seq: const struct hda_verb \*

.. _`snd_hda_sequence_write.description`:

Description
-----------

Send the commands sequentially from the given array.
The array must be terminated with NID=0.

.. _`snd_hda_get_conn_list`:

snd_hda_get_conn_list
=====================

.. c:function:: int snd_hda_get_conn_list(struct hda_codec *codec, hda_nid_t nid, const hda_nid_t **listp)

    get connection list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to parse
    :type nid: hda_nid_t

    :param listp:
        the pointer to store NID list
    :type listp: const hda_nid_t \*\*

.. _`snd_hda_get_conn_list.description`:

Description
-----------

Parses the connection list of the given widget and stores the pointer
to the list of NIDs.

Returns the number of connections, or a negative error code.

Note that the returned pointer isn't protected against the list
modification.  If \ :c:func:`snd_hda_override_conn_list`\  might be called
concurrently, protect with a mutex appropriately.

.. _`snd_hda_get_connections`:

snd_hda_get_connections
=======================

.. c:function:: int snd_hda_get_connections(struct hda_codec *codec, hda_nid_t nid, hda_nid_t *conn_list, int max_conns)

    copy connection list

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to parse
    :type nid: hda_nid_t

    :param conn_list:
        connection list array; when NULL, checks only the size
    :type conn_list: hda_nid_t \*

    :param max_conns:
        max. number of connections to store
    :type max_conns: int

.. _`snd_hda_get_connections.description`:

Description
-----------

Parses the connection list of the given widget and stores the list
of NIDs.

Returns the number of connections, or a negative error code.

.. _`snd_hda_override_conn_list`:

snd_hda_override_conn_list
==========================

.. c:function:: int snd_hda_override_conn_list(struct hda_codec *codec, hda_nid_t nid, int len, const hda_nid_t *list)

    add/modify the connection-list to cache

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to parse
    :type nid: hda_nid_t

    :param len:
        number of connection list entries
    :type len: int

    :param list:
        the list of connection entries
    :type list: const hda_nid_t \*

.. _`snd_hda_override_conn_list.description`:

Description
-----------

Add or modify the given connection-list to the cache.  If the corresponding
cache already exists, invalidate it and append a new one.

Returns zero or a negative error code.

.. _`snd_hda_get_conn_index`:

snd_hda_get_conn_index
======================

.. c:function:: int snd_hda_get_conn_index(struct hda_codec *codec, hda_nid_t mux, hda_nid_t nid, int recursive)

    get the connection index of the given NID

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mux:
        NID containing the list
    :type mux: hda_nid_t

    :param nid:
        NID to select
    :type nid: hda_nid_t

    :param recursive:
        1 when searching NID recursively, otherwise 0
    :type recursive: int

.. _`snd_hda_get_conn_index.description`:

Description
-----------

Parses the connection list of the widget \ ``mux``\  and checks whether the
widget \ ``nid``\  is present.  If it is, return the connection index.
Otherwise it returns -1.

.. _`snd_hda_get_num_devices`:

snd_hda_get_num_devices
=======================

.. c:function:: unsigned int snd_hda_get_num_devices(struct hda_codec *codec, hda_nid_t nid)

    get DEVLIST_LEN parameter of the given widget

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID of the pin to parse
    :type nid: hda_nid_t

.. _`snd_hda_get_num_devices.description`:

Description
-----------

Get the device entry number on the given widget. This is a feature of
DP MST audio. Each pin can have several device entries in it.

.. _`snd_hda_get_devices`:

snd_hda_get_devices
===================

.. c:function:: int snd_hda_get_devices(struct hda_codec *codec, hda_nid_t nid, u8 *dev_list, int max_devices)

    copy device list without cache

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID of the pin to parse
    :type nid: hda_nid_t

    :param dev_list:
        device list array
    :type dev_list: u8 \*

    :param max_devices:
        max. number of devices to store
    :type max_devices: int

.. _`snd_hda_get_devices.description`:

Description
-----------

Copy the device list. This info is dynamic and so not cached.
Currently called only from hda_proc.c, so not exported.

.. _`snd_hda_get_dev_select`:

snd_hda_get_dev_select
======================

.. c:function:: int snd_hda_get_dev_select(struct hda_codec *codec, hda_nid_t nid)

    get device entry select on the pin

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID of the pin to get device entry select
    :type nid: hda_nid_t

.. _`snd_hda_get_dev_select.description`:

Description
-----------

Get the devcie entry select on the pin. Return the device entry
id selected on the pin. Return 0 means the first device entry
is selected or MST is not supported.

.. _`snd_hda_set_dev_select`:

snd_hda_set_dev_select
======================

.. c:function:: int snd_hda_set_dev_select(struct hda_codec *codec, hda_nid_t nid, int dev_id)

    set device entry select on the pin

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID of the pin to set device entry select
    :type nid: hda_nid_t

    :param dev_id:
        device entry id to be set
    :type dev_id: int

.. _`snd_hda_set_dev_select.description`:

Description
-----------

Set the device entry select on the pin nid.

.. _`snd_hda_codec_set_pincfg`:

snd_hda_codec_set_pincfg
========================

.. c:function:: int snd_hda_codec_set_pincfg(struct hda_codec *codec, hda_nid_t nid, unsigned int cfg)

    Override a pin default configuration

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to set the pin config
    :type nid: hda_nid_t

    :param cfg:
        the pin default config value
    :type cfg: unsigned int

.. _`snd_hda_codec_set_pincfg.description`:

Description
-----------

Override a pin default configuration value in the cache.
This value can be read by \ :c:func:`snd_hda_codec_get_pincfg`\  in a higher
priority than the real hardware value.

.. _`snd_hda_codec_get_pincfg`:

snd_hda_codec_get_pincfg
========================

.. c:function:: unsigned int snd_hda_codec_get_pincfg(struct hda_codec *codec, hda_nid_t nid)

    Obtain a pin-default configuration

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to get the pin config
    :type nid: hda_nid_t

.. _`snd_hda_codec_get_pincfg.description`:

Description
-----------

Get the current pin config value of the given pin NID.
If the pincfg value is cached or overridden via sysfs or driver,
returns the cached value.

.. _`snd_hda_codec_set_pin_target`:

snd_hda_codec_set_pin_target
============================

.. c:function:: int snd_hda_codec_set_pin_target(struct hda_codec *codec, hda_nid_t nid, unsigned int val)

    remember the current pinctl target value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        pin NID
    :type nid: hda_nid_t

    :param val:
        assigned pinctl value
    :type val: unsigned int

.. _`snd_hda_codec_set_pin_target.description`:

Description
-----------

This function stores the given value to a pinctl target value in the
pincfg table.  This isn't always as same as the actually written value
but can be referred at any time via \ :c:func:`snd_hda_codec_get_pin_target`\ .

.. _`snd_hda_codec_get_pin_target`:

snd_hda_codec_get_pin_target
============================

.. c:function:: int snd_hda_codec_get_pin_target(struct hda_codec *codec, hda_nid_t nid)

    return the current pinctl target value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        pin NID
    :type nid: hda_nid_t

.. _`snd_hda_shutup_pins`:

snd_hda_shutup_pins
===================

.. c:function:: void snd_hda_shutup_pins(struct hda_codec *codec)

    Shut up all pins

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_shutup_pins.description`:

Description
-----------

Clear all pin controls to shup up before suspend for avoiding click noise.
The controls aren't cached so that they can be resumed properly.

.. _`snd_hda_codec_new`:

snd_hda_codec_new
=================

.. c:function:: int snd_hda_codec_new(struct hda_bus *bus, struct snd_card *card, unsigned int codec_addr, struct hda_codec **codecp)

    create a HDA codec

    :param bus:
        the bus to assign
    :type bus: struct hda_bus \*

    :param card:
        *undescribed*
    :type card: struct snd_card \*

    :param codec_addr:
        the codec address
    :type codec_addr: unsigned int

    :param codecp:
        the pointer to store the generated codec
    :type codecp: struct hda_codec \*\*

.. _`snd_hda_codec_new.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hda_codec_update_widgets`:

snd_hda_codec_update_widgets
============================

.. c:function:: int snd_hda_codec_update_widgets(struct hda_codec *codec)

    Refresh widget caps and pin defaults

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

.. _`snd_hda_codec_update_widgets.description`:

Description
-----------

Forcibly refresh the all widget caps and the init pin configurations of
the given codec.

.. _`snd_hda_codec_setup_stream`:

snd_hda_codec_setup_stream
==========================

.. c:function:: void snd_hda_codec_setup_stream(struct hda_codec *codec, hda_nid_t nid, u32 stream_tag, int channel_id, int format)

    set up the codec for streaming

    :param codec:
        the CODEC to set up
    :type codec: struct hda_codec \*

    :param nid:
        the NID to set up
    :type nid: hda_nid_t

    :param stream_tag:
        stream tag to pass, it's between 0x1 and 0xf.
    :type stream_tag: u32

    :param channel_id:
        channel id to pass, zero based.
    :type channel_id: int

    :param format:
        stream format.
    :type format: int

.. _`__snd_hda_codec_cleanup_stream`:

\__snd_hda_codec_cleanup_stream
===============================

.. c:function:: void __snd_hda_codec_cleanup_stream(struct hda_codec *codec, hda_nid_t nid, int do_now)

    clean up the codec for closing

    :param codec:
        the CODEC to clean up
    :type codec: struct hda_codec \*

    :param nid:
        the NID to clean up
    :type nid: hda_nid_t

    :param do_now:
        really clean up the stream instead of clearing the active flag
    :type do_now: int

.. _`query_amp_caps`:

query_amp_caps
==============

.. c:function:: u32 query_amp_caps(struct hda_codec *codec, hda_nid_t nid, int direction)

    query AMP capabilities

    :param codec:
        the HD-auio codec
    :type codec: struct hda_codec \*

    :param nid:
        the NID to query
    :type nid: hda_nid_t

    :param direction:
        either #HDA_INPUT or #HDA_OUTPUT
    :type direction: int

.. _`query_amp_caps.description`:

Description
-----------

Query AMP capabilities for the given widget and direction.
Returns the obtained capability bits.

When cap bits have been already read, this doesn't read again but
returns the cached value.

.. _`snd_hda_check_amp_caps`:

snd_hda_check_amp_caps
======================

.. c:function:: bool snd_hda_check_amp_caps(struct hda_codec *codec, hda_nid_t nid, int dir, unsigned int bits)

    query AMP capabilities

    :param codec:
        the HD-audio codec
    :type codec: struct hda_codec \*

    :param nid:
        the NID to query
    :type nid: hda_nid_t

    :param dir:
        either #HDA_INPUT or #HDA_OUTPUT
    :type dir: int

    :param bits:
        bit mask to check the result
    :type bits: unsigned int

.. _`snd_hda_check_amp_caps.description`:

Description
-----------

Check whether the widget has the given amp capability for the direction.

.. _`snd_hda_override_amp_caps`:

snd_hda_override_amp_caps
=========================

.. c:function:: int snd_hda_override_amp_caps(struct hda_codec *codec, hda_nid_t nid, int dir, unsigned int caps)

    Override the AMP capabilities

    :param codec:
        the CODEC to clean up
    :type codec: struct hda_codec \*

    :param nid:
        the NID to clean up
    :type nid: hda_nid_t

    :param dir:
        either #HDA_INPUT or #HDA_OUTPUT
    :type dir: int

    :param caps:
        the capability bits to set
    :type caps: unsigned int

.. _`snd_hda_override_amp_caps.description`:

Description
-----------

Override the cached AMP caps bits value by the given one.
This function is useful if the driver needs to adjust the AMP ranges,
e.g. limit to 0dB, etc.

Returns zero if successful or a negative error code.

.. _`snd_hda_codec_amp_update`:

snd_hda_codec_amp_update
========================

.. c:function:: int snd_hda_codec_amp_update(struct hda_codec *codec, hda_nid_t nid, int ch, int dir, int idx, int mask, int val)

    update the AMP mono value

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param ch:
        channel to update (0 or 1)
    :type ch: int

    :param dir:
        #HDA_INPUT or #HDA_OUTPUT
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

.. _`snd_hda_codec_amp_update.description`:

Description
-----------

Update the AMP values for the given channel, direction and index.

.. _`snd_hda_codec_amp_stereo`:

snd_hda_codec_amp_stereo
========================

.. c:function:: int snd_hda_codec_amp_stereo(struct hda_codec *codec, hda_nid_t nid, int direction, int idx, int mask, int val)

    update the AMP stereo values

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param direction:
        #HDA_INPUT or #HDA_OUTPUT
    :type direction: int

    :param idx:
        the index value (only for input direction)
    :type idx: int

    :param mask:
        bit mask to set
    :type mask: int

    :param val:
        the bits value to set
    :type val: int

.. _`snd_hda_codec_amp_stereo.description`:

Description
-----------

Update the AMP values like \ :c:func:`snd_hda_codec_amp_update`\ , but for a
stereo widget with the same mask and value.

.. _`snd_hda_codec_amp_init`:

snd_hda_codec_amp_init
======================

.. c:function:: int snd_hda_codec_amp_init(struct hda_codec *codec, hda_nid_t nid, int ch, int dir, int idx, int mask, int val)

    initialize the AMP value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param ch:
        channel (left=0 or right=1)
    :type ch: int

    :param dir:
        #HDA_INPUT or #HDA_OUTPUT
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

.. _`snd_hda_codec_amp_init.description`:

Description
-----------

Works like \ :c:func:`snd_hda_codec_amp_update`\  but it writes the value only at
the first access.  If the amp was already initialized / updated beforehand,
this does nothing.

.. _`snd_hda_codec_amp_init_stereo`:

snd_hda_codec_amp_init_stereo
=============================

.. c:function:: int snd_hda_codec_amp_init_stereo(struct hda_codec *codec, hda_nid_t nid, int dir, int idx, int mask, int val)

    initialize the stereo AMP value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        NID to read the AMP value
    :type nid: hda_nid_t

    :param dir:
        #HDA_INPUT or #HDA_OUTPUT
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

.. _`snd_hda_codec_amp_init_stereo.description`:

Description
-----------

Call \ :c:func:`snd_hda_codec_amp_init`\  for both stereo channels.

.. _`snd_hda_mixer_amp_volume_info`:

snd_hda_mixer_amp_volume_info
=============================

.. c:function:: int snd_hda_mixer_amp_volume_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Info callback for a standard AMP mixer

    :param kcontrol:
        referred ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        pointer to get/store the data
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_hda_mixer_amp_volume_info.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_mixer_amp_volume_get`:

snd_hda_mixer_amp_volume_get
============================

.. c:function:: int snd_hda_mixer_amp_volume_get(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Get callback for a standard AMP mixer volume

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        pointer to get/store the data
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_hda_mixer_amp_volume_get.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_mixer_amp_volume_put`:

snd_hda_mixer_amp_volume_put
============================

.. c:function:: int snd_hda_mixer_amp_volume_put(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Put callback for a standard AMP mixer volume

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        pointer to get/store the data
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_hda_mixer_amp_volume_put.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_mixer_amp_tlv`:

snd_hda_mixer_amp_tlv
=====================

.. c:function:: int snd_hda_mixer_amp_tlv(struct snd_kcontrol *kcontrol, int op_flag, unsigned int size, unsigned int __user *_tlv)

    TLV callback for a standard AMP mixer volume

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param op_flag:
        operation flag
    :type op_flag: int

    :param size:
        byte size of input TLV
    :type size: unsigned int

    :param _tlv:
        TLV data
    :type _tlv: unsigned int __user \*

.. _`snd_hda_mixer_amp_tlv.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_set_vmaster_tlv`:

snd_hda_set_vmaster_tlv
=======================

.. c:function:: void snd_hda_set_vmaster_tlv(struct hda_codec *codec, hda_nid_t nid, int dir, unsigned int *tlv)

    Set TLV for a virtual master control

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param nid:
        NID of a reference widget
    :type nid: hda_nid_t

    :param dir:
        #HDA_INPUT or #HDA_OUTPUT
    :type dir: int

    :param tlv:
        TLV data to be stored, at least 4 elements
    :type tlv: unsigned int \*

.. _`snd_hda_set_vmaster_tlv.description`:

Description
-----------

Set (static) TLV data for a virtual master volume using the AMP caps
obtained from the reference NID.
The volume range is recalculated as if the max volume is 0dB.

.. _`snd_hda_find_mixer_ctl`:

snd_hda_find_mixer_ctl
======================

.. c:function:: struct snd_kcontrol *snd_hda_find_mixer_ctl(struct hda_codec *codec, const char *name)

    Find a mixer control element with the given name

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param name:
        ctl id name string
    :type name: const char \*

.. _`snd_hda_find_mixer_ctl.description`:

Description
-----------

Get the control element with the given id string and IFACE_MIXER.

.. _`snd_hda_ctl_add`:

snd_hda_ctl_add
===============

.. c:function:: int snd_hda_ctl_add(struct hda_codec *codec, hda_nid_t nid, struct snd_kcontrol *kctl)

    Add a control element and assign to the codec

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param nid:
        corresponding NID (optional)
    :type nid: hda_nid_t

    :param kctl:
        the control element to assign
    :type kctl: struct snd_kcontrol \*

.. _`snd_hda_ctl_add.description`:

Description
-----------

Add the given control element to an array inside the codec instance.
All control elements belonging to a codec are supposed to be added
by this function so that a proper clean-up works at the free or
reconfiguration time.

If non-zero \ ``nid``\  is passed, the NID is assigned to the control element.
The assignment is shown in the codec proc file.

\ :c:func:`snd_hda_ctl_add`\  checks the control subdev id field whether
#HDA_SUBDEV_NID_FLAG bit is set.  If set (and \ ``nid``\  is zero), the lower
bits value is taken as the NID to assign. The #HDA_NID_ITEM_AMP bit
specifies if kctl->private_value is a HDA amplifier value.

.. _`snd_hda_add_nid`:

snd_hda_add_nid
===============

.. c:function:: int snd_hda_add_nid(struct hda_codec *codec, struct snd_kcontrol *kctl, unsigned int index, hda_nid_t nid)

    Assign a NID to a control element

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param kctl:
        the control element to assign
    :type kctl: struct snd_kcontrol \*

    :param index:
        index to kctl
    :type index: unsigned int

    :param nid:
        corresponding NID (optional)
    :type nid: hda_nid_t

.. _`snd_hda_add_nid.description`:

Description
-----------

Add the given control element to an array inside the codec instance.
This function is used when #snd_hda_ctl_add cannot be used for 1:1
NID:KCTL mapping - for example "Capture Source" selector.

.. _`snd_hda_ctls_clear`:

snd_hda_ctls_clear
==================

.. c:function:: void snd_hda_ctls_clear(struct hda_codec *codec)

    Clear all controls assigned to the given codec

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

.. _`snd_hda_lock_devices`:

snd_hda_lock_devices
====================

.. c:function:: int snd_hda_lock_devices(struct hda_bus *bus)

    pseudo device locking

    :param bus:
        the BUS
    :type bus: struct hda_bus \*

.. _`snd_hda_lock_devices.description`:

Description
-----------

toggle card->shutdown to allow/disallow the device access (as a hack)

.. _`snd_hda_unlock_devices`:

snd_hda_unlock_devices
======================

.. c:function:: void snd_hda_unlock_devices(struct hda_bus *bus)

    pseudo device unlocking

    :param bus:
        the BUS
    :type bus: struct hda_bus \*

.. _`snd_hda_codec_reset`:

snd_hda_codec_reset
===================

.. c:function:: int snd_hda_codec_reset(struct hda_codec *codec)

    Clear all objects assigned to the codec

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

.. _`snd_hda_codec_reset.description`:

Description
-----------

This frees the all PCM and control elements assigned to the codec, and
clears the caches and restores the pin default configurations.

When a device is being used, it returns -EBSY.  If successfully freed,
returns zero.

.. _`__snd_hda_add_vmaster`:

\__snd_hda_add_vmaster
======================

.. c:function:: int __snd_hda_add_vmaster(struct hda_codec *codec, char *name, unsigned int *tlv, const char * const *slaves, const char *suffix, bool init_slave_vol, struct snd_kcontrol **ctl_ret)

    create a virtual master control and add slaves

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param name:
        vmaster control name
    :type name: char \*

    :param tlv:
        TLV data (optional)
    :type tlv: unsigned int \*

    :param slaves:
        slave control names (optional)
    :type slaves: const char \* const \*

    :param suffix:
        suffix string to each slave name (optional)
    :type suffix: const char \*

    :param init_slave_vol:
        initialize slaves to unmute/0dB
    :type init_slave_vol: bool

    :param ctl_ret:
        store the vmaster kcontrol in return
    :type ctl_ret: struct snd_kcontrol \*\*

.. _`__snd_hda_add_vmaster.description`:

Description
-----------

Create a virtual master control with the given name.  The TLV data
must be either NULL or a valid data.

\ ``slaves``\  is a NULL-terminated array of strings, each of which is a
slave control name.  All controls with these names are assigned to
the new virtual master control.

This function returns zero if successful or a negative error code.

.. _`snd_hda_add_vmaster_hook`:

snd_hda_add_vmaster_hook
========================

.. c:function:: int snd_hda_add_vmaster_hook(struct hda_codec *codec, struct hda_vmaster_mute_hook *hook, bool expose_enum_ctl)

    Add a vmaster hook for mute-LED

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param hook:
        the vmaster hook object
    :type hook: struct hda_vmaster_mute_hook \*

    :param expose_enum_ctl:
        flag to create an enum ctl
    :type expose_enum_ctl: bool

.. _`snd_hda_add_vmaster_hook.description`:

Description
-----------

Add a mute-LED hook with the given vmaster switch kctl.
When \ ``expose_enum_ctl``\  is set, "Mute-LED Mode" control is automatically
created and associated with the given hook.

.. _`snd_hda_sync_vmaster_hook`:

snd_hda_sync_vmaster_hook
=========================

.. c:function:: void snd_hda_sync_vmaster_hook(struct hda_vmaster_mute_hook *hook)

    Sync vmaster hook

    :param hook:
        the vmaster hook
    :type hook: struct hda_vmaster_mute_hook \*

.. _`snd_hda_sync_vmaster_hook.description`:

Description
-----------

Call the hook with the current value for synchronization.
Should be called in init callback.

.. _`snd_hda_mixer_amp_switch_info`:

snd_hda_mixer_amp_switch_info
=============================

.. c:function:: int snd_hda_mixer_amp_switch_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Info callback for a standard AMP mixer switch

    :param kcontrol:
        referred ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        pointer to get/store the data
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_hda_mixer_amp_switch_info.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_mixer_amp_switch_get`:

snd_hda_mixer_amp_switch_get
============================

.. c:function:: int snd_hda_mixer_amp_switch_get(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Get callback for a standard AMP mixer switch

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        pointer to get/store the data
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_hda_mixer_amp_switch_get.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_mixer_amp_switch_put`:

snd_hda_mixer_amp_switch_put
============================

.. c:function:: int snd_hda_mixer_amp_switch_put(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_value *ucontrol)

    Put callback for a standard AMP mixer switch

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param ucontrol:
        pointer to get/store the data
    :type ucontrol: struct snd_ctl_elem_value \*

.. _`snd_hda_mixer_amp_switch_put.description`:

Description
-----------

The control element is supposed to have the private_value field
set up via HDA_COMPOSE_AMP_VAL\*() or related macros.

.. _`snd_hda_create_dig_out_ctls`:

snd_hda_create_dig_out_ctls
===========================

.. c:function:: int snd_hda_create_dig_out_ctls(struct hda_codec *codec, hda_nid_t associated_nid, hda_nid_t cvt_nid, int type)

    create Output SPDIF-related controls

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param associated_nid:
        NID that new ctls associated with
    :type associated_nid: hda_nid_t

    :param cvt_nid:
        converter NID
    :type cvt_nid: hda_nid_t

    :param type:
        HDA_PCM_TYPE\_\*
        Creates controls related with the digital output.
        Called from each patch supporting the digital out.
    :type type: int

.. _`snd_hda_create_dig_out_ctls.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hda_spdif_out_of_nid`:

snd_hda_spdif_out_of_nid
========================

.. c:function:: struct hda_spdif_out *snd_hda_spdif_out_of_nid(struct hda_codec *codec, hda_nid_t nid)

    get the hda_spdif_out entry from the given NID

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        widget NID
    :type nid: hda_nid_t

.. _`snd_hda_spdif_out_of_nid.description`:

Description
-----------

call within spdif_mutex lock

.. _`snd_hda_spdif_ctls_unassign`:

snd_hda_spdif_ctls_unassign
===========================

.. c:function:: void snd_hda_spdif_ctls_unassign(struct hda_codec *codec, int idx)

    Unassign the given SPDIF ctl

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param idx:
        the SPDIF ctl index
    :type idx: int

.. _`snd_hda_spdif_ctls_unassign.description`:

Description
-----------

Unassign the widget from the given SPDIF control.

.. _`snd_hda_spdif_ctls_assign`:

snd_hda_spdif_ctls_assign
=========================

.. c:function:: void snd_hda_spdif_ctls_assign(struct hda_codec *codec, int idx, hda_nid_t nid)

    Assign the SPDIF controls to the given NID

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param idx:
        the SPDIF ctl idx
    :type idx: int

    :param nid:
        widget NID
    :type nid: hda_nid_t

.. _`snd_hda_spdif_ctls_assign.description`:

Description
-----------

Assign the widget to the SPDIF control with the given index.

.. _`snd_hda_create_spdif_share_sw`:

snd_hda_create_spdif_share_sw
=============================

.. c:function:: int snd_hda_create_spdif_share_sw(struct hda_codec *codec, struct hda_multi_out *mout)

    create Default PCM switch

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        multi-out instance
    :type mout: struct hda_multi_out \*

.. _`snd_hda_create_spdif_in_ctls`:

snd_hda_create_spdif_in_ctls
============================

.. c:function:: int snd_hda_create_spdif_in_ctls(struct hda_codec *codec, hda_nid_t nid)

    create Input SPDIF-related controls

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        audio in widget NID
    :type nid: hda_nid_t

.. _`snd_hda_create_spdif_in_ctls.description`:

Description
-----------

Creates controls related with the SPDIF input.
Called from each patch supporting the SPDIF in.

Returns 0 if successful, or a negative error code.

.. _`snd_hda_codec_set_power_to_all`:

snd_hda_codec_set_power_to_all
==============================

.. c:function:: void snd_hda_codec_set_power_to_all(struct hda_codec *codec, hda_nid_t fg, unsigned int power_state)

    Set the power state to all widgets

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param fg:
        function group (not used now)
    :type fg: hda_nid_t

    :param power_state:
        the power state to set (AC_PWRST\_\*)
    :type power_state: unsigned int

.. _`snd_hda_codec_set_power_to_all.description`:

Description
-----------

Set the given power state to all widgets that have the power control.
If the codec has power_filter set, it evaluates the power state and
filter out if it's unchanged as D3.

.. _`snd_hda_codec_eapd_power_filter`:

snd_hda_codec_eapd_power_filter
===============================

.. c:function:: unsigned int snd_hda_codec_eapd_power_filter(struct hda_codec *codec, hda_nid_t nid, unsigned int power_state)

    A power filter callback for EAPD

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param nid:
        widget NID
    :type nid: hda_nid_t

    :param power_state:
        power state to evalue
    :type power_state: unsigned int

.. _`snd_hda_codec_eapd_power_filter.description`:

Description
-----------

Don't power down the widget if it controls eapd and EAPD_BTLENABLE is set.
This can be used a codec power_filter callback.

.. _`snd_hda_codec_prepare`:

snd_hda_codec_prepare
=====================

.. c:function:: int snd_hda_codec_prepare(struct hda_codec *codec, struct hda_pcm_stream *hinfo, unsigned int stream, unsigned int format, struct snd_pcm_substream *substream)

    Prepare a stream

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param hinfo:
        PCM information
    :type hinfo: struct hda_pcm_stream \*

    :param stream:
        stream tag to assign
    :type stream: unsigned int

    :param format:
        format id to assign
    :type format: unsigned int

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

.. _`snd_hda_codec_prepare.description`:

Description
-----------

Calls the prepare callback set by the codec with the given arguments.
Clean up the inactive streams when successful.

.. _`snd_hda_codec_cleanup`:

snd_hda_codec_cleanup
=====================

.. c:function:: void snd_hda_codec_cleanup(struct hda_codec *codec, struct hda_pcm_stream *hinfo, struct snd_pcm_substream *substream)

    Prepare a stream

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param hinfo:
        PCM information
    :type hinfo: struct hda_pcm_stream \*

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_hda_codec_cleanup.description`:

Description
-----------

Calls the cleanup callback set by the codec with the given arguments.

.. _`snd_hda_add_new_ctls`:

snd_hda_add_new_ctls
====================

.. c:function:: int snd_hda_add_new_ctls(struct hda_codec *codec, const struct snd_kcontrol_new *knew)

    create controls from the array

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param knew:
        the array of struct snd_kcontrol_new
    :type knew: const struct snd_kcontrol_new \*

.. _`snd_hda_add_new_ctls.description`:

Description
-----------

This helper function creates and add new controls in the given array.
The array must be terminated with an empty entry as terminator.

Returns 0 if successful, or a negative error code.

.. _`snd_hda_set_power_save`:

snd_hda_set_power_save
======================

.. c:function:: void snd_hda_set_power_save(struct hda_bus *bus, int delay)

    reprogram autosuspend for the given delay

    :param bus:
        HD-audio bus
    :type bus: struct hda_bus \*

    :param delay:
        autosuspend delay in msec, 0 = off
    :type delay: int

.. _`snd_hda_set_power_save.description`:

Description
-----------

Synchronize the runtime PM autosuspend state from the power_save option.

.. _`snd_hda_check_amp_list_power`:

snd_hda_check_amp_list_power
============================

.. c:function:: int snd_hda_check_amp_list_power(struct hda_codec *codec, struct hda_loopback_check *check, hda_nid_t nid)

    Check the amp list and update the power

    :param codec:
        HD-audio codec
    :type codec: struct hda_codec \*

    :param check:
        the object containing an AMP list and the status
    :type check: struct hda_loopback_check \*

    :param nid:
        NID to check / update
    :type nid: hda_nid_t

.. _`snd_hda_check_amp_list_power.description`:

Description
-----------

Check whether the given NID is in the amp list.  If it's in the list,
check the current AMP status, and update the the power-status according
to the mute status.

This function is supposed to be set or called from the check_power_status
patch ops.

.. _`snd_hda_input_mux_info`:

snd_hda_input_mux_info
======================

.. c:function:: int snd_hda_input_mux_info(const struct hda_input_mux *imux, struct snd_ctl_elem_info *uinfo)

    Info callback helper for the input-mux enum

    :param imux:
        imux helper object
    :type imux: const struct hda_input_mux \*

    :param uinfo:
        pointer to get/store the data
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_hda_input_mux_put`:

snd_hda_input_mux_put
=====================

.. c:function:: int snd_hda_input_mux_put(struct hda_codec *codec, const struct hda_input_mux *imux, struct snd_ctl_elem_value *ucontrol, hda_nid_t nid, unsigned int *cur_val)

    Put callback helper for the input-mux enum

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param imux:
        imux helper object
    :type imux: const struct hda_input_mux \*

    :param ucontrol:
        pointer to get/store the data
    :type ucontrol: struct snd_ctl_elem_value \*

    :param nid:
        input mux NID
    :type nid: hda_nid_t

    :param cur_val:
        pointer to get/store the current imux value
    :type cur_val: unsigned int \*

.. _`snd_hda_enum_helper_info`:

snd_hda_enum_helper_info
========================

.. c:function:: int snd_hda_enum_helper_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo, int num_items, const char * const *texts)

    Helper for simple enum ctls

    :param kcontrol:
        ctl element
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        pointer to get/store the data
    :type uinfo: struct snd_ctl_elem_info \*

    :param num_items:
        number of enum items
    :type num_items: int

    :param texts:
        enum item string array
    :type texts: const char \* const \*

.. _`snd_hda_enum_helper_info.description`:

Description
-----------

process kcontrol info callback of a simple string enum array
when \ ``num_items``\  is 0 or \ ``texts``\  is NULL, assume a boolean enum array

.. _`snd_hda_multi_out_dig_open`:

snd_hda_multi_out_dig_open
==========================

.. c:function:: int snd_hda_multi_out_dig_open(struct hda_codec *codec, struct hda_multi_out *mout)

    open the digital out in the exclusive mode

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

.. _`snd_hda_multi_out_dig_prepare`:

snd_hda_multi_out_dig_prepare
=============================

.. c:function:: int snd_hda_multi_out_dig_prepare(struct hda_codec *codec, struct hda_multi_out *mout, unsigned int stream_tag, unsigned int format, struct snd_pcm_substream *substream)

    prepare the digital out stream

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

    :param stream_tag:
        stream tag to assign
    :type stream_tag: unsigned int

    :param format:
        format id to assign
    :type format: unsigned int

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

.. _`snd_hda_multi_out_dig_cleanup`:

snd_hda_multi_out_dig_cleanup
=============================

.. c:function:: int snd_hda_multi_out_dig_cleanup(struct hda_codec *codec, struct hda_multi_out *mout)

    clean-up the digital out stream

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

.. _`snd_hda_multi_out_dig_close`:

snd_hda_multi_out_dig_close
===========================

.. c:function:: int snd_hda_multi_out_dig_close(struct hda_codec *codec, struct hda_multi_out *mout)

    release the digital out stream

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

.. _`snd_hda_multi_out_analog_open`:

snd_hda_multi_out_analog_open
=============================

.. c:function:: int snd_hda_multi_out_analog_open(struct hda_codec *codec, struct hda_multi_out *mout, struct snd_pcm_substream *substream, struct hda_pcm_stream *hinfo)

    open analog outputs

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

    :param hinfo:
        PCM information to assign
    :type hinfo: struct hda_pcm_stream \*

.. _`snd_hda_multi_out_analog_open.description`:

Description
-----------

Open analog outputs and set up the hw-constraints.
If the digital outputs can be opened as slave, open the digital
outputs, too.

.. _`snd_hda_multi_out_analog_prepare`:

snd_hda_multi_out_analog_prepare
================================

.. c:function:: int snd_hda_multi_out_analog_prepare(struct hda_codec *codec, struct hda_multi_out *mout, unsigned int stream_tag, unsigned int format, struct snd_pcm_substream *substream)

    Preapre the analog outputs.

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

    :param stream_tag:
        stream tag to assign
    :type stream_tag: unsigned int

    :param format:
        format id to assign
    :type format: unsigned int

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

.. _`snd_hda_multi_out_analog_prepare.description`:

Description
-----------

Set up the i/o for analog out.
When the digital out is available, copy the front out to digital out, too.

.. _`snd_hda_multi_out_analog_cleanup`:

snd_hda_multi_out_analog_cleanup
================================

.. c:function:: int snd_hda_multi_out_analog_cleanup(struct hda_codec *codec, struct hda_multi_out *mout)

    clean up the setting for analog out

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param mout:
        hda_multi_out object
    :type mout: struct hda_multi_out \*

.. _`snd_hda_get_default_vref`:

snd_hda_get_default_vref
========================

.. c:function:: unsigned int snd_hda_get_default_vref(struct hda_codec *codec, hda_nid_t pin)

    Get the default (mic) VREF pin bits

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param pin:
        referred pin NID
    :type pin: hda_nid_t

.. _`snd_hda_get_default_vref.description`:

Description
-----------

Guess the suitable VREF pin bits to be set as the pin-control value.

.. _`snd_hda_get_default_vref.note`:

Note
----

the function doesn't set the AC_PINCTL_IN_EN bit.

.. _`snd_hda_correct_pin_ctl`:

snd_hda_correct_pin_ctl
=======================

.. c:function:: unsigned int snd_hda_correct_pin_ctl(struct hda_codec *codec, hda_nid_t pin, unsigned int val)

    correct the pin ctl value for matching with the pin cap

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param pin:
        referred pin NID
    :type pin: hda_nid_t

    :param val:
        pin ctl value to audit
    :type val: unsigned int

.. _`_snd_hda_set_pin_ctl`:

\_snd_hda_set_pin_ctl
=====================

.. c:function:: int _snd_hda_set_pin_ctl(struct hda_codec *codec, hda_nid_t pin, unsigned int val, bool cached)

    Helper to set pin ctl value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param pin:
        referred pin NID
    :type pin: hda_nid_t

    :param val:
        pin control value to set
    :type val: unsigned int

    :param cached:
        access over codec pinctl cache or direct write
    :type cached: bool

.. _`_snd_hda_set_pin_ctl.description`:

Description
-----------

This function is a helper to set a pin ctl value more safely.
It corrects the pin ctl value via \ :c:func:`snd_hda_correct_pin_ctl`\ , stores the
value in pin target array via \ :c:func:`snd_hda_codec_set_pin_target`\ , then
actually writes the value via either \ :c:func:`snd_hda_codec_write_cache`\  or
\ :c:func:`snd_hda_codec_write`\  depending on \ ``cached``\  flag.

.. _`snd_hda_add_imux_item`:

snd_hda_add_imux_item
=====================

.. c:function:: int snd_hda_add_imux_item(struct hda_codec *codec, struct hda_input_mux *imux, const char *label, int index, int *type_idx)

    Add an item to input_mux

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param imux:
        imux helper object
    :type imux: struct hda_input_mux \*

    :param label:
        the name of imux item to assign
    :type label: const char \*

    :param index:
        index number of imux item to assign
    :type index: int

    :param type_idx:
        pointer to store the resultant label index
    :type type_idx: int \*

.. _`snd_hda_add_imux_item.description`:

Description
-----------

When the same label is used already in the existing items, the number
suffix is appended to the label.  This label index number is stored
to type_idx when non-NULL pointer is given.

.. _`snd_hda_bus_reset_codecs`:

snd_hda_bus_reset_codecs
========================

.. c:function:: void snd_hda_bus_reset_codecs(struct hda_bus *bus)

    Reset the bus

    :param bus:
        HD-audio bus
    :type bus: struct hda_bus \*

.. _`snd_print_pcm_bits`:

snd_print_pcm_bits
==================

.. c:function:: void snd_print_pcm_bits(int pcm, char *buf, int buflen)

    Print the supported PCM fmt bits to the string buffer

    :param pcm:
        PCM caps bits
    :type pcm: int

    :param buf:
        the string buffer to write
    :type buf: char \*

    :param buflen:
        the max buffer length
    :type buflen: int

.. _`snd_print_pcm_bits.description`:

Description
-----------

used by hda_proc.c and hda_eld.c

.. This file was automatic generated / don't edit.


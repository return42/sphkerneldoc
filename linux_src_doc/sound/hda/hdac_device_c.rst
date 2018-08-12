.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_device.c

.. _`snd_hdac_device_init`:

snd_hdac_device_init
====================

.. c:function:: int snd_hdac_device_init(struct hdac_device *codec, struct hdac_bus *bus, const char *name, unsigned int addr)

    initialize the HD-audio codec base device

    :param struct hdac_device \*codec:
        device to initialize

    :param struct hdac_bus \*bus:
        but to attach

    :param const char \*name:
        device name string

    :param unsigned int addr:
        codec address

.. _`snd_hdac_device_init.description`:

Description
-----------

Returns zero for success or a negative error code.

This function increments the runtime PM counter and marks it active.
The caller needs to turn it off appropriately later.

The caller needs to set the device's release op properly by itself.

.. _`snd_hdac_device_exit`:

snd_hdac_device_exit
====================

.. c:function:: void snd_hdac_device_exit(struct hdac_device *codec)

    clean up the HD-audio codec base device

    :param struct hdac_device \*codec:
        device to clean up

.. _`snd_hdac_device_register`:

snd_hdac_device_register
========================

.. c:function:: int snd_hdac_device_register(struct hdac_device *codec)

    register the hd-audio codec base device

    :param struct hdac_device \*codec:
        *undescribed*

.. _`snd_hdac_device_register.codec`:

codec
-----

the device to register

.. _`snd_hdac_device_unregister`:

snd_hdac_device_unregister
==========================

.. c:function:: void snd_hdac_device_unregister(struct hdac_device *codec)

    unregister the hd-audio codec base device

    :param struct hdac_device \*codec:
        *undescribed*

.. _`snd_hdac_device_unregister.codec`:

codec
-----

the device to unregister

.. _`snd_hdac_device_set_chip_name`:

snd_hdac_device_set_chip_name
=============================

.. c:function:: int snd_hdac_device_set_chip_name(struct hdac_device *codec, const char *name)

    set/update the codec name

    :param struct hdac_device \*codec:
        the HDAC device

    :param const char \*name:
        name string to set

.. _`snd_hdac_device_set_chip_name.description`:

Description
-----------

Returns 0 if the name is set or updated, or a negative error code.

.. _`snd_hdac_codec_modalias`:

snd_hdac_codec_modalias
=======================

.. c:function:: int snd_hdac_codec_modalias(struct hdac_device *codec, char *buf, size_t size)

    give the module alias name

    :param struct hdac_device \*codec:
        HDAC device

    :param char \*buf:
        string buffer to store

    :param size_t size:
        string buffer size

.. _`snd_hdac_codec_modalias.description`:

Description
-----------

Returns the size of string, like \ :c:func:`snprintf`\ , or a negative error code.

.. _`snd_hdac_make_cmd`:

snd_hdac_make_cmd
=================

.. c:function:: unsigned int snd_hdac_make_cmd(struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int parm)

    compose a 32bit command word to be sent to the HD-audio controller

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to encode

    :param unsigned int verb:
        verb to encode

    :param unsigned int parm:
        parameter to encode

.. _`snd_hdac_make_cmd.description`:

Description
-----------

Return an encoded command verb or -1 for error.

.. _`snd_hdac_exec_verb`:

snd_hdac_exec_verb
==================

.. c:function:: int snd_hdac_exec_verb(struct hdac_device *codec, unsigned int cmd, unsigned int flags, unsigned int *res)

    execute an encoded verb

    :param struct hdac_device \*codec:
        the codec object

    :param unsigned int cmd:
        encoded verb to execute

    :param unsigned int flags:
        optional flags, pass zero for default

    :param unsigned int \*res:
        the pointer to store the result, NULL if running async

.. _`snd_hdac_exec_verb.description`:

Description
-----------

Returns zero if successful, or a negative error code.

This calls the exec_verb op when set in hdac_codec.  If not,
call the default \ :c:func:`snd_hdac_bus_exec_verb`\ .

.. _`snd_hdac_read`:

snd_hdac_read
=============

.. c:function:: int snd_hdac_read(struct hdac_device *codec, hda_nid_t nid, unsigned int verb, unsigned int parm, unsigned int *res)

    execute a verb

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to execute a verb

    :param unsigned int verb:
        verb to execute

    :param unsigned int parm:
        parameter for a verb

    :param unsigned int \*res:
        the pointer to store the result, NULL if running async

.. _`snd_hdac_read.description`:

Description
-----------

Returns zero if successful, or a negative error code.

.. _`_snd_hdac_read_parm`:

\_snd_hdac_read_parm
====================

.. c:function:: int _snd_hdac_read_parm(struct hdac_device *codec, hda_nid_t nid, int parm, unsigned int *res)

    read a parmeter

    :param struct hdac_device \*codec:
        *undescribed*

    :param hda_nid_t nid:
        *undescribed*

    :param int parm:
        *undescribed*

    :param unsigned int \*res:
        *undescribed*

.. _`_snd_hdac_read_parm.description`:

Description
-----------

This function returns zero or an error unlike \ :c:func:`snd_hdac_read_parm`\ .

.. _`snd_hdac_read_parm_uncached`:

snd_hdac_read_parm_uncached
===========================

.. c:function:: int snd_hdac_read_parm_uncached(struct hdac_device *codec, hda_nid_t nid, int parm)

    read a codec parameter without caching

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to read a parameter

    :param int parm:
        parameter to read

.. _`snd_hdac_read_parm_uncached.description`:

Description
-----------

Returns -1 for error.  If you need to distinguish the error more
strictly, use \ :c:func:`snd_hdac_read`\  directly.

.. _`snd_hdac_override_parm`:

snd_hdac_override_parm
======================

.. c:function:: int snd_hdac_override_parm(struct hdac_device *codec, hda_nid_t nid, unsigned int parm, unsigned int val)

    override read-only parameters

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID for the parameter

    :param unsigned int parm:
        the parameter to change

    :param unsigned int val:
        the parameter value to overwrite

.. _`snd_hdac_get_sub_nodes`:

snd_hdac_get_sub_nodes
======================

.. c:function:: int snd_hdac_get_sub_nodes(struct hdac_device *codec, hda_nid_t nid, hda_nid_t *start_id)

    get start NID and number of subtree nodes

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to inspect

    :param hda_nid_t \*start_id:
        the pointer to store the starting NID

.. _`snd_hdac_get_sub_nodes.description`:

Description
-----------

Returns the number of subtree nodes or zero if not found.
This function reads parameters always without caching.

.. _`snd_hdac_refresh_widgets`:

snd_hdac_refresh_widgets
========================

.. c:function:: int snd_hdac_refresh_widgets(struct hdac_device *codec, bool sysfs)

    Reset the widget start/end nodes

    :param struct hdac_device \*codec:
        the codec object

    :param bool sysfs:
        re-initialize sysfs tree, too

.. _`snd_hdac_get_connections`:

snd_hdac_get_connections
========================

.. c:function:: int snd_hdac_get_connections(struct hdac_device *codec, hda_nid_t nid, hda_nid_t *conn_list, int max_conns)

    get a widget connection list

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID

    :param hda_nid_t \*conn_list:
        the array to store the results, can be NULL

    :param int max_conns:
        the max size of the given array

.. _`snd_hdac_get_connections.description`:

Description
-----------

Returns the number of connected widgets, zero for no connection, or a
negative error code.  When the number of elements don't fit with the
given array size, it returns -ENOSPC.

When \ ``conn_list``\  is NULL, it just checks the number of connections.

.. _`snd_hdac_power_up`:

snd_hdac_power_up
=================

.. c:function:: int snd_hdac_power_up(struct hdac_device *codec)

    power up the codec

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_power_up.description`:

Description
-----------

This function calls the runtime PM helper to power up the given codec.
Unlike \ :c:func:`snd_hdac_power_up_pm`\ , you should call this only for the code
path that isn't included in PM path.  Otherwise it gets stuck.

Returns zero if successful, or a negative error code.

.. _`snd_hdac_power_down`:

snd_hdac_power_down
===================

.. c:function:: int snd_hdac_power_down(struct hdac_device *codec)

    power down the codec

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_power_down.description`:

Description
-----------

Returns zero if successful, or a negative error code.

.. _`snd_hdac_power_up_pm`:

snd_hdac_power_up_pm
====================

.. c:function:: int snd_hdac_power_up_pm(struct hdac_device *codec)

    power up the codec

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_power_up_pm.description`:

Description
-----------

This function can be called in a recursive code path like init code
which may be called by PM suspend/resume again.  OTOH, if a power-up
call must wake up the sleeper (e.g. in a kctl callback), use
\ :c:func:`snd_hdac_power_up`\  instead.

Returns zero if successful, or a negative error code.

.. _`snd_hdac_power_down_pm`:

snd_hdac_power_down_pm
======================

.. c:function:: int snd_hdac_power_down_pm(struct hdac_device *codec)

    power down the codec

    :param struct hdac_device \*codec:
        the codec object

.. _`snd_hdac_power_down_pm.description`:

Description
-----------

Like \ :c:func:`snd_hdac_power_up_pm`\ , this function is used in a recursive
code path like init code which may be called by PM suspend/resume again.

Returns zero if successful, or a negative error code.

.. _`snd_hdac_link_power`:

snd_hdac_link_power
===================

.. c:function:: int snd_hdac_link_power(struct hdac_device *codec, bool enable)

    Enable/disable the link power for a codec

    :param struct hdac_device \*codec:
        the codec object

    :param bool enable:
        *undescribed*

.. _`snd_hdac_calc_stream_format`:

snd_hdac_calc_stream_format
===========================

.. c:function:: unsigned int snd_hdac_calc_stream_format(unsigned int rate, unsigned int channels, unsigned int format, unsigned int maxbps, unsigned short spdif_ctls)

    calculate the format bitset

    :param unsigned int rate:
        the sample rate

    :param unsigned int channels:
        the number of channels

    :param unsigned int format:
        the PCM format (SNDRV_PCM_FORMAT_XXX)

    :param unsigned int maxbps:
        the max. bps

    :param unsigned short spdif_ctls:
        HD-audio SPDIF status bits (0 if irrelevant)

.. _`snd_hdac_calc_stream_format.description`:

Description
-----------

Calculate the format bitset from the given rate, channels and th PCM format.

Return zero if invalid.

.. _`snd_hdac_query_supported_pcm`:

snd_hdac_query_supported_pcm
============================

.. c:function:: int snd_hdac_query_supported_pcm(struct hdac_device *codec, hda_nid_t nid, u32 *ratesp, u64 *formatsp, unsigned int *bpsp)

    query the supported PCM rates and formats

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to query

    :param u32 \*ratesp:
        the pointer to store the detected rate bitflags

    :param u64 \*formatsp:
        the pointer to store the detected formats

    :param unsigned int \*bpsp:
        the pointer to store the detected format widths

.. _`snd_hdac_query_supported_pcm.description`:

Description
-----------

Queries the supported PCM rates and formats.  The NULL \ ``ratesp``\ , \ ``formatsp``\ 
or \ ``bsps``\  argument is ignored.

Returns 0 if successful, otherwise a negative error code.

.. _`snd_hdac_is_supported_format`:

snd_hdac_is_supported_format
============================

.. c:function:: bool snd_hdac_is_supported_format(struct hdac_device *codec, hda_nid_t nid, unsigned int format)

    Check the validity of the format

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to check

    :param unsigned int format:
        the HD-audio format value to check

.. _`snd_hdac_is_supported_format.description`:

Description
-----------

Check whether the given node supports the format value.

Returns true if supported, false if not.

.. _`snd_hdac_codec_read`:

snd_hdac_codec_read
===================

.. c:function:: int snd_hdac_codec_read(struct hdac_device *hdac, hda_nid_t nid, int flags, unsigned int verb, unsigned int parm)

    send a command and get the response

    :param struct hdac_device \*hdac:
        the HDAC device

    :param hda_nid_t nid:
        NID to send the command

    :param int flags:
        optional bit flags

    :param unsigned int verb:
        the verb to send

    :param unsigned int parm:
        the parameter for the verb

.. _`snd_hdac_codec_read.description`:

Description
-----------

Send a single command and read the corresponding response.

Returns the obtained response value, or -1 for an error.

.. _`snd_hdac_codec_write`:

snd_hdac_codec_write
====================

.. c:function:: int snd_hdac_codec_write(struct hdac_device *hdac, hda_nid_t nid, int flags, unsigned int verb, unsigned int parm)

    send a single command without waiting for response

    :param struct hdac_device \*hdac:
        the HDAC device

    :param hda_nid_t nid:
        NID to send the command

    :param int flags:
        optional bit flags

    :param unsigned int verb:
        the verb to send

    :param unsigned int parm:
        the parameter for the verb

.. _`snd_hdac_codec_write.description`:

Description
-----------

Send a single command without waiting for response.

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_check_power_state`:

snd_hdac_check_power_state
==========================

.. c:function:: bool snd_hdac_check_power_state(struct hdac_device *hdac, hda_nid_t nid, unsigned int target_state)

    check whether the actual power state matches with the target state

    :param struct hdac_device \*hdac:
        the HDAC device

    :param hda_nid_t nid:
        NID to send the command

    :param unsigned int target_state:
        target state to check for

.. _`snd_hdac_check_power_state.description`:

Description
-----------

Return true if state matches, false if not

.. _`snd_hdac_sync_power_state`:

snd_hdac_sync_power_state
=========================

.. c:function:: unsigned int snd_hdac_sync_power_state(struct hdac_device *codec, hda_nid_t nid, unsigned int power_state)

    wait until actual power state matches with the target state

    :param struct hdac_device \*codec:
        *undescribed*

    :param hda_nid_t nid:
        NID to send the command

    :param unsigned int power_state:
        *undescribed*

.. _`snd_hdac_sync_power_state.description`:

Description
-----------

Return power state or PS_ERROR if codec rejects GET verb.

.. This file was automatic generated / don't edit.


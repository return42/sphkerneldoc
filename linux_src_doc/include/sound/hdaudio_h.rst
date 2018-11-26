.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/hdaudio.h

.. _`snd_hdac_read_parm`:

snd_hdac_read_parm
==================

.. c:function:: int snd_hdac_read_parm(struct hdac_device *codec, hda_nid_t nid, int parm)

    read a codec parameter

    :param codec:
        the codec object
    :type codec: struct hdac_device \*

    :param nid:
        NID to read a parameter
    :type nid: hda_nid_t

    :param parm:
        parameter to read
    :type parm: int

.. _`snd_hdac_read_parm.description`:

Description
-----------

Returns -1 for error.  If you need to distinguish the error more
strictly, use \_snd_hdac_read_parm() directly.

.. This file was automatic generated / don't edit.


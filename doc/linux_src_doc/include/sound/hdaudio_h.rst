.. -*- coding: utf-8; mode: rst -*-

=========
hdaudio.h
=========


.. _`snd_hdac_read_parm`:

snd_hdac_read_parm
==================

.. c:function:: int snd_hdac_read_parm (struct hdac_device *codec, hda_nid_t nid, int parm)

    read a codec parameter

    :param struct hdac_device \*codec:
        the codec object

    :param hda_nid_t nid:
        NID to read a parameter

    :param int parm:
        parameter to read



.. _`snd_hdac_read_parm.description`:

Description
-----------

Returns -1 for error.  If you need to distinguish the error more
strictly, use :c:func:`_snd_hdac_read_parm` directly.


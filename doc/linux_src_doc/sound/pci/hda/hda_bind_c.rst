.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_bind.c

.. _`snd_hda_codec_set_name`:

snd_hda_codec_set_name
======================

.. c:function:: int snd_hda_codec_set_name(struct hda_codec *codec, const char *name)

    set the codec name

    :param struct hda_codec \*codec:
        the HDA codec

    :param const char \*name:
        name string to set

.. _`snd_hda_codec_configure`:

snd_hda_codec_configure
=======================

.. c:function:: int snd_hda_codec_configure(struct hda_codec *codec)

    (Re-)configure the HD-audio codec

    :param struct hda_codec \*codec:
        the HDA codec

.. _`snd_hda_codec_configure.description`:

Description
-----------

Start parsing of the given codec tree and (re-)initialize the whole
patch instance.

Returns 0 if successful or a negative error code.

.. This file was automatic generated / don't edit.


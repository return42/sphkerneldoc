.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/hda/hda_sysfs.c

.. _`snd_hda_get_hint`:

snd_hda_get_hint
================

.. c:function:: const char *snd_hda_get_hint(struct hda_codec *codec, const char *key)

    Look for hint string

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param key:
        the hint key string
    :type key: const char \*

.. _`snd_hda_get_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and returns the value string.  If nothing found, returns NULL.

.. _`snd_hda_get_bool_hint`:

snd_hda_get_bool_hint
=====================

.. c:function:: int snd_hda_get_bool_hint(struct hda_codec *codec, const char *key)

    Get a boolean hint value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param key:
        the hint key string
    :type key: const char \*

.. _`snd_hda_get_bool_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and returns a boolean value parsed from the value.  If no matching
key is found, return a negative value.

.. _`snd_hda_get_int_hint`:

snd_hda_get_int_hint
====================

.. c:function:: int snd_hda_get_int_hint(struct hda_codec *codec, const char *key, int *valp)

    Get an integer hint value

    :param codec:
        the HDA codec
    :type codec: struct hda_codec \*

    :param key:
        the hint key string
    :type key: const char \*

    :param valp:
        pointer to store a value
    :type valp: int \*

.. _`snd_hda_get_int_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and stores the integer value to \ ``valp``\ .  If no matching key is found,
return a negative error code.  Otherwise it returns zero.

.. _`snd_hda_load_patch`:

snd_hda_load_patch
==================

.. c:function:: int snd_hda_load_patch(struct hda_bus *bus, size_t fw_size, const void *fw_buf)

    load a "patch" firmware file and parse it

    :param bus:
        HD-audio bus
    :type bus: struct hda_bus \*

    :param fw_size:
        the firmware byte size
    :type fw_size: size_t

    :param fw_buf:
        the firmware data
    :type fw_buf: const void \*

.. This file was automatic generated / don't edit.


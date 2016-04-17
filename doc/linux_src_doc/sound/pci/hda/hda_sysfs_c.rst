.. -*- coding: utf-8; mode: rst -*-

===========
hda_sysfs.c
===========


.. _`snd_hda_get_hint`:

snd_hda_get_hint
================

.. c:function:: const char *snd_hda_get_hint (struct hda_codec *codec, const char *key)

    Look for hint string

    :param struct hda_codec \*codec:
        the HDA codec

    :param const char \*key:
        the hint key string



.. _`snd_hda_get_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and returns the value string.  If nothing found, returns NULL.



.. _`snd_hda_get_bool_hint`:

snd_hda_get_bool_hint
=====================

.. c:function:: int snd_hda_get_bool_hint (struct hda_codec *codec, const char *key)

    Get a boolean hint value

    :param struct hda_codec \*codec:
        the HDA codec

    :param const char \*key:
        the hint key string



.. _`snd_hda_get_bool_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and returns a boolean value parsed from the value.  If no matching
key is found, return a negative value.



.. _`snd_hda_get_int_hint`:

snd_hda_get_int_hint
====================

.. c:function:: int snd_hda_get_int_hint (struct hda_codec *codec, const char *key, int *valp)

    Get an integer hint value

    :param struct hda_codec \*codec:
        the HDA codec

    :param const char \*key:
        the hint key string

    :param int \*valp:
        pointer to store a value



.. _`snd_hda_get_int_hint.description`:

Description
-----------

Look for a hint key/value pair matching with the given key string
and stores the integer value to ``valp``\ .  If no matching key is found,
return a negative error code.  Otherwise it returns zero.



.. _`snd_hda_load_patch`:

snd_hda_load_patch
==================

.. c:function:: int snd_hda_load_patch (struct hda_bus *bus, size_t fw_size, const void *fw_buf)

    load a "patch" firmware file and parse it

    :param struct hda_bus \*bus:
        HD-audio bus

    :param size_t fw_size:
        the firmware byte size

    :param const void \*fw_buf:
        the firmware data


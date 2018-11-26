.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/info.c

.. _`snd_info_get_line`:

snd_info_get_line
=================

.. c:function:: int snd_info_get_line(struct snd_info_buffer *buffer, char *line, int len)

    read one line from the procfs buffer

    :param buffer:
        the procfs buffer
    :type buffer: struct snd_info_buffer \*

    :param line:
        the buffer to store
    :type line: char \*

    :param len:
        the max. buffer size
    :type len: int

.. _`snd_info_get_line.description`:

Description
-----------

Reads one line from the buffer and stores the string.

.. _`snd_info_get_line.return`:

Return
------

Zero if successful, or 1 if error or EOF.

.. _`snd_info_get_str`:

snd_info_get_str
================

.. c:function:: const char *snd_info_get_str(char *dest, const char *src, int len)

    parse a string token

    :param dest:
        the buffer to store the string token
    :type dest: char \*

    :param src:
        the original string
    :type src: const char \*

    :param len:
        the max. length of token - 1
    :type len: int

.. _`snd_info_get_str.description`:

Description
-----------

Parses the original string and copy a token to the given
string buffer.

.. _`snd_info_get_str.return`:

Return
------

The updated pointer of the original string so that
it can be used for the next call.

.. _`snd_info_create_module_entry`:

snd_info_create_module_entry
============================

.. c:function:: struct snd_info_entry *snd_info_create_module_entry(struct module *module, const char *name, struct snd_info_entry *parent)

    create an info entry for the given module

    :param module:
        the module pointer
    :type module: struct module \*

    :param name:
        the file name
    :type name: const char \*

    :param parent:
        the parent directory
    :type parent: struct snd_info_entry \*

.. _`snd_info_create_module_entry.description`:

Description
-----------

Creates a new info entry and assigns it to the given module.

.. _`snd_info_create_module_entry.return`:

Return
------

The pointer of the new instance, or \ ``NULL``\  on failure.

.. _`snd_info_create_card_entry`:

snd_info_create_card_entry
==========================

.. c:function:: struct snd_info_entry *snd_info_create_card_entry(struct snd_card *card, const char *name, struct snd_info_entry *parent)

    create an info entry for the given card

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param name:
        the file name
    :type name: const char \*

    :param parent:
        the parent directory
    :type parent: struct snd_info_entry \*

.. _`snd_info_create_card_entry.description`:

Description
-----------

Creates a new info entry and assigns it to the given card.

.. _`snd_info_create_card_entry.return`:

Return
------

The pointer of the new instance, or \ ``NULL``\  on failure.

.. _`snd_info_free_entry`:

snd_info_free_entry
===================

.. c:function:: void snd_info_free_entry(struct snd_info_entry *entry)

    release the info entry

    :param entry:
        the info entry
    :type entry: struct snd_info_entry \*

.. _`snd_info_free_entry.description`:

Description
-----------

Releases the info entry.

.. _`snd_info_register`:

snd_info_register
=================

.. c:function:: int snd_info_register(struct snd_info_entry *entry)

    register the info entry

    :param entry:
        the info entry
    :type entry: struct snd_info_entry \*

.. _`snd_info_register.description`:

Description
-----------

Registers the proc info entry.

.. _`snd_info_register.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. This file was automatic generated / don't edit.


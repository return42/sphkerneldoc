.. -*- coding: utf-8; mode: rst -*-

======
info.c
======


.. _`snd_info_get_line`:

snd_info_get_line
=================

.. c:function:: int snd_info_get_line (struct snd_info_buffer *buffer, char *line, int len)

    read one line from the procfs buffer

    :param struct snd_info_buffer \*buffer:
        the procfs buffer

    :param char \*line:
        the buffer to store

    :param int len:
        the max. buffer size



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

.. c:function:: const char *snd_info_get_str (char *dest, const char *src, int len)

    parse a string token

    :param char \*dest:
        the buffer to store the string token

    :param const char \*src:
        the original string

    :param int len:
        the max. length of token - 1



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

.. c:function:: struct snd_info_entry *snd_info_create_module_entry (struct module *module, const char *name, struct snd_info_entry *parent)

    create an info entry for the given module

    :param struct module \*module:
        the module pointer

    :param const char \*name:
        the file name

    :param struct snd_info_entry \*parent:
        the parent directory



.. _`snd_info_create_module_entry.description`:

Description
-----------

Creates a new info entry and assigns it to the given module.



.. _`snd_info_create_module_entry.return`:

Return
------

The pointer of the new instance, or ``NULL`` on failure.



.. _`snd_info_create_card_entry`:

snd_info_create_card_entry
==========================

.. c:function:: struct snd_info_entry *snd_info_create_card_entry (struct snd_card *card, const char *name, struct snd_info_entry *parent)

    create an info entry for the given card

    :param struct snd_card \*card:
        the card instance

    :param const char \*name:
        the file name

    :param struct snd_info_entry \*parent:
        the parent directory



.. _`snd_info_create_card_entry.description`:

Description
-----------

Creates a new info entry and assigns it to the given card.



.. _`snd_info_create_card_entry.return`:

Return
------

The pointer of the new instance, or ``NULL`` on failure.



.. _`snd_info_free_entry`:

snd_info_free_entry
===================

.. c:function:: void snd_info_free_entry (struct snd_info_entry *entry)

    release the info entry

    :param struct snd_info_entry \*entry:
        the info entry



.. _`snd_info_free_entry.description`:

Description
-----------

Releases the info entry.



.. _`snd_info_register`:

snd_info_register
=================

.. c:function:: int snd_info_register (struct snd_info_entry *entry)

    register the info entry

    :param struct snd_info_entry \*entry:
        the info entry



.. _`snd_info_register.description`:

Description
-----------

Registers the proc info entry.



.. _`snd_info_register.return`:

Return
------

Zero if successful, or a negative error code on failure.


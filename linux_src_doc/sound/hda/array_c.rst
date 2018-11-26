.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/array.c

.. _`snd_array_new`:

snd_array_new
=============

.. c:function:: void *snd_array_new(struct snd_array *array)

    get a new element from the given array

    :param array:
        the array object
    :type array: struct snd_array \*

.. _`snd_array_new.description`:

Description
-----------

Get a new element from the given array.  If it exceeds the
pre-allocated array size, re-allocate the array.

Returns NULL if allocation failed.

.. _`snd_array_free`:

snd_array_free
==============

.. c:function:: void snd_array_free(struct snd_array *array)

    free the given array elements

    :param array:
        the array object
    :type array: struct snd_array \*

.. This file was automatic generated / don't edit.


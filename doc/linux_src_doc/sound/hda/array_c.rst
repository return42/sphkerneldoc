.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/array.c

.. _`snd_array_new`:

snd_array_new
=============

.. c:function:: void *snd_array_new(struct snd_array *array)

    get a new element from the given array

    :param struct snd_array \*array:
        the array object

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

    :param struct snd_array \*array:
        the array object

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/api/fd/array.h

.. _`fdarray`:

struct fdarray
==============

.. c:type:: struct fdarray

    Array of file descriptors

.. _`fdarray.definition`:

Definition
----------

.. code-block:: c

    struct fdarray {
        int nr;
        int nr_alloc;
        int nr_autogrow;
        struct pollfd *entries;
        union {
            int idx;
            void *ptr;
        } *priv;
    }

.. _`fdarray.members`:

Members
-------

nr
    *undescribed*

nr_alloc
    *undescribed*

nr_autogrow
    *undescribed*

entries
    *undescribed*

priv
    Per array entry priv area, users should access just its contents,
    not set it to anything, as it is kept in synch with \ ``entries``\ , being
    realloc'ed, \* for instance, in fdarray__{grow,filter}.

.. _`fdarray.description`:

Description
-----------

I.e. using 'fda->priv[N].idx = \* value' where N < fda->nr is ok,
but doing 'fda->priv = malloc(M)' is not allowed.

.. This file was automatic generated / don't edit.


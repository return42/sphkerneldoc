.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/pl111/pl111_drm.h

.. _`pl111_variant_data`:

struct pl111_variant_data
=========================

.. c:type:: struct pl111_variant_data

    encodes IP differences

.. _`pl111_variant_data.definition`:

Definition
----------

.. code-block:: c

    struct pl111_variant_data {
        const char *name;
        bool is_pl110;
        const u32 *formats;
        unsigned int nformats;
    }

.. _`pl111_variant_data.members`:

Members
-------

name
    the name of this variant

is_pl110
    this is the early PL110 variant

formats
    array of supported pixel formats on this variant

nformats
    the length of the array of supported pixel formats

.. This file was automatic generated / don't edit.


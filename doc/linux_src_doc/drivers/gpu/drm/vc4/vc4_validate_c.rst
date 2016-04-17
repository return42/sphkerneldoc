.. -*- coding: utf-8; mode: rst -*-

==============
vc4_validate.c
==============


.. _`validate_args`:

VALIDATE_ARGS
=============

.. c:function:: VALIDATE_ARGS ()



.. _`validate_args.description`:

Description
-----------


The VC4 has no IOMMU between it and system memory.  So, a user with
access to execute command lists could escalate privilege by
overwriting system memory (drawing to it as a framebuffer) or
reading system memory it shouldn't (reading it as a texture, or
uniform data, or vertex data).

This validates command lists to ensure that all accesses are within
the bounds of the GEM objects referenced.  It explicitly whitelists
packets, and looks at the offsets in any address fields to make
sure they're constrained within the BOs they reference.

Note that because of the validation that's happening anyway, this
is where GEM relocation processing happens.



.. _`size_is_lt`:

size_is_lt
==========

.. c:function:: bool size_is_lt (uint32_t width, uint32_t height, int cpp)

    :param uint32_t width:

        *undescribed*

    :param uint32_t height:

        *undescribed*

    :param int cpp:

        *undescribed*



.. _`size_is_lt.description`:

Description
-----------

this function, so we lay out our miptrees accordingly.


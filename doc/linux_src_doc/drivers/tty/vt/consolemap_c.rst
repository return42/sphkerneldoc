.. -*- coding: utf-8; mode: rst -*-

============
consolemap.c
============


.. _`con_set_default_unimap`:

con_set_default_unimap
======================

.. c:function:: int con_set_default_unimap (struct vc_data *vc)

    set default unicode map

    :param struct vc_data \*vc:
        the console we are updating



.. _`con_set_default_unimap.description`:

Description
-----------

Loads the unimap for the hardware font, as defined in uni_hash.tbl.
The representation used was the most compact I could come up
with.  This routine is executed at video setup, and when the
PIO_FONTRESET ioctl is called. 

The caller must hold the console lock



.. _`con_copy_unimap`:

con_copy_unimap
===============

.. c:function:: int con_copy_unimap (struct vc_data *dst_vc, struct vc_data *src_vc)

    copy unimap between two vts

    :param struct vc_data \*dst_vc:
        target

    :param struct vc_data \*src_vc:

        *undescribed*



.. _`con_copy_unimap.description`:

Description
-----------

The caller must hold the console lock when invoking this method



.. _`con_get_unimap`:

con_get_unimap
==============

.. c:function:: int con_get_unimap (struct vc_data *vc, ushort ct, ushort __user *uct, struct unipair __user *list)

    get the unicode map

    :param struct vc_data \*vc:
        the console to read from

    :param ushort ct:

        *undescribed*

    :param ushort __user \*uct:

        *undescribed*

    :param struct unipair __user \*list:

        *undescribed*



.. _`con_get_unimap.description`:

Description
-----------

Read the console unicode data for this console. Called from the ioctl
handlers.


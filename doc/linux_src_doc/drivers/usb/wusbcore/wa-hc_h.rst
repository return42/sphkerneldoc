.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/wusbcore/wa-hc.h

.. _`rpipe_avail_inc`:

rpipe_avail_inc
===============

.. c:function:: int rpipe_avail_inc(struct wa_rpipe *rpipe)

    :param struct wa_rpipe \*rpipe:
        *undescribed*

.. _`__wa_get_status`:

__wa_get_status
===============

.. c:function:: s32 __wa_get_status(struct wahc *wa)

    :param struct wahc \*wa:
        Wire Adapter instance
        \ ``returns``\      < 0 errno code on error, or status bitmap as described
        in WUSB1.0[8.3.1.6].

.. _`__wa_get_status.note`:

NOTE
----

need malloc, some arches don't take USB from the stack

.. _`__wa_wait_status`:

__wa_wait_status
================

.. c:function:: s32 __wa_wait_status(struct wahc *wa, u32 mask, u32 value)

    :param struct wahc \*wa:
        Wire Adapter instance.
        \ ``returns``\      < 0 errno code on error, otherwise status.

    :param u32 mask:
        *undescribed*

    :param u32 value:
        *undescribed*

.. _`__wa_wait_status.description`:

Description
-----------

Loop until the WAs status matches the mask and value (status & mask
== value). Timeout if it doesn't happen.

.. _`__wa_wait_status.fixme`:

FIXME
-----

is there an official specification on how long status
changes can take?

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dcb/dcbnl.c

.. _`dcb_getapp`:

dcb_getapp
==========

.. c:function:: u8 dcb_getapp(struct net_device *dev, struct dcb_app *app)

    retrieve the DCBX application user priority

    :param struct net_device \*dev:
        *undescribed*

    :param struct dcb_app \*app:
        *undescribed*

.. _`dcb_getapp.description`:

Description
-----------

On success returns a non-zero 802.1p user priority bitmap
otherwise returns 0 as the invalid user priority bitmap to
indicate an error.

.. _`dcb_setapp`:

dcb_setapp
==========

.. c:function:: int dcb_setapp(struct net_device *dev, struct dcb_app *new)

    add CEE dcb application data to app list

    :param struct net_device \*dev:
        *undescribed*

    :param struct dcb_app \*new:
        *undescribed*

.. _`dcb_setapp.description`:

Description
-----------

Priority 0 is an invalid priority in CEE spec. This routine
removes applications from the app list if the priority is
set to zero. Priority is expected to be 8-bit 802.1p user priority bitmap

.. _`dcb_ieee_getapp_mask`:

dcb_ieee_getapp_mask
====================

.. c:function:: u8 dcb_ieee_getapp_mask(struct net_device *dev, struct dcb_app *app)

    retrieve the IEEE DCB application priority

    :param struct net_device \*dev:
        *undescribed*

    :param struct dcb_app \*app:
        *undescribed*

.. _`dcb_ieee_getapp_mask.description`:

Description
-----------

Helper routine which on success returns a non-zero 802.1Qaz user
priority bitmap otherwise returns 0 to indicate the dcb_app was
not found in APP list.

.. _`dcb_ieee_setapp`:

dcb_ieee_setapp
===============

.. c:function:: int dcb_ieee_setapp(struct net_device *dev, struct dcb_app *new)

    add IEEE dcb application data to app list

    :param struct net_device \*dev:
        *undescribed*

    :param struct dcb_app \*new:
        *undescribed*

.. _`dcb_ieee_setapp.description`:

Description
-----------

This adds Application data to the list. Multiple application
entries may exists for the same selector and protocol as long
as the priorities are different. Priority is expected to be a
3-bit unsigned integer

.. _`dcb_ieee_delapp`:

dcb_ieee_delapp
===============

.. c:function:: int dcb_ieee_delapp(struct net_device *dev, struct dcb_app *del)

    delete IEEE dcb application data from list

    :param struct net_device \*dev:
        *undescribed*

    :param struct dcb_app \*del:
        *undescribed*

.. _`dcb_ieee_delapp.description`:

Description
-----------

This removes a matching APP data from the APP list

.. This file was automatic generated / don't edit.


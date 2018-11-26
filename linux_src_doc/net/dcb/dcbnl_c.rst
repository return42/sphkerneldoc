.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dcb/dcbnl.c

.. _`dcb_getapp`:

dcb_getapp
==========

.. c:function:: u8 dcb_getapp(struct net_device *dev, struct dcb_app *app)

    retrieve the DCBX application user priority

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param app:
        *undescribed*
    :type app: struct dcb_app \*

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

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param new:
        *undescribed*
    :type new: struct dcb_app \*

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

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param app:
        *undescribed*
    :type app: struct dcb_app \*

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

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param new:
        *undescribed*
    :type new: struct dcb_app \*

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

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

    :param del:
        *undescribed*
    :type del: struct dcb_app \*

.. _`dcb_ieee_delapp.description`:

Description
-----------

This removes a matching APP data from the APP list

.. _`dcb_ieee_getapp_prio_dscp_mask_map`:

dcb_ieee_getapp_prio_dscp_mask_map
==================================

.. c:function:: void dcb_ieee_getapp_prio_dscp_mask_map(const struct net_device *dev, struct dcb_ieee_app_prio_map *p_map)

    For a given device, find mapping from priorities to the DSCP values assigned to that priority. Initialize p_map such that each map element holds a bit mask of DSCP values configured for that priority by APP entries.

    :param dev:
        *undescribed*
    :type dev: const struct net_device \*

    :param p_map:
        *undescribed*
    :type p_map: struct dcb_ieee_app_prio_map \*

.. _`dcb_ieee_getapp_dscp_prio_mask_map`:

dcb_ieee_getapp_dscp_prio_mask_map
==================================

.. c:function:: void dcb_ieee_getapp_dscp_prio_mask_map(const struct net_device *dev, struct dcb_ieee_app_dscp_map *p_map)

    For a given device, find mapping from DSCP values to the priorities assigned to that DSCP value. Initialize p_map such that each map element holds a bit mask of priorities configured for a given DSCP value by APP entries.

    :param dev:
        *undescribed*
    :type dev: const struct net_device \*

    :param p_map:
        *undescribed*
    :type p_map: struct dcb_ieee_app_dscp_map \*

.. _`dcb_ieee_getapp_default_prio_mask`:

dcb_ieee_getapp_default_prio_mask
=================================

.. c:function:: u8 dcb_ieee_getapp_default_prio_mask(const struct net_device *dev)

    2014, the selector value of 1 is used for matching on Ethernet type, with valid PID values >= 1536. A special meaning is then assigned to

    :param dev:
        *undescribed*
    :type dev: const struct net_device \*

.. _`dcb_ieee_getapp_default_prio_mask.protocol-value-of-0`:

protocol value of 0
-------------------

"default priority. For use when priority is not
otherwise specified".

dcb_ieee_getapp_default_prio_mask - For a given device, find all APP entries
of the form {$PRIO, ETHERTYPE, 0} and construct a bit mask of all default
priorities set by these entries.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

=====
reg.c
=====


.. _`wireless-regulatory-infrastructure`:

Wireless regulatory infrastructure
==================================

The usual implementation is for a driver to read a device EEPROM to
determine which regulatory domain it should be operating under, then
looking up the allowable channels in a driver-local table and finally
registering those channels in the wiphy structure.

Another set of compliance enforcement is for drivers to use their
own compliance limits which can be stored on the EEPROM. The host
driver or firmware may ensure these are used.

In addition to all this we provide an extra layer of regulatory
conformance. For drivers which do not have any regulatory
information CRDA provides the complete regulatory solution.
For others it provides a community effort on further restrictions
to enhance compliance.

Note: When number of rules --> infinity we will not be able to
index on alpha2 any more, instead we'll probably have to
rely on some SHA1 checksum of the regdomain for example.



.. _`reg_request_treatment`:

enum reg_request_treatment
==========================

.. c:type:: reg_request_treatment

    regulatory request treatment


.. _`reg_request_treatment.definition`:

Definition
----------

.. code-block:: c

    enum reg_request_treatment {
      REG_REQ_OK,
      REG_REQ_IGNORE,
      REG_REQ_INTERSECT,
      REG_REQ_ALREADY_SET
    };


.. _`reg_request_treatment.constants`:

Constants
---------

:``REG_REQ_OK``:
    continue processing the regulatory request

:``REG_REQ_IGNORE``:
    ignore the regulatory request

:``REG_REQ_INTERSECT``:
    the regulatory domain resulting from this request should
    be intersected with the current one.

:``REG_REQ_ALREADY_SET``:
    the regulatory request will not change the current
    regulatory settings, and no further processing is required.


.. _`freq_in_rule_band`:

freq_in_rule_band
=================

.. c:function:: bool freq_in_rule_band (const struct ieee80211_freq_range *freq_range, u32 freq_khz)

    tells us if a frequency is in a frequency band

    :param const struct ieee80211_freq_range \*freq_range:
        frequency rule we want to query

    :param u32 freq_khz:
        frequency we are inquiring about



.. _`freq_in_rule_band.description`:

Description
-----------

This lets us know if a specific frequency rule is or is not relevant to
a specific frequency's band. Bands are device specific and artificial
definitions (the "2.4 GHz band", the "5 GHz band" and the "60GHz band"),
however it is safe for now to assume that a frequency rule should not be
part of a frequency's band if the start freq or end freq are off by more
than 2 GHz for the 2.4 and 5 GHz bands, and by more than 10 GHz for the
60 GHz band.
This resolution can be lowered and should be considered as we add
regulatory rule support for other "bands".



.. _`regdom_intersect`:

regdom_intersect
================

.. c:function:: struct ieee80211_regdomain *regdom_intersect (const struct ieee80211_regdomain *rd1, const struct ieee80211_regdomain *rd2)

    do the intersection between two regulatory domains

    :param const struct ieee80211_regdomain \*rd1:
        first regulatory domain

    :param const struct ieee80211_regdomain \*rd2:
        second regulatory domain



.. _`regdom_intersect.description`:

Description
-----------

Use this function to get the intersection between two regulatory domains.
Once completed we will mark the alpha2 for the rd as intersected, "98",
as no one single alpha2 can represent this regulatory domain.

Returns a pointer to the regulatory domain structure which will hold the
resulting intersection of rules between rd1 and rd2. We will
:c:func:`kzalloc` this structure for you.



.. _`reg_process_hint_core`:

reg_process_hint_core
=====================

.. c:function:: enum reg_request_treatment reg_process_hint_core (struct regulatory_request *core_request)

    process core regulatory requests

    :param struct regulatory_request \*core_request:

        *undescribed*



.. _`reg_process_hint_core.description`:

Description
-----------

The wireless subsystem can use this function to process
a regulatory request issued by the regulatory core.



.. _`reg_process_hint_user`:

reg_process_hint_user
=====================

.. c:function:: enum reg_request_treatment reg_process_hint_user (struct regulatory_request *user_request)

    process user regulatory requests

    :param struct regulatory_request \*user_request:
        a pending user regulatory request



.. _`reg_process_hint_user.description`:

Description
-----------

The wireless subsystem can use this function to process
a regulatory request initiated by userspace.



.. _`reg_process_hint_driver`:

reg_process_hint_driver
=======================

.. c:function:: enum reg_request_treatment reg_process_hint_driver (struct wiphy *wiphy, struct regulatory_request *driver_request)

    process driver regulatory requests

    :param struct wiphy \*wiphy:

        *undescribed*

    :param struct regulatory_request \*driver_request:
        a pending driver regulatory request



.. _`reg_process_hint_driver.description`:

Description
-----------

The wireless subsystem can use this function to process
a regulatory request issued by an 802.11 driver.

Returns one of the different reg request treatment values.



.. _`reg_process_hint_country_ie`:

reg_process_hint_country_ie
===========================

.. c:function:: enum reg_request_treatment reg_process_hint_country_ie (struct wiphy *wiphy, struct regulatory_request *country_ie_request)

    process regulatory requests from country IEs

    :param struct wiphy \*wiphy:

        *undescribed*

    :param struct regulatory_request \*country_ie_request:
        a regulatory request from a country IE



.. _`reg_process_hint_country_ie.description`:

Description
-----------

The wireless subsystem can use this function to process
a regulatory request issued by a country Information Element.

Returns one of the different reg request treatment values.


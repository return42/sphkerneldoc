.. -*- coding: utf-8; mode: rst -*-

================
rtl819x_HTProc.c
================


.. _`htiotactisdisablemcs15`:

HTIOTActIsDisableMCS15
======================

.. c:function:: bool HTIOTActIsDisableMCS15 (struct ieee80211_device *ieee)

    :param struct ieee80211_device \*ieee:

        *undescribed*



.. _`htiotactisdisablemcs15.overview`:

Overview
--------

Check whether driver should declare capability of receiving MCS15



.. _`htiotactisdisablemcs15.input`:

Input
-----

PADAPTER                Adapter,



.. _`htiotactisdisablemcs15.output`:

Output
------

None



.. _`htiotactisdisablemcs15.return`:

Return
------

true if driver should disable MCS15
2008.04.15        Emily



.. _`htiotactisdisablemcstwospatialstream`:

HTIOTActIsDisableMCSTwoSpatialStream
====================================

.. c:function:: bool HTIOTActIsDisableMCSTwoSpatialStream (struct ieee80211_device *ieee, u8 *PeerMacAddr)

    :param struct ieee80211_device \*ieee:

        *undescribed*

    :param u8 \*PeerMacAddr:

        *undescribed*



.. _`htiotactisdisablemcstwospatialstream.overview`:

Overview
--------

Check whether driver should declare capability of receiving All 2 ss packets



.. _`htiotactisdisablemcstwospatialstream.input`:

Input
-----

PADAPTER                Adapter,



.. _`htiotactisdisablemcstwospatialstream.output`:

Output
------

None



.. _`htiotactisdisablemcstwospatialstream.return`:

Return
------

true if driver should disable all two spatial stream packet
2008.04.21        Emily


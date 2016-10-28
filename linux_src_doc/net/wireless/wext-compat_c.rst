.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wireless/wext-compat.c

.. _`cfg80211_wext_freq`:

cfg80211_wext_freq
==================

.. c:function:: int cfg80211_wext_freq(struct iw_freq *freq)

    get wext frequency for non-"auto"

    :param struct iw_freq \*freq:
        the wext freq encoding

.. _`cfg80211_wext_freq.description`:

Description
-----------

Returns a frequency, or a negative error code, or 0 for auto.

.. This file was automatic generated / don't edit.


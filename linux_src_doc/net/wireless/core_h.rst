.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wireless/core.h

.. _`cfg80211_chandef_dfs_usable`:

cfg80211_chandef_dfs_usable
===========================

.. c:function:: bool cfg80211_chandef_dfs_usable(struct wiphy *wiphy, const struct cfg80211_chan_def *chandef)

    checks if chandef is DFS usable

    :param struct wiphy \*wiphy:
        the wiphy to validate against

    :param const struct cfg80211_chan_def \*chandef:
        the channel definition to check

.. _`cfg80211_chandef_dfs_usable.description`:

Description
-----------

Checks if chandef is usable and we can/need start CAC on such channel.

.. _`cfg80211_chandef_dfs_usable.return`:

Return
------

Return true if all channels available and at least
one channel require CAC (NL80211_DFS_USABLE)

.. This file was automatic generated / don't edit.


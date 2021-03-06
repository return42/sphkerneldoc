.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wireless/reg.h

.. _`regulatory_hint_indoor`:

regulatory_hint_indoor
======================

.. c:function:: int regulatory_hint_indoor(bool is_indoor, u32 portid)

    hint operation in indoor env. or not

    :param is_indoor:
        if true indicates that user space thinks that the
        device is operating in an indoor environment.
    :type is_indoor: bool

    :param portid:
        the netlink port ID on which the hint was given.
    :type portid: u32

.. _`regulatory_netlink_notify`:

regulatory_netlink_notify
=========================

.. c:function:: void regulatory_netlink_notify(u32 portid)

    notify on released netlink socket

    :param portid:
        the netlink socket port ID
    :type portid: u32

.. _`regulatory_hint_found_beacon`:

regulatory_hint_found_beacon
============================

.. c:function:: int regulatory_hint_found_beacon(struct wiphy *wiphy, struct ieee80211_channel *beacon_chan, gfp_t gfp)

    hints a beacon was found on a channel

    :param wiphy:
        the wireless device where the beacon was found on
    :type wiphy: struct wiphy \*

    :param beacon_chan:
        the channel on which the beacon was found on
    :type beacon_chan: struct ieee80211_channel \*

    :param gfp:
        context flags
    :type gfp: gfp_t

.. _`regulatory_hint_found_beacon.description`:

Description
-----------

This informs the wireless core that a beacon from an AP was found on
the channel provided. This allows the wireless core to make educated
guesses on regulatory to help with world roaming. This is only used for
world roaming -- when we do not know our current location. This is
only useful on channels 12, 13 and 14 on the 2 GHz band as channels
1-11 are already enabled by the world regulatory domain; and on
non-radar 5 GHz channels.

Drivers do not need to call this, cfg80211 will do it for after a scan
on a newly found BSS. If you cannot make use of this feature you can
set the wiphy->disable_beacon_hints to true.

.. _`regulatory_hint_country_ie`:

regulatory_hint_country_ie
==========================

.. c:function:: void regulatory_hint_country_ie(struct wiphy *wiphy, enum nl80211_band band, const u8 *country_ie, u8 country_ie_len)

    hints a country IE as a regulatory domain

    :param wiphy:
        the wireless device giving the hint (used only for reporting
        conflicts)
    :type wiphy: struct wiphy \*

    :param band:
        the band on which the country IE was received on. This determines
        the band we'll process the country IE channel triplets for.
    :type band: enum nl80211_band

    :param country_ie:
        pointer to the country IE
    :type country_ie: const u8 \*

    :param country_ie_len:
        length of the country IE
    :type country_ie_len: u8

.. _`regulatory_hint_country_ie.description`:

Description
-----------

We will intersect the rd with the what CRDA tells us should apply
for the alpha2 this country IE belongs to, this prevents APs from
sending us incorrect or outdated information against a country.

The AP is expected to provide Country IE channel triplets for the
band it is on. It is technically possible for APs to send channel
country IE triplets even for channels outside of the band they are
in but for that they would have to use the regulatory extension
in combination with a triplet but this behaviour is currently
not observed. For this reason if a triplet is seen with channel
information for a band the BSS is not present in it will be ignored.

.. _`regulatory_hint_disconnect`:

regulatory_hint_disconnect
==========================

.. c:function:: void regulatory_hint_disconnect( void)

    informs all devices have been disconneted

    :param void:
        no arguments
    :type void: 

.. _`regulatory_hint_disconnect.description`:

Description
-----------

Regulotory rules can be enhanced further upon scanning and upon
connection to an AP. These rules become stale if we disconnect
and go to another country, whether or not we suspend and resume.
If we suspend, go to another country and resume we'll automatically
get disconnected shortly after resuming and things will be reset as well.
This routine is a helper to restore regulatory settings to how they were
prior to our first connect attempt. This includes ignoring country IE and
beacon regulatory hints. The ieee80211_regdom module parameter will always
be respected but if a user had set the regulatory domain that will take
precedence.

Must be called from process context.

.. _`cfg80211_get_unii`:

cfg80211_get_unii
=================

.. c:function:: int cfg80211_get_unii(int freq)

    get the U-NII band for the frequency

    :param freq:
        the frequency for which we want to get the UNII band.
        Get a value specifying the U-NII band frequency belongs to.
        U-NII bands are defined by the FCC in C.F.R 47 part 15.
    :type freq: int

.. _`cfg80211_get_unii.description`:

Description
-----------

Returns -EINVAL if freq is invalid, 0 for UNII-1, 1 for UNII-2A,
2 for UNII-2B, 3 for UNII-2C and 4 for UNII-3.

.. _`regulatory_indoor_allowed`:

regulatory_indoor_allowed
=========================

.. c:function:: bool regulatory_indoor_allowed( void)

    is indoor operation allowed

    :param void:
        no arguments
    :type void: 

.. _`regulatory_pre_cac_allowed`:

regulatory_pre_cac_allowed
==========================

.. c:function:: bool regulatory_pre_cac_allowed(struct wiphy *wiphy)

    if pre-CAC allowed in the current dfs domain

    :param wiphy:
        wiphy for which pre-CAC capability is checked.
        Pre-CAC is allowed only in ETSI domain.
    :type wiphy: struct wiphy \*

.. _`regulatory_propagate_dfs_state`:

regulatory_propagate_dfs_state
==============================

.. c:function:: void regulatory_propagate_dfs_state(struct wiphy *wiphy, struct cfg80211_chan_def *chandef, enum nl80211_dfs_state dfs_state, enum nl80211_radar_event event)

    Propagate DFS channel state to other wiphys \ ``wiphy``\  - wiphy on which radar is detected and the event will be propagated to other available wiphys having the same DFS domain \ ``chandef``\  - Channel definition of radar detected channel \ ``dfs_state``\  - DFS channel state to be set \ ``event``\  - Type of radar event which triggered this DFS state change

    :param wiphy:
        *undescribed*
    :type wiphy: struct wiphy \*

    :param chandef:
        *undescribed*
    :type chandef: struct cfg80211_chan_def \*

    :param dfs_state:
        *undescribed*
    :type dfs_state: enum nl80211_dfs_state

    :param event:
        *undescribed*
    :type event: enum nl80211_radar_event

.. _`regulatory_propagate_dfs_state.description`:

Description
-----------

This function should be called with rtnl lock held.

.. _`reg_dfs_domain_same`:

reg_dfs_domain_same
===================

.. c:function:: bool reg_dfs_domain_same(struct wiphy *wiphy1, struct wiphy *wiphy2)

    Checks if both wiphy have same DFS domain configured \ ``wiphy1``\  - wiphy it's dfs_region to be checked against that of wiphy2 \ ``wiphy2``\  - wiphy it's dfs_region to be checked against that of wiphy1

    :param wiphy1:
        *undescribed*
    :type wiphy1: struct wiphy \*

    :param wiphy2:
        *undescribed*
    :type wiphy2: struct wiphy \*

.. _`reg_reload_regdb`:

reg_reload_regdb
================

.. c:function:: int reg_reload_regdb( void)

    reload the regulatory.db firmware file

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


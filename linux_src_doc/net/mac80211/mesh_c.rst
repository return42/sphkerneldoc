.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/mesh.c

.. _`mesh_matches_local`:

mesh_matches_local
==================

.. c:function:: bool mesh_matches_local(struct ieee80211_sub_if_data *sdata, struct ieee802_11_elems *ie)

    check if the config of a mesh point matches ours

    :param sdata:
        local mesh subif
    :type sdata: struct ieee80211_sub_if_data \*

    :param ie:
        information elements of a management frame from the mesh peer
    :type ie: struct ieee802_11_elems \*

.. _`mesh_matches_local.description`:

Description
-----------

This function checks if the mesh configuration of a mesh point matches the
local mesh configuration, i.e. if both nodes belong to the same mesh network.

.. _`mesh_peer_accepts_plinks`:

mesh_peer_accepts_plinks
========================

.. c:function:: bool mesh_peer_accepts_plinks(struct ieee802_11_elems *ie)

    check if an mp is willing to establish peer links

    :param ie:
        information elements of a management frame from the mesh peer
    :type ie: struct ieee802_11_elems \*

.. _`mesh_accept_plinks_update`:

mesh_accept_plinks_update
=========================

.. c:function:: u32 mesh_accept_plinks_update(struct ieee80211_sub_if_data *sdata)

    update accepting_plink in local mesh beacons

    :param sdata:
        mesh interface in which mesh beacons are going to be updated
    :type sdata: struct ieee80211_sub_if_data \*

.. _`mesh_accept_plinks_update.return`:

Return
------

beacon changed flag if the beacon content changed.

.. _`mesh_rmc_check`:

mesh_rmc_check
==============

.. c:function:: int mesh_rmc_check(struct ieee80211_sub_if_data *sdata, const u8 *sa, struct ieee80211s_hdr *mesh_hdr)

    Check frame in recent multicast cache and add if absent.

    :param sdata:
        interface
    :type sdata: struct ieee80211_sub_if_data \*

    :param sa:
        source address
    :type sa: const u8 \*

    :param mesh_hdr:
        mesh_header
    :type mesh_hdr: struct ieee80211s_hdr \*

.. _`mesh_rmc_check.return`:

Return
------

0 if the frame is not in the cache, nonzero otherwise.

Checks using the source address and the mesh sequence number if we have
received this frame lately. If the frame is not in the cache, it is added to
it.

.. _`ieee80211_fill_mesh_addresses`:

ieee80211_fill_mesh_addresses
=============================

.. c:function:: int ieee80211_fill_mesh_addresses(struct ieee80211_hdr *hdr, __le16 *fc, const u8 *meshda, const u8 *meshsa)

    fill addresses of a locally originated mesh frame

    :param hdr:
        802.11 frame header
    :type hdr: struct ieee80211_hdr \*

    :param fc:
        frame control field
    :type fc: __le16 \*

    :param meshda:
        destination address in the mesh
    :type meshda: const u8 \*

    :param meshsa:
        source address address in the mesh.  Same as TA, as frame is
        locally originated.
    :type meshsa: const u8 \*

.. _`ieee80211_fill_mesh_addresses.description`:

Description
-----------

Return the length of the 802.11 (does not include a mesh control header)

.. _`ieee80211_new_mesh_header`:

ieee80211_new_mesh_header
=========================

.. c:function:: unsigned int ieee80211_new_mesh_header(struct ieee80211_sub_if_data *sdata, struct ieee80211s_hdr *meshhdr, const char *addr4or5, const char *addr6)

    create a new mesh header

    :param sdata:
        mesh interface to be used
    :type sdata: struct ieee80211_sub_if_data \*

    :param meshhdr:
        uninitialized mesh header
    :type meshhdr: struct ieee80211s_hdr \*

    :param addr4or5:
        1st address in the ae header, which may correspond to address 4
        (if addr6 is NULL) or address 5 (if addr6 is present). It may
        be NULL.
    :type addr4or5: const char \*

    :param addr6:
        2nd address in the ae header, which corresponds to addr6 of the
        mesh frame
    :type addr6: const char \*

.. _`ieee80211_new_mesh_header.description`:

Description
-----------

Return the header length.

.. This file was automatic generated / don't edit.


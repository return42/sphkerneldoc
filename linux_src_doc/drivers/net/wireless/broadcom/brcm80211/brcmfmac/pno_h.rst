.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.h

.. _`brcmf_pno_start_sched_scan`:

brcmf_pno_start_sched_scan
==========================

.. c:function:: int brcmf_pno_start_sched_scan(struct brcmf_if *ifp, struct cfg80211_sched_scan_request *req)

    initiate scheduled scan on device.

    :param ifp:
        interface object used.
    :type ifp: struct brcmf_if \*

    :param req:
        configuration parameters for scheduled scan.
    :type req: struct cfg80211_sched_scan_request \*

.. _`brcmf_pno_stop_sched_scan`:

brcmf_pno_stop_sched_scan
=========================

.. c:function:: int brcmf_pno_stop_sched_scan(struct brcmf_if *ifp, u64 reqid)

    terminate scheduled scan on device.

    :param ifp:
        interface object used.
    :type ifp: struct brcmf_if \*

    :param reqid:
        unique identifier of scan to be stopped.
    :type reqid: u64

.. _`brcmf_pno_wiphy_params`:

brcmf_pno_wiphy_params
======================

.. c:function:: void brcmf_pno_wiphy_params(struct wiphy *wiphy, bool gscan)

    fill scheduled scan parameters in wiphy instance.

    :param wiphy:
        wiphy instance to be used.
    :type wiphy: struct wiphy \*

    :param gscan:
        indicates whether the device has support for g-scan feature.
    :type gscan: bool

.. _`brcmf_pno_attach`:

brcmf_pno_attach
================

.. c:function:: int brcmf_pno_attach(struct brcmf_cfg80211_info *cfg)

    allocate and attach module information.

    :param cfg:
        cfg80211 context used.
    :type cfg: struct brcmf_cfg80211_info \*

.. _`brcmf_pno_detach`:

brcmf_pno_detach
================

.. c:function:: void brcmf_pno_detach(struct brcmf_cfg80211_info *cfg)

    detach and free module information.

    :param cfg:
        cfg80211 context used.
    :type cfg: struct brcmf_cfg80211_info \*

.. _`brcmf_pno_find_reqid_by_bucket`:

brcmf_pno_find_reqid_by_bucket
==============================

.. c:function:: u64 brcmf_pno_find_reqid_by_bucket(struct brcmf_pno_info *pi, u32 bucket)

    find request id for given bucket index.

    :param pi:
        pno instance used.
    :type pi: struct brcmf_pno_info \*

    :param bucket:
        index of firmware bucket.
    :type bucket: u32

.. _`brcmf_pno_get_bucket_map`:

brcmf_pno_get_bucket_map
========================

.. c:function:: u32 brcmf_pno_get_bucket_map(struct brcmf_pno_info *pi, struct brcmf_pno_net_info_le *netinfo)

    determine bucket map for given netinfo.

    :param pi:
        pno instance used.
    :type pi: struct brcmf_pno_info \*

    :param netinfo:
        netinfo to compare with bucket configuration.
    :type netinfo: struct brcmf_pno_net_info_le \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/pno.h

.. _`brcmf_pno_start_sched_scan`:

brcmf_pno_start_sched_scan
==========================

.. c:function:: int brcmf_pno_start_sched_scan(struct brcmf_if *ifp, struct cfg80211_sched_scan_request *req)

    initiate scheduled scan on device.

    :param struct brcmf_if \*ifp:
        interface object used.

    :param struct cfg80211_sched_scan_request \*req:
        configuration parameters for scheduled scan.

.. _`brcmf_pno_stop_sched_scan`:

brcmf_pno_stop_sched_scan
=========================

.. c:function:: int brcmf_pno_stop_sched_scan(struct brcmf_if *ifp, u64 reqid)

    terminate scheduled scan on device.

    :param struct brcmf_if \*ifp:
        interface object used.

    :param u64 reqid:
        unique identifier of scan to be stopped.

.. _`brcmf_pno_wiphy_params`:

brcmf_pno_wiphy_params
======================

.. c:function:: void brcmf_pno_wiphy_params(struct wiphy *wiphy, bool gscan)

    fill scheduled scan parameters in wiphy instance.

    :param struct wiphy \*wiphy:
        wiphy instance to be used.

    :param bool gscan:
        indicates whether the device has support for g-scan feature.

.. _`brcmf_pno_attach`:

brcmf_pno_attach
================

.. c:function:: int brcmf_pno_attach(struct brcmf_cfg80211_info *cfg)

    allocate and attach module information.

    :param struct brcmf_cfg80211_info \*cfg:
        cfg80211 context used.

.. _`brcmf_pno_detach`:

brcmf_pno_detach
================

.. c:function:: void brcmf_pno_detach(struct brcmf_cfg80211_info *cfg)

    detach and free module information.

    :param struct brcmf_cfg80211_info \*cfg:
        cfg80211 context used.

.. _`brcmf_pno_find_reqid_by_bucket`:

brcmf_pno_find_reqid_by_bucket
==============================

.. c:function:: u64 brcmf_pno_find_reqid_by_bucket(struct brcmf_pno_info *pi, u32 bucket)

    find request id for given bucket index.

    :param struct brcmf_pno_info \*pi:
        pno instance used.

    :param u32 bucket:
        index of firmware bucket.

.. _`brcmf_pno_get_bucket_map`:

brcmf_pno_get_bucket_map
========================

.. c:function:: u32 brcmf_pno_get_bucket_map(struct brcmf_pno_info *pi, struct brcmf_pno_net_info_le *netinfo)

    determine bucket map for given netinfo.

    :param struct brcmf_pno_info \*pi:
        pno instance used.

    :param struct brcmf_pno_net_info_le \*netinfo:
        netinfo to compare with bucket configuration.

.. This file was automatic generated / don't edit.


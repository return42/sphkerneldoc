.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.h

.. _`brcmf_feat_attach`:

brcmf_feat_attach
=================

.. c:function:: void brcmf_feat_attach(struct brcmf_pub *drvr)

    determine features and quirks.

    :param struct brcmf_pub \*drvr:
        driver instance.

.. _`brcmf_feat_is_enabled`:

brcmf_feat_is_enabled
=====================

.. c:function:: bool brcmf_feat_is_enabled(struct brcmf_if *ifp, enum brcmf_feat_id id)

    query feature.

    :param struct brcmf_if \*ifp:
        interface instance.

    :param enum brcmf_feat_id id:
        feature id to check.

.. _`brcmf_feat_is_enabled.return`:

Return
------

true is feature is enabled; otherwise false.

.. _`brcmf_feat_is_quirk_enabled`:

brcmf_feat_is_quirk_enabled
===========================

.. c:function:: bool brcmf_feat_is_quirk_enabled(struct brcmf_if *ifp, enum brcmf_feat_quirk quirk)

    query chip quirk.

    :param struct brcmf_if \*ifp:
        interface instance.

    :param enum brcmf_feat_quirk quirk:
        quirk id to check.

.. _`brcmf_feat_is_quirk_enabled.return`:

Return
------

true is quirk is enabled; otherwise false.

.. This file was automatic generated / don't edit.


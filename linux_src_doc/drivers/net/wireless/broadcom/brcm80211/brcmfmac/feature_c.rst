.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c

.. _`brcmf_feat_debugfs_read`:

brcmf_feat_debugfs_read
=======================

.. c:function:: int brcmf_feat_debugfs_read(struct seq_file *seq, void *data)

    expose feature info to debugfs.

    :param struct seq_file \*seq:
        sequence for debugfs entry.

    :param void \*data:
        raw data pointer.

.. _`brcmf_feat_iovar_int_get`:

brcmf_feat_iovar_int_get
========================

.. c:function:: void brcmf_feat_iovar_int_get(struct brcmf_if *ifp, enum brcmf_feat_id id, char *name)

    determine feature through iovar query.

    :param struct brcmf_if \*ifp:
        interface to query.

    :param enum brcmf_feat_id id:
        feature id.

    :param char \*name:
        iovar name.

.. _`brcmf_feat_fwcap_debugfs_read`:

brcmf_feat_fwcap_debugfs_read
=============================

.. c:function:: int brcmf_feat_fwcap_debugfs_read(struct seq_file *seq, void *data)

    expose firmware capabilities to debugfs.

    :param struct seq_file \*seq:
        sequence for debugfs entry.

    :param void \*data:
        raw data pointer.

.. This file was automatic generated / don't edit.


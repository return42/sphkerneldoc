.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/feature.c

.. _`brcmf_feat_debugfs_read`:

brcmf_feat_debugfs_read
=======================

.. c:function:: int brcmf_feat_debugfs_read(struct seq_file *seq, void *data)

    expose feature info to debugfs.

    :param seq:
        sequence for debugfs entry.
    :type seq: struct seq_file \*

    :param data:
        raw data pointer.
    :type data: void \*

.. _`brcmf_feat_iovar_int_get`:

brcmf_feat_iovar_int_get
========================

.. c:function:: void brcmf_feat_iovar_int_get(struct brcmf_if *ifp, enum brcmf_feat_id id, char *name)

    determine feature through iovar query.

    :param ifp:
        interface to query.
    :type ifp: struct brcmf_if \*

    :param id:
        feature id.
    :type id: enum brcmf_feat_id

    :param name:
        iovar name.
    :type name: char \*

.. _`brcmf_feat_fwcap_debugfs_read`:

brcmf_feat_fwcap_debugfs_read
=============================

.. c:function:: int brcmf_feat_fwcap_debugfs_read(struct seq_file *seq, void *data)

    expose firmware capabilities to debugfs.

    :param seq:
        sequence for debugfs entry.
    :type seq: struct seq_file \*

    :param data:
        raw data pointer.
    :type data: void \*

.. This file was automatic generated / don't edit.


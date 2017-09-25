.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/hdaudio_ext.h

.. _`hdac_ext_device`:

struct hdac_ext_device
======================

.. c:type:: struct hdac_ext_device

    HDAC Ext device

.. _`hdac_ext_device.definition`:

Definition
----------

.. code-block:: c

    struct hdac_ext_device {
        struct hdac_device hdac;
        struct hdac_ext_bus *ebus;
        struct hda_dai_map nid_list[HDA_MAX_NIDS];
        unsigned int map_cur_idx;
        struct hdac_ext_codec_ops ops;
        struct snd_card *card;
        void *scodec;
        void *private_data;
    }

.. _`hdac_ext_device.members`:

Members
-------

hdac
    hdac core device
    \ ``nid_list``\  - the dai map which matches the dai-name with the nid
    \ ``map_cur_idx``\  - the idx in use in dai_map
    \ ``ops``\  - the hda codec ops common to all codec drivers
    \ ``pvt_data``\  - private data, for asoc contains asoc codec object

ebus
    *undescribed*

nid_list
    *undescribed*

map_cur_idx
    *undescribed*

ops
    *undescribed*

card
    *undescribed*

scodec
    *undescribed*

private_data
    *undescribed*

.. This file was automatic generated / don't edit.


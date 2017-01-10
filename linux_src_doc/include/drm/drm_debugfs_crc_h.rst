.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_debugfs_crc.h

.. _`drm_crtc_crc_entry`:

struct drm_crtc_crc_entry
=========================

.. c:type:: struct drm_crtc_crc_entry

    entry describing a frame's content

.. _`drm_crtc_crc_entry.definition`:

Definition
----------

.. code-block:: c

    struct drm_crtc_crc_entry {
        bool has_frame_counter;
        uint32_t frame;
        uint32_t crcs[DRM_MAX_CRC_NR];
    }

.. _`drm_crtc_crc_entry.members`:

Members
-------

has_frame_counter
    whether the source was able to provide a frame number

frame
    number of the frame this CRC is about, if \ ``has_frame_counter``\  is true

.. _`drm_crtc_crc`:

struct drm_crtc_crc
===================

.. c:type:: struct drm_crtc_crc

    data supporting CRC capture on a given CRTC

.. _`drm_crtc_crc.definition`:

Definition
----------

.. code-block:: c

    struct drm_crtc_crc {
        spinlock_t lock;
        const char *source;
        bool opened;
        struct drm_crtc_crc_entry *entries;
        int head;
        int tail;
        size_t values_cnt;
        wait_queue_head_t wq;
    }

.. _`drm_crtc_crc.members`:

Members
-------

lock
    protects the fields in this struct

source
    name of the currently configured source of CRCs

opened
    whether userspace has opened the data file for reading

entries
    array of entries, with size of \ ``DRM_CRC_ENTRIES_NR``\ 

head
    head of circular queue

tail
    tail of circular queue

values_cnt
    number of CRC values per entry, up to \ ``DRM_MAX_CRC_NR``\ 

wq
    workqueue used to synchronize reading and writing

.. This file was automatic generated / don't edit.


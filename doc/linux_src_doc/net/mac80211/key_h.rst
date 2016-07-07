.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/key.h

.. _`ieee80211_internal_key_flags`:

enum ieee80211_internal_key_flags
=================================

.. c:type:: enum ieee80211_internal_key_flags

    internal key flags

.. _`ieee80211_internal_key_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_internal_key_flags {
        KEY_FLAG_UPLOADED_TO_HARDWARE,
        KEY_FLAG_TAINTED,
        KEY_FLAG_CIPHER_SCHEME
    };

.. _`ieee80211_internal_key_flags.constants`:

Constants
---------

KEY_FLAG_UPLOADED_TO_HARDWARE
    Indicates that this key is present
    in the hardware for TX crypto hardware acceleration.

KEY_FLAG_TAINTED
    Key is tainted and packets should be dropped.

KEY_FLAG_CIPHER_SCHEME
    This key is for a hardware cipher scheme

.. This file was automatic generated / don't edit.


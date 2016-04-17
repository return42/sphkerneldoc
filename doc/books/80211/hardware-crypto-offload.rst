
.. _hardware-crypto-offload:

============================
Hardware crypto acceleration
============================

mac80211 is capable of taking advantage of many hardware acceleration designs for encryption and decryption operations.

The ``set_key`` callback in the ``struct ieee80211_ops`` for a given device is called to enable hardware acceleration of encryption and decryption. The callback takes a ``sta``
parameter that will be NULL for default keys or keys used for transmission only, or point to the station information for the peer for individual keys. Multiple transmission keys
with the same key index may be used when VLANs are configured for an access point.

When transmitting, the TX control data will use the ``hw_key_idx`` selected by the driver by modifying the ``struct ieee80211_key_conf`` pointed to by the ``key`` parameter to the
``set_key`` function.

The ``set_key`` call for the ``SET_KEY`` command should return 0 if the key is now in use, -``EOPNOTSUPP`` or -``ENOSPC`` if it couldn't be added; if you return 0 then hw_key_idx
must be assigned to the hardware key index, you are free to use the full u8 range.

Note that in the case that the ``IEEE80211_HW_SW_CRYPTO_CONTROL`` flag is set, mac80211 will not automatically fall back to software crypto if enabling hardware crypto failed. The
``set_key`` call may also return the value 1 to permit this specific key/algorithm to be done in software.

When the cmd is ``DISABLE_KEY`` then it must succeed.

Note that it is permissible to not decrypt a frame even if a key for it has been uploaded to hardware, the stack will not make any decision based on whether a key has been uploaded
or not but rather based on the receive flags.

The ``struct ieee80211_key_conf`` structure pointed to by the ``key`` parameter is guaranteed to be valid until another call to ``set_key`` removes it, but it can only be used as a
cookie to differentiate keys.

In TKIP some HW need to be provided a phase 1 key, for RX decryption acceleration (i.e. iwlwifi). Those drivers should provide update_tkip_key handler. The ``update_tkip_key``
call updates the driver with the new phase 1 key. This happens every time the iv16 wraps around (every 65536 packets). The ``set_key`` call will happen only once for each key
(unless the AP did rekeying), it will not include a valid phase 1 key. The valid phase 1 key is provided by update_tkip_key only. The trigger that makes mac80211 call this
handler is software decryption with wrap around of iv16.

The ``set_default_unicast_key`` call updates the default WEP key index configured to the hardware for WEP encryption type. This is required for devices that support offload of data
packets (e.g. ARP responses).


.. toctree::
    :maxdepth: 1

    API-enum-set-key-cmd
    API-struct-ieee80211-key-conf
    API-enum-ieee80211-key-flags
    API-ieee80211-get-tkip-p1k
    API-ieee80211-get-tkip-p1k-iv
    API-ieee80211-get-tkip-p2k

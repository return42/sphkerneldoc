
.. _powersave:

=================
Powersave support
=================

mac80211 has support for various powersave implementations.

First, it can support hardware that handles all powersaving by itself, such hardware should simply set the ``IEEE80211_HW_SUPPORTS_PS`` hardware flag. In that case, it will be told
about the desired powersave mode with the ``IEEE80211_CONF_PS`` flag depending on the association status. The hardware must take care of sending nullfunc frames when necessary,
i.e. when entering and leaving powersave mode. The hardware is required to look at the AID in beacons and signal to the AP that it woke up when it finds traffic directed to it.

``IEEE80211_CONF_PS`` flag enabled means that the powersave mode defined in IEEE 802.11-2007 section 11.2 is enabled. This is not to be confused with hardware wakeup and sleep
states. Driver is responsible for waking up the hardware before issuing commands to the hardware and putting it back to sleep at appropriate times.

When PS is enabled, hardware needs to wakeup for beacons and receive the buffered multicast/broadcast frames after the beacon. Also it must be possible to send frames and receive
the acknowledment frame.

Other hardware designs cannot send nullfunc frames by themselves and also need software support for parsing the TIM bitmap. This is also supported by mac80211 by combining the
``IEEE80211_HW_SUPPORTS_PS`` and ``IEEE80211_HW_PS_NULLFUNC_STACK`` flags. The hardware is of course still required to pass up beacons. The hardware is still required to handle
waking up for multicast traffic; if it cannot the driver must handle that as best as it can, mac80211 is too slow to do that.

Dynamic powersave is an extension to normal powersave in which the hardware stays awake for a user-specified period of time after sending a frame so that reply frames need not be
buffered and therefore delayed to the next wakeup. It's compromise of getting good enough latency when there's data traffic and still saving significantly power in idle periods.

Dynamic powersave is simply supported by mac80211 enabling and disabling PS based on traffic. Driver needs to only set ``IEEE80211_HW_SUPPORTS_PS`` flag and mac80211 will handle
everything automatically. Additionally, hardware having support for the dynamic PS feature may set the ``IEEE80211_HW_SUPPORTS_DYNAMIC_PS`` flag to indicate that it can support
dynamic PS mode itself. The driver needs to look at the ``dynamic_ps_timeout`` hardware configuration value and use it that value whenever ``IEEE80211_CONF_PS`` is set. In this
case mac80211 will disable dynamic PS feature in stack and will just keep ``IEEE80211_CONF_PS`` enabled whenever user has enabled powersave.

Driver informs U-APSD client support by enabling ``IEEE80211_VIF_SUPPORTS_UAPSD`` flag. The mode is configured through the uapsd parameter in ``conf_tx`` operation. Hardware needs
to send the QoS Nullfunc frames and stay awake until the service period has ended. To utilize U-APSD, dynamic powersave is disabled for voip AC and all frames from that AC are
transmitted with powersave enabled.

Note: U-APSD client mode is not yet supported with ``IEEE80211_HW_PS_NULLFUNC_STACK``.

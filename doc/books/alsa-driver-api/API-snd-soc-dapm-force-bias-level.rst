
.. _API-snd-soc-dapm-force-bias-level:

=============================
snd_soc_dapm_force_bias_level
=============================

*man snd_soc_dapm_force_bias_level(9)*

*4.6.0-rc1*

Sets the DAPM bias level


Synopsis
========

.. c:function:: int snd_soc_dapm_force_bias_level( struct snd_soc_dapm_context * dapm, enum snd_soc_bias_level level )

Arguments
=========

``dapm``
    The DAPM context for which to set the level

``level``
    The level to set


Description
===========

Forces the DAPM bias level to a specific state. It will call the bias level callback of DAPM context with the specified level. This will even happen if the context is already at
the same level. Furthermore it will not go through the normal bias level sequencing, meaning any intermediate states between the current and the target state will not be entered.

Note that the change in bias level is only temporary and the next time ``snd_soc_dapm_sync`` is called the state will be set to the level as determined by the DAPM core. The
function is mainly intended to be used to used during probe or resume from suspend to power up the device so initialization can be done, before the DAPM core takes over.

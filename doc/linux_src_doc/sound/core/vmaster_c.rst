.. -*- coding: utf-8; mode: rst -*-

=========
vmaster.c
=========

.. _`snd_ctl_make_virtual_master`:

snd_ctl_make_virtual_master
===========================

.. c:function:: struct snd_kcontrol *snd_ctl_make_virtual_master (char *name, const unsigned int *tlv)

    Create a virtual master control

    :param char \*name:
        name string of the control element to create

    :param const unsigned int \*tlv:
        optional TLV int array for dB information


.. _`snd_ctl_make_virtual_master.description`:

Description
-----------

Creates a virtual master control with the given name string.

After creating a vmaster element, you can add the slave controls
via :c:func:`snd_ctl_add_slave` or :c:func:`snd_ctl_add_slave_uncached`.

The optional argument ``tlv`` can be used to specify the TLV information
for dB scale of the master control.  It should be a single element
with #SNDRV_CTL_TLVT_DB_SCALE, #SNDRV_CTL_TLV_DB_MINMAX or
#SNDRV_CTL_TLVT_DB_MINMAX_MUTE type, and should be the max 0dB.

Return: The created control element, or ``NULL`` for errors (ENOMEM).


.. _`snd_ctl_add_vmaster_hook`:

snd_ctl_add_vmaster_hook
========================

.. c:function:: int snd_ctl_add_vmaster_hook (struct snd_kcontrol *kcontrol, void (*hook) (void *private_data, int, void *private_data)

    Add a hook to a vmaster control

    :param struct snd_kcontrol \*kcontrol:
        vmaster kctl element

    :param void (\*hook) (void \*private_data, int):
        the hook function

    :param void \*private_data:
        the private_data pointer to be saved


.. _`snd_ctl_add_vmaster_hook.description`:

Description
-----------

Adds the given hook to the vmaster control element so that it's called
at each time when the value is changed.

Return: Zero.


.. _`snd_ctl_sync_vmaster`:

snd_ctl_sync_vmaster
====================

.. c:function:: void snd_ctl_sync_vmaster (struct snd_kcontrol *kcontrol, bool hook_only)

    Sync the vmaster slaves and hook

    :param struct snd_kcontrol \*kcontrol:
        vmaster kctl element

    :param bool hook_only:
        sync only the hook


.. _`snd_ctl_sync_vmaster.description`:

Description
-----------

Forcibly call the put callback of each slave and call the hook function
to synchronize with the current value of the given vmaster element.
NOP when NULL is passed to ``kcontrol``\ .


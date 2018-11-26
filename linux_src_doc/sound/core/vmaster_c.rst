.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/vmaster.c

.. _`snd_ctl_make_virtual_master`:

snd_ctl_make_virtual_master
===========================

.. c:function:: struct snd_kcontrol *snd_ctl_make_virtual_master(char *name, const unsigned int *tlv)

    Create a virtual master control

    :param name:
        name string of the control element to create
    :type name: char \*

    :param tlv:
        optional TLV int array for dB information
    :type tlv: const unsigned int \*

.. _`snd_ctl_make_virtual_master.description`:

Description
-----------

Creates a virtual master control with the given name string.

After creating a vmaster element, you can add the slave controls
via \ :c:func:`snd_ctl_add_slave`\  or \ :c:func:`snd_ctl_add_slave_uncached`\ .

The optional argument \ ``tlv``\  can be used to specify the TLV information
for dB scale of the master control.  It should be a single element
with #SNDRV_CTL_TLVT_DB_SCALE, #SNDRV_CTL_TLV_DB_MINMAX or
#SNDRV_CTL_TLVT_DB_MINMAX_MUTE type, and should be the max 0dB.

.. _`snd_ctl_make_virtual_master.return`:

Return
------

The created control element, or \ ``NULL``\  for errors (ENOMEM).

.. _`snd_ctl_add_vmaster_hook`:

snd_ctl_add_vmaster_hook
========================

.. c:function:: int snd_ctl_add_vmaster_hook(struct snd_kcontrol *kcontrol, void (*hook)(void *private_data, int), void *private_data)

    Add a hook to a vmaster control

    :param kcontrol:
        vmaster kctl element
    :type kcontrol: struct snd_kcontrol \*

    :param void (\*hook)(void \*private_data, int):
        the hook function

    :param private_data:
        the private_data pointer to be saved
    :type private_data: void \*

.. _`snd_ctl_add_vmaster_hook.description`:

Description
-----------

Adds the given hook to the vmaster control element so that it's called
at each time when the value is changed.

.. _`snd_ctl_add_vmaster_hook.return`:

Return
------

Zero.

.. _`snd_ctl_sync_vmaster`:

snd_ctl_sync_vmaster
====================

.. c:function:: void snd_ctl_sync_vmaster(struct snd_kcontrol *kcontrol, bool hook_only)

    Sync the vmaster slaves and hook

    :param kcontrol:
        vmaster kctl element
    :type kcontrol: struct snd_kcontrol \*

    :param hook_only:
        sync only the hook
    :type hook_only: bool

.. _`snd_ctl_sync_vmaster.description`:

Description
-----------

Forcibly call the put callback of each slave and call the hook function
to synchronize with the current value of the given vmaster element.
NOP when NULL is passed to \ ``kcontrol``\ .

.. _`snd_ctl_apply_vmaster_slaves`:

snd_ctl_apply_vmaster_slaves
============================

.. c:function:: int snd_ctl_apply_vmaster_slaves(struct snd_kcontrol *kctl, int (*func)(struct snd_kcontrol *vslave, struct snd_kcontrol *slave, void *arg), void *arg)

    Apply function to each vmaster slave

    :param kctl:
        vmaster kctl element
    :type kctl: struct snd_kcontrol \*

    :param int (\*func)(struct snd_kcontrol \*vslave, struct snd_kcontrol \*slave, void \*arg):
        function to apply

    :param arg:
        optional function argument
    :type arg: void \*

.. _`snd_ctl_apply_vmaster_slaves.description`:

Description
-----------

Apply the function \ ``func``\  to each slave kctl of the given vmaster kctl.
Returns 0 if successful, or a negative error code.

.. This file was automatic generated / don't edit.


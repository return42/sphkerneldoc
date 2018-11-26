.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/jack.c

.. _`snd_jack_add_new_kctl`:

snd_jack_add_new_kctl
=====================

.. c:function:: int snd_jack_add_new_kctl(struct snd_jack *jack, const char *name, int mask)

    Create a new snd_jack_kctl and add it to jack

    :param jack:
        the jack instance which the kctl will attaching to
    :type jack: struct snd_jack \*

    :param name:
        the name for the snd_kcontrol object
    :type name: const char \*

    :param mask:
        a bitmask of enum snd_jack_type values that can be detected
        by this snd_jack_kctl object.
    :type mask: int

.. _`snd_jack_add_new_kctl.description`:

Description
-----------

Creates a new snd_kcontrol object and adds it to the jack kctl_list.

.. _`snd_jack_add_new_kctl.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_jack_new`:

snd_jack_new
============

.. c:function:: int snd_jack_new(struct snd_card *card, const char *id, int type, struct snd_jack **jjack, bool initial_kctl, bool phantom_jack)

    Create a new jack

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        an identifying string for this jack
    :type id: const char \*

    :param type:
        a bitmask of enum snd_jack_type values that can be detected by
        this jack
    :type type: int

    :param jjack:
        Used to provide the allocated jack object to the caller.
    :type jjack: struct snd_jack \*\*

    :param initial_kctl:
        if true, create a kcontrol and add it to the jack list.
    :type initial_kctl: bool

    :param phantom_jack:
        Don't create a input device for phantom jacks.
    :type phantom_jack: bool

.. _`snd_jack_new.description`:

Description
-----------

Creates a new jack object.

.. _`snd_jack_new.return`:

Return
------

Zero if successful, or a negative error code on failure.
On success \ ``jjack``\  will be initialised.

.. _`snd_jack_set_parent`:

snd_jack_set_parent
===================

.. c:function:: void snd_jack_set_parent(struct snd_jack *jack, struct device *parent)

    Set the parent device for a jack

    :param jack:
        The jack to configure
    :type jack: struct snd_jack \*

    :param parent:
        The device to set as parent for the jack.
    :type parent: struct device \*

.. _`snd_jack_set_parent.description`:

Description
-----------

Set the parent for the jack devices in the device tree.  This
function is only valid prior to registration of the jack.  If no
parent is configured then the parent device will be the sound card.

.. _`snd_jack_set_key`:

snd_jack_set_key
================

.. c:function:: int snd_jack_set_key(struct snd_jack *jack, enum snd_jack_types type, int keytype)

    Set a key mapping on a jack

    :param jack:
        The jack to configure
    :type jack: struct snd_jack \*

    :param type:
        Jack report type for this key
    :type type: enum snd_jack_types

    :param keytype:
        Input layer key type to be reported
    :type keytype: int

.. _`snd_jack_set_key.description`:

Description
-----------

Map a SND_JACK_BTN_* button type to an input layer key, allowing
reporting of keys on accessories via the jack abstraction.  If no
mapping is provided but keys are enabled in the jack type then
BTN_n numeric buttons will be reported.

If jacks are not reporting via the input API this call will have no
effect.

Note that this is intended to be use by simple devices with small
numbers of keys that can be reported.  It is also possible to
access the input device directly - devices with complex input
capabilities on accessories should consider doing this rather than
using this abstraction.

This function may only be called prior to registration of the jack.

.. _`snd_jack_set_key.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_jack_report`:

snd_jack_report
===============

.. c:function:: void snd_jack_report(struct snd_jack *jack, int status)

    Report the current status of a jack

    :param jack:
        The jack to report status for
    :type jack: struct snd_jack \*

    :param status:
        The current status of the jack
    :type status: int

.. This file was automatic generated / don't edit.


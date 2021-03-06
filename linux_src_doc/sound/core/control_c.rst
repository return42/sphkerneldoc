.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/control.c

.. _`snd_ctl_notify`:

snd_ctl_notify
==============

.. c:function:: void snd_ctl_notify(struct snd_card *card, unsigned int mask, struct snd_ctl_elem_id *id)

    Send notification to user-space for a control change

    :param card:
        the card to send notification
    :type card: struct snd_card \*

    :param mask:
        the event mask, SNDRV_CTL_EVENT_*
    :type mask: unsigned int

    :param id:
        the ctl element id to send notification
    :type id: struct snd_ctl_elem_id \*

.. _`snd_ctl_notify.description`:

Description
-----------

This function adds an event record with the given id and mask, appends
to the list and wakes up the user-space for notification.  This can be
called in the atomic context.

.. _`snd_ctl_new`:

snd_ctl_new
===========

.. c:function:: int snd_ctl_new(struct snd_kcontrol **kctl, unsigned int count, unsigned int access, struct snd_ctl_file *file)

    create a new control instance with some elements

    :param kctl:
        the pointer to store new control instance
    :type kctl: struct snd_kcontrol \*\*

    :param count:
        the number of elements in this control
    :type count: unsigned int

    :param access:
        the default access flags for elements in this control
    :type access: unsigned int

    :param file:
        given when locking these elements
    :type file: struct snd_ctl_file \*

.. _`snd_ctl_new.description`:

Description
-----------

Allocates a memory object for a new control instance. The instance has
elements as many as the given number (@count). Each element has given
access permissions (@access). Each element is locked when \ ``file``\  is given.

.. _`snd_ctl_new.return`:

Return
------

0 on success, error code on failure

.. _`snd_ctl_new1`:

snd_ctl_new1
============

.. c:function:: struct snd_kcontrol *snd_ctl_new1(const struct snd_kcontrol_new *ncontrol, void *private_data)

    create a control instance from the template

    :param ncontrol:
        the initialization record
    :type ncontrol: const struct snd_kcontrol_new \*

    :param private_data:
        the private data to set
    :type private_data: void \*

.. _`snd_ctl_new1.description`:

Description
-----------

Allocates a new struct snd_kcontrol instance and initialize from the given
template.  When the access field of ncontrol is 0, it's assumed as
READWRITE access. When the count field is 0, it's assumes as one.

.. _`snd_ctl_new1.return`:

Return
------

The pointer of the newly generated instance, or \ ``NULL``\  on failure.

.. _`snd_ctl_free_one`:

snd_ctl_free_one
================

.. c:function:: void snd_ctl_free_one(struct snd_kcontrol *kcontrol)

    release the control instance

    :param kcontrol:
        the control instance
    :type kcontrol: struct snd_kcontrol \*

.. _`snd_ctl_free_one.description`:

Description
-----------

Releases the control instance created via \ :c:func:`snd_ctl_new`\ 
or \ :c:func:`snd_ctl_new1`\ .
Don't call this after the control was added to the card.

.. _`snd_ctl_add`:

snd_ctl_add
===========

.. c:function:: int snd_ctl_add(struct snd_card *card, struct snd_kcontrol *kcontrol)

    add the control instance to the card

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param kcontrol:
        the control instance to add
    :type kcontrol: struct snd_kcontrol \*

.. _`snd_ctl_add.description`:

Description
-----------

Adds the control instance created via \ :c:func:`snd_ctl_new`\  or
\ :c:func:`snd_ctl_new1`\  to the given card. Assigns also an unique
numid used for fast search.

It frees automatically the control which cannot be added.

.. _`snd_ctl_add.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ctl_replace`:

snd_ctl_replace
===============

.. c:function:: int snd_ctl_replace(struct snd_card *card, struct snd_kcontrol *kcontrol, bool add_on_replace)

    replace the control instance of the card

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param kcontrol:
        the control instance to replace
    :type kcontrol: struct snd_kcontrol \*

    :param add_on_replace:
        add the control if not already added
    :type add_on_replace: bool

.. _`snd_ctl_replace.description`:

Description
-----------

Replaces the given control.  If the given control does not exist
and the add_on_replace flag is set, the control is added.  If the
control exists, it is destroyed first.

It frees automatically the control which cannot be added or replaced.

.. _`snd_ctl_replace.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ctl_remove`:

snd_ctl_remove
==============

.. c:function:: int snd_ctl_remove(struct snd_card *card, struct snd_kcontrol *kcontrol)

    remove the control from the card and release it

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param kcontrol:
        the control instance to remove
    :type kcontrol: struct snd_kcontrol \*

.. _`snd_ctl_remove.description`:

Description
-----------

Removes the control from the card and then releases the instance.
You don't need to call \ :c:func:`snd_ctl_free_one`\ . You must be in
the write lock - down_write(&card->controls_rwsem).

.. _`snd_ctl_remove.return`:

Return
------

0 if successful, or a negative error code on failure.

.. _`snd_ctl_remove_id`:

snd_ctl_remove_id
=================

.. c:function:: int snd_ctl_remove_id(struct snd_card *card, struct snd_ctl_elem_id *id)

    remove the control of the given id and release it

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the control id to remove
    :type id: struct snd_ctl_elem_id \*

.. _`snd_ctl_remove_id.description`:

Description
-----------

Finds the control instance with the given id, removes it from the
card list and releases it.

.. _`snd_ctl_remove_id.return`:

Return
------

0 if successful, or a negative error code on failure.

.. _`snd_ctl_remove_user_ctl`:

snd_ctl_remove_user_ctl
=======================

.. c:function:: int snd_ctl_remove_user_ctl(struct snd_ctl_file *file, struct snd_ctl_elem_id *id)

    remove and release the unlocked user control

    :param file:
        active control handle
    :type file: struct snd_ctl_file \*

    :param id:
        the control id to remove
    :type id: struct snd_ctl_elem_id \*

.. _`snd_ctl_remove_user_ctl.description`:

Description
-----------

Finds the control instance with the given id, removes it from the
card list and releases it.

.. _`snd_ctl_remove_user_ctl.return`:

Return
------

0 if successful, or a negative error code on failure.

.. _`snd_ctl_activate_id`:

snd_ctl_activate_id
===================

.. c:function:: int snd_ctl_activate_id(struct snd_card *card, struct snd_ctl_elem_id *id, int active)

    activate/inactivate the control of the given id

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the control id to activate/inactivate
    :type id: struct snd_ctl_elem_id \*

    :param active:
        non-zero to activate
    :type active: int

.. _`snd_ctl_activate_id.description`:

Description
-----------

Finds the control instance with the given id, and activate or
inactivate the control together with notification, if changed.
The given ID data is filled with full information.

.. _`snd_ctl_activate_id.return`:

Return
------

0 if unchanged, 1 if changed, or a negative error code on failure.

.. _`snd_ctl_rename_id`:

snd_ctl_rename_id
=================

.. c:function:: int snd_ctl_rename_id(struct snd_card *card, struct snd_ctl_elem_id *src_id, struct snd_ctl_elem_id *dst_id)

    replace the id of a control on the card

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param src_id:
        the old id
    :type src_id: struct snd_ctl_elem_id \*

    :param dst_id:
        the new id
    :type dst_id: struct snd_ctl_elem_id \*

.. _`snd_ctl_rename_id.description`:

Description
-----------

Finds the control with the old id from the card, and replaces the
id with the new one.

.. _`snd_ctl_rename_id.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ctl_find_numid`:

snd_ctl_find_numid
==================

.. c:function:: struct snd_kcontrol *snd_ctl_find_numid(struct snd_card *card, unsigned int numid)

    find the control instance with the given number-id

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param numid:
        the number-id to search
    :type numid: unsigned int

.. _`snd_ctl_find_numid.description`:

Description
-----------

Finds the control instance with the given number-id from the card.

The caller must down card->controls_rwsem before calling this function
(if the race condition can happen).

.. _`snd_ctl_find_numid.return`:

Return
------

The pointer of the instance if found, or \ ``NULL``\  if not.

.. _`snd_ctl_find_id`:

snd_ctl_find_id
===============

.. c:function:: struct snd_kcontrol *snd_ctl_find_id(struct snd_card *card, struct snd_ctl_elem_id *id)

    find the control instance with the given id

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the id to search
    :type id: struct snd_ctl_elem_id \*

.. _`snd_ctl_find_id.description`:

Description
-----------

Finds the control instance with the given id from the card.

The caller must down card->controls_rwsem before calling this function
(if the race condition can happen).

.. _`snd_ctl_find_id.return`:

Return
------

The pointer of the instance if found, or \ ``NULL``\  if not.

.. _`snd_ctl_register_ioctl`:

snd_ctl_register_ioctl
======================

.. c:function:: int snd_ctl_register_ioctl(snd_kctl_ioctl_func_t fcn)

    register the device-specific control-ioctls

    :param fcn:
        ioctl callback function
    :type fcn: snd_kctl_ioctl_func_t

.. _`snd_ctl_register_ioctl.description`:

Description
-----------

called from each device manager like pcm.c, hwdep.c, etc.

.. _`snd_ctl_register_ioctl_compat`:

snd_ctl_register_ioctl_compat
=============================

.. c:function:: int snd_ctl_register_ioctl_compat(snd_kctl_ioctl_func_t fcn)

    register the device-specific 32bit compat control-ioctls

    :param fcn:
        ioctl callback function
    :type fcn: snd_kctl_ioctl_func_t

.. _`snd_ctl_unregister_ioctl`:

snd_ctl_unregister_ioctl
========================

.. c:function:: int snd_ctl_unregister_ioctl(snd_kctl_ioctl_func_t fcn)

    de-register the device-specific control-ioctls

    :param fcn:
        ioctl callback function to unregister
    :type fcn: snd_kctl_ioctl_func_t

.. _`snd_ctl_unregister_ioctl_compat`:

snd_ctl_unregister_ioctl_compat
===============================

.. c:function:: int snd_ctl_unregister_ioctl_compat(snd_kctl_ioctl_func_t fcn)

    de-register the device-specific compat 32bit control-ioctls

    :param fcn:
        ioctl callback function to unregister
    :type fcn: snd_kctl_ioctl_func_t

.. _`snd_ctl_boolean_mono_info`:

snd_ctl_boolean_mono_info
=========================

.. c:function:: int snd_ctl_boolean_mono_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Helper function for a standard boolean info callback with a mono channel

    :param kcontrol:
        the kcontrol instance
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        info to store
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_ctl_boolean_mono_info.description`:

Description
-----------

This is a function that can be used as info callback for a standard
boolean control with a single mono channel.

.. _`snd_ctl_boolean_stereo_info`:

snd_ctl_boolean_stereo_info
===========================

.. c:function:: int snd_ctl_boolean_stereo_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo)

    Helper function for a standard boolean info callback with stereo two channels

    :param kcontrol:
        the kcontrol instance
    :type kcontrol: struct snd_kcontrol \*

    :param uinfo:
        info to store
    :type uinfo: struct snd_ctl_elem_info \*

.. _`snd_ctl_boolean_stereo_info.description`:

Description
-----------

This is a function that can be used as info callback for a standard
boolean control with stereo two channels.

.. _`snd_ctl_enum_info`:

snd_ctl_enum_info
=================

.. c:function:: int snd_ctl_enum_info(struct snd_ctl_elem_info *info, unsigned int channels, unsigned int items, const char *const names)

    fills the info structure for an enumerated control

    :param info:
        the structure to be filled
    :type info: struct snd_ctl_elem_info \*

    :param channels:
        the number of the control's channels; often one
    :type channels: unsigned int

    :param items:
        the number of control values; also the size of \ ``names``\ 
    :type items: unsigned int

    :param names:
        an array containing the names of all control values
    :type names: const char \*const

.. _`snd_ctl_enum_info.description`:

Description
-----------

Sets all required fields in \ ``info``\  to their appropriate values.
If the control's accessibility is not the default (readable and writable),
the caller has to fill \ ``info->access``\ .

.. _`snd_ctl_enum_info.return`:

Return
------

Zero.

.. This file was automatic generated / don't edit.


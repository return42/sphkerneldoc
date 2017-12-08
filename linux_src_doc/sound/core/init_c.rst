.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/init.c

.. _`snd_device_initialize`:

snd_device_initialize
=====================

.. c:function:: void snd_device_initialize(struct device *dev, struct snd_card *card)

    Initialize struct device for sound devices

    :param struct device \*dev:
        device to initialize

    :param struct snd_card \*card:
        card to assign, optional

.. _`snd_card_new`:

snd_card_new
============

.. c:function:: int snd_card_new(struct device *parent, int idx, const char *xid, struct module *module, int extra_size, struct snd_card **card_ret)

    create and initialize a soundcard structure

    :param struct device \*parent:
        the parent device object

    :param int idx:
        card index (address) [0 ... (SNDRV_CARDS-1)]

    :param const char \*xid:
        card identification (ASCII string)

    :param struct module \*module:
        top level module for locking

    :param int extra_size:
        allocate this extra size after the main soundcard structure

    :param struct snd_card \*\*card_ret:
        the pointer to store the created card instance

.. _`snd_card_new.description`:

Description
-----------

 Creates and initializes a soundcard structure.

 The function allocates snd_card instance via kzalloc with the given
 space for the driver to use freely.  The allocated struct is stored
 in the given card_ret pointer.

.. _`snd_card_new.return`:

Return
------

Zero if successful or a negative error code.

.. _`snd_card_disconnect`:

snd_card_disconnect
===================

.. c:function:: int snd_card_disconnect(struct snd_card *card)

    disconnect all APIs from the file-operations (user space)

    :param struct snd_card \*card:
        soundcard structure

.. _`snd_card_disconnect.description`:

Description
-----------

 Disconnects all APIs from the file-operations (user space).

.. _`snd_card_disconnect.return`:

Return
------

Zero, otherwise a negative error code.

.. _`snd_card_disconnect.note`:

Note
----

The current implementation replaces all active file->f_op with special
       dummy file operations (they do nothing except release).

.. _`snd_card_disconnect_sync`:

snd_card_disconnect_sync
========================

.. c:function:: void snd_card_disconnect_sync(struct snd_card *card)

    disconnect card and wait until files get closed

    :param struct snd_card \*card:
        card object to disconnect

.. _`snd_card_disconnect_sync.description`:

Description
-----------

This calls \ :c:func:`snd_card_disconnect`\  for disconnecting all belonging components
and waits until all pending files get closed.
It assures that all accesses from user-space finished so that the driver
can release its resources gracefully.

.. _`snd_card_free_when_closed`:

snd_card_free_when_closed
=========================

.. c:function:: int snd_card_free_when_closed(struct snd_card *card)

    Disconnect the card, free it later eventually

    :param struct snd_card \*card:
        soundcard structure

.. _`snd_card_free_when_closed.description`:

Description
-----------

Unlike \ :c:func:`snd_card_free`\ , this function doesn't try to release the card
resource immediately, but tries to disconnect at first.  When the card
is still in use, the function returns before freeing the resources.
The card resources will be freed when the refcount gets to zero.

.. _`snd_card_free`:

snd_card_free
=============

.. c:function:: int snd_card_free(struct snd_card *card)

    frees given soundcard structure

    :param struct snd_card \*card:
        soundcard structure

.. _`snd_card_free.description`:

Description
-----------

This function releases the soundcard structure and the all assigned
devices automatically.  That is, you don't have to release the devices
by yourself.

This function waits until the all resources are properly released.

.. _`snd_card_free.return`:

Return
------

Zero. Frees all associated devices and frees the control
interface associated to given soundcard.

.. _`snd_card_set_id`:

snd_card_set_id
===============

.. c:function:: void snd_card_set_id(struct snd_card *card, const char *nid)

    set card identification name

    :param struct snd_card \*card:
        soundcard structure

    :param const char \*nid:
        new identification string

.. _`snd_card_set_id.description`:

Description
-----------

 This function sets the card identification and checks for name
 collisions.

.. _`snd_card_add_dev_attr`:

snd_card_add_dev_attr
=====================

.. c:function:: int snd_card_add_dev_attr(struct snd_card *card, const struct attribute_group *group)

    Append a new sysfs attribute group to card

    :param struct snd_card \*card:
        card instance

    :param const struct attribute_group \*group:
        attribute group to append

.. _`snd_card_register`:

snd_card_register
=================

.. c:function:: int snd_card_register(struct snd_card *card)

    register the soundcard

    :param struct snd_card \*card:
        soundcard structure

.. _`snd_card_register.description`:

Description
-----------

 This function registers all the devices assigned to the soundcard.
 Until calling this, the ALSA control interface is blocked from the
 external accesses.  Thus, you should call this function at the end
 of the initialization of the card.

.. _`snd_card_register.return`:

Return
------

Zero otherwise a negative error code if the registration failed.

.. _`snd_component_add`:

snd_component_add
=================

.. c:function:: int snd_component_add(struct snd_card *card, const char *component)

    add a component string

    :param struct snd_card \*card:
        soundcard structure

    :param const char \*component:
        the component id string

.. _`snd_component_add.description`:

Description
-----------

 This function adds the component id string to the supported list.
 The component can be referred from the alsa-lib.

.. _`snd_component_add.return`:

Return
------

Zero otherwise a negative error code.

.. _`snd_card_file_add`:

snd_card_file_add
=================

.. c:function:: int snd_card_file_add(struct snd_card *card, struct file *file)

    add the file to the file list of the card

    :param struct snd_card \*card:
        soundcard structure

    :param struct file \*file:
        file pointer

.. _`snd_card_file_add.description`:

Description
-----------

 This function adds the file to the file linked-list of the card.
 This linked-list is used to keep tracking the connection state,
 and to avoid the release of busy resources by hotplug.

.. _`snd_card_file_add.return`:

Return
------

zero or a negative error code.

.. _`snd_card_file_remove`:

snd_card_file_remove
====================

.. c:function:: int snd_card_file_remove(struct snd_card *card, struct file *file)

    remove the file from the file list

    :param struct snd_card \*card:
        soundcard structure

    :param struct file \*file:
        file pointer

.. _`snd_card_file_remove.description`:

Description
-----------

 This function removes the file formerly added to the card via
 \ :c:func:`snd_card_file_add`\  function.
 If all files are removed and \ :c:func:`snd_card_free_when_closed`\  was
 called beforehand, it processes the pending release of
 resources.

.. _`snd_card_file_remove.return`:

Return
------

Zero or a negative error code.

.. _`snd_power_wait`:

snd_power_wait
==============

.. c:function:: int snd_power_wait(struct snd_card *card, unsigned int power_state)

    wait until the power-state is changed.

    :param struct snd_card \*card:
        soundcard structure

    :param unsigned int power_state:
        expected power state

.. _`snd_power_wait.description`:

Description
-----------

 Waits until the power-state is changed.

.. _`snd_power_wait.return`:

Return
------

Zero if successful, or a negative error code.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/ff-core.c

.. _`input_ff_upload`:

input_ff_upload
===============

.. c:function:: int input_ff_upload(struct input_dev *dev, struct ff_effect *effect, struct file *file)

    upload effect into force-feedback device

    :param dev:
        input device
    :type dev: struct input_dev \*

    :param effect:
        effect to be uploaded
    :type effect: struct ff_effect \*

    :param file:
        owner of the effect
    :type file: struct file \*

.. _`input_ff_erase`:

input_ff_erase
==============

.. c:function:: int input_ff_erase(struct input_dev *dev, int effect_id, struct file *file)

    erase a force-feedback effect from device

    :param dev:
        input device to erase effect from
    :type dev: struct input_dev \*

    :param effect_id:
        id of the effect to be erased
    :type effect_id: int

    :param file:
        purported owner of the request
    :type file: struct file \*

.. _`input_ff_erase.description`:

Description
-----------

This function erases a force-feedback effect from specified device.
The effect will only be erased if it was uploaded through the same
file handle that is requesting erase.

.. _`input_ff_event`:

input_ff_event
==============

.. c:function:: int input_ff_event(struct input_dev *dev, unsigned int type, unsigned int code, int value)

    generic handler for force-feedback events

    :param dev:
        input device to send the effect to
    :type dev: struct input_dev \*

    :param type:
        event type (anything but EV_FF is ignored)
    :type type: unsigned int

    :param code:
        event code
    :type code: unsigned int

    :param value:
        event value
    :type value: int

.. _`input_ff_create`:

input_ff_create
===============

.. c:function:: int input_ff_create(struct input_dev *dev, unsigned int max_effects)

    create force-feedback device

    :param dev:
        input device supporting force-feedback
    :type dev: struct input_dev \*

    :param max_effects:
        maximum number of effects supported by the device
    :type max_effects: unsigned int

.. _`input_ff_create.description`:

Description
-----------

This function allocates all necessary memory for a force feedback
portion of an input device and installs all default handlers.
\ ``dev->ffbit``\  should be already set up before calling this function.
Once ff device is created you need to setup its upload, erase,
playback and other handlers before registering input device

.. _`input_ff_destroy`:

input_ff_destroy
================

.. c:function:: void input_ff_destroy(struct input_dev *dev)

    frees force feedback portion of input device

    :param dev:
        input device supporting force feedback
    :type dev: struct input_dev \*

.. _`input_ff_destroy.description`:

Description
-----------

This function is only needed in error path as input core will
automatically free force feedback structures when device is
destroyed.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/ff-core.c

.. _`input_ff_upload`:

input_ff_upload
===============

.. c:function:: int input_ff_upload(struct input_dev *dev, struct ff_effect *effect, struct file *file)

    upload effect into force-feedback device

    :param struct input_dev \*dev:
        input device

    :param struct ff_effect \*effect:
        effect to be uploaded

    :param struct file \*file:
        owner of the effect

.. _`input_ff_erase`:

input_ff_erase
==============

.. c:function:: int input_ff_erase(struct input_dev *dev, int effect_id, struct file *file)

    erase a force-feedback effect from device

    :param struct input_dev \*dev:
        input device to erase effect from

    :param int effect_id:
        id of the effect to be erased

    :param struct file \*file:
        purported owner of the request

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

    :param struct input_dev \*dev:
        input device to send the effect to

    :param unsigned int type:
        event type (anything but EV_FF is ignored)

    :param unsigned int code:
        event code

    :param int value:
        event value

.. _`input_ff_create`:

input_ff_create
===============

.. c:function:: int input_ff_create(struct input_dev *dev, unsigned int max_effects)

    create force-feedback device

    :param struct input_dev \*dev:
        input device supporting force-feedback

    :param unsigned int max_effects:
        maximum number of effects supported by the device

.. _`input_ff_create.description`:

Description
-----------

This function allocates all necessary memory for a force feedback
portion of an input device and installs all default handlers.
\ ``dev``\ ->ffbit should be already set up before calling this function.
Once ff device is created you need to setup its upload, erase,
playback and other handlers before registering input device

.. _`input_ff_destroy`:

input_ff_destroy
================

.. c:function:: void input_ff_destroy(struct input_dev *dev)

    frees force feedback portion of input device

    :param struct input_dev \*dev:
        input device supporting force feedback

.. _`input_ff_destroy.description`:

Description
-----------

This function is only needed in error path as input core will
automatically free force feedback structures when device is
destroyed.

.. This file was automatic generated / don't edit.


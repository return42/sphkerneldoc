.. -*- coding: utf-8; mode: rst -*-

=======
wimax.h
=======


.. _`wimax_st`:

enum wimax_st
=============

.. c:type:: wimax_st

    The different states of a WiMAX device


.. _`wimax_st.definition`:

Definition
----------

.. code-block:: c

    enum wimax_st {
      __WIMAX_ST_NULL,
      WIMAX_ST_DOWN,
      __WIMAX_ST_QUIESCING,
      WIMAX_ST_UNINITIALIZED,
      WIMAX_ST_RADIO_OFF,
      WIMAX_ST_READY,
      WIMAX_ST_SCANNING,
      WIMAX_ST_CONNECTING,
      WIMAX_ST_CONNECTED,
      __WIMAX_ST_INVALID
    };


.. _`wimax_st.constants`:

Constants
---------

:``__WIMAX_ST_NULL``:
    The device structure has been allocated and zeroed,
    but still :c:func:`wimax_dev_add` hasn't been called. There is no state.

:``WIMAX_ST_DOWN``:
    The device has been registered with the WiMAX and
    networking stacks, but it is not initialized (normally that is
    done with 'ifconfig DEV up' [or equivalent], which can upload
    firmware and enable communications with the device).
    In this state, the device is powered down and using as less
    power as possible.
    This state is the default after a call to :c:func:`wimax_dev_add`. It
    is ok to have drivers move directly to ``WIMAX_ST_UNINITIALIZED``
    or ``WIMAX_ST_RADIO_OFF`` in :c:func:`_probe` after the call to
    :c:func:`wimax_dev_add`.
    It is recommended that the driver leaves this state when
    calling 'ifconfig DEV up' and enters it back on 'ifconfig DEV
    down'.

:``__WIMAX_ST_QUIESCING``:
    The device is being torn down, so no API
    operations are allowed to proceed except the ones needed to
    complete the device clean up process.

:``WIMAX_ST_UNINITIALIZED``:
    [optional] Communication with the device
    is setup, but the device still requires some configuration
    before being operational.
    Some WiMAX API calls might work.

:``WIMAX_ST_RADIO_OFF``:
    The device is fully up; radio is off (wether
    by hardware or software switches).
    It is recommended to always leave the device in this state
    after initialization.

:``WIMAX_ST_READY``:
    The device is fully up and radio is on.

:``WIMAX_ST_SCANNING``:
    [optional] The device has been instructed to
    scan. In this state, the device cannot be actively connected to
    a network.

:``WIMAX_ST_CONNECTING``:
    The device is connecting to a network. This
    state exists because in some devices, the connect process can
    include a number of negotiations between user space, kernel
    space and the device. User space needs to know what the device
    is doing. If the connect sequence in a device is atomic and
    fast, the device can transition directly to CONNECTED

:``WIMAX_ST_CONNECTED``:
    The device is connected to a network.

:``__WIMAX_ST_INVALID``:
    This is an invalid state used to mark the
    maximum numeric value of states.


.. _`wimax_st.description`:

Description
-----------


Transitions from one state to another one are atomic and can only
be caused in kernel space with :c:func:`wimax_state_change`. To read the
state, use :c:func:`wimax_state_get`.

States starting with __ are internal and shall not be used or
referred to by drivers or userspace. They look ugly, but that's the
point -- if any use is made non-internal to the stack, it is easier
to catch on review.

All API operations [with well defined exceptions] will take the
device mutex before starting and then check the state. If the state
is ``__WIMAX_ST_NULL``\ , ``WIMAX_ST_DOWN``\ , ``WIMAX_ST_UNINITIALIZED`` or
``__WIMAX_ST_QUIESCING``\ , it will drop the lock and quit with
-\ ``EINVAL``\ , -\ ``ENOMEDIUM``\ , -\ ``ENOTCONN`` or -\ ``ESHUTDOWN``\ .

The order of the definitions is important, so we can do numerical
comparisons (eg: < ``WIMAX_ST_RADIO_OFF`` means the device is not ready
to operate).

